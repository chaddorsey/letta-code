---
name: slack-pins
version: 1.0.0
description: "Slack: Pin and unpin important messages in channels."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack pins --help"
---

# Slack Pins

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack pins <method> [flags]
```

## Common Commands

```bash
# Pin a message
slack pins add --body '{"channel": "C0123ABCDEF", "timestamp": "1234567890.123456"}'

# Unpin a message (use --dry-run first!)
slack pins remove --dry-run --body '{"channel": "C0123ABCDEF", "timestamp": "1234567890.123456"}'

# List pinned messages in a channel
slack pins list --body '{"channel": "C0123ABCDEF"}'
```

## Important

- `timestamp` is the message's `ts` field
- A channel can have at most 100 pinned items
- Bot must be a member of the channel to pin/unpin

## Discovering Commands

```bash
slack pins --help
slack schema pins.add
slack schema pins.list
```
