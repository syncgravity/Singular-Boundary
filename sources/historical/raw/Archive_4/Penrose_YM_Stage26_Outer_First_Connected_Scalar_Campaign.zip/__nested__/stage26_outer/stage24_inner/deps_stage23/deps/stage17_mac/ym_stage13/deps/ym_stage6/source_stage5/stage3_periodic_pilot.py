"""Stage 3: finite toroidal *software* calibration pilot, not a continuum result.

Rational model-set torus is NOT the accepted matched M55 geometry and the
M5 comparator fails the motif gate; statistical outputs cannot be used for
Penrose-specific causal inference or a physical mass-gap claim.
"""
from __future__ import annotations
import argparse, json, hashlib
from collections import defaultdict, deque
from pathlib import Path
import numpy as np
from stage2_rational_torus import build_torus
from stage2_ym_calibration import quadratic_weights, assemble
from corrected_2p1_pilot import (run_chain, face_cluster_loops,
     loop_scalar_obs, measure_wilson_paths, corr_operators)


def square_torus(nx:int,ny:int,area:float):
    if min(nx,ny)<5:raise ValueError('square torus too small for local loops')
    a=(area/(nx*ny))**.5
    vid=lambda i,j: (j%ny)*nx+(i%nx)
    xy=np.array([[i*a,j*a] for j in range(ny) for i in range(nx)])
    edges=[];vectors=[];edge_map={}
    for j in range(ny):
        for i in range(nx):
            for di,dj in ((1,0),(0,1)):
                u,v=vid(i,j),vid(i+di,j+dj)
                key=tuple(sorted((u,v)))
                if key in edge_map:raise AssertionError('duplicate torus link')
                edge_map[key]=len(edges)
                edges.append(key)
                vectors.append(np.array([di*a,dj*a])*(1 if u<v else -1))
    face_idx=[];face_sign=[]
    for j in range(ny):
        for i in range(nx):
            nodes=[vid(i,j),vid(i+1,j),vid(i+1,j+1),vid(i,j+1)]
            ids=[];sg=[]
            for k in range(4):
                u,v=nodes[k],nodes[(k+1)%4]
                ids.append(edge_map[tuple(sorted((u,v)))])
                sg.append(1 if u<v else -1)
            face_idx.append(ids);face_sign.append(sg)
    V,E,F=nx*ny,len(edges),nx*ny
    assert E==2*V and V-E+F==0
    return {'V':V,'E':E,'F':F,'edges':np.array(edges,np.int64),
            'edge_vectors':np.array(vectors,float),'face_idx':np.array(face_idx,np.int64),
            'face_sign':np.array(face_sign,np.int64),'face_areas':np.full(F,a*a),
            'xy':xy,'periods':np.diag([nx*a,ny*a]),'physical_area':area,
            'graph_hash':hashlib.sha256(f'square_torus_{nx}_{ny}_{area:.16g}'.encode()).hexdigest(),
            'stats':{'euler_torus':0,'face_count':F},'spatial_kind':'square_torus','spacing':a}


def periodic_paths(sp,max_steps=3,per_size=12):
    """Shortest nonbacktracking paths, displacement summed from actual wrapped links."""
    V=sp['V']; adj=[[] for _ in range(V)];dv=sp['edge_vectors']
    for eid,(u,v) in enumerate(sp['edges']):
        adj[u].append((int(v),eid,1));adj[v].append((int(u),eid,-1))
    found=defaultdict(list)
    for origin in range(V):
        queue=deque([origin]); shortest={origin:([],np.zeros(2))}
        while queue:
            u=queue.popleft();path,dis=shortest[u]
            if len(path)>=max_steps:continue
            for v,e,s in sorted(adj[u]):
                if v in shortest:continue
                seq=path+[(e,s)]; d=dis+s*dv[e];shortest[v]=(seq,d);queue.append(v)
                if v<=origin:continue
                r=np.linalg.norm(d);n=len(seq)
                # Restrict sharply bent paths; true displacement—not endpoint difference.
                if r>=.52*n*np.min(np.linalg.norm(dv,axis=1)):
                    found[n].append((float(r),origin,v,seq,d.copy()))
    chosen=[]
    for n in range(1,max_steps+1):
        candidates=sorted(found[n],key=lambda a:(a[0],a[1],a[2]))
        if not candidates:continue
        ids=np.unique(np.round(np.linspace(0,len(candidates)-1,min(per_size,len(candidates)))).astype(int))
        chosen.extend((n,*candidates[j]) for j in ids)
    idx=np.full((len(chosen),max_steps),-1,np.int64);sign=np.zeros_like(idx)
    metadata=[]
    for j,(n,r,u,v,seq,d) in enumerate(chosen):
        for k,(eid,s) in enumerate(seq):idx[j,k]=eid;sign[j,k]=s
        metadata.append({'path_id':j,'edges':n,'physical_r':r,'u':u,'v':v,
                         'physical_dx':d.tolist(),'angle':float(np.arctan2(d[1],d[0]))})
    return {'idx':idx,'sign':sign,'length':np.array([x['edges'] for x in metadata],np.int64),
            'u':np.array([x['u'] for x in metadata],np.int64),
            'v':np.array([x['v'] for x in metadata],np.int64),'meta':metadata}


def _basis(sp):
    if sp['spatial_kind']=='square_torus':
        fake=dict(sp);fake['face_areas']=np.where(np.arange(sp['F'])%2==0,1.,2.)
        basis=face_cluster_loops(fake)
        names=['checkerboard_even','checkerboard_odd','adjacent_pair']
    else:
        basis=face_cluster_loops(sp);names=['thin','thick','adjacent_pair']
    return basis,names


def pilot(sp,nt=8,beta=3.5,burn=36,steps=64,thin=4,seeds=(101,211),angle=.95,reference_spacing=None):
    a=(sp['physical_area']/sp['F'])**.5 if reference_spacing is None else float(reference_spacing)
    lat,cal=assemble(sp,nt,beta,a,a)
    paths=periodic_paths(sp)
    basis,names=_basis(sp)
    snapshot={};info={}
    for seed in seeds:
        saved,actions,accept,cache=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],int(seed),burn,steps,thin,angle)
        assert cache<1e-9
        snapshot[str(seed)]=saved
        info[str(seed)]={'n_saved':len(saved),'acceptance':float(accept),
                         'mean_action':float(actions.mean()),'cache_error':float(cache)}
    observations=[]; rectangles=[]
    for arr in snapshot.values():
        obs=[];w=[]
        for links in arr:
            obs.append(loop_scalar_obs(links,nt,sp['E'],basis['idx'],basis['sign'],basis['length'],basis['kind']))
            w.append(measure_wilson_paths(links,nt,sp['E'],sp['V'],paths['idx'],paths['sign'],
                                          paths['length'],paths['u'],paths['v'],min(3,nt//2-1)))
        observations.append(np.array(obs));rectangles.append(np.array(w))
    ob=np.concatenate(observations);wr=np.concatenate(rectangles)
    C=corr_operators(ob)
    ret={'geometry':sp['spatial_kind'],'V':sp['V'],'E':sp['E'],'F':sp['F'],
         'area':float(sp['physical_area']),'graph_hash':sp['graph_hash'],
         'calibration':{'spatial_beta_range':cal['spatial_beta_range'],
                        'temporal_beta_range':cal['temporal_beta_range'],
                        'response_eigenvalues':cal['eig'].tolist()},
         'sampling':{'nt':nt,'beta':beta,'time_spacing':float(a),'reference_spacing':float(a),
                     'burn':burn,'steps':steps,'thin':thin,'seeds':list(seeds),
                     'n_saved':len(ob),'n_chains':len(seeds),'exploratory_only':True},
         'chains':info,'basis':names,'path_count':len(paths['meta']),
         'scalar_C':C.tolist(),'wilson_by_path_size':[],
         'no_mass_or_string_tension_fit':True}
    for n in (1,2,3):
        ii=np.where(paths['length']==n)[0]
        if not len(ii):continue
        ret['wilson_by_path_size'].append({'n_edges':n,
           'r_min':float(min(paths['meta'][i]['physical_r'] for i in ii)),
           'r_max':float(max(paths['meta'][i]['physical_r'] for i in ii)),
           'r_mean':float(np.mean([paths['meta'][i]['physical_r'] for i in ii])),
           'W_by_t':wr[:,ii,:].mean(axis=(0,1)).tolist()})
    return ret,snapshot,{'operators':ob,'wilson':wr},paths


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='outputs');ap.add_argument('--burn',type=int,default=36)
    ap.add_argument('--steps',type=int,default=64);ap.add_argument('--nt',type=int,default=8)
    ap.add_argument('--beta',type=float,default=3.5);ap.add_argument('--four-chains',action='store_true');a=ap.parse_args()
    out=Path(a.out);out.mkdir(exist_ok=True,parents=True)
    pen=build_torus(5);sq=square_torus(13,14,pen['physical_area'])
    a_ref=(pen['physical_area']/pen['F'])**.5
    seeds=(101,211,307,419) if a.four_chains else (101,211)
    for name,sp in [('rational_M5',pen),('square_13x14',sq)]:
        print('RUN',name,'V',sp['V'],'links',a.nt*(sp['V']+sp['E']),flush=True)
        report,configs,measured,paths=pilot(sp,nt=a.nt,beta=a.beta,burn=a.burn,steps=a.steps,
                                            reference_spacing=a_ref,seeds=seeds)
        (out/f'{name}.json').write_text(json.dumps(report,indent=2))
        (out/f'{name}_paths.json').write_text(json.dumps(paths['meta'],indent=2))
        np.savez_compressed(out/f'{name}_measurements.npz',**measured)
        # Save reproducible gauge snapshots as distinct archives.
        np.savez_compressed(out/f'{name}_configs.npz',**{'seed_'+s:x for s,x in configs.items()})
        print('DONE',name,report['sampling']['n_saved'],report['wilson_by_path_size'],flush=True)
if __name__=='__main__':main()
