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
from google.adk.tools import get_user_choice, ToolContext

def create_confluence_page(report: str, tool_context: ToolContext) -> dict:
    """Creates a Confluence page with the given report.

    Expected payload:
        report: str -- markdown or HTML report to publish

    Returns:
        dict: {
            "status": "success" | "error",
            "message": str,
            "page_id": Optional[str]
        }

    Note: This is a placeholder implementation for local testing. Replace or
    wire this function to the MCP Confluence toolset when running in production.
    """
    # This is a placeholder for the actual MCP tool to create a Confluence page.
    # You will need to replace this with your actual implementation.
    import time
    start = time.time()
    print("[tool] create_confluence_page START")
    print(f"Creating Confluence page with the following report:\n{report}")
    duration = time.time() - start
    print(f"[tool] create_confluence_page END elapsed={duration:.3f}s")
    return {"status": "success", "message": "Confluence page created successfully."}


hitl_agent = Agent(
    name="HITLAgent",
    model="gemini-2.5-pro",
    instruction="""You are a Human-in-the-Loop agent. Your job is to present the generated report to the user and ask for their choice.
You must use the `get_user_choice` tool to get the user's choice.
The choices are "Approve" or "Provide Feedback".
If the user provides feedback, you must save it to the session state under the key `user_feedback`. """,
    tools=[get_user_choice],
)

confluence_agent = Agent(
    name="ConfluenceAgent",
    model="gemini-2.5-pro",
    instruction="You are a Confluence agent. Your job is to create a Confluence page with the approved report.",
    tools=[create_confluence_page],
)