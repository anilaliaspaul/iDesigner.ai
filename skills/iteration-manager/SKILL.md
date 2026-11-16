---
name: iteration-manager
description: Use when revising an existing design, tracking feedback, managing versions or preparing final approval.
---

# Iteration Manager

Translate feedback into targeted edits. Preserve approved elements and previous versions. Maintain brief, decisions and revision log. Require explicit approval before finalization. Read references/iteration-and-versioning.md.

## Mandatory revision and approval gates

- Every material revision creates a new version and triggers a complete QA review of the new rendered artifact.
- Never carry a PASS from an earlier version to a revised version.
- If QA is FAIL or UNKNOWN, return the defect list to the designer, correct the issues and rerun QA. Do not ask the user to approve a failed or unverified version.
- After QA PASS, show the preview and QA summary and request explicit user approval.
- If the user requests changes, revise surgically and repeat QA.
- After explicit user approval, ask separately whether the user wants the design opened in Canva.
- Open the exact verified Canva design only after the user agrees. Never auto-open Canva or treat approval of the design as consent to launch the editor.

