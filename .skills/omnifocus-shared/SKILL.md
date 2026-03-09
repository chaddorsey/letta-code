---
name: omnifocus-shared
version: 1.0.0
description: "OmniFocus CLI: Shared patterns for installation, global flags, schema discovery, and security rules."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["omnifocus-cli"]
---

# omnifocus-cli — Shared Reference

## Installation

### Host (Letta Code on macOS)

```bash
pip install ./omnifocus-cli
```

When running on macOS, the CLI calls `/usr/bin/osascript` directly — no HTTP bridge needed. OmniFocus must be installed and running.

### Docker (Standard Letta)

Volume-mounted and pip-installed via `entrypoint-wrapper.sh`. Uses the HTTP bridge at `OMNIFOCUS_BRIDGE_URL` (default: `http://host.docker.internal:8888`) to reach the AppleScript bridge on the macOS host.

Both environments coexist — the bridge auto-detects which transport to use.

## CLI Syntax

```bash
omnifocus-cli [global-flags] <group> <action> [flags]
```

**Global flags go BEFORE the subcommand:**

| Flag | Description |
|------|-------------|
| `--body '{"key": "val"}'` | JSON input (agent-first path) |
| `--format json\|text` | Output format (default: auto-detect) |
| `--fields id,name,...` | Comma-separated output field mask |
| `--dry-run` | Validate and preview, no execution |

## Schema Discovery

```bash
# List all available methods
omnifocus-cli schema --list

# Inspect a method's parameters, types, and requirements
omnifocus-cli schema task.create
```

Always use `schema` to discover parameters before constructing `--body` payloads.

## Input Paths

1. **Agent path (preferred):** `--body '{"name": "Buy milk", "flagged": true}'`
2. **Human path:** `--name "Buy milk" --flagged` (convenience flags per command)

If both `--body` and convenience flags are provided, `--body` wins.

## Exit Codes

| Code | Meaning | Output |
|------|---------|--------|
| 0 | Success | stdout = JSON |
| 1 | Execution error | stderr has details |
| 2 | Validation error | stdout = JSON with field-level errors |

## Security Rules

- **Always** use `--dry-run` before destructive operations (delete, complete, move)
- **Confirm** with user before executing writes that affect multiple items
- UUIDs are opaque — never construct, modify, or guess them
- Dates must be ISO 8601 (e.g., `2026-03-10`, `2026-03-10T17:00:00Z`)

## Workflow Pattern

```
1. omnifocus-cli schema task.create          — discover params
2. omnifocus-cli --body '...' --dry-run task create  — validate
3. omnifocus-cli --body '...' task create             — execute
4. Parse stdout JSON for result
```
