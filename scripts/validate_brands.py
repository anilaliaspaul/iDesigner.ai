#!/usr/bin/env python3
"""Validate brand kits in the user's active project workspace."""
import argparse, json, sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--workspace", default=".", help="Active project/workspace root (defaults to current working directory).")
parser.add_argument("--brand", help="Validate one brand slug; otherwise validate all.")
args = parser.parse_args()

workspace = Path(args.workspace).expanduser().resolve()
brands_dir = workspace / "resources" / "brands"
folders = [brands_dir / args.brand] if args.brand else sorted(
    x for x in brands_dir.iterdir() if x.is_dir() and not x.name.startswith("_")
) if brands_dir.is_dir() else []

errors = 0
warnings = 0
if not folders:
    print(f"No brand kits found in {brands_dir}.")
    sys.exit(0)

for folder in folders:
    print(f"\n== {folder.name} ==")
    profile = folder / "brand.json"
    if not profile.exists():
        print("ERROR: missing brand.json")
        errors += 1
        continue
    try:
        data = json.loads(profile.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: invalid JSON: {exc}")
        errors += 1
        continue

    for key in ["name", "slug", "status", "palette_file", "logo_assets", "typography", "logo_rules", "design_rules"]:
        if key not in data:
            print(f"ERROR: missing field {key}")
            errors += 1

    palette = folder / data.get("palette_file", "palette/palette.json")
    if not palette.exists():
        print(f"ERROR: missing palette file: {palette}")
        errors += 1
    else:
        try:
            palette_data = json.loads(palette.read_text(encoding="utf-8"))
            if not palette_data.get("colors"):
                print("WARNING: palette has no colour tokens yet.")
                warnings += 1
        except Exception as exc:
            print(f"ERROR: invalid palette JSON: {exc}")
            errors += 1

    if not (folder / "design-readme.md").exists():
        print("ERROR: missing design-readme.md")
        errors += 1

    if data.get("status") not in {"active", "approved", "proposed", "draft"}:
        print(f"WARNING: unfamiliar status '{data.get('status')}'.")
        warnings += 1
    elif data.get("status") not in {"active", "approved"}:
        print(f"WARNING: status is '{data.get('status')}'; confirm inferred rules before treating them as official.")
        warnings += 1

    primary = (data.get("logo_assets") or {}).get("primary")
    if not primary:
        print("INFO: no primary logo configured. This is allowed; proceed without a logo or reserve space if requested.")
    elif not (folder / primary).is_file():
        print(f"WARNING: configured logo file not found: {primary}")
        warnings += 1

    typography = data.get("typography", {}).get("language_support", {}).get("fonts", {})
    if not typography.get("malayalam", {}).get("files"):
        print("WARNING: no Malayalam font file configured; verify shaping before Malayalam production.")
        warnings += 1
    if not typography.get("english", {}).get("files"):
        print("WARNING: no English font file configured; verify the chosen font before production.")
        warnings += 1

    print("Brand-kit structure validation completed.")

print(f"\nSummary: {errors} error(s), {warnings} warning(s).")
sys.exit(1 if errors else 0)
