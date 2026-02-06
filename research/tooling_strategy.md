# Tooling Strategy — MCP vs Skills

## Goal

Clearly separate:

- **Developer tools (MCP servers)** used to build/debug the system.
- **Runtime Skills** used by Chimera agents to do work.

## A) Developer Tools (MCP Servers)

These are configured to help the developer maintain traceability and control.

Planned Dev MCP servers:

1. **filesystem MCP**
   - Purpose: safe file read/write and structured edits
2. **git MCP**
   - Purpose: diffs, commit context, history inspection
3. **postgres MCP (future)**
   - Purpose: query Postgres without embedding DB logic into agent core

Principles:

- Dev MCP servers improve workflow and reliability.
- No secrets stored in repo; any credentials remain local.

## B) Runtime Skills (Agent Capabilities)

Skills are versioned capability interfaces the agents call at runtime.

Minimum Phase-1 skills:

- `trend_fetcher`
- `content_generator`
- `social_publisher`

Principles:

- Skills must obey the Skill Envelope contract in `specs/technical.md`.
- Skills may call MCP tools/resources internally, but do not embed vendor SDK logic.
- Skills are test-defined first (TDD empty slots).

## Boundary Rules

- Agent core logic never calls platform APIs directly.
- External data and actions are accessed via MCP tools/resources.
- Specs must be consulted before adding new interfaces or dependencies.
