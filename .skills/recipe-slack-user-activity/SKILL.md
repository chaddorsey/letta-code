---
name: recipe-slack-user-activity
version: 1.0.0
description: "Summarize a user's recent messages across all channels."
metadata:
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins: ["slack"]
      skills: ["slack-search", "slack-users"]
---

# User Activity Summary

> **PREREQUISITE:** Load these skills: `slack-search`, `slack-users`

Find and summarize a user's recent Slack activity.

## Steps

1. Resolve the user:
   ```bash
   slack users +whois --name "Alice"
   ```

2. Search their recent messages:
   ```bash
   slack search messages --body '{"query": "from:@alice", "count": 50, "sort": "timestamp", "sort_dir": "desc"}' --fields "ok,messages"
   ```

3. Narrow by date if needed:
   ```bash
   slack search messages --body '{"query": "from:@alice on:2026-03-10", "count": 50}'
   ```

4. Summarize: which channels they were active in, key topics, decisions made, questions asked.

## Tips

- Search requires a user token (`--as-user`)
- Use `on:YYYY-MM-DD` for date filtering (reliable)
- Do NOT combine `after:` + `before:` (Slack bug)
- To see what someone was *mentioned* in: `slack search messages --body '{"query": "@alice"}'`
