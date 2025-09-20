from google.adk.agents import Agent
from google.adk.client import AgentSpaceClient

# Env-style variables from your setup
PROJECT_ID = "sap-genai-playground-dev-mg"
PROJECT_NUMBER = "339258993962"
AS_APP = "product-curation_1758207367653"
AS_LOCATION = "us"
AGENT_DISPLAY_NAME = "product-curation"
AGENT_DESCRIPTION = ("This agent assists users in discovering relevant "
                     "information, answering queries, and providing "
                     "recommendations based on curated data sources "
                     "within the Discovery Agent framework.")
REASONING_ENGINE_ID = "378412319861899264"
REASONING_ENGINE_LOCATION = "us-central1"

# Full resource name of your Reasoning Engine
REASONING_ENGINE = (
    f"projects/{PROJECT_ID}/locations/{REASONING_ENGINE_LOCATION}/reasoningEngines/{REASONING_ENGINE_ID}"
)

# Create ADK Agent definition
agent = Agent(
    display_name=AGENT_DISPLAY_NAME,
    description=AGENT_DESCRIPTION,
    icon_uri="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg",
    adk_agent_definition={
        "tool_settings": {
            "toolDescription": AGENT_DESCRIPTION,
        },
        "provisioned_reasoning_engine": {
            "reasoningEngine": REASONING_ENGINE,
        },
    },
)

# Create a client pointing to your AgentSpace App
client = AgentSpaceClient(
    project_number=PROJECT_NUMBER,
    location=AS_LOCATION,
    engine_id=AS_APP,
    assistant_id="default_assistant",  # fixed for now
)

# Deploy (create) the agent in AgentSpace
response = client.create_agent(agent)

print("✅ Agent deployed successfully:")
print(response)