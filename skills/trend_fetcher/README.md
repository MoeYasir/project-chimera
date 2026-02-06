# Skill: trend_fetcher

## Purpose

Fetch and normalize trend signals from MCP resources into `Trend[]` objects.

## Contract

This skill MUST use the Skill Interface Envelope defined in `specs/technical.md` (section 2.3).

## Input (Envelope.payload)

```json
{
  "resources": ["news://latest"],
  "window_hours": 24,
  "max_items": 50
}
```

Fields

resources (string[]): MCP resources to read from

window_hours (number): time window for trend aggregation

max_items (number): cap on raw items ingested

Output (Envelope.result)
{
"trends": [
{
"id": "string",
"topic": "string",
"window_start": "ISO-8601",
"window_end": "ISO-8601",
"confidence": 0.0,
"sources": [{"title":"string","url":"string","published_at":"ISO-8601"}],
"keywords": ["string"],
"notes": "string"
}
]
}

Failure Modes (Envelope.status="error")

MCP_UNAVAILABLE: MCP resource cannot be reached

BAD_RESOURCE: resource name invalid / unsupported

VALIDATION_FAILED: output cannot be shaped into Trend schema

---

### `skills/content_generator/README.md`

````md
# Skill: content_generator

## Purpose

Generate content artifacts (text/image/video) via MCP tools, returning an artifact reference plus confidence.

## Contract

This skill MUST use the Skill Interface Envelope defined in `specs/technical.md` (section 2.3).

## Input (Envelope.payload)

````json
{
  "trend_id": "string",
  "content_type": "text",
  "persona_constraints": ["string"],
  "disclosure_level": "assisted"
}


Fields

trend_id (string): ID of the trend being addressed

content_type ("text"|"image"|"video"): artifact type

persona_constraints (string[]): tone/style/safety constraints

disclosure_level ("automated"|"assisted"|"none")

Output (Envelope.result)
{
  "artifact": {
    "type": "text",
    "text": "string",
    "media_urls": []
  }
}


Governance Requirements

Must return confidence in the envelope.

Must provide enough metadata for the Judge to route HITL.

Failure Modes (Envelope.status="error")

TOOL_TIMEOUT: MCP tool call timed out

POLICY_BLOCKED: content violates policy or persona constraints

TOOL_ERROR: MCP tool returned an error


---

### `skills/social_publisher/README.md`
```md
# Skill: social_publisher

## Purpose
Publish a content artifact to a target platform via MCP tools and return the publishing outcome.

## Contract
This skill MUST use the Skill Interface Envelope defined in `specs/technical.md` (section 2.3).

## Input (Envelope.payload)
```json
{
  "platform": "twitter",
  "text_content": "string",
  "media_urls": ["string"],
  "disclosure_level": "assisted"
}


Fields

platform ("twitter"|"instagram"|"threads")

text_content (string)

media_urls (string[], optional)

disclosure_level ("automated"|"assisted"|"none")

Output (Envelope.result)
{
  "publish_event": {
    "platform": "twitter",
    "platform_post_id": "string",
    "status": "published",
    "published_at": "ISO-8601"
  }
}

Failure Modes (Envelope.status="error")

RATE_LIMIT: platform rate limited via MCP tool

TOOL_ERROR: publish tool failed

VALIDATION_FAILED: missing required fields for platform post


---

## 4) Failing tests

### `tests/test_trend_fetcher.py`
```python
def test_trend_schema_contract_is_available():
    """
    This should fail until the schema module exists.
    It defines the empty slot the agent must implement.
    """
    from chimera.schemas import TREND_SCHEMA  # noqa: F401

    assert isinstance(TREND_SCHEMA, dict)
    assert TREND_SCHEMA["type"] == "object"
    assert "required" in TREND_SCHEMA
````
````
