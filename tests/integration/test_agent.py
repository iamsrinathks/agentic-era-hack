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

# mypy: disable-error-code="union-attr"
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent


def test_agent_stream() -> None:
    """
    Integration test for the agent stream functionality.
    Tests that the agent returns valid streaming responses.
    """

    session_service = InMemorySessionService()

    session = session_service.create_session_sync(user_id="test_user", app_name="test")
    runner = Runner(agent=root_agent, session_service=session_service, app_name="test")

    # Turn 1: Initial greeting
    message1 = types.Content(role="user", parts=[types.Part.from_text(text="Hello")])
    events1 = list(
        runner.run(
            new_message=message1,
            user_id="test_user",
            session_id=session.id,
            run_config=RunConfig(streaming_mode=StreamingMode.SSE),
        )
    )
    assert len(events1) > 0, "Expected at least one message"

    response1 = ""
    for event in events1:
        if (
            event.content
            and event.content.parts
            and any(part.text for part in event.content.parts)
        ):
            response1 += event.content.parts[0].text

    assert "product" in response1.lower(), f"Expected agent to ask for a product name, but got: {response1}"

    # Turn 2: Provide product name
    message2 = types.Content(role="user", parts=[types.Part.from_text(text="Data Fusion")])
    events2 = list(
        runner.run(
            new_message=message2,
            user_id="test_user",
            session_id=session.id,
            run_config=RunConfig(streaming_mode=StreamingMode.SSE),
        )
    )
    assert len(events2) > 0, "Expected at least one message"

    response2 = ""
    for event in events2:
        if (
            event.content
            and event.content.parts
            and any(part.text for part in event.content.parts)
        ):
            response2 += event.content.parts[0].text

    assert "discovery" in response2.lower(), f"Expected agent to ask for next action, but got: {response2}"
    assert "security" in response2.lower(), f"Expected agent to ask for next action, but got: {response2}"
    assert "infra" in response2.lower(), f"Expected agent to ask for next action, but got: {response2}"
