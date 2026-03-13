---
name: slack-reminders
version: 1.0.0
description: "Slack: Create, list, and manage reminders."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack reminders --help"
---

# Slack Reminders

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack reminders <method> [flags]
```

## Common Commands

```bash
# Create a reminder with natural language time
slack reminders add --body '{"text": "Review PR", "time": "in 2 hours"}'

# Create a reminder at a specific Unix timestamp
slack reminders add --body '{"text": "Team sync", "time": "1710000000"}'

# Create a reminder for someone else
slack reminders add --body '{"text": "Submit report", "time": "tomorrow at 9am", "user": "U0123ABCDEF"}'

# List all reminders
slack reminders list

# Get a specific reminder
slack reminders info --body '{"reminder": "Rm0123ABCDEF"}'

# Mark a reminder complete
slack reminders complete --body '{"reminder": "Rm0123ABCDEF"}'

# Delete a reminder (use --dry-run first!)
slack reminders delete --dry-run --body '{"reminder": "Rm0123ABCDEF"}'
```

## Important

- `time` accepts natural language ("in 2 hours", "tomorrow at 9am") or Unix timestamps
- Reminders created by a bot token are visible to the bot's installing user
- Reminder IDs start with `Rm`

## Discovering Commands

```bash
slack reminders --help
slack schema reminders.add
slack schema reminders.list
```
