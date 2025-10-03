from fastmcp import Context
from tools.base import get_ai_service

async def _generate_code_core(input_data: str, ctx: Context) -> str:
    await ctx.debug(f"Generating code for: {input_data}")
    ai = get_ai_service()
    prompt = f"Write code for the following requirement:\n{input_data}"
    return ai.ask(prompt)
