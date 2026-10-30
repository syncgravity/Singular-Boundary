"""Stage 16 reproducible physically and orientation matched large-torus path candidates.

Geometry-only; NO new interacting field measurements or nonperturbative matching.
"""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.optimize import linear_sum_assignment
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'ym_stage13/deps/ym_stage7'))
from stage7_large_torus import pair
from stage7_measurement import sparse_paths

def select_matched(square,penrose,rtol=.05,angle_deg=25.):
    sdx=np.array([p['physical_displacement'] for p in square['meta']]);pdx=np.array([p['physical_displacement'] for p in penrose['meta']])
    sr=np.linalg.norm(sdx,axis=1);pr=np.linalg.norm(pdx,axis=1)
    frac=np.abs(sr[:,None]-pr[None,:])/np.maximum(sr[:,None],pr[None,:])
    dot=(sdx@pdx.T)/(sr[:,None]*pr[None,:]);delta=np.rad2deg(np.arccos(np.clip(np.abs(dot),-1,1)))
    valid=(frac<=rtol)&(delta<=angle_deg)
    # Hungarian assignment favors many distinct paths, then close geometry.
    cost=frac/rtol+delta/angle_deg
    cost=np.where(valid,cost,1e5)
    si,pi=linear_sum_assignment(cost)
    pairs=[]
    for i,j in zip(si,pi):
        if not valid[i,j]:continue
        pairs.append({'square_path_index':int(i),'penrose_path_index':int(j),
            'r_square':float(sr[i]),'r_penrose':float(pr[j]),
            'relative_r_difference':float(frac[i,j]),'axis_angle_difference_deg':float(delta[i,j]),
            'square_edge_count':int(square['length'][i]),'penrose_edge_count':int(penrose['length'][j])})
    return {'pairs':pairs,'n_square_candidates':len(sr),'n_penrose_candidates':len(pr),
            'candidate_compatible_pairs':int(valid.sum()),'n_distinct_pairs':len(pairs),
            'matching_rtol':rtol,'matching_angle_deg':angle_deg,
            'source':'deterministic 2D graph path construction; orientation axis modulo pi',
            'admission':'geometry-only screen; no renormalized anisotropy or static potential plateau'}

def write_catalog(outdir=HERE,max_steps=10,n_anchors=180,per_length=100):
    begin=time.perf_counter();P,S=pair()
    q=sparse_paths(S,max_steps=max_steps,n_anchors=n_anchors,per_length=per_length)
    p=sparse_paths(P,max_steps=max_steps,n_anchors=n_anchors,per_length=per_length)
    result=select_matched(q,p)
    result.update({'seconds':time.perf_counter()-begin,'square_hash':S['graph_hash'],
        'penrose_hash':P['graph_hash'],'geometry_tag':'rational M55 and equal-area 151x151 square',
        'n_anchors':n_anchors,'per_length':per_length,'max_steps':max_steps})
    outdir=Path(outdir);outdir.mkdir(exist_ok=True,parents=True)
    (outdir/'MATCHED_PATH_SCREEN.json').write_text(json.dumps(result,indent=2))
    for name,z in (('square',q),('penrose',p)):
        np.savez_compressed(outdir/f'{name}_candidate_paths.npz',**{k:z[k] for k in ['idx','sign','length','u','v']},
            dx=np.asarray([m['physical_displacement'] for m in z['meta']]),
            r=np.asarray([m['physical_r'] for m in z['meta']]))
    return result
if __name__=='__main__':
    r=write_catalog();print(json.dumps({k:v for k,v in r.items() if k!='pairs'},indent=2),flush=True)
