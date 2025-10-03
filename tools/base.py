from config import USE_MOCK_GEMINI
from services.gemini import GeminiService
from services.gemini_mock import MockGeminiService

def get_ai_service():
    return MockGeminiService() if USE_MOCK_GEMINI else GeminiService()
