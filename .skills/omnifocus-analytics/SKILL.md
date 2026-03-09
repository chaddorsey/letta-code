---
name: omnifocus-analytics
version: 1.0.0
description: "OmniFocus: Completion stats, workload analysis, overdue counts, and system health."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["omnifocus-cli"]
    cliHelp: "omnifocus-cli analytics --help"
---

# analytics

> **PREREQUISITE:** Read `../omnifocus-shared/SKILL.md` for installation, global flags, and security rules.

```bash
omnifocus-cli [global-flags] analytics <action> [flags]
```

## Actions

| Action | Description |
|--------|-------------|
| `health` | System health check — overdue count, stale projects, inbox size |
| `workload` | Current workload analysis — tasks by due date, flagged items |
| `trends` | Completion trends over time |
| `summary` | High-level summary across all projects |

Run `omnifocus-cli schema analytics.<action>` for parameters.

## Common Patterns

```bash
# Quick health check
omnifocus-cli analytics health

# Workload overview
omnifocus-cli analytics workload

# Completion trends
omnifocus-cli --body '{"days": 7}' analytics trends

# Full summary
omnifocus-cli analytics summary
```

## Automation Commands

The `automation` group provides diagnostic and cleanup tools:

```bash
omnifocus-cli automation suggest     # Suggest organizational improvements
omnifocus-cli automation diagnose    # Diagnose issues (orphaned tasks, etc.)
omnifocus-cli automation cleanup     # Clean up completed/dropped items
```

Run `omnifocus-cli automation --help` for details.

## See Also

- [omnifocus-review](../omnifocus-review/SKILL.md) — Review workflow
- [recipe-omnifocus-weekly-planning](../recipe-omnifocus-weekly-planning/SKILL.md) — Weekly planning recipe
