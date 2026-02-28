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
| **Validate**| `uv run inv validate` |
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
| **Create** | `uv run inv invoices create --client-name "Name"` |
| **Details** | `uv run inv invoices details [NUMBER]` |
| **Clone** | `uv run inv invoices clone [NUMBER]` |
| **Generate PDF** | `uv run inv invoices pdf [NUMBER]` |
| **Generate HTML**| `uv run inv invoices html [NUMBER]` |

## 🤖 Agent Workflows
Use the following slash command workflows for complex autonomous tasks:
- `/setup`: Project configuration and initialization.
- `/update_deps`: Dependency management.
- `/release`: Versioning and release.
- `/issue_report`: Debugging and diagnostic guidelines.

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
