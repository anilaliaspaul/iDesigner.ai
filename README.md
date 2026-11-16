# iDesigner.ai

**Version 1.3.0** · One creative studio skill system for Claude Code, Cursor, Gemini CLI, Muse Code and OpenAI Codex.

iDesigner.ai is a reference-led creative design workflow. It coordinates specialist skills for art direction, brand protection, image creation, poster design, typography, iteration and independent quality assurance.

## What's included

- Complete creative studio orchestrator and all specialist skills.
- Three role prompts: creative director, brand steward and independent quality reviewer.
- St. Stephen brand kit: official logos, palette, fonts, photographs, reference designs and templates.
- Shared cross-agent instructions and native platform adapters.
- Canonical skills in `skills/` plus a synchronized `.agents/skills/` compatibility mirror.
- Validation and synchronization scripts.

## Start here

Read `docs/PLATFORM-INSTALLATION.md` for platform-specific installation steps. For any design request, the main entry point is:

`skills/graphic-design-studio/SKILL.md`

## Platform support

| Platform | Adapter | Status |
|---|---|---|
| Claude Code | `.claude-plugin/`, `skills/`, `CLAUDE.md` | Native plugin package |
| Cursor | `.cursor-plugin/marketplace.json`, `.cursor/rules/`, `.agents/skills/` | Marketplace + project rules |
| Gemini CLI | `gemini-extension.json`, `GEMINI.md` | Extension context package |
| Muse Code | `.agents/skills/` | Documented project/user skill installation |
| Codex | `plugin.json`, `.codex-plugin/`, `.agents/plugins/` | Portable plugin + compatibility manifest |

**Important:** the skills and design rules are portable; connected tools are not. Image generation, image editing, Canva and Adobe integrations must be available and authorized separately in each host. The plugin discovers available tools at runtime and never pretends a missing integration is installed.

## Validate

```bash
python scripts/sync_portable_skills.py
python scripts/validate_universal.py
```

## Add a brand

Use `scripts/create_brand.py` to scaffold a brand profile, then validate it with `scripts/validate_brands.py`. Keep each brand's logos, fonts, palette and reference designs in its own folder under `resources/brands/`.

## Versioning

See `CHANGELOG.md`. The canonical skill source is `skills/`; never hand-edit `.agents/skills/`. Regenerate the mirror after changing skills.
