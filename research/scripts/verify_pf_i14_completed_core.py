#!/usr/bin/env python3
"""PF-I14 completed-window controls, NEVER replacing original source crops."""
import argparse, collections,json
from pathlib import Path
import numpy as np
from verify_pf_i11_intrinsic_su2 import validate_source,assemble_complex,sha_labels,sha_face_labels
from verify_pf_i9_source_cut_project_bridge import build_direct
from verify_pf_i14_decorated_hull import finite_covariance


def completed_case(source,ngrid,ref):
    tiling=source.build_penrose_tiling(ngrid)
    center=np.mean(tiling['vertices'],axis=0)
    centers=np.array([np.mean(t['positions'],axis=0) for t in tiling['tiles']])
    radius=.35*float(np.max(np.linalg.norm(centers-center,axis=1)))
    direct=build_direct(radius+4,source.GAMMA_GENERIC)
    incident=collections.defaultdict(list)
    for f in direct['faces']:
        accept=np.linalg.norm(np.mean([direct['xy'][v] for v in f],axis=0)-center)<radius
        for v in f:incident[v].append(bool(accept))
    core={v for v,flags in incident.items() if flags and all(flags)}
    C=assemble_complex(core,source.GAMMA_GENERIC,ngrid)
    r=ref[ngrid]
    assert (len(C.labels),len(C.edges),len(C.faces))==(r['n_vertices'],r['n_edges'],r['n_faces'])
    assert sha_labels(C.labels)==r['source_vertices_sha256']
    assert sha_face_labels(C.faces)==r['direct_accepted_faces_sha256']
    row=finite_covariance(C,source.GAMMA_GENERIC,seed=7744+ngrid)
    row['selection']='complete-window incident-face core; differs from original source selected vertices'
    row['original_source_not_replaced']=True
    row['PF_I11_completed_reference_SHA256_verified']=True
    return row


def main():
    p=argparse.ArgumentParser();p.add_argument('--source-file',type=Path,required=True)
    p.add_argument('--completed-ref',type=Path,required=True)
    p.add_argument('--ngrids',nargs='+',type=int,default=[7,25])
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();mod=validate_source(a.source_file)
    reference={r['Ngrid']:r for r in json.loads(a.completed_ref.read_text())['results']}
    rows={str(n):completed_case(mod,n,reference) for n in a.ngrids}
    result={'scope':'completed-window controls ONLY; source original retained separately',
            'results':rows,'physical_time_or_mass_gap_proved':False}
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:(v['V'],v['E'],v['F']) for k,v in rows.items()}))
if __name__=='__main__':main()
