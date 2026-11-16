# Muse Code compatibility adapter

Muse Code's documented, reliable project-level skill location is `.agents/skills/<skill-id>/SKILL.md`. This repository includes a generated mirror of every canonical skill there.

Validate and install the main orchestrator skill:

```bash
muse skills validate ./.agents/skills/graphic-design-studio
muse skills install ./.agents/skills/graphic-design-studio --scope user
```

To enable it for the current project:

```bash
muse skills enable graphic-design-studio --scope project
```

Check the installation with `muse skills list`. Muse Code can also import skills from Claude or Codex, but this package uses the shared Agent Skills-compatible folder directly. No undocumented Muse plugin manifest is assumed.
