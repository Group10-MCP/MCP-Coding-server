# services/gemini_mock.py - Enhanced mock service
class MockGeminiService:
    def ask(self, prompt: str) -> str:
        # Enhanced mock responses based on prompt content
        if "explain" in prompt.lower():
            return self._mock_explanation(prompt)
        elif "review" in prompt.lower():
            return self._mock_review(prompt)
        elif "test" in prompt.lower():
            return self._mock_tests(prompt)
        elif "generate" in prompt.lower() or "write code" in prompt.lower():
            return self._mock_code_generation(prompt)
        else:
            return f"[Mocked Gemini response for: {prompt[:100]}...]"
    
    def _mock_explanation(self, prompt: str) -> str:
        return """This code appears to be a function that processes data. Here's a breakdown:

1. **Function Purpose**: The main function takes input parameters and returns processed results
2. **Key Components**: 
   - Input validation
   - Data transformation logic
   - Error handling
3. **Complexity**: O(n) time complexity, suitable for medium-sized datasets

The code follows good practices with proper error handling and clear variable names."""

    def _mock_review(self, prompt: str) -> str:
        return """Code Review Results:

✅ **Strengths**:
- Good code structure and organization
- Proper error handling implemented
- Clear variable naming conventions

⚠️ **Areas for Improvement**:
- Consider adding more detailed docstrings
- Could benefit from type hints
- Some functions could be broken down further

🔧 **Suggestions**:
- Add input validation for edge cases
- Consider using context managers for resource handling
- Improve test coverage"""

    def _mock_tests(self, prompt: str) -> str:
        return """Generated Unit Tests:"""