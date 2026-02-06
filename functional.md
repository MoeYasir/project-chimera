# Functional Specification

## Actors

- Network Operator (sets goals, monitors fleet)
- Human Reviewer (HITL moderator)
- Developer (extends MCP servers, prompts, infra)

## Core User Stories

### Trend & Context

- As a Planner Agent, I need to ingest trend signals from configured resources so I can propose content opportunities.
- As a Trend Spotter Worker, I need to cluster headlines/topics over a time window to produce a trend alert.
- As a Judge, I must reject trend outputs that do not conform to the `Trend` contract.

### Content Generation

- As a Worker, I need to generate content artifacts (text/image/video) through MCP tools so the core logic stays decoupled from vendor APIs.
- As a Judge, I must validate that generated content complies with persona constraints and policy.

### Publishing / Engagement

- As a Worker, I need to publish content to a platform via MCP tools (never direct API calls).
- As a Planner, I need to create reply tasks when new mentions are detected.
- As a Judge, I must route sensitive topics to HITL regardless of confidence score.

### Governance (HITL)

- As a Judge, I must attach a confidence score to each output and route it by thresholds:
  - > 0.90 auto-approve
  - 0.70–0.90 async approval
  - < 0.70 reject/retry

## Out of Scope for this submission

- Actual model calls
- Real platform credentials
- Real wallet operations
