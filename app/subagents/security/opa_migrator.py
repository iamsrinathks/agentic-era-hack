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

def get_opa_migrator_agent():
    opa_migrator_agent = Agent(
        name="OpaMigratorAgent",
        model="gemini-2.5-flash",
        instruction="""You are a policy migration specialist. Your job is to migrate OPA Rego policies to Google Cloud custom Organization Policies for the product: {user:product_name}.

    You MUST follow this workflow:
    1.  Use the `get_contents` tool to find and read the Rego policies in the repository.
        - Expected `get_contents` return shape (MCP): {"content": "base64-encoded-file"} or {"files": [{"path": str, "content": str}]}
    2.  Translate the Rego policy to a custom Organization Policy.
    3.  Use the `push_multiple_files` tool to commit the new Organization Policy to the repository.
        - Expected `push_multiple_files` payload (MCP): {"branch": str, "files": [{"path": str, "content": str}], "message": str}
        - Expected return: {"status": "success" | "error", "details": ...}
    """
    )
    return opa_migrator_agent

opa_migrator_agent = get_opa_migrator_agent()



