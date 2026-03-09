---
name: omnifocus-projects
version: 1.0.0
description: "OmniFocus: List, create, update, and manage projects and folders."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["omnifocus-cli"]
    cliHelp: "omnifocus-cli project --help"
---

# project & folder

> **PREREQUISITE:** Read `../omnifocus-shared/SKILL.md` for installation, global flags, and security rules.

```bash
omnifocus-cli [global-flags] project <action> [flags]
omnifocus-cli [global-flags] folder <action> [flags]
```

## Project Actions

| Action | Description |
|--------|-------------|
| `list` | List all projects (filterable by status) |
| `get` | Get project details by ID |
| `create` | Create a new project |
| `update` | Update project properties |
| `complete` | Mark a project as completed |
| `move` | Move project to a folder |
| `convert` | Convert task to project or vice versa |
| `get-group-type` | Get project grouping (parallel/sequential) |
| `set-group-type` | Set project grouping |

## Folder Actions

| Action | Description |
|--------|-------------|
| `list` | List all folders |
| `get` | Get folder details by ID |
| `create` | Create a new folder |
| `delete` | Delete a folder (use `--dry-run` first) |
| `tree` | Show folder hierarchy tree |

Run `omnifocus-cli schema project.<action>` or `omnifocus-cli schema folder.<action>` for parameters.

## Common Patterns

```bash
# List active projects (compact)
omnifocus-cli --fields id,name,status project list

# Create a sequential project in a folder
omnifocus-cli --body '{"name": "Q2 Planning", "folderId": "fold123", "sequential": true}' project create

# View folder tree
omnifocus-cli folder tree

# Move project to a different folder
omnifocus-cli --body '{"projectId": "proj123", "folderId": "fold456"}' project move
```

## See Also

- [omnifocus-tasks](../omnifocus-tasks/SKILL.md) — Task operations within projects
- [omnifocus-search](../omnifocus-search/SKILL.md) — Search across projects
