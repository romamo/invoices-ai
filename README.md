# Invoice Generator

An **AI-First User Empowerment Platform** for personal and business invoice management.

## 🚀 The Philosophy
This project is designed to empower end-users by combining powerful CLI tools with intelligent AI agents.
- **User-Centric**: Built for humans to manage their invoicing needs with minimal friction.
- **AI-Integrated**: Designed to be navigated and operated by AI agents (Antigravity, Cursor) who understand your data and tools.
- **Open Data**: All data is stored in human-readable Markdown and YAML files, ensuring you and your AI assistant always have full visibility and control.

## 🤖 AI Agent Instructions
If you are an AI assistant helping the user with this project, please refer to the unified agent instructions:

- **All Agents**: Refer to [AGENTS.md](AGENTS.md) for specialized workflows, core principles, and CLI cheat sheets.

## Features
- **Client Management**: Store client details in human-readable formats or SQL databases.
- **Product Tracking**: Define products in simple YAML files for easy AI editing.
- **Invoice Generation**: Create professional HTML and PDF invoices.
- **Template System**: Fully customizable Jinja2 templates.


- **Product Management**: Define products in YAML files.
- **Invoice Generation**: Create HTML invoices (PDF if native deps available).
- **Template System**: Customizable Jinja2 templates.

## Structure
```
.
├── src/                # Source scripts (extract_invoice.py)
├── Inbox/              # Input documents (PDFs for extraction)
├── Outbox/             # Generated invoices (PDF/HTML)
├── Sent/               # Sent invoices archive
├── data/               # Persistent data storage
│   ├── invoice.db      # SQLite database (if using local backend)
│   └── ...             # Markdown files (if using files backend)
├── assets/             # Logos and images
└── README.md
```

## PDF Extraction
To extract text from a PDF invoice:
`uv run extract-invoice <path_to_pdf>`
Example: `uv run extract-invoice Inbox/invoice.pdf`

## How to Control
You can manage the project using the `uv run inv` CLI. If you are using an AI-assisted editor, simply ask the agent to "run the setup workflow" or "create a new invoice for client X".


### Commands
- **Setup**: `uv run inv setup` (Interactive configuration)
- **Validate UBL**: `uv run inv validate invoice [XML]` (checks a UBL 2.1 XML file, not the stored `data/`)
- **Extract**: `uv run extract-invoice [PDF]`
- **Configuration**: `uv run inv config show`
- **Add Client**: `uv run inv clients create --name "Client Name"`
- **Add Company**: `uv run inv companies create`
- **Add Product**: `uv run inv products create`
- **Add Payment Note**: `uv run inv payment-notes create`
- **Create Invoice**: `uv run inv invoices create --client-name "Name"`
- **List Invoices**: `uv run inv invoices list`
- **Clone Invoice**: `uv run inv invoices clone [INVOICE_NUMBER]`

## Adding Products
You can use the CLI to create products interactively:
`uv run inv products create`

Alternatively, create a new YAML file in `data/products/`.
Example `data/products/1.service.yaml`:
```yaml
id: 1
name: "Premium Support"
price: 200.0
unit: "hour"
```
The filename must start with a unique integer ID (e.g., `1.anything.yaml`).
