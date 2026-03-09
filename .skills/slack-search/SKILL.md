---
name: slack-search
version: 1.0.0
description: "Slack: Search messages and files with Slack query syntax."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack search --help"
---

# Slack Search

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

**NOTE:** Search requires a **user token** (xoxp). Set `SLACK_MCP_XOXP_TOKEN` or use `--as-user`.

```bash
slack search <method> [flags]
```

## Common Commands

```bash
# Search messages
slack search messages --body '{"query": "project update", "count": 10}'

# Search with Slack query syntax
slack search messages --body '{"query": "from:@john in:#general project"}'

# Search by date (RELIABLE)
slack search messages --body '{"query": "on:2026-03-08 standup"}'

# Search files
slack search files --body '{"query": "filename:report.pdf"}'
```

## Known Slack API Quirks

- **Date filtering:** `on:YYYY-MM-DD` works reliably
- **BROKEN:** Combining `after:YYYY-MM-DD` + `before:YYYY-MM-DD` returns 0 results — this is a known Slack API bug. Use `on:` for single days or search without date filters and filter results yourself.
- **Rate limits:** Search is Tier 2 (20 requests per minute)

## Query Syntax

| Operator | Example | Description |
|----------|---------|-------------|
| `from:` | `from:@john` | Messages from a user |
| `in:` | `in:#general` | Messages in a channel |
| `on:` | `on:2026-03-08` | Messages on a specific date |
| `has:` | `has:link` | Messages with links/reactions/pins |
| `is:` | `is:starred` | Starred messages |

## Discovering Commands

```bash
slack search --help
slack schema search.messages
```
