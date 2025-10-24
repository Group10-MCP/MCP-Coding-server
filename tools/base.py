from config import USE_MOCK_GEMINI, GEMINI_API_KEY
from services.gemini_mock import MockGeminiService

def get_ai_service():
    if USE_MOCK_GEMINI:
        return MockGeminiService()
    
    try:
        from services.gemini import GeminiService
        return GeminiService()
    except (ImportError, ValueError) as e:
        print(f"Warning: Falling back to mock service. Reason: {e}")
        return MockGeminiService()