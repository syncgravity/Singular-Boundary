#!/usr/bin/env python3
"""Forensic inventory and strict full-retained-incidence peeling checker."""
import json,zipfile,hashlib,sys
from pathlib import Path
from collections import defaultdict
import numpy as np
ROOT=Path('/mnt/data')
def peel(faces,fill):
    faces={str(k):tuple(map(str,v)) for k,v in faces.items()}
    remaining=set(map(str,fill));active=set(faces);steps=[]
    if not remaining<=active: raise ValueError('Fill labels missing from retained faces')
    if any(len(es)!=len(set(es)) for es in faces.values()):raise ValueError('Repeated edges in face')
    while True:
        users=defaultdict(set)
        for f in active:
            for e in faces[f]:users[e].add(f)
        eligible=sorted((f,e) for f in remaining for e in faces[f] if users[e]=={f})
        if not eligible:break
        f,e=eligible[0];steps.append({'face':f,'private_edge':e});remaining.remove(f);active.remove(f)
    return {'fill_count':len(fill),'peeled_count':len(steps),'unpeeled':sorted(remaining),'steps':steps,'full_certificate':not remaining}
def inventory():
    p=ROOT/'penrose_complete_catalogue.npz';x=np.load(p,allow_pickle=False)
    info={'catalogue_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'catalogue_fields':{k:{'shape':list(x[k].shape),'dtype':str(x[k].dtype)} for k in x.files},'catalogue_metadata':{'graph_hash':str(x['graph_hash']),'coverage_version':str(x['coverage_version'])},'candidate_files':[]}
    for f in sorted(ROOT.glob('R3*')):
        if f.is_dir():
            for p in f.rglob('*'):
                if p.is_file() and any(s in p.name.lower() for s in ['incidence','bianchi','q14','face','peeling']):info['candidate_files'].append(str(p.relative_to(ROOT)))
    return info
if __name__=='__main__':
    if len(sys.argv)==2:
        data=json.loads(Path(sys.argv[1]).read_text());print(json.dumps(peel(data['faces'],data['fill']),indent=2))
    else:print(json.dumps(inventory(),indent=2))
