---
name: slack-channels
version: 1.0.0
description: "Slack: List channels, get channel info, read channel history."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack conversations --help"
---

# Slack Channels

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack conversations <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| `+find` | Find channels by name substring |

## Common Commands

```bash
# List public channels
slack conversations list --body '{"types": "public_channel", "limit": 100}'

# Get channel info
slack conversations info --body '{"channel": "C0123ABCDEF"}'

# Read recent messages
slack conversations history --body '{"channel": "C0123ABCDEF", "limit": 50}'

# Find a channel by name
slack conversations +find --name "project"
```

## Important

- Channel names do NOT include `#` — use `general`, not `#general`
- Prefer channel IDs (`C0123ABCDEF`) over names for reliability
- Use `--fields` to limit response size: `--fields "ok,channels"`
- Pagination: use `--page-all` or pass `cursor` in `--body`

## Discovering Commands

```bash
slack conversations --help
slack schema conversations.list
slack schema conversations.history
```
