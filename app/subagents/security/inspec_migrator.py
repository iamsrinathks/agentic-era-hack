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
from app.subagents.security.prompts import return_instructions_inspec_migrator
 

def migrate_inspec_to_sha(inspec_policy_path: str, tool_context: ToolContext) -> dict:
    """Migrates a Chef Inspec policy to a custom SHA policy."""
    # Placeholder for actual implementation
    print(f"Migrating Inspec policy from '{inspec_policy_path}' to a new SHA Policy.")
    # In a real implementation, you would read the file, translate the logic,
    # and then use a tool to write the new policy.
    return {"status": "success", "message": f"Migration of '{inspec_policy_path}' initiated."}

inspec_migrator_agent = Agent(
    name="InspecMigratorAgent",
    model="gemini-2.5-flash",
    instruction=return_instructions_inspec_migrator(),
    tools=[migrate_inspec_to_sha],
)
