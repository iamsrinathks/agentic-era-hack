# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, StreamableHTTPConnectionParams
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
from app.subagents.security.prompts import return_instructions_main_security
from app.subagents.security.org_policy_writer import get_org_policy_workflow_agent
from app.subagents.security.sha_writer import get_sha_workflow_agent
from app.subagents.security.opa_migrator import get_opa_migrator_agent
from app.subagents.security.inspec_migrator import get_inspec_migrator_agent

def get_security_agent():
    def _normalize_mcp_api_url(url: str | None) -> str | None:
        if not url:
            return None
        u = url.strip().rstrip("/")
        if u.endswith("/mcp/api"):
            return u
        if u.endswith("/mcp"):
            return u + "/api"
        if "/mcp" not in u:
            return u + "/mcp/api"
        return u

    gitlab_base = os.getenv("GITLAB_BASE_URL") or os.getenv("GITLAB_MCP_URL")
    gitlab_base = _normalize_mcp_api_url(gitlab_base)
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
        )
        agent_tools.append(gitlab_mcp)
    else:
        # Avoid constructing StreamableHTTPConnectionParams with a None url which
        # causes pydantic validation errors at import time. If GitLab MCP settings
        # are not present, skip adding the tool and continue with offline-only ops.
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
        ],
    )
    return security_agent

security_agent = get_security_agent()
