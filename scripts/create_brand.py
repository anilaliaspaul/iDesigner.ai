#!/usr/bin/env python3
"""Create a draft brand kit in the user's active project workspace."""
import argparse, json, re, shutil
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--slug", required=True)
parser.add_argument("--name", required=True)
parser.add_argument("--workspace", default=".", help="Active project/workspace root (defaults to current working directory).")
args = parser.parse_args()

slug = args.slug.lower().strip()
name = args.name.strip()
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
    raise SystemExit("Slug must contain lowercase letters, numbers and hyphens only.")
if not name:
    raise SystemExit("Brand name cannot be empty.")

workspace = Path(args.workspace).expanduser().resolve()
template = PLUGIN_ROOT / "resources" / "brands" / "_template"
brands_dir = workspace / "resources" / "brands"
dest = brands_dir / slug
if dest.exists():
    raise SystemExit(f"Brand already exists: {dest}")
if not template.is_dir():
    raise SystemExit(f"Generic brand template is missing: {template}")

brands_dir.mkdir(parents=True, exist_ok=True)
shutil.copytree(template, dest)
data_path = dest / "brand.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
data["slug"] = slug
data["name"] = name
data["status"] = "proposed"
data.setdefault("branding_text", [])
data.setdefault("recurring_brand_text", [])
data.setdefault("source_provenance", {})
data["source_provenance"].setdefault("method", "interview")
data_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

readme = f"""# {name} — Brand Guide

**Status: PROPOSED.** Confirm inferred rules with the brand owner before treating them as official.

## Brand identity
- Official name: {name}
- Address / location:
- Website:
- Industry / organization type:
- Audience:
- Positioning:
- Mission / purpose:
- Personality / tone:

## Required branding text
- Tagline / motto:
- Recurring brand text:
- Contact details:
- Mandatory wording:

## Source and confidence
- Source type: existing kit / website / posters / logo / interview
- Source pages and filenames:
- Confirmed:
- Inferred:
- Unknown:
- User approval:

## Logo
- Primary logo:
- Variants:
- Clear space / minimum size:
- Approved backgrounds:
- Restrictions:
- Never invent or redraw a missing official logo.

## Colour and typography
- Palette: palette/palette.json
- Font inventory: typography/font-inventory.json
- Display / heading / body fonts:
- Script and language support:
- Fallbacks:

## Visual language
- Photography:
- Illustration:
- Recurring motifs:
- Preferred layout / composition:
- Avoid / cliché blacklist:

## Reference designs
Record each source file, its role, date if known, whether it is an approved brand example or campaign inspiration, and what must be retained.

## Change log
Record user-approved updates to identity, palette, typography, logo rules and recurring copy.
"""
(dest / "design-readme.md").write_text(readme, encoding="utf-8")

asset_folders = {
    "01-Logos": "Store exact original logo files and variants here. Never overwrite or edit the source originals.",
    "04-Reference-Design": "Store user-supplied brand posters and reference designs. Record which elements are recurring identity versus one-off campaign treatment.",
    "05-Photography": "Store approved brand photography and exact identity-critical subject images. Record source and usage permissions.",
    "research": "Store comparable-brand research, source links, design insights and the task-specific cliché blacklist."
}
for folder, note in asset_folders.items():
    target = dest / folder
    target.mkdir(parents=True, exist_ok=True)
    (target / "README.md").write_text(f"# {folder}\n\n{note}\n", encoding="utf-8")

print(f"Created proposed brand kit: {dest}")
print("Add source assets, complete brand details, then run scripts/validate_brands.py --workspace <workspace>.")
