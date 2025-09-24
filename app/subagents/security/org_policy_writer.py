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

from google.adk.agents import Agent, SequentialAgent
from app.tools.search_tools import SearchTool, ReadWebpageTool
import os
import re
from google.adk.tools import ToolContext
from app.subagents.security.prompts import return_instructions_org_policy_writer, return_instructions_terraform_module_generator


# Researcher Agent
org_policy_researcher_agent = Agent(
    name="OrgPolicyResearcherAgent",
    model="gemini-2.5-flash",
    instruction=return_instructions_terraform_module_generator(),
    tools=[SearchTool(), ReadWebpageTool()],
)

# Writer Agent
def write_org_policy_tf(multi_file_tf_string: str, tool_context: ToolContext) -> dict:
    """
    Writes one or more Terraform .tf files from a delimited string.

    Args:
        multi_file_tf_string: A string containing one or more Terraform blocks,
                              separated by '=== <filename>.tf ==='.
        tool_context: The context object for the tool.

    Returns:
        A dictionary with the status and a summary message.
    """
    output_dir = os.path.join(os.getcwd(), "output", "org_policies_tf")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Regex to find filenames like === filename.tf ===
    file_pattern = re.compile(r'===\s*([^=\s]+.tf)\s*===')
    file_delimiters = list(file_pattern.finditer(multi_file_tf_string))
    
    results = []
    for i, delimiter in enumerate(file_delimiters):
        filename = delimiter.group(1)
        start_index = delimiter.end()
        end_index = file_delimiters[i+1].start() if i + 1 < len(file_delimiters) else len(multi_file_tf_string)
        
        content = multi_file_tf_string[start_index:end_index].strip()
        output_path = os.path.join(output_dir, filename)

        try:
            with open(output_path, "w") as f:
                f.write(content)
            results.append(f"SUCCESS: Wrote '{output_path}'.")
        except Exception as e:
            results.append(f"FAILURE: Could not write file '{filename}'. Error: {e}")

    if not results:
        return {"status": "error", "message": "No valid Terraform file blocks were found in the input."}

    return {
        "status": "complete",
        "message": "\n".join(results)
    }


org_policy_writer_agent = Agent(
    name="OrgPolicyWriterAgent",
    model="gemini-2.5-flash",
    instruction=return_instructions_org_policy_writer(),
    tools=[write_org_policy_tf],
)

# Workflow Agent
org_policy_workflow_agent = SequentialAgent(
    name="OrgPolicyWorkflowAgent",
    sub_agents=[org_policy_researcher_agent, org_policy_writer_agent],
    description="A workflow agent that researches, generates, and saves all possible custom Organization Policies for a given product as Terraform module files.",
)
