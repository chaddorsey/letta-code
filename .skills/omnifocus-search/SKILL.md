---
name: omnifocus-search
version: 1.0.0
description: "OmniFocus: Search and filter tasks, projects, and tags."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["omnifocus-cli"]
    cliHelp: "omnifocus-cli search --help"
---

# search, tags & perspectives

> **PREREQUISITE:** Read `../omnifocus-shared/SKILL.md` for installation, global flags, and security rules.

## Search

```bash
omnifocus-cli [global-flags] search [flags]
```

Run `omnifocus-cli schema search` for all filter parameters.

```bash
# Search by text
omnifocus-cli --body '{"query": "budget report"}' --fields id,name,projectName search

# Search with filters
omnifocus-cli --body '{"query": "meeting", "flagged": true, "status": "active"}' search
```

## Tags

```bash
omnifocus-cli [global-flags] tags <action> [flags]
```

| Action | Description |
|--------|-------------|
| `list` | List all tags |
| `get` | Get tag details by ID |
| `create` | Create a new tag |
| `rename` | Rename an existing tag |
| `delete` | Delete a tag (use `--dry-run` first) |

```bash
omnifocus-cli --fields id,name tags list
omnifocus-cli --body '{"name": "waiting-for"}' tags create
```

## Perspectives

```bash
omnifocus-cli [global-flags] perspective <action> [flags]
```

| Action | Description |
|--------|-------------|
| `list` | List available perspectives |
| `get` | Get perspective details and contents |
| `switch` | Switch OmniFocus to a perspective |

```bash
omnifocus-cli --fields id,name perspective list
omnifocus-cli --body '{"perspectiveId": "persp123"}' perspective get
```

## Tips

- Always use `--fields` to limit output on search and list operations
- Combine search filters for precise results
- Tags are the primary organizational axis alongside projects
