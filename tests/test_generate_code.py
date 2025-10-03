import pytest
from tools.generate_code import generate_code_tool
from services.gemini_mock import MockGeminiService
from config import USE_MOCK_GEMINI

def test_generate_code_mocked(monkeypatch):
    # force mock
    monkeypatch.setenv("USE_MOCK_GEMINI", "true")
    # Alternatively, monkeypatch get_ai_service to return MockGeminiService
    result = generate_code_tool("build a REST API in Python")
    assert "[Mocked Gemini response" in result
