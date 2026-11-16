#!/usr/bin/env python3
"""Validate brand profile structure and report production-readiness warnings."""
import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BRANDS = ROOT/'resources'/'brands'
p = argparse.ArgumentParser()
p.add_argument('--brand', help='Validate one brand slug; otherwise validate all.')
args = p.parse_args()
folders = [BRANDS/args.brand] if args.brand else sorted(x for x in BRANDS.iterdir() if x.is_dir() and not x.name.startswith('_'))
errors=0; warnings=0
if not folders: print('No brand folders found.'); sys.exit(0)
for folder in folders:
    print(f'\n== {folder.name} ==')
    profile=folder/'brand.json'
    if not profile.exists(): print('ERROR: missing brand.json'); errors+=1; continue
    try: data=json.loads(profile.read_text(encoding='utf-8'))
    except Exception as e: print(f'ERROR: invalid JSON: {e}'); errors+=1; continue
    for key in ['name','slug','status','palette_file','logo_assets','typography','logo_rules','design_rules']:
        if key not in data: print(f'ERROR: missing field {key}'); errors+=1
    palette=folder/data.get('palette_file','palette/palette.json')
    if not palette.exists(): print(f'ERROR: missing palette file: {palette}'); errors+=1
    else:
        try: json.loads(palette.read_text(encoding='utf-8'))
        except Exception as e: print(f'ERROR: invalid palette JSON: {e}'); errors+=1
    if not (folder/'design-readme.md').exists(): print('ERROR: missing design-readme.md'); errors+=1
    if data.get('status') != 'active': print(f"WARNING: status is '{data.get('status')}', not active; require user confirmation before production."); warnings+=1
    logos=data.get('logo_assets') or {}
    primary=logos.get('primary')
    if not primary: print('BLOCKER: no approved primary logo configured; the studio must ask the user for the official logo before design production.'); warnings+=1
    elif not (folder/primary).exists(): print(f'WARNING: configured primary logo not found: {primary}'); warnings+=1
    colors={}
    if palette.exists():
        try: colors=json.loads(palette.read_text(encoding='utf-8')).get('colors',{})
        except Exception: pass
    if not colors: print('WARNING: no confirmed palette tokens found.'); warnings+=1
    typography=data.get('typography',{}).get('language_support',{}).get('fonts',{})
    if 'malayalam' not in typography or not typography.get('malayalam',{}).get('files'): print('WARNING: no Malayalam font file configured; verify approved Malayalam shaping/font before bilingual production.'); warnings+=1
    if 'english' not in typography or not typography.get('english',{}).get('files'): print('WARNING: no English font file configured; verify approved English font before production.'); warnings+=1
    print('Validation checks completed.')
print(f'\nSummary: {errors} error(s), {warnings} warning(s).')
sys.exit(1 if errors else 0)
