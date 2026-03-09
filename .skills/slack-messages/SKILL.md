---
name: slack-messages
version: 1.0.0
description: "Slack: Send messages, reply in threads, update and delete messages."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack chat --help"
---

# Slack Messages

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack chat <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| `+send` | Send a message (resolves channel names to IDs) |

## Common Commands

```bash
# Send a message (resolves channel name)
slack chat +send --channel general --text "Hello world"

# Send via raw API (use channel ID)
slack chat postMessage --body '{"channel": "C0123ABCDEF", "text": "Hello world"}'

# Reply in a thread
slack chat +send --channel general --text "Thread reply" --thread-ts "1234567890.123456"

# Update a message
slack chat update --body '{"channel": "C0123ABCDEF", "ts": "1234567890.123456", "text": "Updated text"}'

# Delete a message
slack chat delete --body '{"channel": "C0123ABCDEF", "ts": "1234567890.123456"}'

# Add a reaction
slack reactions add --body '{"channel": "C0123ABCDEF", "timestamp": "1234567890.123456", "name": "thumbsup"}'
```

## Important

- `thread_ts` is the **parent message** timestamp, not the reply's timestamp
- Use `--dry-run` before delete operations
- `+send` resolves channel names; raw `postMessage` requires channel IDs

## Discovering Commands

```bash
slack chat --help
slack schema chat.postMessage
slack schema chat.update
```
