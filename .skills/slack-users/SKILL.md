---
name: slack-users
version: 1.0.0
description: "Slack: List users, get user info, lookup by email."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack users --help"
---

# Slack Users

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack users <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| `+whois` | Find a user by name or email |

## Common Commands

```bash
# Find a user by name
slack users +whois --name "John"

# Find a user by email
slack users +whois --email "john@example.com"

# Get user info by ID
slack users info --body '{"user": "U0123ABCDEF"}'

# List all users
slack users list --body '{"limit": 200}' --fields "ok,members"
```

## Discovering Commands

```bash
slack users --help
slack schema users.info
slack schema users.lookupByEmail
```
