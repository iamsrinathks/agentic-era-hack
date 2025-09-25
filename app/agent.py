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

import os

import google.auth
from google.adk.agents import Agent
from google.adk.tools import ToolContext
from app.subagents.discovery.agent import get_discovery_agent
from app.subagents.security.agent import get_security_agent
from app.prompts import return_instructions_root
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams

# Instead of monkeypatching internals, add a logging Filter to suppress
# the noisy OpenTelemetry "Failed to detach context" ValueError logs that
# appear when tokens created in one async context are detached in another.
# This keeps OpenTelemetry behavior unchanged while preventing noisy errors
# in logs when running in Agent Engine.
try:
    import logging

    class _OtelDetachFilter(logging.Filter):
        """Filter out ValueError tracebacks from OpenTelemetry detach failures.

        Matches the known error substring emitted by the OpenTelemetry helper
        that logs the 'Failed to detach context' message. This is a non-invasive
        approach suitable for production deployments.
        """

        def filter(self, record: logging.LogRecord) -> bool:  # pragma: no cover - logging only
            try:
                msg = record.getMessage()
            except Exception:
                return True
            # If the message contains the specific 'Failed to detach context'
            # indicator, drop it. Otherwise, keep the log record.
            if "Failed to detach context" in msg and "was created in a different Context" in msg:
                return False
            return True

    # Attach the filter to the opentelemetry logger if present.
    _otel_logger = logging.getLogger("opentelemetry")
    _otel_logger.addFilter(_OtelDetachFilter())
except Exception:
    # If logging or opentelemetry logger is unavailable, do nothing.
    pass

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

# Emit sanitized env info at startup to help diagnose MCP URL misconfiguration
try:
    import logging

    _startup_logger = logging.getLogger("agent.startup")

    def _mask_token_present(val: str) -> str:
        return "<set>" if val else "<not-set>"

    conf_mcp = os.getenv("CONFLUENCE_MCP_URL", "")
    conf_pat = os.getenv("CONFLUENCE_PAT", "")
    gitlab_base = os.getenv("GITLAB_BASE_URL", os.getenv("GITLAB_MCP_URL", ""))
    gitlab_token = os.getenv("GITLAB_TOKEN", "")

    _startup_logger.info("ENV: CONFLUENCE_MCP_URL=%s", conf_mcp or "<not-set>")
    _startup_logger.info("ENV: CONFLUENCE_PAT set=%s", _mask_token_present(conf_pat))
    _startup_logger.info("ENV: GITLAB_BASE_URL=%s", gitlab_base or "<not-set>")
    _startup_logger.info("ENV: GITLAB_TOKEN set=%s", _mask_token_present(gitlab_token))
    _startup_logger.info("Note: MCP stream API must be at '/mcp/api' (POST). '/mcp' is human GET-only page.")
except Exception:
    pass


def save_product_name(product_name: str, tool_context: ToolContext) -> dict:
    """Saves the product name to the user's session state.

    Expected payload:
        product_name: str

    Returns:
        dict: {"status": "success"} on success.
    Side effects:
        Persists value at tool_context.state['user:product_name'].
    """
    import time
    start = time.time()
    print(f"[tool] save_product_name START product_name={product_name}")
    tool_context.state["user:product_name"] = product_name
    duration = time.time() - start
    print(f"[tool] save_product_name END elapsed={duration:.3f}s")
    return {"status": "success"}


discovery_agent = get_discovery_agent()
security_agent = get_security_agent()

confluence_mcp_url = os.getenv("CONFLUENCE_MCP_URL", "http://0.0.0.0:8088/mcp")
confluence_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=confluence_mcp_url,
        headers_to_pass={"Authorization": f"Bearer {os.getenv('CONFLUENCE_PAT', '')}"},
    ),
    errlog=None,
)

root_agent = Agent(
    name="csp_product_curation_agent",
    model="gemini-2.5-pro",
    instruction=return_instructions_root(),
    tools=[save_product_name, confluence_toolset],
    sub_agents=[discovery_agent, security_agent],
    description="Orchestrates the product discovery, human-in-the-loop feedback, and final reporting.",
)