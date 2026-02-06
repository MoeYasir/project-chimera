# Skill: social_publisher

## Purpose

Publish a content artifact to a target platform via MCP tools and return the publishing outcome.

## Contract

This skill MUST use the Skill Interface Envelope defined in `specs/technical.md` (section 2.3).

## Input (Envelope.payload)

````json
{
  "platform": "twitter",
  "text_content": "string",
  "media_urls": ["string"],
  "disclosure_level": "assisted"
}


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

RATE_LIMIT

TOOL_ERROR

VALIDATION_FAILED


Commit:

```bash
git add skills/social_publisher/README.md
git commit -m "feat(skills): add social_publisher skill contract"
git push
````
