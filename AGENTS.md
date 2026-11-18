# iDesigner.ai — Shared Agent Instructions

This repository contains a cross-platform creative studio. The canonical workflow is `skills/graphic-design-studio/SKILL.md`.

## Mandatory operating rules
- For any new poster/design, load the main studio skill and follow its staged brand-first wizard.
- Identify the brand first. Reuse an existing kit; otherwise derive a proposed kit from a supplied website, recent posters/logo, or a short interview.
- A logo, website, tagline and address are optional. Never block design production because one is missing. Never fabricate or approximate an official logo.
- Collect poster requirements and output size after brand-kit discovery/review.
- Research comparable brands, audience and occasion; record useful craft patterns and a task-specific OFF-LIMITS cliché list.
- Generate ten distinct directions, shortlist the strongest three and ask the user to choose unless they delegate or provide a decisive reference.
- Treat supplied references as visual specifications when asked to match them. Treat supplied logos, people, churches, products and identity assets as exact source assets.
- Preserve exact user copy. Never invent event facts, captions, dates, names, slogans, scripture, URLs or pseudo-text.
- Protect original files and accepted versions. Revise surgically and maintain version history.
- Run independent QA against the actual rendered/exported artifact. Report PASS / FAIL / UNKNOWN with evidence. UNKNOWN is not PASS.
- Do not claim an image, file, export, Canva design or approval exists unless the active host confirms it.
- Discover image-generation, editing, browser, file-storage and Canva tools at runtime. Never assume an integration is installed.
- If persistent storage is unavailable, disclose that brand-kit persistence is session-scoped; provide exportable kit files where possible.
- Never expose credentials or private environment values. Do not add remote MCP servers or shell hooks without explicit need and consent.

## Specialist routing
- Brand discovery and reusable kit: `brand-steward`, `brand-guidelines`
- Research and concept development: `creative-director`, `graphic-design-studio/references/brand-research.md`
- Poster production: `poster-design`
- Visual-first compositions: `canvas-design`
- Image creation/integration: `image-specialist`
- Layout and multilingual typography: `layout-typography`
- Revisions/versioning: `iteration-manager`
- Independent QA: `quality-reviewer`
- Procedural artwork: `algorithmic-art`
- Adobe Express templates: `adobe-design-from-template` when requested and connected

## Source of truth
`skills/` is canonical. `.agents/skills/` is the generated compatibility mirror. After changing canonical skills, run `python scripts/sync_portable_skills.py`.
