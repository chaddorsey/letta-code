---
name: recipe-omnifocus-daily-review
version: 1.0.0
description: "Multi-step daily review: inbox processing, overdue triage, flagged tasks check, and review queue."
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["omnifocus-cli"]
      skills: ["omnifocus-shared", "omnifocus-tasks", "omnifocus-review", "omnifocus-analytics"]
---

# Daily Review

> **PREREQUISITE:** Load the following skills to execute this recipe: `omnifocus-shared`, `omnifocus-tasks`, `omnifocus-review`, `omnifocus-analytics`

Process inbox, triage overdue items, review flagged tasks, and advance the review queue.

## Steps

1. **Check system health** — get overdue count, inbox size, and stale project count:
   ```bash
   omnifocus-cli analytics health
   ```

2. **Process inbox** — list and triage unprocessed items:
   ```bash
   omnifocus-cli --fields id,name,dateAdded inbox list
   ```
   For each item, decide: assign to project, defer, flag, or delete.

3. **Review overdue tasks** — find tasks past their due date:
   ```bash
   omnifocus-cli --body '{"query": "", "overdue": true}' --fields id,name,dueDate,projectName search
   ```
   For each: reschedule, complete, or drop.

4. **Check flagged tasks** — verify today's priorities:
   ```bash
   omnifocus-cli --body '{"flagged": true, "status": "active"}' --fields id,name,dueDate search
   ```

5. **Advance review queue** — mark reviewed projects:
   ```bash
   omnifocus-cli review next
   # Inspect the project, then:
   omnifocus-cli --body '{"projectId": "<id>"}' review mark
   ```
   Repeat until queue is clear or time is up.

6. **Summary** — final workload snapshot:
   ```bash
   omnifocus-cli analytics workload
   ```
