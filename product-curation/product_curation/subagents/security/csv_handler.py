from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .org_policy_writer import get_org_policy_workflow_agent
from .sha_writer import get_sha_workflow_agent

def get_csv_handler_agent():
    """This function creates and returns the CsvHandlerAgent."""

    # Create instances of the agents that will be used as tools.
    org_policy_agent = get_org_policy_workflow_agent()
    sha_policy_agent = get_sha_workflow_agent()

    # The instruction for the CsvHandlerAgent's LLM. This instruction tells the
    # agent how to process the CSV content and when to call the sub-agent tools.
    instruction = """
    You are a CSV processing specialist. Your task is to process the content of an uploaded CSV file that the user provides.

    Here is your workflow:
    1. The user will upload a CSV file. The content of this file will be provided to you.
    2. You must parse this CSV content row by row.
    3. For each row, you MUST examine the 'Guardrail Type' column.
    4. Based on the 'Guardrail Type', you will call the appropriate tool:
        - If the 'Guardrail Type' contains 'Org Policy', you MUST call the 'OrgPolicyWorkflowAgent' tool.
        - If the 'Guardrail Type' contains 'SHA', you MUST call the 'ShaWorkflowAgent' tool.
    5. The input for these tools must be a descriptive prompt constructed from the other columns in the row. For example: "Generate a policy for [Control Title]: [Implementation Description]"
    6. You must call the correct tool for each and every row that has a valid 'Guardrail Type'.
    7. After you have called the tools for all the relevant rows, collect the results and present a summary to the user.
    """

    # The CsvHandlerAgent is an LLM agent that uses other agents as tools.
    csv_handler_agent = Agent(
        name="CsvHandlerAgent",
        model="gemini-2.5-flash",
        instruction=instruction,
        tools=[
            AgentTool(agent=org_policy_agent),
            AgentTool(agent=sha_policy_agent)
        ],
    )

    return csv_handler_agent