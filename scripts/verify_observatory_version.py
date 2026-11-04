#!/usr/bin/env python3
"""Fail if Research Observatory HTML header/footer and README current version diverge."""
from pathlib import Path
import re
import json
root=Path(__file__).resolve().parents[1]
page=(root/'observatory/index.html').read_text(encoding='utf-8')
readme=(root/'README.md').read_text(encoding='utf-8')
h=re.search(r'Research Observatory <span class="small">(v[0-9]+\.[0-9]+)</span>',page)
f=re.search(r'Research Observatory (v[0-9]+\.[0-9]+) · GitHub-hosted source',page)
d=re.search(r'Research Observatory current source version: (v[0-9]+\.[0-9]+)',readme)
assert h and f and d,(bool(h),bool(f),bool(d))
assert h.group(1)==f.group(1)==d.group(1),(h.group(1),f.group(1),d.group(1))
assert 'v0.2</span>' not in page
graph=(root/'observatory/proofpaths.js').read_text(encoding='utf-8')
match=re.search(r'const routes=(\[.*?\]);window\.SB_PROOF_PATHS=routes;',graph,re.S)
assert match,'Missing Observatory route array'
routes=json.loads(match.group(1))
ids=[x['id'] for x in routes]
assert len(ids)==len(set(ids)),'Duplicate Observatory route ids'
count=re.search(r'This private source tree contains (\d+) distinct proof pathways',readme)
assert count and int(count.group(1))==len(routes),(count.group(1) if count else None,len(routes))
print('PASS Observatory header/footer/README synchronized:',h.group(1))
print('PASS proof-path README count, route ids:',len(routes))
