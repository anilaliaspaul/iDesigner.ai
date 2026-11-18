# Cross-platform installation

iDesigner.ai uses one canonical, brand-neutral skill library. It contains no preconfigured client identity, sample organization, church, company, logo or brand assets. Each user creates or selects their own brand kit in the active project workspace.

## Compatibility and what each adapter does

| Host | Native entry point | Install / enable path | Notes |
|---|---|---|---|
| Claude Code | `.claude-plugin/` + `skills/` | `claude plugin marketplace add anilaliaspaul/iDesigner.ai` then `claude plugin install idesigner-ai@idesigner-ai-marketplace` | Uses the same skills and bundled agent role prompts. |
| Cursor | `.cursor-plugin/`, `.cursor/rules/`, `.agents/skills/` | Add the repository from Cursor Settings → Plugins/Marketplaces, or use it as a project. | Marketplace UI/format may vary by release. |
| Gemini CLI | `gemini-extension.json` + `GEMINI.md` | `gemini extensions install https://github.com/anilaliaspaul/iDesigner.ai` | Extension supplies persistent context. |
| Muse Code | `.agents/skills/` | `muse skills validate ./.agents/skills/graphic-design-studio` then install using Muse's documented skills workflow. | Verify with `muse skills list`. |
| Codex | `plugin.json`, `.codex-plugin/plugin.json`, `.agents/plugins/` | Add the repository marketplace in Codex Plugins, or use the local plugin folder for testing. | Root manifest is portable; Codex compatibility manifest is retained. |

## Brand-independent onboarding

1. Ask the user which brand the design is for.
2. Search the active workspace brand registry for a matching saved `brand.json`.
3. If found, load the saved brand kit and ask whether to use or update it.
4. If not found, tell the user and ask permission before creating a new kit.
5. After consent, collect official name, address, recurring branding text, tagline, logo and website. If there is no website, request recent posters/designs as visual evidence. Optional fields may be skipped.
6. Save and validate the kit in the user's active workspace, re-read it, and use it as the source of truth for the design.

The plugin repository contains only the generic template at `resources/brands/_template/`. It does not contain a default client brand. Client logos, posters, photos, fonts and private identity assets belong in the user's workspace and must not be committed to this public repository without explicit permission.

## Tool parity is not automatic

A shared skill can travel between agents; tool access cannot. Each host must separately provide or connect:
- image-generation/image-editing capability;
- file read/write and image preview capability;
- optional Canva integration for editable handoff;
- optional Adobe Express integration;
- live web search for comparable-brand research.

The plugin discovers tools at runtime and must state limitations honestly. It does not install credentials, bypass permissions or guarantee identical model results across hosts. If persistent file storage is unavailable, disclose that the brand kit cannot be retained beyond the available session/workspace.

## Versioning

- Plugin package version: `1.4.0`
- Canonical skills: `skills/`
- Compatibility mirror: `.agents/skills/`
- Do not hand-edit the generated mirror; regenerate it from the canonical source.
