import asyncio
import json
from typing import Any, Dict

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types

from app.agent import root_agent

app = FastAPI()


def sse_event(payload: Dict[str, Any]) -> bytes:
    return f"data: {json.dumps(payload)}\n\n".encode("utf-8")


@app.post("/run_sse")
async def run_sse(request: Request):
    """
    Lightweight SSE wrapper for local ADK Runner.

    Expects payload matching LocalBackendPayload:
    {
      "appName": "app",
      "userId": "user",
      "sessionId": "session",
      "newMessage": { parts: [{ text: "..." }], role: "user" },
      "streaming": true
    }
    """

    body = await request.json()

    try:
        user_id = body.get("userId") or body.get("user_id")
        session_id = body.get("sessionId") or body.get("session_id")
        new_message = body.get("newMessage") or body.get("new_message")
        if not user_id or not session_id or not new_message:
            raise HTTPException(status_code=400, detail="Missing required fields")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Build runner and session service
    session_service = InMemorySessionService()
    await session_service.create_session(app_name="app", user_id=user_id, session_id=session_id)

    runner = Runner(agent=root_agent, app_name="app", session_service=session_service)

    # Construct genai content
    parts = new_message.get("parts", [])
    text_parts = [p.get("text", "") for p in parts if isinstance(p, dict)]
    user_text = "\n".join(text_parts)

    async def event_generator():
        try:
            async for event in runner.run_async(
                user_id=user_id,
                session_id=session_id,
                new_message=genai_types.Content(role="user", parts=[genai_types.Part.from_text(text=user_text)])
            ):
                # Each event may contain content.parts. Emit each part as its own SSE data event
                if event.content and getattr(event.content, "parts", None):
                    for part in event.content.parts:
                        part_payload = {
                            "content": {"parts": []},
                            "author": getattr(event, "author", None) or body.get("appName") or "discovery_agent",
                        }

                        # Map part fields (text, thought, function_call, function_response) if present
                        p: Dict[str, Any] = {}
                        if getattr(part, "text", None):
                            p["text"] = getattr(part, "text")
                        # ADK Part shape may not expose thought flag; include if present
                        if getattr(part, "thought", None) is not None:
                            p["thought"] = getattr(part, "thought")
                        # function call/response may be nested attributes
                        if getattr(part, "function_call", None):
                            p["function_call"] = getattr(part, "function_call")
                        if getattr(part, "function_response", None):
                            p["function_response"] = getattr(part, "function_response")

                        part_payload["content"]["parts"].append(p)

                        yield sse_event(part_payload)

                # If the event is final, emit metadata about completion
                if getattr(event, "is_final_response", lambda: False)():
                    meta = {
                        "author": getattr(event, "author", None) or body.get("appName") or "discovery_agent",
                        "isFinal": True,
                    }
                    yield sse_event(meta)

        except Exception as e:
            # Emit error event then close
            error_payload = {"content": {"parts": [{"text": f"Error: {str(e)}"}]} , "author": "error"}
            yield sse_event(error_payload)

    return StreamingResponse(event_generator(), media_type="text/event-stream")
