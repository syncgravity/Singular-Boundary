"""Bounded-size, gauge-invariant measurement plans for large Stage 7 torus.

Spatial path anchors are *subsampled* (not all 22k sources) to avoid O(V^2)
shortest-path construction; true physical separations include torus seams.
This does not change gauge ensemble or action. Scalar and torelon channels are
physical observables but only yield masses given a converged, fitted ensemble.
"""
from __future__ import annotations
import time,json
from collections import deque,defaultdict
import numpy as np
from stage4_smearing_flux import (staple_structure,ape_spatial,measure_scalar_groups,
 measure_winding,winding_paths,square_scalar_basis)
from corrected_2p1_pilot import face_cluster_loops,measure_wilson_paths

def sparse_paths(sp,max_steps=5,n_anchors=80,per_length=20):
    adj=[[] for _ in range(sp['V'])]
    dv=np.asarray(sp['edge_vectors'],float)
    for e,(u,v) in enumerate(sp['edges']):
        adj[int(u)].append((int(v),e,1));adj[int(v)].append((int(u),e,-1))
    anchors=np.unique(np.linspace(0,sp['V']-1,min(n_anchors,sp['V']),dtype=np.int64))
    by_length=defaultdict(list)
    minlen=float(np.min(np.linalg.norm(dv,axis=1)))
    for origin in anchors:
        q=deque([int(origin)]);visited={int(origin):([],np.zeros(2,float))}
        while q:
            v=q.popleft();seq,disp=visited[v]
            if len(seq)>=max_steps:continue
            for w,e,sg in adj[v]:
                if w in visited:continue
                step=seq+[(e,sg)];d=disp+sg*dv[e]
                visited[w]=(step,d);q.append(w)
                n=len(step);r=float(np.linalg.norm(d))
                if w!=origin and r>=.55*n*minlen:
                    by_length[n].append((r,int(origin),int(w),step,d.copy()))
    out=[]
    for n in range(1,max_steps+1):
        candidates=sorted(by_length[n],key=lambda x:(x[0],x[1],x[2]))
        if not candidates:continue
        # Subsample over ordered distances and locations. Many distinct torus
        # source paths occur even though the lattice has a small set of edge sizes.
        ix=np.unique(np.rint(np.linspace(0,len(candidates)-1,min(per_length,len(candidates)))).astype(int))
        out.extend((n,candidates[k]) for k in ix)
    ids=np.full((len(out),max_steps),-1,np.int64);sg=np.zeros_like(ids)
    lens=np.zeros(len(out),np.int64);u=np.zeros(len(out),np.int64);v=np.zeros(len(out),np.int64);meta=[]
    for i,(n,(r,src,dst,seq,d)) in enumerate(out):
        ids[i,:n]=[e for e,s in seq];sg[i,:n]=[s for e,s in seq]
        lens[i]=n;u[i]=src;v[i]=dst
        meta.append({'edges':n,'physical_r':r,'origin':src,'destination':dst,'physical_displacement':d.tolist()})
    return {'idx':ids,'sign':sg,'length':lens,'u':u,'v':v,'meta':meta}

def build_measurement_plan(sp):
    staple=staple_structure(sp,'inverse_area')
    scalar=square_scalar_basis(sp) if sp['spatial_kind']=='square_torus' else face_cluster_loops(sp)
    flux=winding_paths(sp,nanchors=2,max_steps=230)
    paths=sparse_paths(sp,n_anchors=80,max_steps=5,per_length=20)
    return (staple,scalar,flux,paths)

def measure_configuration(links,nt,sp,plan,levels=(0,2,6)):
    staple,scalar,flux,paths=plan
    E=sp['E'];V=sp['V']
    obs=np.empty((nt,3*len(levels)),float)
    tore=np.empty((nt,2*len(levels)),float)
    rect=np.empty((len(levels),len(paths['length']),nt//2),float)
    for j,l in enumerate(levels):
        v=links if l==0 else ape_spatial(links,nt,E,*staple,.4,l)
        obs[:,3*j:3*j+3]=measure_scalar_groups(v,nt,E,scalar['idx'],scalar['sign'],scalar['length'],scalar['kind'])
        tore[:,2*j:2*j+2]=measure_winding(v,nt,E,flux['idx'],flux['sign'],flux['length'],flux['direction'])
        rect[j,:,:]=measure_wilson_paths(v,nt,E,V,paths['idx'],paths['sign'],paths['length'],paths['u'],paths['v'],nt//2)
    return obs,tore,rect

if __name__=='__main__':
 from stage7_large_torus import pair
 for name,sp in zip(('penrose','square'),pair()):
  t=time.monotonic();plan=build_measurement_plan(sp)
  print(name,'planning seconds',time.monotonic()-t,'operators',len(plan[1]['length']),
        'windings',plan[2]['length'].tolist(),'paths',len(plan[3]['length']),flush=True)
  from pathlib import Path
  with open(Path(__file__).resolve().parent/(name+'_measurement_plan.json'),'w') as f:
   json.dump({'geometry':name,'number_scalar_loops':len(plan[1]['length']),
    'winding_lengths_edges':plan[2]['length'].tolist(),
    'winding_physical_lengths':[z['length'] for z in plan[2]['meta']],
    'number_paths':len(plan[3]['length']),
    'path_lengths_m':sorted({round(z['physical_r'],7) for z in plan[3]['meta']}),
    'note':'plan only; no admitted spectroscopy measurements'},f,indent=2)
