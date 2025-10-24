import sys
from fastmcp import FastMCP, Context
from tools.generate_code import _generate_code_core
from tools.code_review import _code_review_core
from tools.code_explain import _code_explain_core
from tools.unit_tests import _generate_unit_tests_core
from tools.mockito_test_tool import _generate_mockito_test_core
from tools.jira_intergration import (
        get_jira_issue_details,
        generate_code_from_jira
    )

mcp = FastMCP(name="Enhanced MCP Server with Jira & Gemini")


@mcp.tool(name="generate_code", description="Generate code based on input requirements and programming language")
async def generate_code(
        requirements: str, 
        language: str = "python",
        context: str = "",
        ctx: Context = None
    ) -> str:
        return await _generate_code_core(requirements, language, context, ctx)

@mcp.tool(name="review_code", description="Review code for quality, best practices and suggest improvements")
async def review_code(
        code: str, 
        language: str = "python",
        guidelines: str = "",
        ctx: Context = None
    ) -> str:
        return await _code_review_core(code, language, guidelines, ctx)

@mcp.tool(name="explain_code", description="Explain code in simple terms with complexity analysis")
async def explain_code(
        code: str, 
        language: str = "python",
        detail_level: str = "medium",
        ctx: Context = None
    ) -> str:
        return await _code_explain_core(code, language, detail_level, ctx)

@mcp.tool(name="generate_unit_tests", description="Generate comprehensive unit tests for provided code")
async def generate_unit_tests(
        code: str,
        language: str = "python",
        test_framework: str = "",
        coverage_goal: int = 80,
        ctx: Context = None
    ) -> str:
        return await _generate_unit_tests_core(code, language, test_framework, coverage_goal, ctx)

@mcp.tool(name="generate_mockito_tests", description="Generate Mockito-based JUnit tests for a given Java class and method")
async def generate_mockito_tests(
        target_class: str,
        target_method: str,
        description: str = "",
        ctx: Context = None
) -> str:
    return await _generate_mockito_test_core(target_class, target_method, description, ctx)



@mcp.tool(name="get_jira_issue", description="Get Jira issue details without exposing sensitive data to AI")
async def get_jira_issue(
        issue_key: str,
        ctx: Context = None
    ) -> dict:
        return await get_jira_issue_details(issue_key, ctx)

@mcp.tool(name="generate_code_from_jira", description="Generate code based on Jira issue requirements (safe data handling)")
async def generate_code_from_jira_issue(
        issue_key: str,
        language: str = "python",
        additional_requirements: str = "",
        ctx: Context = None
    ) -> str:
        return await generate_code_from_jira(issue_key, language, additional_requirements, ctx)

if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run(transport="http", host="0.0.0.0", port=8100, path="/mcp")
