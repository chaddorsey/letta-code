#!/usr/bin/env python3
"""
time-remaining.py — Precise daily time reporting utility.

Usage:
    python3 time-remaining.py '<schedule_json>'
    python3 time-remaining.py  (uses built-in example for testing)

Input JSON schema:
    {
        "work_end": "17:00",          # end of working day (default: 17:00)
        "busy_blocks": [              # meetings and blocked time
            {"name": "...", "start": "HH:MM", "end": "HH:MM"},
            ...
        ]
    }

Output JSON:
    {
        "current_time": "09:08",
        "next_meeting": {"name": "...", "start": "11:00", "minutes_away": 112, "minutes_away_formatted": "1h 52min"},
        "available_windows": [
            {"start": "09:08", "end": "11:00", "duration_minutes": 112, "duration_formatted": "1h 52min", "label": "..."},
            ...
        ],
        "total_available_minutes": 262,
        "total_available_formatted": "4h 22min"
    }
"""

import json
import sys
from datetime import datetime, date, timedelta


def fmt(minutes: int) -> str:
    """Format minutes as '2h 15min' or '45min'."""
    if minutes <= 0:
        return "0min"
    h, m = divmod(minutes, 60)
    if h and m:
        return f"{h}h {m}min"
    elif h:
        return f"{h}h"
    else:
        return f"{m}min"


def to_minutes(t: str) -> int:
    """Convert 'HH:MM' to minutes since midnight."""
    h, m = map(int, t.split(":"))
    return h * 60 + m


def from_minutes(total: int) -> str:
    """Convert minutes since midnight to 'HH:MM'."""
    h, m = divmod(total, 60)
    return f"{h:02d}:{m:02d}"


def merge_busy(blocks: list) -> list:
    """Merge overlapping or adjacent busy blocks, sorted by start time."""
    if not blocks:
        return []
    sorted_blocks = sorted(blocks, key=lambda b: b["start_min"])
    merged = [sorted_blocks[0].copy()]
    for block in sorted_blocks[1:]:
        last = merged[-1]
        if block["start_min"] <= last["end_min"]:
            # Overlapping — extend end, combine names
            if block["end_min"] > last["end_min"]:
                last["end_min"] = block["end_min"]
                last["name"] = last["name"] + " / " + block["name"]
        else:
            merged.append(block.copy())
    return merged


def compute(schedule: dict) -> dict:
    now = datetime.now()
    current_min = now.hour * 60 + now.minute
    current_str = f"{now.hour:02d}:{now.minute:02d}"

    work_end_str = schedule.get("work_end", "17:00")
    work_end_min = to_minutes(work_end_str)

    # Parse and enrich busy blocks
    raw_blocks = []
    for b in schedule.get("busy_blocks", []):
        start_min = to_minutes(b["start"])
        end_min = to_minutes(b["end"])
        if end_min > current_min and end_min <= work_end_min:
            raw_blocks.append({
                "name": b["name"],
                "start_min": start_min,
                "end_min": end_min,
            })

    busy = merge_busy(raw_blocks)

    # Find next meeting (first busy block that starts after now)
    next_meeting = None
    for b in busy:
        if b["start_min"] > current_min:
            mins_away = b["start_min"] - current_min
            next_meeting = {
                "name": b["name"],
                "start": from_minutes(b["start_min"]),
                "minutes_away": mins_away,
                "minutes_away_formatted": fmt(mins_away),
            }
            break

    # If currently IN a meeting, find when it ends
    in_meeting = None
    for b in busy:
        if b["start_min"] <= current_min < b["end_min"]:
            mins_remaining = b["end_min"] - current_min
            in_meeting = {
                "name": b["name"],
                "ends": from_minutes(b["end_min"]),
                "minutes_remaining": mins_remaining,
                "minutes_remaining_formatted": fmt(mins_remaining),
            }
            break

    # Compute available windows from now to end of day
    # Build list of boundary points: [now, ...busy starts/ends..., work_end]
    windows = []
    cursor = current_min

    for b in busy:
        # Skip blocks entirely in the past
        if b["end_min"] <= cursor:
            continue
        # If currently inside this block, skip to its end
        if b["start_min"] <= cursor:
            cursor = b["end_min"]
            continue
        # There's a gap before this block starts
        gap_start = cursor
        gap_end = b["start_min"]
        duration = gap_end - gap_start
        if duration > 0:
            windows.append({
                "start": from_minutes(gap_start),
                "end": from_minutes(gap_end),
                "duration_minutes": duration,
                "duration_formatted": fmt(duration),
                "label": f"{from_minutes(gap_start)} – {from_minutes(gap_end)}",
            })
        cursor = b["end_min"]

    # Final window from last meeting end to work end
    if cursor < work_end_min:
        duration = work_end_min - cursor
        windows.append({
            "start": from_minutes(cursor),
            "end": work_end_str,
            "duration_minutes": duration,
            "duration_formatted": fmt(duration),
            "label": f"{from_minutes(cursor)} – {work_end_str}",
        })

    total_available = sum(w["duration_minutes"] for w in windows)

    return {
        "current_time": current_str,
        "in_meeting": in_meeting,
        "next_meeting": next_meeting,
        "available_windows": windows,
        "total_available_minutes": total_available,
        "total_available_formatted": fmt(total_available),
    }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        schedule = json.loads(sys.argv[1])
    else:
        print(json.dumps({
            "error": "No schedule provided.",
            "usage": "python3 time-remaining.py '<schedule_json>'",
            "hint": "Schedule must be fetched fresh from the calendar agent each day. Do not hardcode.",
            "example": {
                "work_end": "17:00",
                "busy_blocks": [
                    {"name": "Example Meeting", "start": "10:00", "end": "11:00"}
                ]
            }
        }, indent=2))
        sys.exit(1)

    result = compute(schedule)
    print(json.dumps(result, indent=2))
