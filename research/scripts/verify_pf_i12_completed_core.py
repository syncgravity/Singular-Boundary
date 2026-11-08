#!/usr/bin/env python3
"""PF-I12 boundary-control only: accepted-window full-star core, never
substituted for author's original source-retained vertex population.
"""
from __future__ import annotations
import argparse,collections,json
from pathlib import Path
import numpy as np
from verify_pf_i11_intrinsic_su2 import validate_source,assemble_complex,sha_labels,sha_face_labels
from verify_pf_i9_source_cut_project_bridge import build_direct
from verify_pf_i12_two_sector_coupling import transverse_pairs


def compare_one(source,ngrid,reference,collar=4):
    tiling=source.build_penrose_tiling(ngrid)
    center=np.asarray(tiling['vertices']).mean(axis=0)
    centers=np.asarray([np.mean(t['positions'],axis=0) for t in tiling['tiles']])
    cutoff=.35*float(np.max(np.linalg.norm(centers-center,axis=1)))
    d=build_direct(cutoff+collar,source.GAMMA_GENERIC)
    incident=collections.defaultdict(list)
    for f in d['faces']:
        xy=np.asarray([d['xy'][v] for v in f])
        keep=np.linalg.norm(xy.mean(axis=0)-center)<cutoff
        for v in f:incident[v].append(bool(keep))
    core={v for v,checks in incident.items() if checks and all(checks)}
    C=assemble_complex(core,source.GAMMA_GENERIC,ngrid)
    r=reference[ngrid]
    assert (len(C.labels),len(C.edges),len(C.faces))==(r['n_vertices'],r['n_edges'],r['n_faces']),ngrid
    assert sha_labels(C.labels)==r['source_vertices_sha256']
    assert sha_face_labels(C.faces)==r['direct_accepted_faces_sha256']
    pairs=transverse_pairs(C)
    return {'Ngrid':ngrid,'population':'completed_window_core, not published source retained core',
            'vertices':len(C.labels),'edges':len(C.edges),'faces':len(C.faces),
            'transverse_pairs_shared_vertex_four_families':len(pairs),
            'beta0_exact_first_order_logZ_lambda_derivative':-.75*len(pairs),
            'source_original_count':len(source.select_interior_vertices(tiling,.35)),
            'completed_source_face_SHA256_verified':True}


def main():
    p=argparse.ArgumentParser();p.add_argument('--source-script',type=Path,required=True)
    p.add_argument('--pf-i11-completed-reference',type=Path,required=True)
    p.add_argument('--ngrids',type=int,nargs='+',default=[7,20,25])
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();source=validate_source(a.source_script)
    ref={r['Ngrid']:r for r in json.loads(a.pf_i11_completed_reference.read_text())['results']}
    rows=[]
    for n in a.ngrids:
        row=compare_one(source,n,ref)
        rows.append(row);print(n,row['transverse_pairs_shared_vertex_four_families'],flush=True)
    a.output.write_text(json.dumps({'scope':'separate full-window collar source control; no physical time or continuum proof','results':rows},indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
