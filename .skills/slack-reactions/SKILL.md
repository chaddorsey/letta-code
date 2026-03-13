---
name: slack-reactions
version: 1.0.0
description: "Slack: Add, remove, and list emoji reactions on messages."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack reactions --help"
---

# Slack Reactions

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack reactions <method> [flags]
```

## Common Commands

```bash
# Add a reaction
slack reactions add --body '{"channel": "C0123ABCDEF", "timestamp": "1234567890.123456", "name": "thumbsup"}'

# Remove a reaction
slack reactions remove --body '{"channel": "C0123ABCDEF", "timestamp": "1234567890.123456", "name": "thumbsup"}'

# Get reactions on a message
slack reactions get --body '{"channel": "C0123ABCDEF", "timestamp": "1234567890.123456"}'

# List all reactions by the authenticated user
slack reactions list --body '{"count": 20}'
```

## Important

- `name` is the emoji name WITHOUT colons — use `thumbsup`, not `:thumbsup:`
- `timestamp` is the message's `ts` field (e.g., `1234567890.123456`)
- `reactions.get` and `reactions.list` work with either bot or user token
- `reactions.add` and `reactions.remove` require `reactions:write` scope

## Discovering Commands

```bash
slack reactions --help
slack schema reactions.add
slack schema reactions.get
```
