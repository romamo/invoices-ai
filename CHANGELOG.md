# Changelog

## [Unreleased]

### Added
- `CLAUDE.md` with project guidance for Claude Code, including the 6.0 draft -> issue lifecycle and known py-invoices issues

### Changed
- Updated `py-invoices` dependency to `>=7.0.0` (pydantic-invoices 1.8.0): each company has its own number series (company 2 now numbers as `RM-INV-...`), `pdf` / `html` honor `INVOICES_OUTPUT_DIR` and `--cwd`, and the bank account given to `create` is stored on the invoice. Breaking: rendering no longer replaces an existing file; pass `--overwrite`
- `CLAUDE.md` and `AGENTS.md` drop the workarounds for romamo/py-invoices#12-#16, fixed in 7.0.0
- `extract-invoice` fails fast: a missing `pdfplumber` raises `ImportError` with the install command instead of prompting to install it, a missing file raises `FileNotFoundError`, and usage errors go to stderr

### Removed
- `.agent/workflows/update_deps.md` (dependency updates follow the `dependency-bumper` skill)

## [0.7.0] - 2026-11-18

### Added
- `clone-invoice` skill (`.agent/skills/clone-invoice/SKILL.md`): clones a client's last invoice and issues it (`--issue`, or `invoices update` then `invoices issue`) before rendering

### Changed
- Updated `py-invoices` dependency to `>=6.0.0` (pydantic-invoices 1.7.0). Breaking: `invoices create` and `invoices clone` now make drafts; pass `--issue`, or run `invoices issue` after adjusting the draft with `invoices update`
- Raised `requires-python` to `>=3.14` (required by py-invoices 6.0.0) and pinned `.python-version` to 3.14
- Documented the draft -> issue lifecycle, `invoices update`, `invoices issue`, credit-note corrections and `validate data` in `AGENTS.md` and `README.md`
- Setup workflow notes the SQL migration needed when an existing SQL database is upgraded to py-invoices 6.0.0

## [0.6.0] - 2026-02-28

### Added
- Unified `AGENTS.md` to provide comprehensive instructions for all AI agents.

### Changed
- Updated `py-invoices` dependency to `>=1.9.0`.
- Standardized CLI usage to `uv run inv` for efficiency.
- Refined `README.md` to reference the unified agent documentation.

### Removed
- Legacy editor-specific agent instructions (`.cursorrules`, `GEMINI.md`).

## [0.5.0] - 2026-02-28

### Changed
- Updated `py-invoices` dependency to `>=1.8.4`.
- Updated documentation to use `inv` as the primary CLI command prefix.
- Refined README with clearer setup and usage instructions.

## [0.4.0] - 2026-01-07

### Added
- Improved AI agent access to local data folders by moving ignore rules from `.gitignore` to `.git/info/exclude`.

### Changed
- Synchronized dependencies to use registry versions of `py-invoices` and `pydantic-invoices` instead of local editables.

## [0.3.0] - 2026-01-07

### Added
- Professionalized project metadata in `pyproject.toml` (Authors, License, Repository URLs).
- Formalized `extract-invoice` CLI script.
- Standardized package structure under `src/invoice_generator`.

### Changed
- Updated `extract_invoice.py` with a proper `main()` entry point.
- Refined agent rules and documentations for the new CLI command.

## [0.2.0] - 2026-01-07

### Added
- Redefined project as an **AI-First User Empowerment Platform**.
- Dedicated [GEMINI.md](GEMINI.md) for Antigravity/Gemini agent specialization.
- Dedicated [.cursorrules](.cursorrules) for Cursor AI agent specialization.
- Core philosophy: User Empowerment + AI + powerful CLI Tools.
- Relative paths in documentation for better portability.

### Changed
- Unified and simplified `README.md` to focus on project philosophy.
- Moved Antigravity-specific instructions to `GEMINI.md`.

## [0.1.0] - 2026-01-05
