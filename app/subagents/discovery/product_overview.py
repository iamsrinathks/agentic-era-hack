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
from agent_era_hack.app.subagents.discovery.prompts import return_instructions_product_overview

# TODO: Replace with your actual data store ID
vertex_search_tool = VertexAiSearchTool(data_store_id="projects/421445844116/locations/us/collections/default_collection/dataStores/curation-csp-datastore_1758067422268")

product_overview_agent = Agent(
    name="ProductOverviewAgent",
    model="gemini-2.5-pro",
    instruction=return_instructions_product_overview(),
    tools=[google_search, vertex_search_tool],
)