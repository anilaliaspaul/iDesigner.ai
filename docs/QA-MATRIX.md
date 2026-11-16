# Cross-platform QA matrix

## Static checks completed by the package validator
- All platform manifests parse as JSON.
- Every adapter entrypoint exists.
- Every canonical skill has a byte-identical `.agents/skills/` mirror.
- All manifests use the same package version.
- St. Stephen brand kit files are present.
- Skill frontmatter is present.

## Runtime checks to perform after installation
- Claude Code: `/plugin` confirms plugin enabled; invoke `graphic-design-studio`.
- Cursor: confirm marketplace plugin/rule appears; invoke a design request and inspect skill loading.
- Gemini CLI: `gemini extensions list`; start a new session and ask for a poster workflow.
- Muse Code: `muse skills validate ./.agents/skills/graphic-design-studio`, then `muse skills list`.
- Codex: confirm plugin is enabled and invoke the design workflow.

## Functional smoke test
Ask each host: "Create a reference-led event poster. First inspect the supplied reference and brand kit, ask for missing dimensions, preserve the exact copy and official logo, then propose a production route. Do not generate until I approve the brief."

Expected:
1. Main studio workflow is selected.
2. The agent inspects available references and assets.
3. It asks only for missing essentials, including canvas dimensions.
4. It does not invent text or event facts.
5. It discovers image generation and Canva availability rather than assuming them.
6. It requires independent QA and a separate user-approval gate.
7. It reports unavailable integrations honestly.

## Limits
This package validation does not prove every host marketplace accepts its latest manifest schema, nor does it test image generation or Canva in a connected account. Those require a runtime install and smoke test in each target host.
