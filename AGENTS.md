# AI Agent Instructions (AGENTS.md)

This document provides instructions and a cheat sheet for AI Agents (Antigravity, Cursor, etc.) operating in this workspace.

## 🎯 Your Role
Your core purpose is to **empower the end-user** to manage their business needs (invoicing, client management, product tracking) using the integrated tools in this project. You are a partner to the user, translating their high-level goals into precise tool executions using the `py-invoices` CLI and managing the project's human-readable data files.

## 🚀 Core Principles
- **CLI First**: Always use `uv run inv` for core operations, and `uv run extract-invoice` for PDF text extraction.
- **Human-Readable Data**: Persistent data is largely stored in `data/` as Markdown or YAML. This allows both the user and you to easily read, edit, and collaborate on records.
- **Agentic Workflows**: Use the workflows defined in `.agent/workflows/` (or similar agents paths) for complex tasks like setup or deployments.

## 🛠️ CLI Operations
The main CLI tool is `inv` (alias for `py-invoices`). **Always use `uv run` to execute commands.**

| Action | Command |
| :--- | :--- |
| **Setup** | `uv run inv setup` |
| **Init** | `uv run inv init` |
| **Config** | `uv run inv config show` |
| **Validate UBL** | `uv run inv validate invoice [XML]` (UBL 2.1 file only; does not check `data/`) |
| **Extract** | `uv run extract-invoice [PDF]` |

### 🏗️ Entity Management

#### Companies & Clients
- **List Companies:** `uv run inv companies list`
- **Create Company:** `uv run inv companies create`
- **List Clients:** `uv run inv clients list`
- **Create Client:** `uv run inv clients create --name "Client Name"`

#### Products & Payments
- **List Products:** `uv run inv products list`
- **Create Product:** `uv run inv products create`
- **Payment Notes:** `uv run inv payment-notes [list|create]`

### 📄 Invoice Operations

| Action | Command |
| :--- | :--- |
| **List** | `uv run inv invoices list` |
| **Create (draft)** | `uv run inv invoices create --client-name "Name"` |
| **Create and issue** | `uv run inv invoices create --client-name "Name" --issue` |
| **Details** | `uv run inv invoices details [NUMBER]` |
| **Clone (draft)** | `uv run inv invoices clone [NUMBER] [--unit-price X] [--quantity N] [--description "..."] [--due-date YYYY-MM-DD]` |
| **Clone and issue** | `uv run inv invoices clone [NUMBER] --issue` |
| **Edit draft** | `uv run inv invoices update DRAFT-<id> ...` (drafts only) |
| **Issue draft** | `uv run inv invoices issue DRAFT-<id>` |
| **Correct issued** | `uv run inv credit-notes create ...` |
| **Generate PDF** | `uv run inv invoices pdf [NUMBER]` |
| **Generate HTML**| `uv run inv invoices html [NUMBER]` |
| **Check stored data** | `uv run inv validate data` (read-only; never add `--seal` without the user's explicit yes) |

#### Invoice lifecycle (py-invoices 6.0+)
- `invoices create` and `invoices clone` store a **draft** numbered `DRAFT-<id>`; a draft renders with a DRAFT watermark and must never be sent to a client
- `invoices issue DRAFT-<id>` assigns the final gapless number (e.g. `INV-2026-0018`), locks the content with a SHA-256 hash and marks it `SENT`. Use the issued number for `pdf` / `html`
- `--issue` on `create` / `clone` does both in one step; use it when nothing needs adjusting
- Issued invoices cannot be edited or deleted. Fix mistakes with `credit-notes create`, not by editing `data/invoices/*.md` (a hand edit makes `validate data` fail)
- Bank details live in payment notes: change them with `payment-notes create`, then `payment-notes set-default`, then `payment-notes deactivate` on the old one

## 🤖 Agent Workflows
Use the following slash command workflows for complex autonomous tasks:
- `/setup`: Project configuration and initialization.
- `/update_deps`: Dependency management.
- `/release`: Versioning and release.
- `/issue_report`: Debugging and diagnostic guidelines.

Skills in `.agent/skills/`:
- `clone-invoice`: Clone a client's last invoice, issue it and render PDF/HTML.

## 📂 Project Structure & Data
- `src/`: Custom scripts and integration logic.
- `Inbox/`: Place incoming invoices here for extraction (`uv run extract-invoice Inbox/invoice.pdf`).
- `Outbox/`: Generated invoices (PDF/HTML) appear here.
- `Sent/`: Sent invoices archive.
- `data/`: Persistent data storage (Markdown/YAML/SQLite).
  - `data/companies/*.md`: Company profiles.
  - `data/clients/*.md`: Client profiles.
  - `data/products/*.yaml`: Product definitions (filename format: `1.service.yaml`).
- `assets/`: Logos and images.
