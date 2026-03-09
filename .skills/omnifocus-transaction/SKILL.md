---
name: omnifocus-transaction
version: 1.0.0
description: "OmniFocus: Batch operations with preview, accept, and rollback."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["omnifocus-cli"]
    cliHelp: "omnifocus-cli transaction --help"
---

# transaction & validate

> **PREREQUISITE:** Read `../omnifocus-shared/SKILL.md` for installation, global flags, and security rules.

```bash
omnifocus-cli [global-flags] transaction <action> [flags]
omnifocus-cli [global-flags] validate <action> [flags]
```

## Transaction Actions

| Action | Description |
|--------|-------------|
| `begin` | Start a new transaction (batch of operations) |
| `execute` | Execute a prepared transaction |
| `accept` | Accept and finalize a transaction |
| `rollback` | Roll back an executed transaction |
| `history` | View past transactions |

## Validate Actions

| Action | Description |
|--------|-------------|
| `transaction` | Validate a transaction before execution |
| `move` | Validate a move operation |
| `create` | Validate a create operation |

Run `omnifocus-cli schema transaction.<action>` or `omnifocus-cli schema validate.<action>` for parameters.

## Batch Workflow

```bash
# 1. Begin a transaction with multiple operations
omnifocus-cli --body '{"operations": [
  {"action": "create", "params": {"name": "Task A"}},
  {"action": "create", "params": {"name": "Task B"}},
  {"action": "complete", "params": {"taskId": "abc123"}}
]}' transaction begin

# 2. Validate before executing
omnifocus-cli --body '{"transactionId": "txn789"}' validate transaction

# 3. Execute the transaction
omnifocus-cli --body '{"transactionId": "txn789"}' transaction execute

# 4. Accept if results look good
omnifocus-cli --body '{"transactionId": "txn789"}' transaction accept

# 5. Or rollback if something went wrong
omnifocus-cli --body '{"transactionId": "txn789"}' transaction rollback
```

## Tips

- Always validate before executing
- Use transactions for multi-step operations that should succeed or fail together
- Review transaction history to audit past batch operations
