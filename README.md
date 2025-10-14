# FastMCP Server with JWT Authentication

This project is a FastMCP-powered server that provides AI-driven code utilities with secure JWT-based authentication. It includes tools for generating code, reviewing code, and explaining code snippets using a Gemini-like AI service.

## 🚀 Features

- 🔐 **JWT Authentication Middleware**  
  Ensures secure access to tools via Bearer token validation.

- 🤖 **AI-Powered Code Tools**  
  - `generate_code`: Generate code from natural language requirements  
  - `review_code`: Perform detailed code reviews  
  - `explain_code`: Explain code snippets in simple terms

- 🧠 **Gemini Service Integration**  
  Easily switch between a mock Gemini service and a real one using environment variables.

## 🛠️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fastmcp-jwt-server.git
cd fastmcp-jwt-server

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Set Environment Variables
Create a .env file or export variables manually:
JWT_SECRET=your_jwt_secret_key
JWT_ALGO=HS256
USE_MOCK_GEMINI=true

### 4. Run the Server
python main.py

Server will start at: http://localhost:8000/mcp

📦 Project Structure
├── config.py                # Environment config
├── main.py                  # MCP server entry point
├── middleware/
│   └── jwt_auth.py          # JWTAuthMiddleware
├── services/
│   ├── gemini.py            # Real Gemini service stub
│   └── gemini_mock.py       # Mock Gemini service
├── tools/
│   ├── base.py              # AI service selector
│   ├── code_explain.py      # Explain code tool
│   ├── code_review.py       # Review code tool
│   └── generate_code.py     # Generate code tool

