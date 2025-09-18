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

from google.adk.agents import Agent, SequentialAgent, ParallelAgent
from google.adk.tools import get_user_choice
from google.adk.tools.agent_tool import AgentTool

# Import sub-agents
from app.subagents.discovery.product_overview import product_overview_agent
from app.subagents.discovery.discovery_infrastructure import discovery_infrastructure_agent
from app.subagents.discovery.discovery_security import discovery_security_agent
from app.subagents.discovery.discovery_networking import discovery_networking_agent
from app.subagents.discovery.recritic import recritic_agent
from app.subagents.discovery.confluence import confluence_agent
from app.subagents.discovery.prompts import return_instructions_discovery_orchestrator

# Define the research unit
research_and_critique_agent = SequentialAgent(
    name="ResearchAndCritiqueAgent",
    description="Runs a detailed analysis of a product and produces a draft report. Takes the product name and user feedback as input.",
    sub_agents=[
        ParallelAgent(
            name="ResearchAgents",
            sub_agents=[
                product_overview_agent,
                discovery_infrastructure_agent,
                discovery_security_agent,
                discovery_networking_agent,
            ],
        ),
        recritic_agent,
    ],
)

# Define the main orchestrator agent
discovery_agent = Agent(
    name="DiscoveryAgent",
    model="gemini-2.5-pro",
    instruction=return_instructions_discovery_orchestrator(),
    tools=[
        AgentTool(research_and_critique_agent),
        AgentTool(confluence_agent),
        get_user_choice,
    ],
    description="Orchestrates the product discovery, human-in-the-loop feedback, and final reporting.",
)
