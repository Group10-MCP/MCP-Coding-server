# services/gemini.py
class GeminiService:
    def ask(self, prompt: str) -> str:
        # Real integration stub: Example of what you might do
        # For now, placeholder
        # You might call an HTTP API, openai‑style, etc.
        return f"[Gemini real response to: {prompt}]"


# services/gemini_mock.py
class MockGeminiService:
    def ask(self, prompt: str) -> str:
        return f"[Mocked Gemini response for prompt: {prompt}]"
