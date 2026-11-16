# Iteration and versioning

For substantial projects maintain:

```text
output/projects/<project-slug>/
├── brief.json
├── asset-map.json
├── production-prompt.md
├── design-decisions.md
├── feedback-log.md
├── qa-report.md
├── versions/v01/preview.png
├── versions/v02/preview.png
└── final/
```

Keep the original brief and source assets immutable. Record reference roles, locked elements, prompt revisions and exact changes. Never overwrite prior versions. Preserve approved parts during iteration. User approval is explicit and separate from a successful save/export operation.
