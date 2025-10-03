from fastmcp import Context
from tools.base import get_ai_service

async def _code_explain_core(input_data: str, ctx: Context) -> str:
    await ctx.debug("Explaining code input")
    ai = get_ai_service()
    prompt = f"Explain the following code snippet in simple terms:\n{input_data}"
    return ai.ask(prompt)
