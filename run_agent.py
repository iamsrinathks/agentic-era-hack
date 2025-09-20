import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from app.agent import root_agent
from google.genai import types as genai_types


async def main():
    """Runs the agent with a sample query."""
    session_service = InMemorySessionService()
    session_id = "test_session"
    
    # Set initial state when creating the session
    initial_state = {"user:product_name": "AlloyDB"}
    await session_service.create_session(
        app_name="app", user_id="test_user", session_id=session_id, state=initial_state
    )

    runner = Runner(
        agent=root_agent, app_name="app", session_service=session_service
    )
    query = "Retry publishing the report"
    async for event in runner.run_async(
        user_id="test_user",
        session_id=session_id,
        new_message=genai_types.Content(
            role="user", 
            parts=[genai_types.Part.from_text(text=query)]
        ),
    ):
        if event.is_final_response():
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())