#!/usr/bin/env python3
"""PF-I13 separate source-authenticated completed-window control graph.

Never replaces the author's original source selection. Uses source gamma
and direct accepted-window collar under the PF-I11 reference fingerprints.
"""
from __future__ import annotations
import argparse,collections,json
from pathlib import Path
import numpy as np
from verify_pf_i11_intrinsic_su2 import validate_source,assemble_complex,sha_labels,sha_face_labels
from verify_pf_i9_source_cut_project_bridge import build_direct
from verify_pf_i13_global_gluing import face_pair_graph,verify_phason_height_inversion


def one_completed(source,ngrid,reference):
    original=source.build_penrose_tiling(ngrid)
    center=np.asarray(original['vertices']).mean(axis=0)
    centers=np.asarray([np.mean(t['positions'],axis=0) for t in original['tiles']])
    cutoff=.35*float(np.max(np.linalg.norm(centers-center,axis=1)))
    direct=build_direct(cutoff+4,source.GAMMA_GENERIC)
    incident=collections.defaultdict(list)
    for f in direct['faces']:
        keep=np.linalg.norm(np.mean([direct['xy'][v] for v in f],axis=0)-center)<cutoff
        for v in f:incident[v].append(bool(keep))
    core={v for v,b in incident.items() if b and all(b)}
    C=assemble_complex(core,source.GAMMA_GENERIC,ngrid)
    a=reference[ngrid]
    assert (len(C.labels),len(C.edges),len(C.faces))==(a['n_vertices'],a['n_edges'],a['n_faces'])
    assert sha_labels(C.labels)==a['source_vertices_sha256']
    assert sha_face_labels(C.faces)==a['direct_accepted_faces_sha256']
    r=face_pair_graph(C)
    h=verify_phason_height_inversion(C,source.GAMMA_GENERIC)
    assert r['chromatic_number_exactly_three']
    return {'Ngrid':ngrid,'selection':'independent full-window incident-star core, not original finite source selection',
        'source_reference_SHA_match':True,'face_graph':r,'phason_inversion':h}


def main():
    p=argparse.ArgumentParser();p.add_argument('--source-file',type=Path,required=True)
    p.add_argument('--reference',type=Path,required=True)
    p.add_argument('--ngrids',nargs='+',type=int,default=[7,20,25]);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();s=validate_source(a.source_file);data={x['Ngrid']:x for x in json.loads(a.reference.read_text())['results']}
    rows=[]
    for n in a.ngrids:
        r=one_completed(s,n,data);rows.append(r);print('completed N',n,'faces',r['face_graph']['faces'],'odd',r['face_graph']['odd_cycle_length'],flush=True)
    a.output.write_text(json.dumps({'scope':'separate source full-window corrected-core controls only','results':rows,'physical_mass_gap_proved':False},indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
