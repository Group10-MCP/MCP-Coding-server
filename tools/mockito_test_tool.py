from fastmcp import Context
from tools.base import get_ai_service

async def _generate_mockito_test_core(
        target_class: str,
        target_method: str,
        description: str,
        ctx: Context
) -> str:
    """
    Generate Mockito-style unit test code for a Java class and method using AI.
    """

    await ctx.debug(f"Generating Mockito tests for {target_class}.{target_method}")

    if not target_class or not target_method:
        return "Error: Both target_class and target_method are required."

    ai = get_ai_service()

    prompt = f"""
    You are a professional Java developer specializing in automated testing.
    Write a **Mockito-based JUnit test class** for the following:

    - **Target class:** {target_class}
    - **Target method:** {target_method}

    Context:
    {description}

    Requirements:
    1. Use `@Mock`, `@InjectMocks`, and `MockitoAnnotations.openMocks(this)`
    2. Include both positive and negative test cases
    3. Use `when(...).thenReturn(...)` or `verify(...)` where appropriate
    4. Include proper `@BeforeEach` setup
    5. Use clear and descriptive test names
    6. Include necessary imports and class structure

    Return the complete test class ready to run.
    """

    return ai.ask(prompt)
