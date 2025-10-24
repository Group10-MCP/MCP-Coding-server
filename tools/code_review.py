from fastmcp import Context
from tools.base import get_ai_service

async def _code_review_core(
    code: str, 
    language: str, 
    guidelines: str,
    ctx: Context
) -> str:
    await ctx.debug(f"Reviewing {language} code")
    
    ai = get_ai_service()
    
    prompt = f"""
    Perform a comprehensive code review for the following {language} code:
    
    CODE:
    ```{language}
    {code}
    ```
    
    ADDITIONAL GUIDELINES:
    {guidelines}
    
    Please provide a detailed review covering:
    1. Code quality and readability
    2. Potential bugs or issues
    3. Security concerns
    4. Performance optimizations
    5. Best practices adherence
    6. Suggestions for improvement
    
    Format the review with clear sections and specific recommendations.
    """
    
    return ai.ask(prompt)