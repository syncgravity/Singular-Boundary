#!/usr/bin/env python3
"""Fail closed when any tracked theorem/audit Markdown is missing from the live inventory.

Indexing is ONLY discovery. This program never certifies a mathematical claim.
Run from repository: python scripts/verify_theorem_inventory.py [--write]
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

RELPATH="docs/research/THEOREM_INDEX_CURRENT"
SCHEMA="singular-boundary.theorem-file-inventory.v1"

def git_blob(path: Path) -> str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def inventory(root: Path) -> tuple[list[dict],list[dict]]:
    def collect(dirname):
        paths=sorted((root/dirname).glob("*.md"),key=lambda p: p.name)
        return [{"path":p.relative_to(root).as_posix(),"git_blob_sha":git_blob(p),"index_status":"indexed-only"} for p in paths]
    return collect("research/theorems"),collect("research/audits")

def md_doc(data:dict)->str:
    th=data['theorems']; au=data['audits']
    header=("# Current theorem-file index — complete source-tree coverage\n\n"
        f"**{len(th)} theorem Markdown records** under `research/theorems/`; "
        f"**{len(au)} research-audit Markdown records** listed separately. "
        f"Historical verified discovery snapshot: **{data['historical_baseline_paths']}** theorem paths, retained unchanged.\n\n"
        "**Discovery only, never mathematical certification.** A path/hash means the exact source file was indexed, not that its mathematical argument has been checked, accepted, or extended to a continuum theorem. Read the full source, correction history and claim ledger before relying on any result. All P0–P5 Yang–Mills gates, T0–T5 quasicrystalline transfer work, and the independent gravitational goal remain OPEN.\n\n"
        f"Source-tree SHA at inventory creation: `{data['source_tree_sha']}`. "
        "Regenerate/check with `python scripts/verify_theorem_inventory.py --write` / without arguments. "
        "A private pull-request CI check rejects newly added or modified records if this index is stale.\n\n"
        "## Canonical theorem records\n\n| Original theorem record | Git blob SHA-1 (prefix) | Index status |\n|---|---|---|\n")
    lines=[f"| [{r['path'].split('/')[-1]}](../../{r['path']}) | `{r['git_blob_sha'][:12]}` | Indexed only |" for r in th]
    section="\n\n## Separate research-audit records\n\n| Audit record | Git blob SHA-1 (prefix) | Index status |\n|---|---|---|\n"
    lines2=[f"| [{r['path'].split('/')[-1]}](../../{r['path']}) | `{r['git_blob_sha'][:12]}` | Indexed audit only |" for r in au]
    return header+'\n'.join(lines)+section+'\n'.join(lines2)+'\n'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true',help='regenerate current-tree index after source edits');args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    theorem,audit=inventory(root)
    jpath=root/(RELPATH+'.json'); mpath=root/(RELPATH+'.md')
    if args.write:
        try:tree=subprocess.check_output(['git','rev-parse','HEAD^{tree}'],cwd=root,text=True).strip()
        except Exception:tree='working-tree-uncommitted'
        data={'schema':SCHEMA,'snapshot_date':'2026-11-06','source_tree_sha':tree,
              'historical_baseline_paths':740,'theorem_count':len(theorem),'audit_count':len(audit),
              'scope':{'theorem_records':'research/theorems/*.md','audit_records':'research/audits/*.md'},
              'theorems':theorem,'audits':audit}
        jpath.parent.mkdir(parents=True,exist_ok=True)
        jpath.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        mpath.write_text(md_doc(data),encoding='utf8')
        print(f'WRITTEN: {len(theorem)} theorem paths, {len(audit)} audit paths; discovery only')
        return
    if not jpath.is_file() or not mpath.is_file():
        raise AssertionError('Current complete theorem index absent; run --write')
    data=json.loads(jpath.read_text(encoding='utf8'))
    assert data['schema']==SCHEMA
    assert data['historical_baseline_paths']==740, 'historical baseline must be preserved'
    assert data['theorem_count']==len(theorem)==len(data['theorems']),'theorem coverage mismatch'
    assert data['audit_count']==len(audit)==len(data['audits']),'audit coverage mismatch'
    assert data['theorems']==theorem,'unindexed theorem, removed path, or theorem SHA changed'
    assert data['audits']==audit,'unindexed audit, removed path, or audit SHA changed'
    text=mpath.read_text(encoding='utf8')
    for row in theorem:
        needle=f"| [{row['path'].split('/')[-1]}](../../{row['path']}) | `{row['git_blob_sha'][:12]}` | Indexed only |"
        assert text.count(needle)==1, f'missing or duplicate index link: {row["path"]}'
    for row in audit:
        needle=f"| [{row['path'].split('/')[-1]}](../../{row['path']}) | `{row['git_blob_sha'][:12]}` | Indexed audit only |"
        assert text.count(needle)==1, f'missing or duplicate audit link: {row["path"]}'
    gpath=root/'observatory/knowledge-graph.json'
    if gpath.exists():
        g=json.loads(gpath.read_text(encoding='utf8'))
        assert g['indexed_theorem_paths']==740,'historical theorem count must remain unmodified'
        assert g.get('current_theorem_paths')==len(theorem),'Observatory current theorem count mismatch'
        assert g.get('current_audit_paths')==len(audit),'Observatory current audit count mismatch'
        assert g.get('theorem_inventory')=='docs/research/THEOREM_INDEX_CURRENT.json'
        assert all(x['status']=='open' for x in g['nodes'] if x['kind'] in ('gate','goal'))
    print(json.dumps({'status':'PASS','theorem_paths':len(theorem),'audit_paths':len(audit),'historical_paths':740,'meaning':'file provenance and discoverability only; zero mathematical proof claims certified'},indent=2))

if __name__=='__main__':
    try:main()
    except Exception as ex:
        print('THEOREM_INDEX_FAIL:',type(ex).__name__,str(ex),file=sys.stderr)
        sys.exit(1)
