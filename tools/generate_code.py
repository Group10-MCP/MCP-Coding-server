from fastmcp import Context
from tools.base import get_ai_service

async def _generate_code_core(
    requirements: str, 
    language: str, 
    context: str,
    ctx: Context
) -> str:
    await ctx.debug(f"Generating {language} code for: {requirements[:100]}...")
    
    # Validate input requirements
    if not requirements or len(requirements.strip()) < 10:
        return "Error: Requirements are too vague or incomplete. Please provide more detailed requirements including:\n- Expected inputs/outputs\n- Specific functionality needed\n- Any constraints or preferences\n- Example usage if possible"
    
    ai = get_ai_service()
    
    prompt = f"""
    Write {language} code for the following requirements:
    
    REQUIREMENTS:
    {requirements}
    
    CONTEXT/ADDITIONAL INFORMATION:
    {context}
    
    Please generate:
    1. Clean, production-ready code
    2. Proper error handling and validation
    3. Documentation/comments where appropriate
    4. Follow {language} best practices and style guidelines
    5. Consider performance and security aspects
    
    If the requirements are unclear or insufficient, please ask for clarification rather than generating potentially incorrect code.
    """
    
    response = ai.ask(prompt)
    
    if any(phrase in response.lower() for phrase in ["clarification", "more information", "unclear", "insufficient"]):
        return f"Update: {response}\n\nPlease provide more detailed requirements for better code generation."
    
    return response