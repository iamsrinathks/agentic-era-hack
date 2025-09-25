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
from google.adk.agents import Agent, SequentialAgent, ParallelAgent
from google.adk.tools import get_user_choice
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential

# Import sub-agents
from app.subagents.discovery.product_overview import get_product_overview_agent
from app.subagents.discovery.discovery_infrastructure import get_discovery_infrastructure_agent
from app.subagents.discovery.discovery_security import get_discovery_security_agent
from app.subagents.discovery.discovery_networking import get_discovery_networking_agent
from app.subagents.discovery.recritic import get_recritic_agent
from app.subagents.discovery.prompts import return_instructions_discovery_orchestrator
from app.subagents.discovery.hitl import create_confluence_page

def get_discovery_agent():
    # Define the research unit
    research_and_critique_agent = SequentialAgent(
        name="ResearchAndCritiqueAgent",
        description="Runs a detailed analysis of a product and produces a draft report. Takes the product name and user feedback as input.",
        sub_agents=[
            ParallelAgent(
                name="ResearchAgents",
                sub_agents=[
                    get_product_overview_agent(),
                    get_discovery_infrastructure_agent(),
                    get_discovery_security_agent(),
                    get_discovery_networking_agent(),
                ],
            ),
            get_recritic_agent(),
        ],
    )

    confluence_mcp = None
    conf_url = os.getenv("CONFLUENCE_MCP_URL")
    conf_pat = os.getenv("CONFLUENCE_PAT")

    def _normalize_mcp_api_url(url: str | None) -> str | None:
        if not url:
            return None
        u = url.strip()
        # remove trailing slash
        u = u.rstrip("/")
        # if already endswith /mcp/api keep
        if u.endswith("/mcp/api"):
            return u
        # if endswith /mcp, convert to /mcp/api
        if u.endswith("/mcp"):
            return u + "/api"
        # if user provided only host (no path), append /mcp/api
        if "/mcp" not in u:
            return u + "/mcp/api"
        # otherwise leave as-is
        return u

    # conf_url = _normalize_mcp_api_url(conf_url)

    if conf_url and conf_pat:
        auth_scheme, auth_credential = token_to_scheme_credential(
            "apikey", "header", "Authorization", f"Bearer {conf_pat}"
        )
        confluence_mcp = McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=conf_url,
            ),
            auth_scheme=auth_scheme,
            auth_credential=auth_credential,
            errlog=None,
        )
    else:
        print("Warning: CONFLUENCE_MCP_URL or CONFLUENCE_PAT not set; Confluence MCP tool will not be available.")

    # Define the main orchestrator agent
    discovery_agent = Agent(
        name="DiscoveryAgent",
        model="gemini-2.5-pro",
        instruction=return_instructions_discovery_orchestrator(),
        tools=[
            AgentTool(research_and_critique_agent),
            get_user_choice,
            create_confluence_page,
        ] + ([confluence_mcp] if confluence_mcp is not None else []),
        description="Orchestrates the product discovery, human-in-the-loop feedback, and final reporting.",
    )
    return discovery_agent

discovery_agent = get_discovery_agent()