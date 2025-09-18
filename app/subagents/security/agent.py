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

from google.adk.agents import Agent
from agent_era_hack.app.subagents.security.prompts import return_instructions_main_security
from agent_era_hack.app.subagents.security.org_policy_writer import org_policy_workflow_agent
from agent_era_hack.app.subagents.security.sha_writer import sha_workflow_agent
from agent_era_hack.app.subagents.security.opa_migrator import opa_migrator_agent
from agent_era_hack.app.subagents.security.inspec_migrator import inspec_migrator_agent
from toolbox_core import ToolboxSyncClient
import os

# Initialize Toolbox client
github_mcp_url = os.environ["GITHUB_MCP_URL"]
github_toolbox = ToolboxSyncClient(github_mcp_url)

# Load all the tools from toolset
github_tools = github_toolbox.load_toolset("github_toolset")

security_agent = Agent(
    name="SecurityAgent",
    model="gemini-2.5-flash",
    instruction=return_instructions_main_security(),
    tools=[github_tools],
    sub_agents=[
        org_policy_workflow_agent,
        sha_workflow_agent,
        opa_migrator_agent,
        inspec_migrator_agent,
    ],
)
