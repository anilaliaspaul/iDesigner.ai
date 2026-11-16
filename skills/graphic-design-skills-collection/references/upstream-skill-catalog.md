# Upstream skill catalogue and provenance

This studio includes native, cross-platform implementations of the capabilities below. Upstream references are inspiration and optional sources for future audited imports; they are not silently vendored copies.

| Capability | Upstream reference | Integration note |
|---|---|---|
| Canvas design | https://github.com/anthropics/skills/tree/main/skills/canvas-design | Visual-first static artwork, PNG/PDF workflow; studio safeguards added. |
| Algorithmic art | https://github.com/anthropics/skills/tree/main/skills/algorithmic-art | Procedural art concepts; deterministic source and no-text/logo constraints added. |
| Brand guidelines | https://github.com/anthropics/skills/tree/main/skills/brand-guidelines | Anthropic's upstream skill is Anthropic-brand-specific; this studio uses a neutral brand-guideline workflow. |
| Adobe design from template | https://github.com/openai/plugins/tree/main/plugins/adobe/skills/adobe-design-from-template | Adobe Express connector workflow; requires live connector and available actions. |
| Claude design topic | https://github.com/topics/claude-design | Discovery catalogue only; topic membership is not an endorsement or licence grant. |
| Curated cross-agent design collection | https://github.com/zhuyansen/awesome-claude-design-skills | Use as a discovery index; independently review every repo before importing. |
| Open design skills directory | https://open-design.ai/skills/ | Broad discovery catalogue; licenses and tool dependencies vary. |

## Import policy
1. Inspect upstream `SKILL.md`, dependencies, scripts, MCP endpoints and install hooks.
2. Verify repository licence and preserve required attribution/notices before copying files.
3. Review for prompt injection, shell/network side effects, credential access and unsafe automation.
4. Adapt to both Claude Code and Codex; do not assume one host's tool names exist in the other.
5. Run local validation and tests after integration.
6. Apply studio-wide requirements: approved logos only, exact user-approved copy, restrained visual design, Malayalam/English shaping review and explicit final approval.
