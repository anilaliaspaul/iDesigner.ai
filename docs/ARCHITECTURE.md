# Universal architecture

- `skills/`: canonical source for the orchestrator and specialist workflows.
- `.agents/skills/`: generated mirror for Muse Code and other Agent Skills-compatible hosts.
- `agents/`: role prompts for creative director, brand steward and independent quality reviewer.
- `resources/brands/`: brand kits and exact source assets.
- `workflows/`: reusable production workflows.
- `AGENTS.md`: cross-agent policy and entrypoint.
- `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/`: small host-specific adapters.
- `plugin.json`: portable Agent Plugins manifest.
- `.claude-plugin/`, `.cursor-plugin/`, `.codex-plugin/`, `.muse-plugin/`: host metadata.

The canonical skill source must be changed once. Run `python scripts/sync_portable_skills.py` to refresh `.agents/skills/`. No API keys, MCP endpoints or shell lifecycle hooks are bundled by default.
