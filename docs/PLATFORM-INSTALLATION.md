# Cross-platform installation

iDesigner.ai 1.3.0 uses one canonical skill library. Platform files are thin adapters around it. The shared creative workflow is in `skills/graphic-design-studio/SKILL.md`; specialist skills and St. Stephen brand assets remain in the same repository.

## Compatibility and what each adapter does

| Host | Native entry point | Install / enable path | Notes |
|---|---|---|---|
| Claude Code | `.claude-plugin/` + `skills/` | `claude plugin marketplace add anilaliaspaul/iDesigner.ai` then `claude plugin install idesigner-ai@idesigner-ai-marketplace` | Uses the same skills and bundled agent role prompts. |
| Cursor | `.cursor-plugin/`, `.cursor/rules/`, `.agents/skills/` | Add `https://github.com/anilaliaspaul/iDesigner.ai` from Cursor Settings → Plugins/Marketplaces, or use the repo as a project with `.cursor/rules/` and `.agents/skills/`. | Cursor-specific marketplace UI/format may vary by release. Shared AGENTS.md is also present. |
| Gemini CLI | `gemini-extension.json` + `GEMINI.md` | `gemini extensions install https://github.com/anilaliaspaul/iDesigner.ai` | The extension supplies persistent context; skills are available in the repository's `skills/` folder. |
| Muse Code | `.agents/skills/` | `muse skills validate ./.agents/skills/graphic-design-studio` then `muse skills install ./.agents/skills/graphic-design-studio --scope user` | Muse's documented project-skill location is `.agents/skills/<id>/SKILL.md`. Run `muse skills list` to verify. |
| Codex | `plugin.json`, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Add the repo marketplace in Codex Plugins, or use the local plugin folder for testing. | Root `plugin.json` is the portable Agent Plugins manifest; `.codex-plugin/plugin.json` is retained for compatibility. |

## Recommended setup

1. Clone the repository.
2. Install the native adapter for your preferred host.
3. Confirm the `graphic-design-studio` skill is visible.
4. Keep brand assets under `resources/brands/<brand-slug>/`.
5. When editing canonical skills, edit `skills/` then run `python scripts/sync_portable_skills.py`.
6. Run `python scripts/validate_universal.py` before committing or releasing.

## Tool parity is not automatic

A shared skill can travel between agents; tool access cannot. Each host must separately provide or connect:
- an image-generation/image-editing capability;
- file read/write and image preview capability;
- optional Canva MCP for the editable handoff;
- optional Adobe Express integration if that workflow is requested.

The plugin discovers tools at runtime. It must use the best available route and state limitations honestly. It does not install API credentials, bypass platform permissions, or guarantee that one image model produces identical results across hosts.

## Brand assets

The included `resources/brands/ststephen/` kit is retained as a sample brand profile. Treat its logos, fonts, photos, reference designs and palette as user-owned assets. Do not assume other brands use St. Stephen's identity. Add new brands using `scripts/create_brand.py` and validate with `scripts/validate_brands.py`.

## Versioning

- Plugin package version: `1.3.0`
- Canonical skills: `skills/`
- Compatibility mirror: `.agents/skills/`
- Do not hand-edit the generated mirror; regenerate it from the canonical source.
