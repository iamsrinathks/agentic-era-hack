from google.adk.agents import Agent
from .prompts import return_instructions_recritic
 
def get_recritic_agent():
    with open("product_curation/subagents/discovery/docs/discovery_questionnaire_template.md", "r") as f:
        template = f.read()
 
    recritic_agent = Agent(
        name="ReCriticAgent",
        model="gemini-2.5-pro",
        instruction=return_instructions_recritic(template),
    )
    return recritic_agent

recritic_agent = get_recritic_agent()