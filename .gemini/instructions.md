# Project Quick Reference (Cheat Sheet)

Always use `uv run` to execute commands in this project.

## 🚀 Core CLI Commands
The main CLI tool is `py-invoices`.

| Action | Command |
| :--- | :--- |
| **Setup** | `uv run py-invoices setup` |
| **Init** | `uv run py-invoices init` |
| **Config** | `uv run py-invoices config show` |
| **Validate**| `uv run py-invoices validate` |

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

## 🛠️ Utility Scripts
- **Extract PDF Text:** `uv run src/extract_invoice.py Inbox/file.pdf`

## 🤖 Agent Workflows
Run these via my system (e.g., "Run the setup workflow"):
- `setup`: Interactive project setup.
- `update_deps`: Update project dependencies.
- `release`: Release a new version.
- `issue_report`: Debug and report issues.

## 📂 Project Structure
- `Inbox/`: Place incoming invoices here for extraction.
- `Outbox/`: Generated invoices (PDF/HTML) appear here.
- `Sent/`: Archive for sent invoices.
- `data/`: Persistent storage (Markdown/YAML/SQLite).
- `src/`: Custom scripts and integration logic.
