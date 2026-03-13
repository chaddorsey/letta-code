---
name: slack-bookmarks
version: 1.0.0
description: "Slack: Manage channel bookmarks (saved links)."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["slack"]
    cliHelp: "slack bookmarks --help"
---

# Slack Bookmarks

> **PREREQUISITE:** Read `../slack-shared/SKILL.md` for auth, global flags, and security rules.

```bash
slack bookmarks <method> [flags]
```

## Common Commands

```bash
# List bookmarks in a channel
slack bookmarks list --body '{"channel_id": "C0123ABCDEF"}'

# Add a bookmark
slack bookmarks add --body '{"channel_id": "C0123ABCDEF", "title": "Project Wiki", "type": "link", "link": "https://wiki.example.com"}'

# Edit a bookmark
slack bookmarks edit --body '{"channel_id": "C0123ABCDEF", "bookmark_id": "Bk0123ABCDEF", "title": "Updated Title"}'

# Remove a bookmark (use --dry-run first!)
slack bookmarks remove --dry-run --body '{"channel_id": "C0123ABCDEF", "bookmark_id": "Bk0123ABCDEF"}'
```

## Discovering Commands

```bash
slack bookmarks --help
slack schema bookmarks.add
slack schema bookmarks.list
```
