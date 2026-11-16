#!/usr/bin/env python3
"""Create a versioned design project workspace."""
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--slug',required=True); p.add_argument('--brand',required=True); p.add_argument('--title',required=True)
a=p.parse_args()
slug=a.slug.lower().strip()
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug): raise SystemExit('Invalid project slug.')
brand=ROOT/'resources'/'brands'/a.brand
if not brand.exists(): raise SystemExit(f'Unknown brand: {a.brand}')
base=ROOT/'output'/'projects'/slug
if base.exists(): raise SystemExit(f'Project already exists: {base}')
for d in ['versions/v01','final','assets']:(base/d).mkdir(parents=True,exist_ok=True)
profile=json.loads((brand/'brand.json').read_text(encoding='utf-8'))
brief={'project_slug':slug,'title':a.title,'brand_slug':a.brand,'brand_name':profile.get('name'),'status':'briefing','created_at':datetime.now(timezone.utc).isoformat(),'format':None,'audience':None,'objective':None,'exact_copy':{},'facts_to_confirm':[],'canva_design_id':None,'canva_edit_url':None}
(base/'brief.json').write_text(json.dumps(brief,indent=2)+'\n',encoding='utf-8')
(base/'design-decisions.md').write_text('# Design decisions\n\nAppend decisions; do not rewrite history.\n',encoding='utf-8')
(base/'feedback-log.md').write_text('# Feedback log\n\n## v01\n- Pending first draft.\n',encoding='utf-8')
(base/'qa-report.md').write_text('# QA report\n\nPending design draft.\n',encoding='utf-8')
(base/'asset-log.json').write_text('[]\n',encoding='utf-8')
(base/'versions/v01/README.md').write_text('# Version v01\n\nStore preview and metadata for the first design draft here.\n',encoding='utf-8')
print(base)
