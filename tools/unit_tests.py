from fastmcp import Context
from tools.base import get_ai_service

async def _generate_unit_tests_core(
    code: str, 
    language: str, 
    test_framework: str, 
    coverage_goal: int,
    ctx: Context
) -> str:
    await ctx.debug(f"Generating unit tests for {language} code")
    
    if len(code.strip()) < 50:
        return "Error: Provided code is too short or incomplete to generate meaningful unit tests. Please provide more complete code."
    
    ai = get_ai_service()
    
    if not test_framework:
        test_framework = _get_default_test_framework(language)
    
    prompt = f"""
    Generate comprehensive unit tests for the following {language} code.
    Use {test_framework} test framework.
    Aim for at least {coverage_goal}% test coverage.
    
    Code to test:
    ```{language}
    {code}
    ```
    
    Requirements:
    1. Cover all major functions and edge cases
    2. Include both positive and negative test cases
    3. Use appropriate mocking where necessary
    4. Include descriptive test names and comments
    5. Ensure tests are independent and can run in any order
    
    Please provide the complete test code with imports and setup.
    """
    
    return ai.ask(prompt)

def _get_default_test_framework(language: str) -> str:
    """Get default test framework for a programming language"""
    frameworks = {
        "python": "pytest",
        "javascript": "jest",
        "java": "junit",
        "csharp": "xunit",
        "go": "testing",
        "ruby": "rspec"
    }
    return frameworks.get(language.lower(), "standard testing framework")