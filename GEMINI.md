# Antigravity / Gemini Agent Instructions

This document provides instructions and a cheat sheet for the **Antigravity Agent** (Gemini).

## 🎯 Your Role
Your core purpose is to **empower the user** to manage their business needs (invoicing, client management, product tracking) using the integrated tools in this project. You are a partner to the user, translating their high-level goals into precise tool executions.

## 🚀 Core CLI Commands
The main CLI tool is `py-invoices`. Always use `uv run` to execute commands.

| Action | Command |
| :--- | :--- |
| **Setup** | `uv run py-invoices setup` |
| **Init** | `uv run py-invoices init` |
| **Config** | `uv run py-invoices config show` |
| **Validate**| `uv run py-invoices validate` |
| **Extract** | `uv run extract-invoice [PDF]` |

## 🏗️ Entity Management

### Companies & Clients
- **List Companies:** `uv run py-invoices companies list`
- **Create Company:** `uv run py-invoices companies create`
- **List Clients:** `uv run py-invoices clients list`
- **Create Client:** `uv run py-invoices clients create --name "Client Name"`

### Products & Payments
- **List Products:** `uv run py-invoices products list`
- **Create Product:** `uv run py-invoices products create`
- **Payment Notes:** `uv run py-invoices payment-notes [list|create]`

## 📄 Invoice Operations

| Action | Command |
| :--- | :--- |
| **List** | `uv run py-invoices invoices list` |
| **Create** | `uv run py-invoices invoices create --client-name "Name"` |
| **Details** | `uv run py-invoices invoices details [NUMBER]` |
| **Clone** | `uv run py-invoices invoices clone [NUMBER]` |
| **Generate PDF** | `uv run py-invoices invoices pdf [NUMBER]` |
| **Generate HTML**| `uv run py-invoices invoices html [NUMBER]` |

## 🤖 Agent Workflows
Use the following workflows for complex tasks. They are optimized for your autonomous execution:
- `/setup`: Project configuration and initialization.
- `/update_deps`: Dependency management.
- `/release`: Versioning and release.
- `/issue_report`: Debugging and diagnostic guidelines.

## 📂 Project Structure
- `Inbox/`: Place incoming invoices here for extraction.
- `Outbox/`: Generated invoices (PDF/HTML) appear here.
- `data/`: Persistent storage (Markdown/YAML/SQLite). Human-readable formats allow you to easily read and edit records for the user.
- `src/`: Custom scripts and integration logic.
