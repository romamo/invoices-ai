# Invoice Generator

A CLI-based invoice generator powered by Python, `uv`, and `Typer`.


## Antigravity Agent Instructions

If you are the Antigravity Agent, follow these steps to configure and use the project:

### 1. Check Configuration
Run `uv run py-invoices config show`.
- If the "Backend" is "memory", you **MUST** run the setup procedure (Step 2).
- If the "Backend" is "sqlite", "files", or "mysql", you can skip to **Initialization** (Step 3).

### 2. Setup (If Backend is Memory)
Run one of the following commands to configure persistent storage.

**Option A: Local (SQLite)**
`uv run py-invoices setup --backend sqlite --db-url sqlite:///data/invoice.db --output-dir Outbox --force`

**Option B: Direct (Files)**
`uv run py-invoices setup --backend files --storage-path ./data --file-format md --output-dir Outbox --force`

**Option C: Remote (MySQL)**
`uv run py-invoices setup --backend mysql --db-url mysql://user:pass@localhost/db_name --output-dir Outbox --force`

### 3. Initialize
After setup, ALWAYS run:
`uv run py-invoices init`

### 4. Verify
Run `uv run py-invoices config show` again to confirm the backend is correct.

## Features
- **Client Management**: Store client details in your preferred backend (SQLite, Files, MySQL etc.).


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
To extract text from a PDF invoice (useful for analysis):
`uv run src/extract_invoice.py <path_to_pdf>`
Example: `uv run src/extract_invoice.py Inbox/invoice.pdf`

## How to Control
Run commands using `uv run py-invoices [COMMAND]`.


### Commands
- **Setup**: `uv run py-invoices setup` (Interactive configuration)
- **Initialize**: `uv run py-invoices init` (Create data directories)
- **Configuration**: `uv run py-invoices config show`
- **Add Client**: `uv run py-invoices clients create --name "Client Name"`
- **Add Company**: `uv run py-invoices companies create`
- **Add Product**: `uv run py-invoices products create`
- **Add Payment Note**: `uv run py-invoices payment-notes create`
- **Create Invoice**: `uv run py-invoices invoices create --client-name "Name"`
- **List Invoices**: `uv run py-invoices invoices list`
- **Clone Invoice**: `uv run py-invoices invoices clone [INVOICE_NUMBER]`

## Adding Products
You can use the CLI to create products interactively:
`uv run py-invoices products create`

Alternatively, create a new YAML file in `data/products/`.
Example `data/products/1.service.yaml`:
```yaml
id: 1
name: "Premium Support"
price: 200.0
unit: "hour"
```
The filename must start with a unique integer ID (e.g., `1.anything.yaml`).
