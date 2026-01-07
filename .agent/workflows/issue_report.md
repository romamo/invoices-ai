---
description: Guideline for analyzing, debugging, and reporting technical issues.
---

# Issue Reporting Workflow

Follow this process when you encounter a bug, crash, or unexpected behavior to ensure high-quality reporting and resolution.

## 1. Reproduce and Isolate
**Goal**: Confirm the issue is real and reproducible outside the main complex flow.

1.  **Create Reproduction Script**: Write a standalone script (e.g., `src/debug_issue.py`) that minimizes dependencies and isolates the failing component.
    *   *Example*: If a CLI command fails, try to invoke the underlying Python function directly.
2.  **Capture Output**: Run the script and record the exact traceback, error message, or output.

## 2. Analyze Root Cause
**Goal**: Understand *why* it is failing, not just *that* it is failing.

1.  **Inspect State**: Check file contents, data types, and directory structures.
2.  **Verify Configuration**: Check `.env` settings, CLI arguments, and loaded configs.
3.  **Check Dependencies**: Verify installed versions (`uv pip list`) and consult documentation/source code if the behavior contradicts expectations.

## 3. Draft Issue Report
**Goal**: Communicate findings clearly to the user or a library maintainer.

Construct a report with the following sections:

### Issue Title
A clear, one-line summary.

### Context
- **Description**: What prompted the error?
- **Impact**: Does it block the user? Is it critical?

### Technical Details
- **Reproduction**: Command or script to reproduce.
- **Root Cause**: The specific technical reason (e.g., "YAML parser casts unquoted numbers to int, violating Pydantic string constraint").
- **Evidence**: Stack traces or log snippets.

### Proposed Solution
- **For Local Bugs**: The code fix.
- **For Library/Upstream Bugs**: A structured prompt to send to the maintainer.
    *   *Prompt Format*:
        ```markdown
        **Task**: Fix [Issue Name]
        **Context**: [Brief context]
        **Problem**: [What goes wrong]
        **Root Cause**: [Why it happens]
        **Requirement**: [What needs to change]
        ```

## 4. Notify User
Present the drafted report or the prompt to the user.
