#!/usr/bin/env python3
"""PF-I11 control: full accepted-window incident-star core, NOT source-retained vertices.

The original de Bruijn truncated source population remains unchanged. This
independently compares a fully window-collared central core and its gauge
2-complex; physical meaning/time/reflection are NOT inferred from this test.
"""
from pathlib import Path
import argparse,json
import numpy as np
from collections import defaultdict
from verify_pf_i11_intrinsic_su2 import validate_source,assemble_complex,case_summary
try:
    from verify_pf_i9_source_cut_project_bridge import build_direct
except ImportError:
    from verify_source_cut_project_bridge import build_direct


def one_corrected(source,ngrid,collar=4):
    tiling=source.build_penrose_tiling(ngrid)
    center=np.asarray(tiling['vertices']).mean(axis=0)
    centers=np.asarray([np.mean(t['positions'],axis=0) for t in tiling['tiles']])
    cutoff=.35*float(np.max(np.linalg.norm(centers-center,axis=1)))
    # This independent direct geometry uses four 5-cube-slice windows and
    # accepted 2-coordinate face triangles. Does NOT enumerate grid crossings.
    d=build_direct(cutoff+collar,source.GAMMA_GENERIC)
    incident=defaultdict(list)
    for f in d['faces']:
        xy=np.array([d['xy'][v] for v in f])
        accepted=bool(np.linalg.norm(xy.mean(axis=0)-center)<cutoff)
        for a in f:incident[a].append(accepted)
    core={a for a,ok in incident.items() if ok and all(ok)}
    C=assemble_complex(core,source.GAMMA_GENERIC,source_Ngrid=ngrid)
    raw_faces={frozenset(f) for f in d['faces'] if all(v in core for v in f)}
    assert raw_faces=={frozenset(f) for f in C.faces}
    summary=case_summary(C,flat=False)
    summary['source_retained_vertices']=len(source.select_interior_vertices(tiling,.35))
    summary['direct_full_window_core']=True
    summary['source_population_unchanged']=True
    summary['center_cutoff_radius']=cutoff
    summary['explicit_window_collar_radius']=cutoff+collar
    summary['direct_initial_window_vertices']=len(d['labels'])
    return summary


def main():
    p=argparse.ArgumentParser();p.add_argument('--source-script',type=Path,required=True)
    p.add_argument('--ngrids',nargs='+',type=int,default=[7,10,12,15,18,20,23,25])
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();s=validate_source(a.source_script)
    rows=[]
    for n in a.ngrids:
        q=one_corrected(s,n);rows.append(q)
        print(json.dumps({k:q[k] for k in ['Ngrid','n_vertices','n_edges','n_faces','full_components','free_group_rank_if_complete','all_faces_collapse','source_retained_vertices']}),flush=True)
    a.output.write_text(json.dumps({'scope':'Independent FULL acceptance-window core at same physical center/cut, not original source-retained population','results':rows,'continuum_gap_proved':False},indent=2,sort_keys=True)+'\n')

if __name__=='__main__':main()
