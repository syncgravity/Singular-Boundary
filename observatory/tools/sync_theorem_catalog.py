#!/usr/bin/env python3
"""Synchronize the searchable Observatory catalog and Proof Atlas source count.

This is a *source locator*, not mathematical theorem certification. It consumes
the canonical Git-byte-verified THEOREM_INDEX_LIVE.json registry. Run the
existing research/scripts/verify_theorem_index.py before this check.

Usage from the repository:
  python observatory/tools/sync_theorem_catalog.py --write
  python observatory/tools/sync_theorem_catalog.py --check
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LIVE = ROOT / 'docs/research/THEOREM_INDEX_LIVE.json'
NAV = ROOT / 'docs/research/THEOREM_INDEX.md'
CURRENT = ROOT / 'docs/research/THEOREM_INDEX_CURRENT.md'
CAT = ROOT / 'observatory/catalog.js'
GRAPH = ROOT / 'observatory/knowledge-graph.json'
GRAPH_JS = ROOT / 'observatory/knowledge-graph-data.js'
CAT_PREFIX = 'window.SB_CATALOG='
GRAPH_PREFIX = 'window.SB_KNOWLEDGE_GRAPH='

def parse_js(path: Path, prefix: str):
    s = path.read_text(encoding='utf-8').strip()
    if not s.startswith(prefix) or not s.endswith(';'):
        raise AssertionError(f'Unexpected JS catalog framing: {path}')
    return json.loads(s[len(prefix):-1])

def records():
    live=json.loads(LIVE.read_text(encoding='utf-8'))
    old=parse_js(CAT,CAT_PREFIX)
    registered=live['theorems']
    assert live['schema']=='singular-boundary-theorem-index-v1'
    assert live['count']==len(registered) and len(registered)>0
    paths=[r['path'] for r in registered]
    assert paths==sorted(set(paths)), 'Live paths must be unique and bytewise sorted'
    historical={r['path']:r for r in old['records']}
    assert set(historical).issubset(set(paths)), 'Previously displayed theorem was lost'
    result=[]
    for r in registered:
        assert r['indexing_status']=='source-file-indexed' and r['certification']=='not-inferred'
        p=r['path']
        assert p.startswith('research/theorems/') and p.endswith('.md')
        item=dict(historical.get(p,{}))
        item.update(path=p,sha=r['git_blob_sha'],size=r['bytes'])
        item.setdefault('track','unclassified')
        item.setdefault('evidence','Indexed path and Git blob only')
        item.setdefault('scope','Source body not individually audited in this investigation')
        result.append(item)
    assert len(result)==len(paths)
    old['count']=len(result)
    old['records']=result
    old['index_kind']='source-discovery-only'
    old['historical_baseline_count']=live['baseline_historical_count']
    old['complete_index']='docs/research/THEOREM_INDEX_LIVE.json'
    old['source_commit']=live['source_commit']
    return old,live

def current_markdown(catalog,live):
    out=['# Current complete theorem source navigator','','**Current source files:** **%d** indexed paths in this checkout. **Historical baseline:** %d records.'%(catalog['count'],live['baseline_historical_count']),
    'This is source discovery, not independent proof certification or closure of any P0–P5 / Penrose / gravitational goal.','',
    '[Historical navigator and later appendices](THEOREM_INDEX.md) · [Source-hashed canonical registry](THEOREM_INDEX_LIVE.json) · [Curated Proof Atlas](../../observatory/graph.html)','',
    '| Theorem source file | Git blob SHA-1 |','| --- | --- |']
    for r in catalog['records']:
        p=r['path'];out.append('| [%s](../../%s) | `%s` |'%(p.rsplit('/',1)[1],p,r['sha']))
    out.extend(['', '**Coverage: %d / %d source files indexed.**'%(catalog['count'],catalog['count']), 'All scientific statuses must be established separately from the source file.',''])
    return '\n'.join(out)

def expected():
    cat,live=records()
    graph=json.loads(GRAPH.read_text(encoding='utf-8'))
    assert graph['schema']=='singular-boundary.knowledge-graph.v1'
    assert graph['catalog_baseline'], 'Do not erase historic provenance'
    graph['indexed_theorem_paths']=cat['count']
    graph['historical_indexed_theorem_paths']=live['baseline_historical_count']
    graph['complete_theorem_index']='docs/research/THEOREM_INDEX_LIVE.json'
    graph['theorem_index_status']='source-file-indexed; no proof certification inferred'
    if graph.get('version') in ('v2.69-pf-i16-four-face-c2222','v2.70-pf-i16-dressed-locality','v2.71-pf-i16-refined-rotor','v2.72-pf-i16-pointwise-kato-bochner'):
        graph['version']='v2.72-pf-i16-pointwise-kato-bochner'
    graph['git_branch']='main'
    node=next((n for n in graph['nodes'] if n['id']=='R-INDEX'),None)
    assert node is not None, 'Proof Atlas source-index node required'
    node['title']='%d current indexed theorem source files (%d historical baseline)'%(cat['count'],live['baseline_historical_count'])
    node['summary']='All tracked research/theorems Markdown source files appear in the searchable index and source-hashed registry. Indexing only; source access does not certify any mathematical result.'
    node['detail']='Current source count %d, historical discovery baseline %d. All P0–P5 and separate Penrose/gravity objectives remain OPEN. The curated Proof Atlas graph has distinct review scopes.'%(cat['count'],live['baseline_historical_count'])
    import hashlib
    raw=LIVE.read_bytes()
    blob_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    registry_path='docs/research/THEOREM_INDEX_LIVE.json'
    registry_source={'title':'Complete current theorem source registry','path':registry_path,'git_blob_sha':blob_sha,
      'url':'https://github.com/syncgravity/singular-boundary/blob/'+blob_sha+'/'+registry_path}
    node['sources']=[src for src in node.get('sources',[]) if src.get('path')!=registry_path]+[registry_source]

    output={
        CAT:CAT_PREFIX+json.dumps(cat,ensure_ascii=False,separators=(',',':'))+';\n',
        CURRENT:current_markdown(cat,live),
        GRAPH:json.dumps(graph,ensure_ascii=False,indent=2)+'\n',
        GRAPH_JS:GRAPH_PREFIX+json.dumps(graph,ensure_ascii=False,separators=(',',':'))+';\n'
    }
    return output,cat,graph

def check_nav(live):
    text=NAV.read_text(encoding='utf-8')
    match=re.findall(r'(?:\.\./\.\./)?research/theorems/([A-Za-z0-9_.-]+\.md)',text)
    links=['research/theorems/'+x for x in match]
    paths=[r['path'] for r in live['theorems']]
    assert len(links)==len(paths) and set(links)==set(paths), 'Historical navigator lacks sources'
    assert len(set(links))==len(links), 'Duplicate theorem links'

def main():
    ap=argparse.ArgumentParser()
    modes=ap.add_mutually_exclusive_group(required=True)
    modes.add_argument('--write',action='store_true')
    modes.add_argument('--check',action='store_true')
    args=ap.parse_args()
    outputs,cat,graph=expected()
    live=json.loads(LIVE.read_text(encoding='utf-8'))
    check_nav(live)
    if args.write:
        for path,contents in outputs.items():
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(contents,encoding='utf-8')
    else:
        wrong=[]
        for p,c in outputs.items():
            if not p.is_file():wrong.append(str(p.relative_to(ROOT)));continue
            if p==CAT:
                matches=parse_js(p,CAT_PREFIX)==cat
            elif p==GRAPH:
                matches=json.loads(p.read_text(encoding='utf-8'))==graph
            elif p==GRAPH_JS:
                matches=parse_js(p,GRAPH_PREFIX)==graph
            else:
                matches=p.read_text(encoding='utf-8')==c
            if not matches:wrong.append(str(p.relative_to(ROOT)))
        if wrong:raise AssertionError('Stale Observatory theorem source inventory: '+', '.join(wrong))
    assert cat['count']==len(cat['records'])==graph['indexed_theorem_paths']
    assert graph['historical_indexed_theorem_paths']==live['baseline_historical_count']
    assert all(n['status']=='open' for n in graph['nodes'] if n['kind'] in ('gate','goal'))
    print('PASS: %d theorem source records, historical %d, graph/browser/catalog synchronized, gates OPEN'%(cat['count'],live['baseline_historical_count']))

if __name__=='__main__':
    try:main()
    except Exception as exc:print('FAIL:',repr(exc),file=sys.stderr);sys.exit(1)
