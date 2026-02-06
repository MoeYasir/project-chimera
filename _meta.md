# Project Chimera — Spec Kit Meta

## Vision

Build an autonomous influencer "factory" that can research trends, generate content, publish to platforms, and manage engagement under governance. The system is designed so a swarm of AI agents can implement features with minimal ambiguity.

## Prime Directives

1. **Specs are the source of truth.** No implementation code is written unless `specs/` is ratified.
2. **All external interaction is via MCP.** Direct API calls from agent core logic are prohibited.
3. **Governance is mandatory.** Every action is validated by a Judge and routed to HITL based on confidence and sensitivity.
4. **Traceability is required.** Work should be reproducible through Docker + CI.

## System Pattern

- **Planner → Worker → Judge** (FastRender-style swarm roles)
- Planner decomposes goals into tasks.
- Workers execute atomic tasks using tools/resources.
- Judge validates outputs, enforces policies, applies optimistic concurrency controls when committing state.

## Non-Goals (This submission)

- Building full production integrations (Twitter/IG/etc).
- Producing a final generated video.
- Optimizing for cost/performance beyond basic constraints.

## Key Constraints

- Multi-tenancy isolation (future).
- Budget controls for expensive workflows (future).
- Compliance posture: disclosure / labeling where platforms support it.

## References

- Project Chimera SRS (2026 Edition)
- Agentic Infrastructure Challenge (3-Day)
