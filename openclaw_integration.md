# OpenClaw Integration (Optional Spec)

## Purpose

Enable Project Chimera agents to publish their availability/capabilities to an agent network (OpenClaw-style) so other agents can discover and coordinate with Chimera.

## Principles

- No direct cross-agent execution. All inbound requests become Planner tasks.
- Governance applies: Planner → Worker → Judge, and HITL routing still applies.
- No secrets in payloads. Status is informational.

## Proposed Public Status Resource

Expose a read-only MCP Resource:

- Resource: `openclaw://agents/{agent_id}/status`

### Response Contract (JSON)

```json
{
  "agent_id": "string",
  "display_name": "string",
  "availability": "online | busy | offline",
  "capabilities": [
    "fetch_trends",
    "generate_content",
    "publish_content",
    "reply_comment"
  ],
  "requires_hitl": true,
  "policy_flags": ["no_politics", "ai_disclosure_enabled"],
  "last_heartbeat_at": "ISO-8601 timestamp",
  "version": "string"
}
```
