---
name: omnifocus-tasks
version: 1.0.0
description: "OmniFocus: Create, complete, update, list, move, and organize tasks."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["omnifocus-cli"]
    cliHelp: "omnifocus-cli task --help"
---

# task

> **PREREQUISITE:** Read `../omnifocus-shared/SKILL.md` for installation, global flags, and security rules.

```bash
omnifocus-cli [global-flags] task <action> [flags]
```

## Actions

| Action | Description |
|--------|-------------|
| `create` | Create a new task (name required) |
| `get` | Get task details by ID |
| `update` | Update task properties |
| `complete` | Mark a task as completed |
| `delete` | Delete a task (use `--dry-run` first) |
| `move` | Move task to a different project or inbox |
| `list` | List tasks (filterable) |
| `subtasks` | List subtasks of a task |
| `add-subtask` | Add a subtask to a parent task |
| `hierarchy` | Show task hierarchy tree |
| `flatten` | Flatten a task group |
| `batch-status` | Check status of multiple tasks |
| `get-group-type` | Get grouping type of a task |
| `set-group-type` | Set grouping type (parallel, sequential) |

Run `omnifocus-cli schema task.<action>` to see all parameters for any action.

## Common Patterns

```bash
# Create a flagged task with a due date
omnifocus-cli --body '{"name": "Review proposal", "flagged": true, "dueDate": "2026-03-15"}' task create

# List inbox tasks (compact output)
omnifocus-cli --fields id,name,flagged,dueDate task list

# Complete a task (dry-run first)
omnifocus-cli --body '{"taskId": "abc123"}' --dry-run task complete
omnifocus-cli --body '{"taskId": "abc123"}' task complete

# Move a task to a project
omnifocus-cli --body '{"taskId": "abc123", "projectId": "proj456"}' task move

# Create with tags and estimated duration
omnifocus-cli --body '{"name": "Write report", "tagIds": ["tag1","tag2"], "estimatedMinutes": 60}' task create
```

## Inbox Operations

The `inbox` command group handles inbox-specific workflows:

```bash
omnifocus-cli inbox list                    # List inbox tasks
omnifocus-cli inbox process                 # Get next inbox item for processing
omnifocus-cli inbox context                 # Inbox summary with counts
omnifocus-cli inbox bulk                    # Batch process inbox items
```

Run `omnifocus-cli inbox --help` for details.

## Tips

- Always use `--fields` on list operations to limit token usage
- Use `--dry-run` before `complete`, `delete`, and `move` operations
- Subtask operations require the parent task ID
