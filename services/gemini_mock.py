class MockGeminiService:
    def ask(self, prompt: str) -> str:
        # Simple unified response logic
        response_templates = {
            "explain": """Code Explanation:

This code appears to implement a well-structured function that:
- Takes input parameters and returns processed results
- Includes proper error handling
- Follows good coding practices
- Uses clear variable naming

The main logic focuses on data processing with appropriate validation.""",
            
            "review": """Code Review:

✅ Positive Aspects:
- Clean code structure
- Good error handling
- Readable variable names

⚠️ Suggestions:
- Add more comments
- Consider edge cases
- Improve test coverage

Overall: Good quality code with minor improvements needed.""",
            
            "test": """Generated Unit Tests:

```python
import pytest

def test_basic_functionality():
    \"\"\"Test main functionality\"\"\"
    assert True  # Replace with actual tests

def test_edge_cases():
    \"\"\"Test boundary conditions\"\"\"
    assert True  # Replace with edge case tests
```""",
            
            "generate": """```python
def solution():
    \"\"\"Generated code based on requirements\"\"\"
    # Implementation goes here
    return "result"
```"""
        }
        
        prompt_lower = prompt.lower()
        
        if "explain" in prompt_lower:
            return response_templates["explain"]
        elif "review" in prompt_lower:
            return response_templates["review"]
        elif "test" in prompt_lower:
            return response_templates["test"]
        elif "generate" in prompt_lower or "write code" in prompt_lower:
            return response_templates["generate"]
        else:
            return f"Mock AI response to: {prompt[:200]}..."