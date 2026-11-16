#!/usr/bin/env python3
"""Validate manifests, skill mirrors and required cross-agent entrypoints."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
required = [
    "plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json", ".cursor-plugin/marketplace.json",
    "gemini-extension.json", "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    ".cursor/rules/idesigner-ai.mdc", ".muse-plugin/README.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        raise SystemExit(f"Missing required adapter file: {rel}")
for rel in ["plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json", ".cursor-plugin/marketplace.json",
            "gemini-extension.json", ".agents/plugins/marketplace.json"]:
    json.loads((ROOT / rel).read_text(encoding="utf-8"))
subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
               cwd=ROOT, check=True)
print("Universal package validation passed.")
