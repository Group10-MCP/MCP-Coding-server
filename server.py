from fastmcp import FastMCP, Context
from tools.generate_code import _generate_code_core
from tools.code_review import _code_review_core
from tools.code_explain import _code_explain_core
mcp = FastMCP(name="MCP Server with JWT")

@mcp.tool(name="generate_code", description="Generate code based on input requirements")
async def generate_code(input_data: str, ctx: Context) -> str:
    return await _generate_code_core(input_data, ctx)
@mcp.tool(name="review_code", description="Review code for quality and best practices")
async def review_code(input_data: str, ctx: Context) -> str:
    return await _code_review_core(input_data, ctx)
@mcp.tool(name="explain_code", description="Explain code in simple terms")
async def explain_code(input_data: str, ctx: Context) -> str:
    return await _code_explain_core(input_data, ctx)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000, path="/mcp")
