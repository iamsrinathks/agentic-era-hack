from google.adk.agents import Agent
from google.adk.tools import google_search, VertexAiSearchTool
from .prompts import return_instructions_discovery_security
 
def get_discovery_security_agent():
    vertex_search_tool = VertexAiSearchTool(data_store_id="projects/339258993962/locations/global/collections/default_collection/dataStores/dds-discovery-agent-vai-ds")
 
    discovery_security_agent = Agent(
        name="DiscoverySecurityAgent",
        model="gemini-2.5-pro",
        instruction=return_instructions_discovery_security(),
        tools=[google_search, vertex_search_tool],
    )
    return discovery_security_agent

discovery_security_agent = get_discovery_security_agent()