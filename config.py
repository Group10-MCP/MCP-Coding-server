import os

JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
JWT_ALGO = os.getenv("JWT_ALGO", "HS256")
USE_MOCK_GEMINI = os.getenv("USE_MOCK_GEMINI", "true").lower() in ("1","true","yes")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

JIRA_URL = os.getenv("JIRA_URL", "https://1jira.fnb.co.za")
JIRA_EMAIL = os.getenv("EMAIL", "")
JIRA_API_TOKEN = os.getenv("API_TOKEN", "")