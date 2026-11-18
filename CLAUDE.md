# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo actually is

This is **not** primarily a code project. It is a **data workspace + thin wrapper** around the
[`py-invoices`](https://github.com/romamo/py-invoices) PyPI package. Almost all behavior — the entire
`inv` CLI (clients, companies, products, invoices, PDF/HTML rendering, templates) — lives in the
`py-invoices` dependency, **not** in this repository. Source code here is a single helper:
`src/invoice_generator/extract_invoice.py` (the `extract-invoice` CLI for dumping PDF text/tables via pdfplumber).

Practical consequence: when invoice logic misbehaves, the bug is almost always upstream in `py-invoices`,
not in local files. Follow `.agent/workflows/issue_report.md` to isolate it, then report upstream rather
than patching here. Do not modify `.venv` to simulate a fix (see global rules).

## Commands

All commands use `uv run` (per global rules). The `inv` command is an alias for `py-invoices`.

```bash
uv run inv setup        # interactive backend configuration (writes .env)
uv run inv init         # initialize storage (run after setup)
uv run inv config show  # show resolved config
uv run inv validate invoice Outbox/file.xml  # validate a UBL 2.1 XML invoice (does not check data/)
uv run inv validate data                     # check no issued invoice in data/ changed (read-only)
uv run extract-invoice Inbox/file.pdf   # dump text/tables from a PDF

uv run inv clients   [list|create --name "..."]
uv run inv companies [list|create]
uv run inv products  [list|create]
uv run inv payment-notes [list|create]

uv run inv invoices list
uv run inv invoices create --client-name "Name" [--issue]
uv run inv invoices details [NUMBER]
uv run inv invoices clone   [NUMBER] [--issue] [--unit-price X] [--quantity N] [--description ...] [--due-date ...]
uv run inv invoices update  DRAFT-<id> ...   # drafts only
uv run inv invoices issue   DRAFT-<id>       # assign the final number and lock the invoice
uv run inv invoices pdf     [NUMBER] --output-dir Outbox
uv run inv invoices html    [NUMBER] --output-dir Outbox
uv run inv credit-notes create ...           # the only way to correct an issued invoice
```

### Draft -> issue lifecycle (py-invoices 6.0+)

`create` and `clone` make a draft numbered `DRAFT-<id>` that renders with a DRAFT watermark; never render
or send a draft. `invoices issue` (or `--issue` on `create` / `clone`) assigns the next gapless number,
stores a SHA-256 `content_hash` and marks it `SENT`. Issued invoices cannot be edited or deleted, and a
hand edit of `data/invoices/*.md` makes `validate data` fail. Every issued invoice in `data/` is sealed.

Known upstream issues to work around:
- Numbering is one sequence across all companies (romamo/py-invoices#12): do not issue invoices for
  company 2 through `issue` until it is fixed
- `pdf` / `html` ignore `INVOICES_OUTPUT_DIR` and write to `output/` unless `--output-dir` is passed
  (romamo/py-invoices#14), and they overwrite an existing file of the same invoice without warning
  (romamo/py-invoices#15): check the target before re-rendering an invoice that was already sent
- Relative paths such as a company's `logo_path` resolve against the process directory, not `--cwd`
  (romamo/py-invoices#13): run the CLI from the repository root

### PDF generation on macOS (important)

`inv invoices pdf` uses WeasyPrint, which needs Homebrew's native libs (Pango/cairo). Prefix with the
library path or it will fail to load:

```bash
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run inv invoices pdf [NUMBER]
```

## Data model and storage

Configured by `.env` (`files` backend, Markdown format). Entities live under `data/<entity>/` as
**Markdown files with a YAML frontmatter block** holding all fields:

- `data/companies/`, `data/clients/`, `data/products/`, `data/payment_notes/`, `data/invoices/`
- Each file is named `<id>.md` (e.g. `data/invoices/8.md`) and the name must match the `id` inside it:
  the files backend updates by file name (romamo/py-invoices#16). Note the README's mention of `.yaml`
  product files describes a different format than what this `md` backend actually produces — trust the
  on-disk `.md` files.
- Each entity dir has a `_meta.json` with `{"next_id": N}` tracking ID allocation. Do not hand-edit IDs
  carelessly; the CLI manages them.
- `data/audit_logs/` and `data/assets/` (logos), `data/templates/` (Jinja2 `*.html.j2` invoice templates).

**Invoices snapshot client/company data at creation time** (`client_name_snapshot`,
`client_address_snapshot`, `company_*_snapshot`, plus embedded `lines`). Editing a client later does not
retroactively change historical invoices — that is by design. Computed fields (`total_amount`,
`balance_due`, `is_overdue`, ...) are persisted in the frontmatter too.

Prefer editing data through the CLI rather than hand-editing `.md` files, so totals, snapshots, and
`_meta.json` stay consistent.

## Workflow directories

- `Inbox/` — incoming PDFs to extract. `Outbox/` — generated invoices (`INVOICES_OUTPUT_DIR`; earlier renders
  are in `output/`, see romamo/py-invoices#14). `Sent/` — archive.
- `.agent/workflows/*.md` — agent playbooks invoked as slash-style commands: `setup`, `release`,
  `issue_report`. Read the relevant one before doing that task.
- `.agent/skills/clone-invoice/SKILL.md` — packaged skill: clone a client's latest invoice, issue it, render outputs.
- `AGENTS.md` — the canonical agent cheat sheet; keep it and this file in sync when CLI usage changes.

## Releasing

Follow `.agent/workflows/release.md`: clean tree → update `CHANGELOG.md` → `uv version --bump
{major|minor|patch}` → also bump `__version__` in `src/invoice_generator/__init__.py` → tag `vX.Y.Z` →
push tags. Releases in this repo are typically just bumping the pinned `py-invoices` version in
`pyproject.toml` and recording it in the changelog.

Note: the release workflow references `uv run pytest tests/test_version.py`, but there is no `tests/`
directory in this repo — there is no local test suite to run.
