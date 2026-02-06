# Skill: content_generator

## Purpose

Generate content artifacts (text/image/video) via MCP tools, returning an artifact reference plus confidence.

## Contract

This skill MUST use the Skill Interface Envelope defined in `specs/technical.md` (section 2.3).

## Input (Envelope.payload)

```json
{
  "trend_id": "string",
  "content_type": "text",
  "persona_constraints": ["string"],
  "disclosure_level": "assisted"
}
```

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

Failure Modes (Envelope.status="error")

TOOL_TIMEOUT: MCP tool call timed out

POLICY_BLOCKED: content violates policy/persona constraints

TOOL_ERROR: MCP tool returned an error

#### Paste into `skills/social_publisher/README.md`

````md
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
```
````

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

Commit:

```bash
git add skills/
git commit -m "feat(skills): add content_generator and social_publisher skill contracts"
git push
```
