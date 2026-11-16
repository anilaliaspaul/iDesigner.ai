#!/usr/bin/env python3
"""Sync canonical skills/ into the .agents/skills compatibility mirror."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / ".agents" / "skills"
TARGET.mkdir(parents=True, exist_ok=True)

for item in SOURCE.iterdir():
    if item.is_dir() and (item / "SKILL.md").is_file():
        destination = TARGET / item.name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(item, destination)

print(f"Synced {sum(1 for p in SOURCE.iterdir() if p.is_dir() and (p/'SKILL.md').exists())} skills.")
