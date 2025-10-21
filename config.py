import os

JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
JWT_ALGO = os.getenv("JWT_ALGO", "HS256")
USE_MOCK_GEMINI = os.getenv("USE_MOCK_GEMINI", "true").lower() in ("1","true","yes")
