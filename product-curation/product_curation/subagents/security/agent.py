import os
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import get_user_choice
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
from .org_policy_writer import get_org_policy_workflow_agent
from .sha_writer import get_sha_workflow_agent
from .opa_migrator import get_opa_migrator_agent
from .inspec_migrator import get_inspec_migrator_agent
from .prompts import return_instructions_main_security
from .csv_handler import get_csv_handler_agent
 
def get_security_agent():
    gitlab_base = os.getenv("GITLAB_BASE_URL") or os.getenv("GITLAB_MCP_URL")
    gitlab_token = os.getenv("GITLAB_TOKEN")
 
    gitlab_mcp = None
    agent_tools = []
 
    if gitlab_base and gitlab_token:
        auth_scheme, auth_credential = token_to_scheme_credential(
            "apikey", "header", "PRIVATE-TOKEN", gitlab_token
        )
        gitlab_mcp = McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=gitlab_base,
            ),
            auth_scheme=auth_scheme,
            auth_credential=auth_credential,
            errlog=None,
        )
        agent_tools.append(gitlab_mcp)
    else:
        print("Warning: GITLAB_BASE_URL or GITLAB_TOKEN not set; skipping GitLab MCPToolset")
 
    security_agent = Agent(
        name="SecurityAgent",
        model="gemini-2.5-flash",
        instruction=return_instructions_main_security(),
        tools=agent_tools,
        sub_agents=[
            get_org_policy_workflow_agent(),
            get_sha_workflow_agent(),
            get_opa_migrator_agent(),
            get_inspec_migrator_agent(),
            get_csv_handler_agent(),
        ],
    )
    return security_agent
 