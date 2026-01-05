---
description: Interactive Agent-driven setup for the project
---

# Agent Setup Instructions

Follow these steps to configure the project for the user.

1.  **Ensure Directory Structure**: Check that `input/`, `output/`, and `data/` directories exist. Create them if missing.
2.  **Present Options**: Ask the user which setup they prefer from the list below.
2.  **Confirm Details**: Once a choice is made, present the exact command you are about to run and ask for explicit confirmation.
3.  **Execute**: Run the setup command, followed by the initialization command.

## Setup Templates

### 1. Direct (Files)
*Best for simple local usage without a database server.*
- **Arguments**: `--backend files --storage-path ./data --file-format md --force`
- **Command**: `uv run invoice setup --backend files --storage-path ./data --file-format md --force`

### 2. Local (SQLite)
*Best for robust local usage.*
- **Arguments**: `--backend sqlite --db-url sqlite:///data/invoice.db --force`
- **Command**: `uv run invoice setup --backend sqlite --db-url sqlite:///data/invoice.db --force`

### 3. Remote (MySQL)
*Best for multi-user or hosted environments.*
- **Arguments**: `--backend mysql --db-url mysql://user:pass@localhost/db_name --force`
- **Command**: `uv run invoice setup --backend mysql --db-url mysql://user:pass@localhost/db_name --force`
- *Note: Ask user if they need to customize the DB URL.*

### 4. Custom
*Full control.*
- **Command**: `uv run invoice setup` (interactive)

## Initialization
After successful setup, ALWAYS run:
```bash
uv run invoice init
```
