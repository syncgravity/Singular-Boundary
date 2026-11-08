#!/usr/bin/env python3
"""PF-I11 restricted D5 graph/face reflection search; NOT a time/no-go theorem.

Only literal permutations of the five source basis indices, with no integer
translations, phason shifts, or transformation of an emergent temporal sector.
"""
from __future__ import annotations
from pathlib import Path
import argparse,json,math
from verify_pf_i11_intrinsic_su2 import validate_source,source_complex,PHI,canonical_edge


def reflected_label(v,k,flipped):
    w=[0]*5
    for j in range(5):w[(k-j if flipped else k+j)%5]=v[j]
    return tuple(w)


def source_edge_weight(e):
    a,b=e
    j=next(j for j in range(5) if a[j]!=b[j])
    k=min(a[j],b[j])
    return 1.0 if math.floor((k+1)/PHI)!=math.floor(k/PHI) else PHI**-2


def check_one(C):
    vertices=set(C.labels);edges=set(C.edges);faces={frozenset(f) for f in C.faces}
    out=[]
    for flip in (False,True):
        for k in range(5):
            if not flip and k==0:continue
            transform=lambda v:reflected_label(v,k,flip)
            vv={transform(v) for v in C.labels}
            ee={canonical_edge(transform(a),transform(b)) for a,b in C.edges}
            ff={frozenset(transform(v) for v in f) for f in C.faces}
            ev=vertices==vv;fe=faces==ff;ed=edges==ee
            weight_all=ed and all(abs(source_edge_weight(e)-source_edge_weight(canonical_edge(transform(e[0]),transform(e[1]))))<1e-14 for e in edges)
            out.append({'is_spatial_index_reflection':flip,'shift_k':k,
                        'preserves_source_vertices_exact':ev,
                        'preserves_source_edges_exact':ed,
                        'preserves_accepted_rhombus_faces_exact':fe,
                        'preserves_Fibonacci_edge_weights':weight_all,
                        'number_vertices_not_in_image':len(vertices-vv),
                        'number_faces_not_in_image':len(faces-ff)})
    return {'Ngrid':C.source_Ngrid,'n_vertices':len(vertices),'n_faces':len(faces),
            'exact_restricted_D5_weighted_face_symmetries':sum(z['preserves_source_vertices_exact'] and z['preserves_source_edges_exact'] and z['preserves_accepted_rhombus_faces_exact'] and z['preserves_Fibonacci_edge_weights'] for z in out),
            'all_nonidentity_permutations':out,
            'interpretation':'A D5 spatial index permutation is not by itself a temporal/reflection-positivity involution. Missing symmetries in one finite selected source graph do not exclude other phases, translations, or emergent-time structures.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source-script',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--ngrids',nargs='+',type=int,default=[7,12,25]);a=p.parse_args()
    validate_source(a.source_script)
    rows=[check_one(source_complex(a.source_script,n)) for n in a.ngrids]
    a.output.write_text(json.dumps({'scope':'Restricted ordinary D5 index maps of each original source finite weighted 2-complex. Not physical time.', 'results':rows},indent=2,sort_keys=True)+'\n')
    for r in rows:
        print(json.dumps({k:r[k] for k in ['Ngrid','n_vertices','exact_restricted_D5_weighted_face_symmetries']}))
