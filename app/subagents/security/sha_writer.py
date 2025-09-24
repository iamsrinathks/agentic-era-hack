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
import json
from google.adk.tools import ToolContext

# Researcher Agent
sha_researcher_agent = Agent(
    name="ShaResearcherAgent",
    model="gemini-2.5-flash",
    instruction="""You are an autonomous research and coding agent. Your sole purpose is to generate JSON configurations for all possible Security Health Analytics custom modules for the product: {user:product_name}.

You MUST follow this workflow precisely. Do not deviate.
1.  Your first action is to use the `search` tool to find the official Google Cloud documentation that lists all available detectors for Security Health Analytics custom modules related to the product '{user:product_name}'.
2.  From the search results, use the `read_webpage` tool to read the content of the most relevant documentation page.
3.  From the webpage content, you MUST identify every single available detector.
4.  For each and every detector you find, you MUST generate a complete, valid JSON file. You MUST NOT generate YAML or HCL.
5.  The JSON format MUST be exactly as follows, with correct JSON syntax:
    ```json
    {{
      "display_name": "A display name for the custom module",
      "description": "A description of the custom module.",
      "custom_config": {{
        "predicate": {{
          "expression": "resource.service_account.email == \"your-service-account@your-project.iam.gserviceaccount.com\""
        }},
        "resource_selector": {{
          "resource_types": ["iam.googleapis.com/ServiceAccount"]
        }},
        "severity": "HIGH",
        "recommendation": "A recommendation for the user."
      }}
    }}
    ```
6.  You MUST then combine all of the generated JSON files into a single string. Each JSON block MUST be separated by a file delimiter line, like this: `=== detector_name.json ===`
7.  Your final output MUST be only this multi-file string. Do not add any conversational text or explanations.
""",
    tools=[SearchTool(), ReadWebpageTool()],
)

# Writer Agent
def write_sha_policy_json(multi_file_json_string: str, tool_context: ToolContext) -> dict:
    """
    Writes one or more JSON files for SHA custom modules from a delimited string.

    Args:
        multi_file_json_string: A string containing one or more JSON blocks,
                                separated by '=== <filename>.json ==='.
        tool_context: The context object for the tool.

    Returns:
        A dictionary with the status and a summary message.
    """
    output_dir = os.path.join(os.getcwd(), "output", "sha_policies_json")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Regex to find filenames like === filename.json ===
    file_pattern = re.compile(r'===\s*([^=\s]+.json)\s*===')
    file_delimiters = list(file_pattern.finditer(multi_file_json_string))
    
    results = []
    for i, delimiter in enumerate(file_delimiters):
        filename = delimiter.group(1)
        start_index = delimiter.end()
        end_index = file_delimiters[i+1].start() if i + 1 < len(file_delimiters) else len(multi_file_json_string)
        
        content = multi_file_json_string[start_index:end_index].strip()
        output_path = os.path.join(output_dir, filename)

        try:
            # Validate that the content is valid JSON
            json.loads(content)
            with open(output_path, "w") as f:
                f.write(content)
            results.append(f"SUCCESS: Wrote '{output_path}'.")
        except json.JSONDecodeError as e:
            results.append(f"FAILURE: Invalid JSON content for '{filename}'. Error: {e}")
        except Exception as e:
            results.append(f"FAILURE: Could not write file '{filename}'. Error: {e}")

    if not results:
        return {"status": "error", "message": "No valid JSON file blocks were found in the input."}

    return {
        "status": "complete",
        "message": "\n".join(results)
    }


sha_writer_agent = Agent(
    name="ShaWriterAgent",
    model="gemini-2.5-flash",
    instruction="You are a policy writer. Your job is to take the provided multi-file JSON string and use the `write_sha_policy_json` tool to save each policy to its own .json file.",
    tools=[write_sha_policy_json],
)

# Workflow Agent
sha_workflow_agent = SequentialAgent(
    name="ShaWorkflowAgent",
    sub_agents=[sha_researcher_agent, sha_writer_agent],
    description="A workflow agent that researches, generates, and saves all possible custom Security Health Analytics modules for a given product as JSON files.",
)