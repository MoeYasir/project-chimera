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

````json
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
          "published_at": { "type": "string", "description": "ISO 8601 timestamp" }
        }
      }
    },
    "keywords": { "type": "array", "minItems": 1, "items": { "type": "string" } },
    "notes": { "type": "string" }
  }
}

## 2.2 Agent Task (Planner → Worker)

{
  "type": "object",
  "required": ["task_id", "task_type", "priority", "context", "created_at", "status"],
  "properties": {
    "task_id": { "type": "string", "description": "uuid" },
    "task_type": {
      "type": "string",
      "enum": ["fetch_trends", "generate_content", "publish_content", "reply_comment"]
    },
    "priority": { "type": "string", "enum": ["high", "medium", "low"] },
    "context": {
      "type": "object",
      "required": ["goal_description", "required_resources"],
      "properties": {
        "goal_description": { "type": "string" },
        "persona_constraints": { "type": "array", "items": { "type": "string" } },
        "required_resources": { "type": "array", "items": { "type": "string" } }
      }
    },
    "created_at": { "type": "string", "description": "ISO 8601 timestamp" },
    "status": { "type": "string", "enum": ["pending", "in_progress", "review", "complete"] }
  }
}

## 2.3 Skill Interface Envelope (Runtime)
All Skills accept a single JSON payload and return a single JSON payload.

Input:

{
  "type": "object",
  "required": ["skill_name", "request_id", "payload"],
  "properties": {
    "skill_name": { "type": "string" },
    "request_id": { "type": "string" },
    "payload": { "type": "object" }
  }
}
Output:

{
  "type": "object",
  "required": ["request_id", "status", "result"],
  "properties": {
    "request_id": { "type": "string" },
    "status": { "type": "string", "enum": ["ok", "error"] },
    "result": { "type": "object" },
    "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
    "error": {
      "type": "object",
      "required": ["code", "message"],
      "properties": {
        "code": { "type": "string" },
        "message": { "type": "string" }
      }
    }
  }
}
Database Implementation Notes (Phase 1)
Primary datastore: PostgreSQL

Access method: psql / SQL migrations (future phase)

Responsibility in this phase:

Define schemas only

No live database initialization

No credentials committed

PostgreSQL will store:

Task metadata

Content metadata

Publishing logs

Confidence scores

HITL decisions

Vector memory and external data sources are explicitly excluded from PostgreSQL
and are accessed only via MCP servers.

Database Schema (ERD) — Video/Content Metadata (Phase 1)
erDiagram
  AGENT ||--o{ CAMPAIGN : runs
  CAMPAIGN ||--o{ TASK : creates
  TASK ||--o{ CONTENT_ASSET : produces
  CONTENT_ASSET ||--o{ PUBLISH_EVENT : publishes
  CONTENT_ASSET ||--o{ HITL_REVIEW : reviewed

  AGENT {
    uuid id
    string handle
    string persona_id
    timestamptz created_at
  }

  CAMPAIGN {
    uuid id
    uuid agent_id
    string goal
    string status
    timestamptz created_at
  }

  TASK {
    uuid id
    uuid campaign_id
    string task_type
    string priority
    string status
    jsonb context
    timestamptz created_at
  }

  CONTENT_ASSET {
    uuid id
    uuid task_id
    string asset_type
    text text_content
    jsonb media_urls
    float confidence
    timestamptz created_at
  }

  PUBLISH_EVENT {
    uuid id
    uuid content_asset_id
    string platform
    string platform_post_id
    string status
    timestamptz published_at
  }

  HITL_REVIEW {
    uuid id
    uuid content_asset_id
    string decision
    text reviewer_notes
    timestamptz reviewed_at
  }

---

## After you paste it: commit command (good checkpoint)

```bash
git add specs/technical.md
git commit -m "specs: add task and skill contracts plus DB ERD"
git push
````
