---
name: clone-invoice
description: Clone the last invoice of a specific client to create a new one, and optionally generate output formats like PDF or HTML.
---

# Clone Invoice Skill

This skill provides step-by-step instructions for an agent to clone the last invoice of a specific client using the `py-invoices` CLI.

## When to Use

Use this skill when the user asks to clone the last invoice of a specific client. This workflow assumes the client and at least one of their invoices already exist in the system.

## Instructions

Follow these instructions to execute the cloning process reliably:

### Step 1: Identify the Last Invoice of the Specified Client
1. List all available invoices:
   ```bash
   uv run inv invoices list
   ```
2. Search through the list of invoices for the specified client's name.
3. Find the most recent (last) invoice number (e.g., `INV-2026-0005`) for that specific client.

### Step 2: Clone and Issue the Invoice
Since py-invoices 6.0, `invoices clone` creates a draft numbered `DRAFT-<id>` that renders with a DRAFT watermark. Never render or send a draft; issue it first.

1. If nothing needs changing, clone and issue in one step:
   ```bash
   uv run inv invoices clone [INVOICE_IDENTIFIER] --issue
   ```
   Note the issued number (e.g., `INV-2026-0018`) from the command output.
2. If the amount, quantity, description or due date changes, clone to a draft with line flags (`--unit-price`, `--quantity`, `--description`, `--due-date`), adjust further with `uv run inv invoices update DRAFT-<id> ...` if needed, then issue it:
   ```bash
   uv run inv invoices clone [INVOICE_IDENTIFIER] --unit-price 1200
   uv run inv invoices issue DRAFT-<id>
   ```
   Note the issued number from the `invoices issue` output; that is `[NEW_INVOICE_NUMBER]` below.
3. An issued invoice cannot be edited or deleted. If it is wrong, correct it with `uv run inv credit-notes create`.

### Step 3: Generate Output Formats (PDF / HTML)
To ensure system dependencies like `WeasyPrint` and `Pango` load successfully on macOS, always supply the correct library paths when generating files.

- **To generate PDF**:
  ```bash
  DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run inv invoices pdf [NEW_INVOICE_NUMBER]
  ```
- **To generate HTML**:
  ```bash
  uv run inv invoices html [NEW_INVOICE_NUMBER]
  ```

### Step 4: Verify & Report
1. Verify the cloned invoice's details:
   ```bash
   uv run inv invoices details [NEW_INVOICE_NUMBER]
   ```
2. Report the new invoice number, date, client name, and paths to any generated PDF/HTML files to the user.
