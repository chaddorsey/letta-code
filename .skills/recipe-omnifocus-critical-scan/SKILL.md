---
name: recipe-omnifocus-critical-scan
version: 0.1.0
description: "Fast critical-task scan: overdue + flagged + inbox, with optional keyword focus (e.g., CAMEL)."
metadata:
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins: ["omnifocus-cli", "python3"]
      skills: ["omnifocus-shared", "omnifocus-search", "omnifocus-tasks"]
---

# OmniFocus Critical Scan (recipe)

Goal: in ~30–60 seconds, answer **“what could bite me today?”**

This recipe is optimized for the current OmniFocus CLI behavior:
- `search` requires at least one filter flag
- `search --overdue/--flagged` can be slow; avoid piping to `head`
- prefer **JSON → python summarizer**

## 1) Collect raw data (JSON)

```bash
# Inbox (fast)
omnifocus-cli inbox list --limit 200 > /tmp/of_inbox.json

# Overdue (may take a bit)
omnifocus-cli search --overdue --limit 200 > /tmp/of_overdue.json

# Flagged (may take a bit)
omnifocus-cli search --flagged --limit 300 > /tmp/of_flagged.json
```

## 2) Summarize and highlight “critical today”

This script prints:
- counts
- overdue tasks
- flagged tasks
- keyword hits (proposal/CAMEL/etc.)

```bash
python3 - <<'PY'
import json, datetime, re
from pathlib import Path

def load(path):
    p = Path(path)
    if not p.exists():
        return []
    raw = p.read_text()
    return json.loads(raw) if raw.strip() else []

def parse_dt(s):
    if not s:
        return None
    # OmniFocus emits ISO; treat 'Z' as UTC
    try:
        return datetime.datetime.fromisoformat(s.replace('Z', '+00:00'))
    except Exception:
        return None

def norm_task(t):
    return {
        "id": t.get("id"),
        "name": t.get("name"),
        "project": t.get("projectName") or t.get("project") or None,
        "due": parse_dt(t.get("dueDate")),
        "due_raw": t.get("dueDate"),
        "flagged": bool(t.get("flagged")),
        "note": (t.get("note") or "")
    }

now = datetime.datetime.now(datetime.timezone.utc)

inbox = [norm_task(t) for t in load('/tmp/of_inbox.json')]
overdue = [norm_task(t) for t in load('/tmp/of_overdue.json')]
flagged = [norm_task(t) for t in load('/tmp/of_flagged.json')]

# Optional keyword focus (tweak as needed)
keywords = [
    "camel", "proposal", "nsf", "loi", "research.gov",
    "budget", "justification", "dmp", "management plan", "msu",
    "sprint", "c4"
]
kw_re = re.compile(r"(?:%s)" % "|".join(re.escape(k) for k in keywords), re.IGNORECASE)

def hits(tasks):
    out=[]
    for t in tasks:
        blob = (t['name'] or '') + "\n" + (t['note'] or '')
        if kw_re.search(blob):
            out.append(t)
    return out

def fmt(t):
    due = t['due'].astimezone().strftime('%Y-%m-%d %H:%M') if t['due'] else ''
    proj = f" [{t['project']}]" if t['project'] else ''
    return f"- {t['name']}{proj}" + (f" (due {due})" if due else "")

print(f"Now (local): {datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M')}\n")
print(f"Inbox: {len(inbox)} | Overdue: {len(overdue)} | Flagged: {len(flagged)}\n")

print("== Overdue ==")
for t in sorted(overdue, key=lambda x: x['due'] or now):
    print(fmt(t))

print("\n== Flagged ==")
for t in flagged:
    print(fmt(t))

print("\n== Keyword hits (inbox+overdue+flagged) ==")
all_tasks = inbox + overdue + flagged
seen=set(); uniq=[]
for t in all_tasks:
    if t['id'] in seen: continue
    seen.add(t['id']); uniq.append(t)
for t in hits(uniq):
    print(fmt(t))
PY
```

## 3) Next tweaks (intentionally left easy)

- Add a `--today-only` mode (due within 24h)
- Add “top 3” prioritization logic (flagged+proposal-keywords first)
- Map tasks to “Do now / Do later / Delegate / Drop” buckets
- Emit Markdown you can paste into daily briefing
