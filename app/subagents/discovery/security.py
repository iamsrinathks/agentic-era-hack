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
from google.adk.tools import google_search, VertexAiSearchTool
from app.subagents.discovery.prompts import return_instructions_security

# TODO: Replace with your actual data store ID
vertex_search_tool = VertexAiSearchTool(data_store_id="YOUR_DATA_STORE_ID")

security_agent = Agent(
    name="SecurityAgent",
    model="gemini-2.5-pro",
    instruction=return_instructions_security(),
    tools=[google_search, vertex_search_tool],
)