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
from app.subagents.security.prompts import return_instructions_sha_researcher, return_instructions_sha_writer
# Researcher Agent
sha_researcher_agent = Agent(
    name="ShaResearcherAgent",
    model="gemini-2.5-flash",
    instruction=return_instructions_sha_researcher(),
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
    instruction=return_instructions_sha_writer(),
    tools=[write_sha_policy_json],
)

# Workflow Agent
sha_workflow_agent = SequentialAgent(
    name="ShaWorkflowAgent",
    sub_agents=[sha_researcher_agent, sha_writer_agent],
    description="A workflow agent that researches, generates, and saves all possible custom Security Health Analytics modules for a given product as JSON files.",
)