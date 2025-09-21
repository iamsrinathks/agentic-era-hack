# Agent Codebase Summary: CSP Product Curation Agent

## 1. Overview

This document provides a summary of the `csp_product_curation_agent` codebase.
The agent is designed to assist with the product curation process for Google Cloud products.
It is a multi-agent system that uses a hierarchical approach to delegate tasks to specialized sub-agents.

## 2. Codebase Structure

The codebase is organized into the following directories:
- `app`: Contains the main agent and sub-agent definitions.
- `deployment`: Contains scripts and configuration for deploying the agent.
- `tests`: Contains unit and integration tests for the agent.

### 2.1. Root Agent

The root agent is defined in `app/agent.py`. It is responsible for:
- Greeting the user and asking for the product name.
- Delegating tasks to the `discovery` and `security` sub-agents.

### 2.2. Sub-agents

The agent has two main sub-agents:
- **Discovery Agent**: Performs a discovery on the product, including product overview, infrastructure, security, and networking.
- **Security Agent**: Performs a detailed security analysis of the product.

## 3. Workflow

The agent follows a specific workflow to perform the product curation.

### 3.1. Initialization

1.  The user starts a conversation with the agent.
2.  The root agent greets the user and asks for the product name.
3.  The user provides the product name.
4.  The root agent saves the product name in the session state.

### 3.2. Task Delegation

1.  The root agent presents the user with a menu of available tasks (e.g., "Discovery", "Security").
2.  The user selects a task.
3.  The root agent delegates the task to the corresponding sub-agent.

### 3.3. Discovery Workflow

The discovery workflow is orchestrated by the `discovery_agent`.

1.  **Research**: The `discovery_agent` runs a `ResearchAndCritiqueAgent` which is a sequential agent that runs a parallel agent for research and then a `recritic_agent`.
    - The `ParallelAgent` runs four sub-agents in parallel:
        - `ProductOverviewAgent`
        - `DiscoveryInfrastructureAgent`
        - `DiscoverySecurityAgent`
        - `DiscoveryNetworkingAgent`
    - Each of these agents gathers information about the product and generates a report.
2.  **Critique**: The `recritic_agent` reviews the reports from the research agents and generates a consolidated report.
3.  **Human-in-the-Loop**: The `discovery_agent` presents the consolidated report to the user for approval.
4.  **Publishing**: If the user approves the report, the `discovery_agent` publishes the report to Confluence using the `confluence_toolset`.

**Example Snippet from `app/subagents/discovery/agent.py`:**
```python
# Define the research unit
research_and_critique_agent = SequentialAgent(
    name="ResearchAndCritiqueAgent",
    description="Runs a detailed analysis of a product and produces a draft report. Takes the product name and user feedback as input.",
    sub_agents=[
        ParallelAgent(
            name="ResearchAgents",
            sub_agents=[
                get_product_overview_agent(),
                get_discovery_infrastructure_agent(),
                get_discovery_security_agent(),
                get_discovery_networking_agent(),
            ],
        ),
        get_recritic_agent(),
    ],
)
```

### 3.4. Security Workflow

The security workflow is orchestrated by the `security_agent`.
The `security_agent` uses four sub-agents to perform a detailed security analysis of the product:
- `OrgPolicyWorkflowAgent`
- `ShaWorkflowAgent`
- `OpaMigratorAgent`
- `InspecMigratorAgent`

## 4. Usage

To use the agent, you need to:
1.  Install the dependencies: `make install`
2.  Set the required environment variables in the `.env` file (e.g., `CONFLUENCE_MCP_URL`, `CONFLUENCE_PAT`).
3.  Run the agent locally: `make playground`
