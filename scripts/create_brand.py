#!/usr/bin/env python3
"""Create a draft brand resource folder from the studio template."""
import argparse, json, re, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--slug', required=True)
parser.add_argument('--name', required=True)
args = parser.parse_args()
slug = args.slug.lower().strip()
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
    raise SystemExit('Slug must contain lowercase letters, numbers and hyphens only.')
template = ROOT / 'resources' / 'brands' / '_template'
dest = ROOT / 'resources' / 'brands' / slug
if dest.exists(): raise SystemExit(f'Brand already exists: {dest}')
shutil.copytree(template, dest)
data = json.loads((dest/'brand.json').read_text(encoding='utf-8'))
data['slug'] = slug
data['name'] = args.name
(dest/'brand.json').write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
(dest/'design-readme.md').write_text(f'# {args.name}\n\n**Status: DRAFT.** Complete this guide with user-confirmed brand rules.\n\n## Brand essence\n- Mission / audience:\n- Personality:\n- Tone of voice:\n\n## Logo usage\n- Primary logo:\n- Clear space:\n- Minimum size:\n- Approved backgrounds:\n- Never:\n\n## Typography\n- Display:\n- Headings:\n- Body:\n- Fallbacks and language support:\n\n## Visual language\n- Photography:\n- Illustration:\n- Layout preferences:\n- Avoid:\n', encoding='utf-8')
print(f'Created draft brand: {dest}')
print('Add approved assets, complete the guide and run scripts/validate_brands.py before production.')
