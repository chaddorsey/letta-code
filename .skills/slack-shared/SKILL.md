---
name: slack-shared
version: 1.0.0
description: "Slack CLI: Shared patterns for authentication, global flags, and output formatting."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
---

# Slack CLI — Shared Reference

## Installation

**macOS host (Letta Code):**
```bash
pip install ./slack-cli
```

**Docker (standard Letta):**
Volume-mount source into container, then `pip install /app/tools/slack-cli/` in entrypoint-wrapper.sh.

## Authentication

```bash
# Set bot token (required)
export SLACK_BOT_TOKEN=xoxb-your-token

# Set user token (optional, needed for search)
export SLACK_MCP_XOXP_TOKEN=xoxp-your-token

# Verify
slack auth status
slack auth test
```

## CLI Syntax

```bash
slack <resource> <method> [flags]
slack <resource> +<helper> [flags]
```

## Global Flags

| Flag | Description |
|------|-------------|
| `--body '{"key": "val"}'` | Raw JSON parameters (agent-first path) |
| `--format <FORMAT>` | Output format: `json` (default), `text`, `csv`, `yaml` |
| `--fields <FIELDS>` | Comma-separated fields to include in output |
| `--dry-run` | Validate without calling the API |
| `--page-all` | Auto-paginate through all results |
| `--page-limit <N>` | Max pages when using --page-all (default: 10) |
| `--as-user` | Force user token (xoxp) |
| `--as-bot` | Force bot token (xoxb) |

## Schema Discovery

```bash
# List all command groups
slack schema

# List methods in a group
slack schema --group conversations

# Inspect a specific method's parameters
slack schema chat.postMessage
```

Use `slack schema` output to build your `--body` flags.

## Security Rules

- **Never** output tokens or secrets directly
- **Always** use `--dry-run` before destructive operations (delete, archive)
- Prefer `--fields` to limit response size and token cost
- Prefer channel/user IDs over names for reliability

## Error Format

Errors are always JSON on stdout:
```json
{"ok": false, "error": "channel_not_found", "detail": "Channel 'C999' does not exist"}
```

Exit codes: 0 (success), 1 (execution error), 2 (validation error).
