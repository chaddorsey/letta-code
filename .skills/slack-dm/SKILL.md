---
name: slack-dm
version: 1.0.0
description: "Slack: Send direct messages and manage DM conversations."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack conversations --help"
---

# Slack Direct Messages

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

## Common Commands

```bash
# Open a DM with a user
slack conversations open --body '{"users": "U0123ABCDEF"}'

# Send a DM (after opening — use the channel ID returned)
slack chat postMessage --body '{"channel": "D0123ABCDEF", "text": "Hey, quick question..."}'

# List DM conversations
slack conversations list --body '{"types": "im", "limit": 50}'

# Read DM history
slack conversations history --body '{"channel": "D0123ABCDEF", "limit": 20}'
```

## Workflow: Send a DM

1. Open DM: `slack conversations open --body '{"users": "U0123ABCDEF"}'` -> get channel ID
2. Send message: `slack chat postMessage --body '{"channel": "<DM_CHANNEL_ID>", "text": "Hello"}'`

Or use the +send helper with the DM channel ID directly.

## Discovering Commands

```bash
slack schema conversations.open
slack schema chat.postMessage
```
