---
description: Interactive Agent-driven setup for the project
---

# Agent Setup Instructions

Follow these steps to configure the project for the user.

1.  **Ensure Directory Structure**: Check that `Inbox/`, `Outbox/`, and `data/` directories exist. Create them if missing.
2.  **Present Options**: Ask the user which setup they prefer from the list below.
2.  **Confirm Details**: Once a choice is made, present the exact command you are about to run and ask for explicit confirmation.
3.  **Execute**: Run the setup command, followed by the initialization command.

## Setup Templates

### 1. Direct (Files)
*Best for simple local usage without a database server.*
- **Arguments**: `--backend files --storage-path ./data --file-format md --output-dir Outbox --force`
- **Command**: `uv run py-invoices setup --backend files --storage-path ./data --file-format md --output-dir Outbox --force`

### 2. Local (SQLite)
*Best for robust local usage.*
- **Arguments**: `--backend sqlite --db-url sqlite:///data/invoice.db --output-dir Outbox --force`
- **Command**: `uv run py-invoices setup --backend sqlite --db-url sqlite:///data/invoice.db --output-dir Outbox --force`

### 3. Remote (MySQL)
*Best for multi-user or hosted environments.*
- **Arguments**: `--backend mysql --db-url mysql://user:pass@localhost/db_name --output-dir Outbox --force`
- **Command**: `uv run py-invoices setup --backend mysql --db-url mysql://user:pass@localhost/db_name --output-dir Outbox --force`
- *Note: Ask user if they need to customize the DB URL.*

### 4. Custom
*Full control.*
- **Command**: `uv run py-invoices setup` (interactive)

## Initialization
After successful setup, ALWAYS run:
```bash
uv run py-invoices init
```

## Upgrading an Existing SQL Database to py-invoices 6.0
A `sqlite` or `mysql` database created before py-invoices 6.0.0 needs the schema migration from the
"Migration" section of the 6.0.0 entry in the py-invoices CHANGELOG before any command runs against it
(it adds `invoices.payment_notes_snapshot`, `invoices.content_hash` and the audit `entity_type` /
`entity_id` / `corrects_id` columns). The `files` backend needs no migration.

Then check the stored invoices (read-only):
```bash
uv run inv validate data
```
It lists invoices issued before 6.0 as "unsealed". `uv run inv validate data --seal` records a hash and an
audit entry for each of them, vouching for their current content; run it only after the user confirms the
stored data is correct and explicitly agrees.
