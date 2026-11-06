#!/usr/bin/env python3
"""Verify source-hashed complete theorem registry against the current Git checkout.

The registry attests discoverability and exact source bytes; it never certifies claims.
Run in any complete Git working-tree checkout, including PR CI.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,re,subprocess,sys
from pathlib import Path

CATALOG='docs/research/THEOREM_INDEX_LIVE.json'
NAV='docs/research/THEOREM_INDEX.md'
PATTERN=re.compile(r'(?:\.\./\.\./)?research/theorems/([A-Za-z0-9_.-]+\.md)')

def git(*args):
    result=subprocess.run(['git',*args],capture_output=True,check=True)
    return result.stdout

def run(root:Path):
    root=root.resolve()
    if not (root/'.git').exists():
        raise AssertionError('Must run in a full Git working-tree checkout; archive alone is insufficient')
    source=git('-C',str(root),'ls-files','-z','--','research/theorems')
    paths=sorted(x.decode() for x in source.split(b'\0') if x and x.endswith(b'.md'))
    assert paths and len(paths)==len(set(paths))
    all_p=set(paths)
    catalog=json.loads((root/CATALOG).read_text())
    assert catalog['schema']=='singular-boundary-theorem-index-v1'
    records=catalog['theorems']
    assert catalog['count']==len(records)==len(paths)
    assert [r['path'] for r in records]==paths
    for item in records:
        p=item['path']
        assert item['indexing_status']=='source-file-indexed' and item['certification']=='not-inferred'
        assert p.startswith('research/theorems/') and p.endswith('.md') and '..' not in p
        raw=(root/p).read_bytes()
        assert len(raw)==item['bytes'],p
        calculated=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert calculated==item['git_blob_sha'],p
        assert git('-C',str(root),'hash-object',p).decode().strip()==calculated
    md=(root/NAV).read_text()
    links=['research/theorems/'+x for x in PATTERN.findall(md)]
    count=collections.Counter(links)
    assert set(count)==all_p,(len(set(count)),len(all_p),sorted(all_p-set(count))[:10],sorted(set(count)-all_p)[:10])
    assert all(n==1 for n in count.values()),[(p,n) for p,n in count.items() if n!=1][:10]
    assert 'Historical baseline' in md and 'Current branch additions' in md
    print(json.dumps({'status':'PASS','indexed_theorem_paths':len(paths),'no_missing_or_ghost_links':True,
                      'exact_once':True,'blob_hashes_verified':len(paths),'index_certification':'not-inferred'},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,default=Path.cwd());a=p.parse_args()
    try:run(a.repo)
    except Exception as exc:
        print('FAIL theorem index:',repr(exc),file=sys.stderr);sys.exit(1)
