from fastmcp import Context
from tools.base import get_ai_service

async def _code_explain_core(
    code: str, 
    language: str, 
    detail_level: str,
    ctx: Context
) -> str:
    await ctx.debug(f"Explaining {language} code with {detail_level} detail")
    
    ai = get_ai_service()
    
    detail_instructions = {
        "low": "Provide a high-level overview focusing on the main purpose",
        "medium": "Explain the main components and flow with some technical details",
        "high": "Provide detailed explanation including algorithms, complexity, and implementation details"
    }
    
    instruction = detail_instructions.get(detail_level, detail_instructions["medium"])
    
    prompt = f"""
    Explain the following {language} code in simple terms:
    
    CODE:
    ```{language}
    {code}
    ```
    
    Please provide an explanation that:
    {instruction}
    
    Also include:
    - Overall purpose and functionality
    - Key components and their roles
    - Any important algorithms or patterns used
    - Potential improvements or considerations
    """
    
    return ai.ask(prompt)