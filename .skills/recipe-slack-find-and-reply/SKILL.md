---
name: recipe-slack-find-and-reply
version: 1.0.0
description: "Search for a message then reply in its thread."
metadata:
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins: ["slack"]
      skills: ["slack-search", "slack-messages"]
---

# Find and Reply

> **PREREQUISITE:** Load these skills: `slack-search`, `slack-messages`

Search for a specific message, then post a threaded reply.

## Steps

1. Search for the message:
   ```bash
   slack search messages --body '{"query": "from:@alice in:#project budget update", "count": 5}' --fields "ok,messages"
   ```

2. From results, extract the `channel.id` and `ts` of the target message.

3. Confirm with user before replying (always).

4. Post a threaded reply using the message's `ts` as `thread_ts`:
   ```bash
   slack chat postMessage --body '{"channel": "C0123ABCDEF", "thread_ts": "1234567890.123456", "text": "Thanks for the update. Two questions..."}'
   ```

## Tips

- Search requires a user token (`--as-user`)
- `thread_ts` is the **parent message's** timestamp — this is what makes it a threaded reply
- Always preview with `--dry-run` before posting
- If the message is already in a thread, use the thread's parent `ts`, not the reply's `ts`
