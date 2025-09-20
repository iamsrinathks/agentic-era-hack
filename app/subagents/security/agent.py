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
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
# from agent_era_hack.app.subagents.security.prompts import return_instructions_main_security
# from agent_era_hack.app.subagents.security.org_policy_writer import org_policy_workflow_agent
# from agent_era_hack.app.subagents.security.sha_writer import sha_workflow_agent
# from agent_era_hack.app.subagents.security.opa_migrator import opa_migrator_agent
# from agent_era_hack.app.subagents.security.inspec_migrator import inspec_migrator_agent
from app.subagents.security.prompts import return_instructions_main_security
from app.subagents.security.org_policy_writer import org_policy_workflow_agent
from app.subagents.security.sha_writer import sha_workflow_agent
from app.subagents.security.opa_migrator import opa_migrator_agent
from app.subagents.security.inspec_migrator import inspec_migrator_agent

auth_scheme, auth_credential = token_to_scheme_credential(
    "apikey", "header", "PRIVATE-TOKEN", os.getenv("GITLAB_TOKEN")
)

gitlab_mcp = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=os.getenv("GITLAB_BASE_URL"),
    ),
    auth_scheme=auth_scheme,
    auth_credential=auth_credential,
)

security_agent = Agent(
    name="SecurityAgent",
    model="gemini-2.5-flash",
    instruction=return_instructions_main_security(),
    tools=[gitlab_mcp],
    sub_agents=[
        org_policy_workflow_agent,
        sha_workflow_agent,
        opa_migrator_agent,
        inspec_migrator_agent,
    ],
)
