from google.adk.agents import Agent
from google.adk.tools import google_search, VertexAiSearchTool
from .prompts import return_instructions_product_overview
# TODO: Replace with your actual data store ID
 
def get_product_overview_agent():
    vertex_search_tool = VertexAiSearchTool(data_store_id="projects/339258993962/locations/global/collections/default_collection/dataStores/dds-discovery-agent-vai-ds")
 
    product_overview_agent = Agent(
        name="ProductOverviewAgent",
        model="gemini-2.5-pro",
        instruction=return_instructions_product_overview(),
        tools=[google_search, vertex_search_tool],
    )
    return product_overview_agent

product_overview_agent = get_product_overview_agent()
