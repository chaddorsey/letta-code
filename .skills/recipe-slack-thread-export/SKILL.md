---
name: recipe-slack-thread-export
version: 1.0.0
description: "Export a Slack thread with all replies."
metadata:
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins: ["slack"]
      skills: ["slack-messages", "slack-channels"]
---

# Export a Slack Thread

> **PREREQUISITE:** Load these skills: `slack-messages`, `slack-channels`

Export a complete thread (parent message + all replies) from a channel.

## Steps

1. Get the parent message: `slack conversations history --body '{"channel": "C0123ABCDEF", "latest": "1234567890.123457", "oldest": "1234567890.123455", "inclusive": true, "limit": 1}'`
2. Get all replies: `slack conversations history --body '{"channel": "C0123ABCDEF", "oldest": "1234567890.123456", "limit": 200}' --page-all`
3. Note: Slack's `conversations.replies` API method can also be used if available

## Tips

- Thread timestamps (`thread_ts`) identify the parent message
- Use `--fields` to extract just the text and user fields
- For large threads, use `--page-all --page-limit 5` to get all replies
