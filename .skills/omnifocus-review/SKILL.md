---
name: omnifocus-review
version: 1.0.0
description: "OmniFocus: Review workflow — list items for review, mark reviewed, advance to next."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["omnifocus-cli"]
    cliHelp: "omnifocus-cli review --help"
---

# review

> **PREREQUISITE:** Read `../omnifocus-shared/SKILL.md` for installation, global flags, and security rules.

```bash
omnifocus-cli [global-flags] review <action> [flags]
```

## Actions

| Action | Description |
|--------|-------------|
| `list` | List projects due for review |
| `mark` | Mark a project as reviewed |
| `next` | Get the next project due for review |

Run `omnifocus-cli schema review.<action>` for parameters.

## Common Patterns

```bash
# See what needs review
omnifocus-cli --fields id,name,lastReviewDate review list

# Get next item to review
omnifocus-cli review next

# Mark a project as reviewed
omnifocus-cli --body '{"projectId": "proj123"}' review mark
```

## Review Workflow

1. `review list` — see all projects due for review
2. `review next` — get the top item
3. Inspect the project (tasks, status, progress)
4. `review mark` — mark reviewed and move to next

## See Also

- [recipe-omnifocus-daily-review](../recipe-omnifocus-daily-review/SKILL.md) — Full daily review workflow
- [omnifocus-analytics](../omnifocus-analytics/SKILL.md) — Health and workload metrics
