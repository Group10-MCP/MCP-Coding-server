import jwt
from fastmcp import Context
from fastmcp.server.middleware import Middleware
from fastmcp.exceptions import MCPError
from config import JWT_SECRET, JWT_ALGO

class JWTAuthMiddleware(Middleware):
    async def on_call_tool(self, context, call_next):
        ctx: Context = context.fastmcp_context

        from fastmcp.server.dependencies import get_http_headers
        headers = get_http_headers()
        auth = headers.get("authorization", "")

        token = None
        if auth.startswith("Bearer "):
            token = auth[len("Bearer "):]

        if not token:
            raise MCPError("Unauthorized: missing token", status_code=401)

        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except jwt.PyJWTError:
            raise MCPError("Unauthorized: invalid token", status_code=401)

        # store in context state
        ctx.set_state("user", payload)

        return await call_next()
