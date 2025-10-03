# tools/code_review.py

from fastmcp import Context
from tools.base import get_ai_service

async def _code_review_core(input_data: str, ctx: Context) -> str:
    await ctx.debug("Reviewing code input")
    ai = get_ai_service()
    prompt = f"Please perform a detailed code review of the following code:\n{input_data}"
    return ai.ask(prompt)
