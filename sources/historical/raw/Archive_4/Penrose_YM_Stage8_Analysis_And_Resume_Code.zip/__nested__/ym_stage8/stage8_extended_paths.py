"""Build long-distance SU(2) Wilson-line path plans (geometry only).

This does not modify Stage 7 checkpoint measurement definitions or claim a
string-tension fit. The pre-registered additional paths can be evaluated from
future production configurations with a separately versioned measurement key.
"""
import json
from pathlib import Path
import numpy as np
from stage7_large_torus import pair
from stage7_measurement import sparse_paths

def certify(sp,paths):
    edges=np.asarray(sp['edges'],dtype=np.int64)
    edgevec=np.asarray(sp['edge_vectors'],dtype=float)
    for i,n in enumerate(paths['length']):
        cur=int(paths['u'][i]); disp=np.zeros(2,float)
        for eid,sign in zip(paths['idx'][i,:n],paths['sign'][i,:n]):
            u,v=edges[eid]
            if sign==1 and cur==u:cur=int(v)
            elif sign==-1 and cur==v:cur=int(u)
            else:raise AssertionError('path is not edge-contiguous')
            disp+=sign*edgevec[eid]
        if cur!=int(paths['v'][i]):raise AssertionError('wrong end vertex')
        if not np.allclose(disp,paths['meta'][i]['physical_displacement'],atol=1e-10):
            raise AssertionError('displacement mismatch')
    return True

def run(root):
    root=Path(root);root.mkdir(exist_ok=True,parents=True)
    result={}
    for name,sp in zip(('penrose','square'),pair()):
        paths=sparse_paths(sp,max_steps=12,n_anchors=48,per_length=24)
        certify(sp,paths)
        fn=root/f'{name}_extra_paths.npz'
        np.savez_compressed(fn,idx=paths['idx'],sign=paths['sign'],length=paths['length'],
                            origin=paths['u'],destination=paths['v'],
                            physical_r=np.array([v['physical_r'] for v in paths['meta']]),
                            physical_dxdy=np.array([v['physical_displacement'] for v in paths['meta']]))
        r=np.array([v['physical_r'] for v in paths['meta']])
        result[name]={'number_paths':int(len(r)),
                       'max_steps':12,'min_r':float(r.min()),'max_r':float(r.max()),
                       'all_paths_contiguous_and_physical_displacements_certified':True,
                       'source_geometry_sha256':sp['graph_hash']}
    (root/'stage8_extra_paths_report.json').write_text(json.dumps(result,indent=2))
    return result
if __name__=='__main__':print(json.dumps(run(Path(__file__).resolve().parent),indent=2))
