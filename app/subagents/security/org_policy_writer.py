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
#from agent_era_hack.app.tools.search_tools import SearchTool, ReadWebpageTool
from app.tools.search_tools import SearchTool, ReadWebpageTool
import os
import re
from google.adk.tools import ToolContext

# Researcher Agent
org_policy_researcher_agent = Agent(
    name="OrgPolicyResearcherAgent",
    model="gemini-2.5-flash",
    instruction="""You are an autonomous research and coding agent. Your sole purpose is to generate Terraform module blocks for all possible custom Organization Policies for the product: {user:product_name}.

You MUST follow this workflow precisely. Do not deviate.
1.  Your first action is to use the `search` tool to find the official Google Cloud documentation page that lists all available custom Organization Policy constraints for the product '{user:product_name}'.
2.  From the search results, use the `read_webpage` tool to read the content of the most relevant documentation page.
3.  From the webpage content, you MUST identify every single available constraint.
4.  For each and every constraint you find, you MUST generate a complete, valid Terraform module block. You MUST NOT generate YAML.
5.  The Terraform format MUST be exactly as follows, with correct HCL syntax and indentation:
    ```terraform
    module "org_policy_the_policy_name" {{
      source      = "terraform-google-modules/org-policy/google"
      constraint  = "customConstraints/custom.ConstraintName"
      title       = "A display name for the constraint"
      description = "A description of the constraint."
      expression  = <<CEL
    resource.cel_expression_goes_here == true
    CEL
    }}
    ```
6.  You MUST then combine all of the generated module blocks into a single string. Each block MUST be separated by a file delimiter line, like this: `=== org_policy_the_policy_name.tf ===`
7.  Your final output MUST be only this multi-file string. Do not add any conversational text or explanations.
""",
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
    instruction="You are a policy writer. Your job is to take the provided multi-file Terraform string and use the `write_org_policy_tf` tool to save each policy to its own .tf file.",
    tools=[write_org_policy_tf],
)

# Workflow Agent
org_policy_workflow_agent = SequentialAgent(
    name="OrgPolicyWorkflowAgent",
    sub_agents=[org_policy_researcher_agent, org_policy_writer_agent],
    description="A workflow agent that researches, generates, and saves all possible custom Organization Policies for a given product as Terraform module files.",
)
