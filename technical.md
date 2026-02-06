# Technical Specification

## 1) Architecture Overview

Pattern: Planner/Worker/Judge services with queues.

- task_queue: Planner -> Worker
- review_queue: Worker -> Judge

External access is via MCP only:

- Resources: read-only (e.g., news://latest)
- Tools: executable (e.g., twitter.post, ideogram.generate)

## 2) Contracts (JSON Schemas)

### 2.1 Trend

```json
{
  "type": "object",
  "required": [
    "id",
    "topic",
    "window_start",
    "window_end",
    "confidence",
    "sources",
    "keywords"
  ],
  "properties": {
    "id": { "type": "string" },
    "topic": { "type": "string", "minLength": 3 },
    "window_start": { "type": "string", "description": "ISO 8601 timestamp" },
    "window_end": { "type": "string", "description": "ISO 8601 timestamp" },
    "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
    "sources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["title", "url", "published_at"],
        "properties": {
          "title": { "type": "string" },
          "url": { "type": "string" },
          "published_at": {
            "type": "string",
            "description": "ISO 8601 timestamp"
          }
        }
      }
    },
    "keywords": {
      "type": "array",
      "minItems": 1,
      "items": { "type": "string" }
    },
    "notes": { "type": "string" }
  }
}
```

## Database Implementation Notes (Phase 1)

- Primary datastore: PostgreSQL
- Access method: `psql` / SQL migrations (future phase)
- Responsibility in this phase:
  - Define schemas only
  - No live database initialization
  - No credentials committed

PostgreSQL will store:

- Task metadata
- Content metadata
- Publishing logs
- Confidence scores
- HITL decisions

Vector memory and external data sources are explicitly excluded from PostgreSQL
and are accessed only via MCP servers.
