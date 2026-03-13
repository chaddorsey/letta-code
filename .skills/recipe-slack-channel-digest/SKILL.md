---
name: recipe-slack-channel-digest
version: 1.0.0
description: "Summarize a specific channel's activity over a date range."
metadata:
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins: ["slack"]
      skills: ["slack-channels", "slack-messages"]
---

# Channel Digest

> **PREREQUISITE:** Load these skills: `slack-channels`, `slack-messages`

Summarize a specific channel's messages over a date range.

## Steps

1. Resolve the channel:
   ```bash
   slack conversations +find --name "project-alpha"
   ```

2. Fetch messages in the time range (Unix timestamps):
   ```bash
   slack conversations history --body '{"channel": "C0123ABCDEF", "oldest": "1709856000", "latest": "1710028800", "limit": 200}' --page-all --fields "ts,text,user,reply_count,reactions"
   ```

3. For threads with replies, fetch the full thread:
   ```bash
   slack conversations history --body '{"channel": "C0123ABCDEF", "oldest": "1234567890.123456", "limit": 100}'
   ```

4. Resolve user IDs to names:
   ```bash
   slack users info --body '{"user": "U0123ABCDEF"}' --fields "id,real_name"
   ```

5. Summarize: key decisions, action items, open questions, and active threads.

## Tips

- Convert dates to Unix timestamps (e.g., 2026-03-10 00:00 EST = 1741579200)
- Use `--fields` to keep responses lean
- Messages with `reply_count > 0` have threads worth expanding
- Messages with `reactions` often signal important content
