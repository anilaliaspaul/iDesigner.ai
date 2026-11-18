# Cross-platform QA matrix

## Static checks
- All platform manifests parse as JSON and share the same version.
- Every adapter entrypoint exists.
- Every canonical skill and studio reference has a byte-identical .agents mirror.
- The only shipped brand directory is the empty generic template; no client identity is bundled.
- Brand-kit creation writes to the active workspace, not the installed plugin folder.
- Brand template supports proposed kits and does not require a logo.
- Wizard and research references exist.
- Tests cover brand lookup/consent, website-to-poster fallback, reference object mapping, ten-to-three concepts, mobile/accessibility QA and rework.
- Skill frontmatter is valid.

## Runtime checks
- Claude Code: confirm plugin enabled; invoke graphic-design-studio.
- Cursor: confirm marketplace plugin/rule appears; invoke a brand-first poster request.
- Gemini CLI: list extensions; start a new session and ask for a poster workflow.
- Muse Code: validate the graphic-design-studio skill and confirm it appears in the skill list.
- Codex: confirm plugin is enabled and invoke the design workflow.

## Functional smoke test
Ask each host: "I need a poster for a new brand. Ask which brand and search the active project workspace for an existing brand kit. If none exists, tell me and ask permission to create one. Collect official name, address, branding text, tagline, logo and website. If there is no website, ask me to upload a recent poster. Save the brand kit in my project workspace, validate it and reload it. Then ask what to design and the size. If I provide a reference, identify every object, ask for exact replacement assets, resolve missing objects with my choice or suggested alternatives, and ask whether to retain brand typography or use reference typography. Recreate it with the brand identity. If no reference is supplied, research the broad category, avoid clichés, generate ten directions and shortlist three. Produce the design, run independent mobile/accessibility/copy/brand QA, rework failures until PASS, and only then show it for approval."

Expected: brand-first; workspace search before creation; explicit consent; no bundled/default client brand; brand files saved outside plugin installation; no-website poster fallback; exact object asset intake; reference typography choice; no-reference research and ten-to-three selection; exact copy; independent PASS/FAIL/UNKNOWN; designer rework until PASS; user approval only after PASS; honest disclosure of missing web, image, storage or Canva tools.

## Limits
Static validation cannot prove every host marketplace accepts its latest schema or that connected image generation, browser, storage and Canva integrations work in a specific account. Run runtime checks in each host.
