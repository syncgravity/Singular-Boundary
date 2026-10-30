#!/usr/bin/env python3
"""Check a sufficient *exact* SU(2) Wilson local-energy certificate.
Input JSON: {"faces": {"face_id": ["edge_id", ...]}, "fill": ["face_id", ...]}
All retained faces must be included. An edge is private for a face if it
occurs in exactly that face among *currently retained* faces.
This test is sufficient, not necessary. No claim about Penrose data is made
without the actual prism incidence file.
"""
import json,sys
from collections import defaultdict
from pathlib import Path

def certify(data):
    faces={str(k):list(map(str,v)) for k,v in data['faces'].items()}
    fill=set(map(str,data['fill']))
    if not fill<=faces.keys():raise ValueError('Fill face missing from retained incidence')
    if any(len(edges)!=len(set(edges)) for edges in faces.values()):
        raise ValueError('Repeated edge within face: requires separate analysis')
    active=set(faces); remaining=set(fill); steps=[]
    while remaining:
        edge_faces=defaultdict(set)
        for f in active:
            for e in faces[f]:edge_faces[e].add(f)
        eligible=[]
        for f in sorted(remaining):
            private=sorted(e for e in faces[f] if edge_faces[e]=={f})
            if private:eligible.append((f,private[0]))
        if not eligible:break
        f,e=eligible[0]
        steps.append({'face':f,'private_edge':e})
        active.remove(f);remaining.remove(f)
    return {'retained_count':len(faces),'fill_count':len(fill),
            'peeled_count':len(steps),'peeled_steps':steps,
            'unpeeled':sorted(remaining),
            'full_certificate':not remaining,
            'uniform_energy_bound_if_full':'lambda E S_fill <= 1.5 * fill_count',
            'explanation':'Sequential integration of the private edge at each step gives Z_R=z(lambda)^fill_count Z_{R\\fill}; when only part peels, exact factorization applies to the peeled subset.'}

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: peeling_certificate.py incidence.json')
    print(json.dumps(certify(json.loads(Path(sys.argv[1]).read_text())),indent=2))
