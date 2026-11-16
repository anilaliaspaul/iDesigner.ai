# iDesigner.ai

![iDesigner.ai — Brand-aware Creative Design Studio](assets/idesigner-ai-wordmark.png)

A single brand-aware design plugin for **Claude Code and OpenAI Codex**. It uses Canva as the primary editable design workspace, supports provider-based image generation through the connected assistant's available tools, and maintains local brand resources and project revision history.

> **Status:** Starter implementation / integration scaffold. Current version: **1.0.0**. The skills, brand registry, onboarding and validation scripts are included. Canva access still requires a user-authorized Canva MCP connection in each agent environment. Image generation is provider-adaptive: the skill uses image-generation tools available in the active host; it does not ship API keys or a private image-generation service.

## Release 1.0.0

Initial public release of iDesigner.ai. This release establishes the plugin identity, Claude Code and Codex manifests, specialist design workflows, brand onboarding, quality-review rules, Canva integration guidance, and product logo assets.

## What is included

- Claude Code plugin manifest and Codex portable + compatibility manifests.
- One main `graphic-design-studio` skill plus focused specialist skills.
- Canva remote MCP configuration at `https://api.canva.com/connect/v1/mcp`.
- Multi-brand local resource structure with sample brand profiles to replace.
- Brand onboarding script and brand validation script.
- Guided flow: brand → output-size intake → optional reference-image analysis and prompt review → creative routes → Canva design → review → revisions → approval → export.
- Per-project brief, decision log, feedback log, versioned previews and final deliverables.
- Mandatory output-platform/dimension question for each new design; optional reference-image intake with critical visual analysis and supplied-prompt review.
- Strict minimalist design guardrails, exact-copy-only policy and logo hard stop.
- Malayalam + English mixed-script typography checks and per-brand font inventories.

## Included specialist skills

- **Canvas design**: visual-first artwork and static compositions.
- **Poster design**: event, campaign and informational posters.
- **Algorithmic art**: reproducible procedural patterns and generative visuals.
- **Brand guidelines**: onboarding, logo/font inventories and brand-rule enforcement.
- **Adobe design from template**: Adobe Express template search/customization when its connector is available.
- **Graphic design skills collection**: catalogue and router for all specialist skills.
- Existing Canva workflow, layout/typography, image specialist, iteration and quality-review skills remain included.

The new skills are available in both Claude Code and Codex through the shared `skills/` directory. Adobe Express is an optional renderer and requires its own connected/authorized integration; it is not bundled as an always-available service. See `skills/graphic-design-skills-collection/references/upstream-skill-catalog.md` for upstream sources and import/licensing policy.

## Quick start

### 1. Extract and place the folder

Keep this directory in a stable location, for example:

```text
~/ai-tools/iDesigner.ai
```

Do not move `resources/brands` outside the plugin unless you also update `config/studio-config.json`.

### 2. Add your brand assets

Each brand lives in `resources/brands/<brand-slug>/`:

```text
brand-name/
├── logos/                 # SVG/PNG; include primary, monochrome and reversed variants
├── typography/            # licensed fonts, Malayalam + English font inventory
├── palette/               # palette.json
├── reference-designs/     # approved examples only
├── assets/                # approved brand-specific imagery/patterns
├── brand.json             # machine-readable identity
└── design-readme.md       # human-readable rules and exceptions
```

Replace the sample profiles with your real brand assets. The starter profiles are intentionally marked as examples and must not be treated as official identities.

**Logo rule:** production is blocked until the official logo is present in the selected brand's `logos/` folder. The studio must ask you to provide it; it must never invent, redraw or approximate one.

**Malayalam + English:** place approved font files in `typography/` (recommended subfolders `malayalam/` and `english/`) and update `font-inventory.json`. Verify Malayalam conjunct shaping and glyph coverage in Canva. If no suitable font is available, the studio must ask before using a fallback.

### 3. Connect Canva

This plugin includes `mcp.json` for Codex and `.mcp.json` for Claude Code, both pointing to Canva's official remote MCP endpoint.

1. In Canva Developer Portal, create an app and enable **Canva MCP** under the Outside Canva integration settings.
2. Configure the OAuth redirect URI required by your client.
3. Keep the client secret in the agent's secure OAuth/credential settings. Never commit it, place it in `mcp.json`, or paste it into a prompt.
4. Connect/authenticate the Canva MCP server in Claude Code or Codex and approve the requested Canva permissions.
5. Verify the connected tools include design creation, editing, export, asset upload and brand/template discovery where your Canva plan allows them.

Canva MCP requires each user to authenticate individually. Canva states that some features such as brand kits, brand templates, autofill and resizing may require Canva Pro or above. See the official links below.

### 4. Install in Claude Code

Use the local plugin directory:

```bash
claude --plugin-dir /absolute/path/to/iDesigner.ai
```

To install directly from GitHub through the plugin marketplace, run:

```bash
/plugin marketplace add anilaliaspaul/iDesigner.ai
/plugin install idesigner-ai@idesigner-ai
```

For an offline/local installation, use the local directory with `--plugin-dir` as above. Restart/reload Claude Code after changing plugin files. The main skill is available as `/idesigner-ai:graphic-design-studio` when the plugin is loaded.

### 5. Install in Codex

The repository includes a Codex marketplace at `.agents/plugins/marketplace.json`, so it can be installed directly from GitHub without copying it into a date-specific workspace:

```bash
codex plugin marketplace add anilaliaspaul/iDesigner.ai --ref main
codex plugin add idesigner-ai --marketplace idesigner-ai
```

For a local installation, add the stable plugin folder as the marketplace source, then install it:

```bash
codex plugin marketplace add /absolute/path/to/iDesigner.ai
codex plugin add idesigner-ai --marketplace idesigner-ai
```

The portable root `plugin.json` is the preferred manifest; `.codex-plugin/plugin.json` is included as a compatibility fallback. The plugin cache is managed by Codex and should not be edited.

For local skill-only use, copy `skills/graphic-design-studio/` into your project's `.agents/skills/graphic-design-studio/` folder. The skill remains useful without Canva MCP, but Canva actions will be unavailable until connected.

### 6. Validate the starter project

```bash
python scripts/validate_brands.py
python scripts/create_brand.py --slug demo-brand --name "Demo Brand"
```

## First use

Invoke the studio skill and say something like:

> Create an event poster. Start by showing me the available brands.

The skill must ask for the brand first when it is not already unambiguously specified, then gather the design brief. It should not ask for every possible detail up front; it asks only for missing essentials.

## Design workflow

1. Discover brands from `resources/brands/` and load the chosen `brand.json` + `design-readme.md`.
2. Confirm asset availability and flag missing/contradictory brand rules.
3. Collect format, audience, objective, exact copy, CTA, dimensions, deadline and supplied assets as needed.
4. Produce 2–3 distinct creative directions with rationale before generating the full design.
5. Use Canva MCP to create an editable Canva design, prefer an approved brand template or brand kit when available, and use exact supplied logos/assets.
6. Show the Canva preview/edit link and request targeted feedback.
7. Apply only requested changes; preserve all unrelated approved elements.
8. Save a revision record locally. Never overwrite prior approved versions.
9. Obtain explicit approval before final export/commit when the Canva operation is destructive or saves edits to an existing design.
10. Export requested digital/print formats and record the final Canva URL and exported file locations.

## Design quality and language safeguards

The default look is professional, minimalist and editorial: one focal point, generous whitespace, disciplined alignment, a restrained palette and only purposeful visual elements. The studio actively avoids cluttered AI-generated poster aesthetics, random floating words, decorative labels, fake stamps, filler captions, arbitrary icons, gratuitous effects and generic AI flourishes.

Only copy supplied by you or explicitly approved by you may appear on the artwork. No invented slogans, scripture, captions, dates, hashtags, microcopy or pseudo-text. Generated imagery must contain no text or logos; requested wording is placed separately as editable Canva text.

For Malayalam + English designs, preserve complete phrases and exact wording. Never split words or detach Malayalam vowel signs/diacritics. Use fonts with verified glyph coverage and shaping, and inspect the actual Canva preview and export. When text does not fit, change the layout or ask for approved shorter wording; never break the sentence to force a fit.

## Image generation policy

Use the active host's image-generation provider or Canva image-generation tools when available. Keep provider selection configurable and avoid hard-coding one vendor. Generated images must not invent text, logos, dates, real people, or brand marks. Place critical text and logos as editable Canva elements. For real people, use only supplied/authorized reference photos and preserve identity.

## Configuration

Edit `config/studio-config.json` to set the resource directory, default output location, default formats and preferred image provider. Relative paths resolve from the plugin root.

## Important limitations

- The scaffold does not contain your actual logos, fonts, palette or design rules. Add them before using the example brands in production.
- Canva MCP availability and tool names can vary by client rollout. The skill tells the agent to discover the live tools instead of assuming a fixed tool list.
- The ChatGPT Canva connection does not automatically authorize Claude Code or Codex. Authenticate separately in each client.
- Brand template and brand-kit features can depend on the Canva plan and the permissions of the signed-in user.
- Provider-based image generation depends on the connected host's available image tools and account entitlements.

## Official documentation

- [Canva MCP overview](https://www.canva.dev/docs/apps/mcp/)
- [Canva MCP quickstart](https://www.canva.dev/docs/apps/quickstart/)
- [Canva MCP access and permissions](https://www.canva.dev/docs/apps/mcp/access/)
- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [OpenAI skills](https://developers.openai.com/plugins/build/skills)
- [Claude Code plugin structure](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev)


## Quality review in release 1.0.0

Release 1.0.0 includes a mandatory semantic content review before visual QA. It checks communication type, audience, single main message, tone, repeated meaning across headings/ribbons/body/footer, personal-vs-institutional voice, and whether each sentence adds value. Personal messages must speak directly to the recipient and must not repeat context already established by the headline or award ribbon. Redundant or audience-inappropriate copy is a hard FAIL, even when the artwork looks polished.


## Mandatory quality and approval lifecycle

Every new design and every material revision follows the same enforced sequence:

1. Create the complete render and inspect the actual artifact.
2. Run the independent Quality Reviewer skill. It must return PASS / FAIL / UNKNOWN with evidence.
3. If QA is FAIL or UNKNOWN, fix the defects and rerun the full QA. The user is not asked to approve an unverified design.
4. After QA PASS, show the preview and QA summary and request explicit user approval.
5. If the user requests changes, revise and repeat QA.
6. After the user explicitly approves the design, ask separately whether they want it opened in Canva.
7. Open the verified Canva design only after the user agrees. Design approval alone is not permission to launch Canva.
8. Export and record the approved deliverables and QA/approval history.

QA PASS, user approval, and permission to open Canva are three separate states. The plugin must never infer one from another.
