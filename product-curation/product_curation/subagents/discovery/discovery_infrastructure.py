from google.adk.agents import Agent
from google.adk.tools import google_search, VertexAiSearchTool
from google.adk.tools.agent_tool import AgentTool
 
from .prompts import return_instructions_discovery_infrastructure
 
 
def get_discovery_infrastructure_agent():
    vertex_search_tool = VertexAiSearchTool(data_store_id="projects/339258993962/locations/global/collections/default_collection/dataStores/dds-discovery-agent-vai-ds")
 
    discovery_infrastructure_agent = Agent(
        name="DiscoveryInfrastructureAgent",
        model="gemini-2.5-pro",
        instruction=return_instructions_discovery_infrastructure(),
        tools=[google_search, vertex_search_tool],
    )
    return discovery_infrastructure_agent

discovery_infrastructure_agent = get_discovery_infrastructure_agent()