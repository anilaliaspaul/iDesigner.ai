# Iteration and versioning

Each project must have:

```text
output/projects/<project-slug>/
├── brief.json
├── design-decisions.md
├── feedback-log.md
├── asset-log.json
├── qa-report.md
├── versions/
│   ├── v01/preview.png
│   ├── v02/preview.png
│   └── ...
└── final/
```

- Use `v01`, `v02`, etc. for each meaningful draft. Never overwrite a prior version.
- Keep the original brief immutable; append approved changes in `design-decisions.md`.
- Translate feedback into a targeted change list before editing.
- Record which elements are locked/approved and must not change.
- After editing, obtain a new preview and run relevant QA checks.
- A design is `approved` only after explicit user approval. A Canva save/commit is not the same as user approval of the final artwork.
- When editing an existing Canva design, follow the connected tool's transaction model and obtain required approval before committing.
- Do not overwrite a previously approved Canva design unless the user explicitly asks for an in-place update. Prefer a duplicate/new design for new campaign versions.
