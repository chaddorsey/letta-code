---
name: recipe-slack-pulse-report
version: 1.0.0
description: "Generate a Slack activity summary (pulse report) covering DMs, public channels, and @-mentions for a time period."
metadata:
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins: ["slack"]
      skills: ["slack-channels", "slack-messages", "slack-search", "slack-users", "slack-dm"]
---

# Slack Pulse Report

> **PREREQUISITE:** Load these skills: `slack-channels`, `slack-messages`, `slack-search`, `slack-users`, `slack-dm`

Generate a structured Slack activity summary for a requested time period (typically 1 day).

## Output Structure

### 1. Personal Channels

- Summarize activity in user's DMs and MPDMs for the period
- Play-by-play style: top topics, key posters, what they're asking about or advocating for (as bullets)
- Annotate sentiment/mood if notable
- List ALL URLs and files shared in DMs/MPDMs (raw list, no annotation)

### 2. Public Activity

For each top-traffic public channel:
- 1-2 paragraph play-by-play: current discussion topics, questions, key poster contributions
- Bullet what key posters are asking or advocating for
- Annotate sentiment if meaningful
- List important links/files shared (skip mundane/bot links)

### 3. @-mentions

All personal @-mentions received during the period, formatted as:
- From **[First Name]** in [#channel](permalink) on [Date, Time]: [message excerpt]
- Hyperlink "in #channel" to the Slack post permalink

## Formatting Rules

- Hyperlink the first couple words of each bullet (channel names, key actions like "Bill replied", "Leslie explained") to the relevant Slack message or thread permalink
- This makes summaries actionable and easy to reference

## Steps

1. **Identify the time range** — convert requested period to Unix timestamps for `oldest`/`latest` params.

2. **Personal channels (DMs/MPDMs):**
   ```bash
   slack conversations list --body '{"types": "im,mpim", "limit": 100}' --fields "id,user,is_mpim,name"
   ```
   For each active DM/MPDM, fetch history:
   ```bash
   slack conversations history --body '{"channel": "D0123ABCDEF", "oldest": "UNIX_START", "latest": "UNIX_END", "limit": 200}' --fields "ts,text,user,files,attachments"
   ```

3. **Identify top public channels** — use recent Slack analytics if available, otherwise:
   ```bash
   slack conversations list --body '{"types": "public_channel", "limit": 200}' --fields "id,name,num_members"
   ```

4. **Fetch public channel history** for each top channel:
   ```bash
   slack conversations history --body '{"channel": "C0123ABCDEF", "oldest": "UNIX_START", "latest": "UNIX_END", "limit": 200}' --page-all --fields "ts,text,user,reply_count,reactions,files,attachments"
   ```

5. **Fetch @-mentions:**
   ```bash
   slack search messages --body '{"query": "@USER on:YYYY-MM-DD", "count": 50}' --fields "ok,messages"
   ```
   Extract permalink, sender, channel, and message excerpt for each mention.

6. **Resolve user IDs to names:**
   ```bash
   slack users info --body '{"user": "U0123ABCDEF"}' --fields "id,real_name,profile.display_name"
   ```

7. **Compose the report** following the output structure above.

## Tips

- Convert dates to Unix timestamps (e.g., `date -d "2026-03-10" +%s` or calculate manually)
- Use `--fields` aggressively — channel history responses are large
- For threads with `reply_count > 0`, consider fetching replies for important discussions
- Messages with reactions often signal important content worth highlighting
- Search requires user token (`--as-user`)
- For permalinks: construct as `https://WORKSPACE.slack.com/archives/CHANNEL_ID/p{ts_without_dot}`
  (e.g., ts `1234567890.123456` → `p1234567890123456`)

## Example Output

```
Slack Activity Summary for March 10, 2026

Personal Channels:
- [Leslie in MPDM](link): Discussed NASA solicitation timeline, asking whether
  proposal draft is ready for internal review by Friday.
- Links shared: https://example.com/nasa-rfp-2026.pdf

Public Activity:
- #dev: [Chad shared](link) benchmarks for the new API migration. Discussion on
  whether to proceed with Option A (incremental) or Option B (full rewrite).
  Key posters asking: timeline for staging deploy, test coverage requirements.
- #general: [Danielle posted](link) update on NEED Act reintroduction.
  Positive sentiment — team excited about funding implications.

@-mentions:
- From Cynthia in [#proposal-plans](link) on Mar 10, 2:15 PM: "Can you review
  the budget section before tomorrow's call?"
- From Leslie in [#moda-blockly-dev](link) on Mar 10, 4:30 PM: "Your widget
  layout PR is ready for review"
```
