---
description: Update project dependencies and sync documentation
---

# Update Dependencies & Docs Workflow

Follow this checklist to update the project dependencies to the latest versions, review changes in `py-invoices`, and update the project documentation accordingly.

## 1. Update Dependencies

First, update the lockfile and install the latest versions of dependencies.

// turbo
1.  Run `uv lock --upgrade` to update `uv.lock` with latest versions.
// turbo
2.  Run `uv sync` to install these new versions into the environment.

## 2. Verify Update

Ensure the update didn't break basic functionality.

1.  Run `uv run py-invoices --help` and ensure it runs without error.
2.  Run `uv pip list` to confirm the version of `py-invoices` is what you expect.

## 3. Review Changes

Check the `py-invoices` changelog to see what's new.

1.  Read `../py-invoices/CHANGELOG.md` to see recent features, breaking changes, or fixes.
2.  Note any new CLI commands, configuration options, or argument changes.

## 4. Update Documentation

Update this project's documentation to reflect any changes.

1.  **README.md**:
    - Update installation instructions if needed.
    - Update usage examples if CLI commands changed.
    - Add sections for new features if relevant.
2.  **.agent/workflows**:
    - Update `setup.md` if the setup process or arguments changed.
    - Update any other workflows that might be affected.

## 5. Commit Changes

Once everything is updated and verified:

1.  Commit the changes to `uv.lock`, `pyproject.toml` (if changed manually), and any updated documentation.
    - Message: `chore: update dependencies and docs`
