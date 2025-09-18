"""
Script to package and deploy the Product Discovery Agent to VertexAI Agent Engine.
# Copyright 2025 Google LLC
# Licensed under the Apache License, Version 2.0
# Copyright 2025 Google LLC
# Licensed under the Apache License, Version 2.0
deploy_vertexai_agent.py
Script to deploy the Product Discovery Agent to VertexAI Agent Engine.
"""
 
# Copyright 2025 Google LLC
# Licensed under the Apache License, Version 2.0
 
import os
from absl import app, flags
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp
 
load_dotenv()
 
FLAGS = flags.FLAGS
flags.DEFINE_string("project_id", None, "GCP project ID.")
flags.DEFINE_string("location", None, "GCP location.")
flags.DEFINE_string("bucket", None, "GCP bucket.")
flags.DEFINE_string("resource_id", None, "ReasoningEngine resource ID.")
flags.DEFINE_bool("create", False, "Create a new agent.")
flags.DEFINE_bool("delete", False, "Delete an existing agent.")
flags.mark_bool_flags_as_mutual_exclusive(["create", "delete"])
 
# Import the orchestrator/root agent
from agentic_era_hack.app.agent import root_agent
 
def create(env_vars: dict) -> None:
    adk_app = AdkApp(
        agent=root_agent,
        enable_tracing=True,
    )
 
    extra_packages = ["./agentic_era_hack"]
 
    remote_agent = agent_engines.create(
        adk_app,
        requirements=[
            "google-adk>=1.10.0",
            "google-cloud-aiplatform[agent_engines]>=1.93.0",
            "pydantic",
            "requests",
            "python-dotenv",
            "google-genai",
            "absl-py",
            "bs4"
        ],
        extra_packages=extra_packages,
        env_vars=env_vars,
    )
    print(f"Created remote agent: {remote_agent.resource_name}")
 
def delete(resource_id: str) -> None:
    remote_agent = agent_engines.get(resource_id)
    remote_agent.delete(force=True)
    print(f"Deleted remote agent: {resource_id}")
 
def main(argv: list[str]) -> None:
    # Prefer CLI flags, then environment variables (including .env)
    project_id = FLAGS.project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
    location = FLAGS.location or os.getenv("GOOGLE_CLOUD_LOCATION")
    bucket = FLAGS.bucket or os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
    env_vars = {}
 
    print(f"PROJECT: {project_id}")
    print(f"LOCATION: {location}")
    print(f"BUCKET: {bucket}")
 
    if not project_id:
        print("Missing required environment variable: GOOGLE_CLOUD_PROJECT")
        return
    elif not location:
        print("Missing required environment variable: GOOGLE_CLOUD_LOCATION")
        return
    elif not bucket:
        print("Missing required environment variable: GOOGLE_CLOUD_STORAGE_BUCKET")
        return
 
    env_vars["DISABLE_WEB_DRIVER"] = "1"
 
    vertexai.init(
        project=project_id,
        location=location,
        staging_bucket=f"gs://{bucket}",
    )
 
    if FLAGS.create:
        create(env_vars)
    elif FLAGS.delete:
        if not FLAGS.resource_id:
            print("resource_id is required for delete")
            return
        delete(FLAGS.resource_id)
    else:
        print("Unknown command. Use --create or --delete.")
 
if __name__ == "__main__":
    app.run(main)
 