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

import google.auth
from google.adk.agents import Agent
from google.adk.tools import ToolContext
from app.subagents.discovery.agent import discovery_agent
from app.subagents.security.agent import security_agent
from app.subagents.infra.agent import infra_agent
from app.prompts import return_instructions_root


_, project_id = google.auth.default()
if not project_id:
    project_id = os.environ.get("GCLOUD_PROJECT")
if not project_id:
    raise ValueError(
        "Could not determine Google Cloud project. "
        "Set the GCLOUD_PROJECT environment variable or run "
        "'gcloud auth application-default login'."
    )
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


def save_product_name(product_name: str, tool_context: ToolContext) -> dict:
    """Saves the product name to the user's session state."""
    tool_context.state["user:product_name"] = product_name
    return {"status": "success"}


root_agent = Agent(
    name="csp_product_curation_agent",
    model="gemini-2.5-pro",
    instruction=return_instructions_root(),
    tools=[save_product_name],
    sub_agents=[discovery_agent, security_agent, infra_agent],
)
