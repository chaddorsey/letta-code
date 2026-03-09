---
name: slack-files
version: 1.0.0
description: "Slack: List and manage files."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack files --help"
---

# Slack Files

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack files <method> [flags]
```

## Common Commands

```bash
# List recent files
slack files list --body '{"count": 20}'

# List files in a channel
slack files list --body '{"channel": "C0123ABCDEF", "count": 10}'

# Get file info
slack files info --body '{"file": "F0123ABCDEF"}'

# Delete a file (use --dry-run first!)
slack --dry-run files delete --body '{"file": "F0123ABCDEF"}'
```

## Discovering Commands

```bash
slack files --help
slack schema files.list
```
