import requests
from requests.auth import HTTPBasicAuth
from fastmcp import Context
from config import JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN
from tools.base import get_ai_service

class JiraService:
    def __init__(self):
        self.base_url = JIRA_URL
        self.auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    
    def get_issue(self, issue_key: str) -> dict:
        """Get Jira issue details without exposing to external AI"""
        if not JIRA_EMAIL or not JIRA_API_TOKEN:
            raise ValueError("Jira credentials not configured")
        
        url = f"{self.base_url}/rest/api/2/issue/{issue_key}"
        
        try:
            response = requests.get(
                url, 
                auth=self.auth, 
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch Jira issue {issue_key}: {str(e)}")

async def get_jira_issue_details(issue_key: str, ctx: Context) -> dict:
    """Get Jira issue details safely (no data sent to Gemini)"""
    await ctx.debug(f"Fetching Jira issue: {issue_key}")
    
    jira_service = JiraService()
    issue_data = jira_service.get_issue(issue_key)
    
    safe_data = {
        "key": issue_data.get("key"),
        "summary": issue_data.get("fields", {}).get("summary"),
        "description": issue_data.get("fields", {}).get("description"),
        "status": issue_data.get("fields", {}).get("status", {}).get("name"),
        "priority": issue_data.get("fields", {}).get("priority", {}).get("name"),
        "reporter": issue_data.get("fields", {}).get("reporter", {}).get("displayName"),
        "assignee": issue_data.get("fields", {}).get("assignee", {}).get("displayName"),
        "fix_versions": [v.get("name") for v in issue_data.get("fields", {}).get("fixVersions", [])],
        "components": [c.get("name") for c in issue_data.get("fields", {}).get("components", [])],
        "labels": issue_data.get("fields", {}).get("labels", [])
    }
    
    return safe_data

async def generate_code_from_jira(issue_key: str, language: str, additional_requirements: str, ctx: Context) -> str:
    """Generate code based on Jira issue requirements with safe data handling"""
    await ctx.debug(f"Generating code from Jira issue: {issue_key}")
    
    issue_details = await get_jira_issue_details(issue_key, ctx)
    
    if not issue_details.get("description") and not additional_requirements:
        return "Error: Jira issue lacks description and no additional requirements provided. Please add more details to the issue or provide additional requirements."
    
    requirements_text = issue_details.get("description", "")
    summary_text = issue_details.get("summary", "")
    
    prompt = f"""
    Based on the following Jira issue requirements, generate {language} code:
    
    Issue Summary: {summary_text}
    Requirements: {requirements_text}
    Additional Requirements: {additional_requirements}
    
    Please generate clean, production-ready code that addresses these requirements.
    Include proper error handling, documentation, and follow best practices for {language}.
    """
    
    ai = get_ai_service()
    return ai.ask(prompt)