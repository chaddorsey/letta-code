---
name: recipe-omnifocus-weekly-planning
version: 1.0.0
description: "Weekly planning: review all projects, assess workload trends, set flagged priorities for the week."
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["omnifocus-cli"]
      skills: ["omnifocus-shared", "omnifocus-tasks", "omnifocus-projects", "omnifocus-review", "omnifocus-analytics"]
---

# Weekly Planning

> **PREREQUISITE:** Load the following skills to execute this recipe: `omnifocus-shared`, `omnifocus-tasks`, `omnifocus-projects`, `omnifocus-review`, `omnifocus-analytics`

Review all projects, analyze completion trends, clear the review queue, and flag priorities for the coming week.

## Steps

1. **Completion trends** — see what got done last week:
   ```bash
   omnifocus-cli --body '{"days": 7}' analytics trends
   ```

2. **Project review** — list all projects due for review:
   ```bash
   omnifocus-cli --fields id,name,status,lastReviewDate review list
   ```
   For each project:
   - Check active tasks: `omnifocus-cli --body '{"projectId": "<id>"}' --fields id,name,dueDate task list`
   - Assess progress, defer stale tasks, add missing tasks
   - Mark reviewed: `omnifocus-cli --body '{"projectId": "<id>"}' review mark`

3. **Workload check** — verify load is manageable:
   ```bash
   omnifocus-cli analytics workload
   ```

4. **Set weekly priorities** — flag the key tasks for the week:
   ```bash
   omnifocus-cli --body '{"taskId": "<id>", "flagged": true}' task update
   ```

5. **Folder structure audit** — check for organizational issues:
   ```bash
   omnifocus-cli folder tree
   omnifocus-cli automation diagnose
   ```

6. **Clean up** — archive completed items:
   ```bash
   omnifocus-cli automation cleanup
   ```

7. **Final summary**:
   ```bash
   omnifocus-cli analytics summary
   ```
