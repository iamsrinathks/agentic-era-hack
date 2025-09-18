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
from google.adk.tools import ToolContext

def create_confluence_page(report: str, tool_context: ToolContext) -> dict:
    """Creates a Confluence page with the given report and signals that the discovery process is complete."""
    # This is a placeholder for the actual MCP tool to create a Confluence page.
    # You will need to replace this with your actual implementation.
    print(f"Creating Confluence page with the following report:\n{report}")
    tool_context.state["confluence_page_created"] = True
    
    # Signal to the runner to hand control back to the parent agent.
    tool_context.actions.transfer_to_parent = True
    
    return {"status": "success", "message": "Confluence page created successfully. The discovery process is now complete and I am returning you to the main menu."}

confluence_agent = Agent(
    name="ConfluenceAgent",
    model="gemini-2.5-flash",
    description="Creates a Confluence page with an approved report.",
    instruction="You are a Confluence agent. Your job is to create a Confluence page with the approved report provided to you. You must use the `create_confluence_page` tool.",
    tools=[create_confluence_page],
)