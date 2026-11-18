# iDesigner.ai

**Version 1.4.2** · A brand-first, research-led creative studio for Claude Code, Cursor, Gemini CLI, Muse Code and OpenAI Codex.

iDesigner.ai helps an AI agent work like a modern graphic-design studio: discover the brand, build a reusable brand kit, understand the poster brief, research the visual category, develop concepts, produce artwork and independently validate the final export.

## The design wizard

1. **Identify the brand.** Ask for the brand name and search the active workspace registry.
2. **Create only with consent.** If no kit exists, say so and ask permission. Collect name, address, branding text, tagline, logo and website. If there is no website, request recent posters/designs. Save, validate and reload the kit.
3. **Define the poster.** Collect purpose, audience, exact copy, language, facts, CTA and required assets.
4. **Choose the creative path.** Reference supplied: recreate it with exact object assets and brand integration. No reference: research the broad visual landscape, avoid clichés, develop ten directions and shortlist three.
5. **Produce and verify.** Senior graphic design production, independent senior QA, rework until PASS, then user approval and export.

The wizard is conversational and staged. It reuses known information and allows optional brand fields to be skipped.

## What's included

- Context-aware brand-asset selection: official logos are protected, while optional brand photography is used only when it strengthens the specific design.

- Creative-studio orchestrator and specialist skills for art direction, brand stewardship, poster design, image creation, typography, iteration and independent QA.
- Brand onboarding, reusable brand-kit schema and website/poster/logo discovery.
- Brand research and anti-cliché framework with ten-to-three concept selection.
- English and Malayalam typography guidance.
- Cross-agent adapters and canonical skills in skills/, with a synchronized .agents/skills/ compatibility mirror.
- Generic brand template, validation/synchronization scripts and project workflows.

## Start here

Read docs/PLATFORM-INSTALLATION.md. The main entry point is skills/graphic-design-studio/SKILL.md; the wizard is specified in skills/graphic-design-studio/references/design-wizard.md.

## Platform support

| Platform | Adapter | Status |
|---|---|---|
| Claude Code | .claude-plugin/, skills/, CLAUDE.md | Native plugin package |
| Cursor | .cursor-plugin/marketplace.json, .cursor/rules/, .agents/skills/ | Marketplace + project rules |
| Gemini CLI | gemini-extension.json, GEMINI.md | Extension context package |
| Muse Code | .agents/skills/ | Documented project/user skill installation |
| Codex | plugin.json, .codex-plugin/, .agents/plugins/ | Portable plugin + compatibility manifest |

**Important:** skill instructions are portable; connected tools are not. Image generation, image editing, browser research, persistent file storage, Canva and Adobe integrations must be available and authorized separately in each host. The plugin must disclose missing capabilities rather than pretending they exist.

## Brand kits

The repository contains only an empty generic template. It does not ship with a default client or organization. Search for an existing brand kit first; if none exists, ask permission before creating one. Use scripts/create_brand.py --slug example-brand --name "Example Brand" to scaffold the profile. Collect the website; if unavailable, request recent posters/designs. Save exact logos, photos, references, palette, typography and recurring text in the active workspace. Optional details may be skipped. Validate with scripts/validate_brands.py.

Store client/private brand assets in the active project/workspace. Do not commit them to this public repository without explicit permission.

## Validate

    python scripts/sync_portable_skills.py
    python scripts/validate_universal.py
    python scripts/validate_brands.py

## Versioning

See CHANGELOG.md. skills/ is canonical; never hand-edit .agents/skills/. Regenerate the mirror after changing skills.
