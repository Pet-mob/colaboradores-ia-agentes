# AI Platform Context – colaboradores-ia-agentes

## Project Goal

This repository is building an **AI Agent Platform** that simulates a **software company operated by AI agents**.

The goal is to create multiple specialized AI agents organized in teams that can collaborate to build, maintain, and support software products automatically.

The platform must be modular, scalable, and able to manage multiple software projects.

---

# Core Concept

The system acts like an **AI-driven company**.

Agents are organized in teams:

- Product Team
- Development Team
- Support Team
- SRE / Maintenance Team
- Marketing Team

Each team contains specialized agents that collaborate to complete tasks.

All work is coordinated by an **Orchestrator Agent**.

---

# Current MVP Scope

For the MVP version we are implementing a **minimal working AI team** composed of:

1. Orchestrator Agent
2. Planner Agent
3. Developer Agent
4. QA Agent

Workflow:

Idea → Planning → Development → Review

Example flow:

User Idea:
"Create a login system"

Planner Agent:

- Breaks idea into technical tasks

Developer Agent:

- Generates code

QA Agent:

- Reviews code and detects issues

---

# Repository Structure

The repository structure must remain modular and scalable.

```
colaboradores-ia-agentes
│
├ agents
│   ├ orchestrator.py
│   ├ planner_agent.py
│   ├ developer_agent.py
│   └ qa_agent.py
│
├ teams
│
├ tasks
│   └ dev_tasks.py
│
├ projects
│
├ memory
│
├ tools
│
├ logs
│
├ config
│   └ settings.py
│
├ main.py
│
└ requirements.txt
```

Each directory has a purpose:

agents → definitions of AI agents
teams → logical grouping of agents
tasks → task definitions
projects → registered external projects
memory → long term AI memory
tools → integrations (GitHub, Docker, file editing)
logs → execution logs

---

# Design Principles

The system must follow these principles:

1. Modular architecture
2. Clear separation of responsibilities
3. Expandable agent system
4. Ability to support multiple software projects
5. Logging and observability
6. Task-based workflow
7. Central orchestration

Agents should not execute logic directly without tasks.

All work must be task-driven.

---

# Agent Responsibilities

## Orchestrator Agent

Main controller of the system.

Responsibilities:

- receive requests
- select appropriate agents
- manage workflow
- coordinate tasks
- monitor results

---

## Planner Agent

Transforms ideas into structured tasks.

Responsibilities:

- break down goals
- create technical tasks
- define development steps

---

## Developer Agent

Implements tasks by generating code.

Responsibilities:

- generate code
- suggest architecture
- write functions and APIs

---

## QA Agent

Validates code produced by developers.

Responsibilities:

- analyze code
- detect errors
- suggest improvements
- identify potential bugs

---

# Future Platform Capabilities

This platform will evolve to support:

Multiple software projects

Example:

```
projects/
  pet_on_api.json
  petshop_webapp.json
  pet_on_app.json
```

Projects managed by this platform:

| Project          | Stack              | Description                     |
| ---------------- | ------------------ | ------------------------------- |
| `pet.on.Api`     | .NET (C#)          | Backend API principal da Petmob |
| `petshop.webapp` | Vue.js, JavaScript | Web app para petshops           |
| `pet.on.app`     | React Native       | App mobile para usuários finais |

Each project contains:

- repository URL
- technology stack
- deployment configuration

---

# Future Specialized Agents

Development Team:

- .NET Developer Agent (pet.on.Api)
- Vue.js Developer Agent (petshop.webapp)
- React Native Developer Agent (pet.on.app)
- DevOps Docker Agent

Product Team:

- Product Manager Agent
- UX Agent
- Analyst Agent

Support Team:

- Support Agent
- Bug Reporter Agent

SRE Team:

- Monitoring Agent
- Incident Response Agent

Marketing Team:

- Content Agent
- SEO Agent
- Campaign Agent

---

# Long Term Vision

The platform should become an **AI Software Factory** capable of:

- generating code for pet.on.Api (.NET), petshop.webapp (Vue.js) and pet.on.app (React Native)
- maintaining all three Petmob projects
- responding to issues and bugs
- creating documentation
- managing releases
- supporting multiple products

---

# Coding Guidelines

When generating code:

- prefer clear and modular Python code
- separate responsibilities across files
- avoid large monolithic functions
- use logging where appropriate
- maintain clean architecture

---

# Next Development Goals

Copilot should help implement:

1. Agent definitions
2. Task system
3. Orchestrator workflow
4. Execution pipeline
5. Logging system
6. Basic memory storage

---

# Key Rule

All logic must revolve around **agents executing tasks through orchestration**.

Avoid tightly coupled code.

Focus on building a scalable AI agent platform.
