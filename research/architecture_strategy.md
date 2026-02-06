# Architecture Strategy — Project Chimera

## Objective

Design a spec-driven, agentic infrastructure (“the factory”) for Autonomous Influencers such that a swarm of AI agents can implement features safely and consistently.

## Agent Pattern Selection

### Chosen Pattern: Hierarchical Swarm (Planner → Worker → Judge)

**Why**

- Separates responsibilities cleanly (planning, execution, validation).
- Enables parallelism: multiple Workers can execute tasks in parallel.
- Central governance: Judge enforces policy + HITL routing.

### Alternatives Considered

- **Sequential Chain**: simpler but slower and harder to scale; governance becomes “after-the-fact.”
- **Fully decentralized swarm**: high coordination complexity and risk of conflicting changes.

## Human-in-the-Loop (HITL) Placement

HITL is applied at the **Judge stage**:

- Worker produces a candidate output + confidence.
- Judge routes based on thresholds:
  - **> 0.90** auto-approve
  - **0.70–0.90** HITL approval queue
  - **< 0.70** reject/retry
- Sensitive topics always routed to HITL regardless of confidence.

## Data Strategy

### Primary DB: PostgreSQL (Phase 1)

**Reason**

- Strong relational integrity for high-velocity metadata (tasks, content assets, publish events).
- Easy auditability for governance and traceability.

### What we store in Postgres

- Task lifecycle state (pending → in_progress → review → complete)
- Content metadata (type, URLs, confidence, timestamps)
- Publishing logs (platform, post_id, status)
- HITL review decisions

### What we do NOT store in Postgres (Phase 1)

- Vector memory / embeddings store (kept behind MCP)
- External resources (news/social scraping) beyond references/URLs

## Orchestration & Queues

Two logical queues:

- `task_queue`: Planner → Worker
- `review_queue`: Worker → Judge

## Constraints / Guardrails

- No direct third-party API calls from core logic; integrations must be behind MCP.
- Specs are the source of truth (no implementation before specs are ratified).
- Never commit secrets or credentials; use environment injection later.

## Next Steps

- Formalize OpenClaw status publishing contract (specs/openclaw_integration.md).
- Define skill interfaces and write failing tests for contracts.
- Lock governance via Docker + CI + AI review policy.
