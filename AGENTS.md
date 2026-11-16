# iDesigner.ai — Shared Agent Instructions

This repository contains the iDesigner.ai creative design studio. The canonical workflow is the `graphic-design-studio` skill in `skills/graphic-design-studio/SKILL.md`.

## Mandatory operating rules
- For any design, poster, invitation, social graphic, brand asset, visual campaign, image-generation or design-review task, load and follow the `graphic-design-studio` skill first.
- Load only the relevant specialist skills from `skills/` and use the skill collection router when appropriate.
- Treat supplied reference images as visual specifications when the user asks to match them. Treat supplied logos, people, churches, products and other identity assets as exact source assets, not inspiration to redraw.
- Preserve exact user copy. Never invent event facts, captions, dates, names, slogans, scripture, URLs or pseudo-text.
- For fixed-size artwork, use `design-size-intake`; ask for width, height and units if missing. Do not silently choose a canvas size.
- Protect original files and accepted versions. Revise surgically and maintain version history.
- Run independent QA against the actual rendered/exported artifact. Report PASS / FAIL / UNKNOWN with evidence. UNKNOWN is not PASS.
- Do not claim an image, file, export, Canva design or approval exists unless the active host confirms it.
- Discover available image-generation, editing, file, browser and Canva tools at runtime. Never assume a tool or connector is installed.
- If the active host lacks image generation, provide a complete production prompt and a supported editable/layout alternative; disclose the limitation.
- Canva is an editable handoff only after the artwork passes QA and the user explicitly approves it. If Canva is not connected, report the handoff as pending; do not block delivery of the approved export.
- Never expose API keys, credentials or private environment values. Do not add remote MCP servers or shell hooks without an explicit need and user consent.

## Specialist routing
- Art direction/reference analysis: `creative-director`
- Brand/logo/asset integrity: `brand-steward`, `brand-guidelines`
- Posters and campaigns: `poster-design`
- Visual-first compositions: `canvas-design`
- Image creation/integration: `image-specialist`
- Layout and multilingual typography: `layout-typography`
- Revisions/versioning: `iteration-manager`
- Independent QA: `quality-reviewer`
- Procedural artwork: `algorithmic-art`
- Adobe Express templates: `adobe-design-from-template` when the user asks for it and the integration exists

## Source of truth
`skills/` is canonical. `.agents/skills/` is a generated compatibility mirror for hosts such as Muse Code. When changing a skill, update the canonical copy and run `python scripts/sync_portable_skills.py`.
