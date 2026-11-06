#!/usr/bin/env python3
"""Complete, *discovery-only* theorem-path index; fail closed on missing/stale entries.

From the repository root:
  python observatory/tools/build_theorem_catalog.py --write
  python observatory/tools/build_theorem_catalog.py --check

Never infer mathematical validity from a filename or Git blob. The curated graph
and claim ledger, not this file index, assess claims and proof obligations.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
THEOREMS = ROOT / 'research' / 'theorems'
CAT = ROOT / 'observatory' / 'catalog.js'
INDEX = ROOT / 'docs' / 'research' / 'THEOREM_INDEX_CURRENT.md'
GRAPH = ROOT / 'observatory' / 'knowledge-graph.json'
GRAPHDATA = ROOT / 'observatory' / 'knowledge-graph-data.js'
PREFIX = 'window.SB_CATALOG='
GPREFIX = 'window.SB_KNOWLEDGE_GRAPH='

def load_js_json(path, prefix):
    s=path.read_text(encoding='utf-8').strip()
    if not s.startswith(prefix) or not s.endswith(';'):
        raise ValueError(f'Unsupported JS data prefix/suffix: {path}')
    return json.loads(s[len(prefix):-1])

def git_blob_sha(content):
    return hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()

def actual_files():
    if not THEOREMS.is_dir(): raise FileNotFoundError(THEOREMS)
    return {f.relative_to(ROOT).as_posix():(git_blob_sha(f.read_bytes()),len(f.read_bytes()))
        for f in sorted(THEOREMS.rglob('*.md')) if f.is_file()}

def graph_references():
    if not GRAPH.is_file(): return {}
    g=json.loads(GRAPH.read_text(encoding='utf-8'))
    d={}
    for n in g.get('nodes',[]):
      for s in n.get('sources',[]):
        p=s.get('path','')
        if p.startswith('research/theorems/'):
          d.setdefault(p,[]).append(n.get('id',''))
    return {p:sorted(set(ids)) for p,ids in d.items()}

def records_for(actual,old):
    previous={r['path']:r for r in old.get('records',[])}
    refs=graph_references()
    records=[]
    for p,(sha,size) in sorted(actual.items()):
      record={**previous.get(p,{})}
      record.update(path=p,sha=sha,size=size)
      record.setdefault('track','unclassified')
      record.setdefault('evidence','Indexed path and Git blob only')
      record.setdefault('scope','Source body not individually audited in this investigation')
      # Valid curated graph nodes refer to specific source bodies; these links
      # are navigation, NOT status certification.
      if p in refs: record['graph_nodes']=refs[p]
      else: record.pop('graph_nodes',None)
      records.append(record)
    return records

def current_markdown(records):
    lines=['# Current complete theorem-file index','',
      '**Scope:** all tracked Markdown paths under `research/theorems/` in this checked-out revision. '
      'An indexed file is **not** a verified theorem, an independent proof, or a closed continuum gate.','',
      f'**Current theorem files:** **{len(records)}**. '
      'Historical 740-record snapshot: [THEOREM_INDEX.md](THEOREM_INDEX.md); '
      'older 538-record snapshot: [November 4](THEOREM_INDEX_SNAPSHOT_2026-11-04.md).','',
      'The SHA-1 column is the complete **Git blob ID for the file bytes**. '
      'The index is rebuilt by `python observatory/tools/build_theorem_catalog.py --write` '
      'and checked by `--check` in repository CI. ','',
      '| Source theorem record | Git blob SHA-1 |', '|---|---|']
    for record in records:
      path=record['path'];name=Path(path).name;sha=record['sha']
      lines.append(f'| [{name}](../../{path}) | `{sha}` |')
    lines.extend(['',f'**Coverage:** {len(records)} of {len(records)} tracked theorem Markdown files indexed.',
      'Scientific status is source- and model-dependent; consult the source body, '
      'its correction chain, and the curated [Proof Atlas](../../observatory/graph.html).',''])
    return '\n'.join(lines)

def index_rows(s):
    pat=re.compile(r'^\| \[([^\]]+)\]\(\.\./\.\./(research/theorems/[^\)]+\.md)\) \| `([0-9a-f]{40})` \|$',re.M)
    found={}
    for name,path,sha in pat.findall(s):
      if path in found: raise ValueError('Duplicate index path: '+path)
      if name!=Path(path).name: raise ValueError('Wrong filename label: '+path)
      found[path]=sha
    return found

def check(actual):
    errors=[];cat=load_js_json(CAT,PREFIX)
    records=cat.get('records',[])
    if cat.get('count')!=len(records): errors.append(f'catalog count field {cat.get("count")} != list size {len(records)}')
    paths=[r.get('path') for r in records]
    if len(set(paths))!=len(paths):errors.append('duplicate catalog paths')
    if paths!=sorted(paths):errors.append('catalog paths are not sorted')
    seen={r['path']:r['sha'] for r in records}
    actual_sha={p:v[0] for p,v in actual.items()}
    if set(seen)!=set(actual_sha):
      errors.append(f'catalog missing={sorted(set(actual_sha)-set(seen))} stale_paths={sorted(set(seen)-set(actual_sha))}')
    changed={p:(seen[p],actual_sha[p]) for p in actual_sha.keys()&seen.keys() if seen[p]!=actual_sha[p]}
    if changed:errors.append('catalog mismatched blob SHA: '+str(changed))
    index=index_rows(INDEX.read_text(encoding='utf-8')) if INDEX.exists() else {}
    if index!=actual_sha:
      errors.append(f'index paths/hashes mismatch: missing={sorted(set(actual_sha)-set(index))}; extraneous={sorted(set(index)-set(actual_sha))}; changed={[p for p in actual_sha.keys()&index.keys() if index[p]!=actual_sha[p]]}')
    if GRAPH.is_file():
      g=json.loads(GRAPH.read_text(encoding='utf-8'))
      if g.get('indexed_theorem_paths')!=len(actual):errors.append('graph indexed_theorem_paths differs from actual files')
      if GRAPHDATA.is_file():
        d=load_js_json(GRAPHDATA,GPREFIX)
        if d!=g:errors.append('graph and client JS data differ')
    if errors:
      for e in errors: print('FAIL:',e,file=sys.stderr)
      raise SystemExit(1)
    print(f'PASS: {len(actual)} / {len(actual)} theorem files indexed with exact Git blob SHA; full graph metadata synchronized')

def write(actual):
    cat=load_js_json(CAT,PREFIX)
    records=records_for(actual,cat)
    cat['count']=len(records);cat['records']=records
    cat['index_kind']='discovery_only'
    CAT.write_text(PREFIX+json.dumps(cat,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    INDEX.write_text(current_markdown(records),encoding='utf-8')
    if GRAPH.exists():
      g=json.loads(GRAPH.read_text(encoding='utf-8'))
      g['indexed_theorem_paths']=len(records)
      g['complete_theorem_index']='docs/research/THEOREM_INDEX_CURRENT.md'
      GRAPH.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
      GRAPHDATA.write_text(GPREFIX+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    print(f'WRITE: {len(records)} indexed theorem files; discovery only; no gate status changed')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true');mode.add_argument('--check',action='store_true')
    args=parser.parse_args()
    inventory=actual_files()
    if args.write:write(inventory)
    check(inventory)
