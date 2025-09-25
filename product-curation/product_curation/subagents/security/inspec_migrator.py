from google.adk.agents import Agent
from google.adk.tools import ToolContext
from .prompts import return_instructions_inspec_migrator
 
def migrate_inspec_to_sha(inspec_policy_path: str, tool_context: ToolContext) -> dict:
    """Migrates a Chef Inspec policy to a custom SHA policy."""
    # Placeholder for actual implementation
    print(f"Migrating Inspec policy from '{inspec_policy_path}' to a new SHA Policy.")
    # In a real implementation, you would read the file, translate the logic,
    # and then use a tool to write the new policy.
    return {"status": "success", "message": f"Migration of '{inspec_policy_path}' initiated."}
 
def get_inspec_migrator_agent():
    inspec_migrator_agent = Agent(
        name="InspecMigratorAgent",
        model="gemini-2.5-flash",
        instruction=return_instructions_inspec_migrator()
    )
    return inspec_migrator_agent