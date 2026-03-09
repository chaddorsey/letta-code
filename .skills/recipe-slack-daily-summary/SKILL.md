---
name: recipe-slack-daily-summary
version: 1.0.0
description: "Search today's messages across key channels and summarize activity."
metadata:
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins: ["slack"]
      skills: ["slack-channels", "slack-search"]
---

# Daily Slack Summary

> **PREREQUISITE:** Load these skills: `slack-channels`, `slack-search`

Search today's messages across key channels and produce a summary.

## Steps

1. Find key channels: `slack conversations +find --name "general"`
2. Get today's messages from each channel: `slack conversations history --body '{"channel": "C0123ABCDEF", "limit": 100}'`
3. Alternatively, search across all channels: `slack search messages --body '{"query": "on:2026-03-08", "count": 100}'`
4. Review results and summarize key themes, decisions, and action items

## Tips

- Use `on:YYYY-MM-DD` for date filtering (reliable)
- Do NOT use `after:` + `before:` together (Slack bug -- returns 0 results)
- Use `--fields "ok,messages"` to reduce response size
- Search requires a user token (`SLACK_MCP_XOXP_TOKEN`)
