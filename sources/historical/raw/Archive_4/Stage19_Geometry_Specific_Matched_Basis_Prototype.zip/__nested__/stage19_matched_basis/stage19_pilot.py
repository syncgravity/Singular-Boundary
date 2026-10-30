#!/usr/bin/env python3
"""Stage19 read-only extended face-cluster scalar pilot. No mass claims."""
import sys,json,hashlib,argparse,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
DEPS=HERE/'vendor'
sys.path[:0]=[str(DEPS),str(DEPS/'ym_stage13/deps/ym_stage7'),str(DEPS/'ym_stage13/deps/ym_stage6/source_stage5')]
from stage7_checkpointed import setup_geometry
from stage4_smearing_flux import measure_scalar_groups,trace_spatial_path

def boundary(sp, face_list):
    ed={}
    for f in face_list:
        for e,s in zip(sp['face_idx'][f],sp['face_sign'][f]):
            e=int(e);s=int(s)
            if e in ed:
                if ed[e]!=-s:return None
                del ed[e]
            else: ed[e]=s
    arcs={}
    for e,s in ed.items():
        a,b=map(int,sp['edges'][e]);a,b=(a,b) if s==1 else (b,a)
        if a in arcs:return None
        arcs[a]=(b,e,s)
    if not arcs:return None
    a=next(iter(arcs));start=a;path=[]
    while a in arcs:
        b,e,s=arcs.pop(a);path.append((e,s));a=b
        if a==start:break
    if a!=start or arcs or len(set(e for e,s in path))!=len(path):return None
    return path

def catalogue(sp,sizes=(3,5,8),per_size=96,seed=19):
    nf=int(sp['F']);inc={}
    for f in range(nf):
        for e in sp['face_idx'][f]:inc.setdefault(int(e),[]).append(f)
    adj=[set() for _ in range(nf)]
    for fs in inc.values():
        if len(fs)==2:a,b=fs;adj[a].add(b);adj[b].add(a)
    rng=np.random.default_rng(seed)
    groups=[];areas=[];kinds=[];faces_used=[]
    for typ,nfaces in enumerate(sizes):
        count=0
        # Random face seeds, face-growth deterministic given RNG; avoid repeated clusters.
        seen=set()
        for origin in rng.permutation(nf):
            if count>=per_size:break
            cluster={int(origin)};front=set(adj[int(origin)])
            while len(cluster)<nfaces and front:
                nxt=int(rng.choice(sorted(front)));front.remove(nxt)
                if nxt in cluster:continue
                cluster.add(nxt);front.update(adj[nxt]-cluster)
            if len(cluster)!=nfaces:continue
            key=tuple(sorted(cluster))
            if key in seen:continue
            path=boundary(sp,key)
            if path is None:continue
            seen.add(key);groups.append(path);kinds.append(typ);faces_used.append(key)
            areas.append(float(np.sum(sp['face_areas'][list(key)])))
            count+=1
        if count<per_size:raise ValueError(f'Only {count}/{per_size} loops for type {nfaces}')
    ll=np.array([len(x) for x in groups],np.int64);maxlen=int(ll.max())
    ids=np.full((len(ll),maxlen),-1,np.int64);sg=np.zeros_like(ids)
    for j,p in enumerate(groups):
        for k,(e,s) in enumerate(p):ids[j,k]=e;sg[j,k]=s
    return {'idx':ids,'sign':sg,'length':ll,'kind':np.array(kinds,np.int64),
            'areas':np.array(areas),'face_ids':faces_used,'sizes':list(sizes)}

def measurement(links,sp,cat,nt=20):
    E=int(sp['E']);idx=cat['idx'];sg=cat['sign'];ll=cat['length'];kind=cat['kind']
    # One operator for each geometric size; equal weight per sampled cluster.
    return measure_scalar_groups(links,nt,E,idx,sg,ll,kind,nkind=len(cat['sizes']))

def gauge_test(links,sp,cat,nt=20,seed=119):
    from wilson_torus import mul
    # Test gauge covariance on one full time slice without ever changing the supplied field.
    rng=np.random.default_rng(seed); E=int(sp['E']); V=int(sp['V']); t=3
    gt=rng.normal(size=(V,4));gt/=np.linalg.norm(gt,axis=1)[:,None]
    trial=links.copy();edges=np.asarray(sp['edges'])
    for e,(u,v) in enumerate(edges):
        x=mul(gt[u],links[t*E+e]);y=gt[v].copy();y[1:]*=-1
        trial[t*E+e]=mul(x,y)
    sample=np.arange(0,len(cat['length']),max(1,len(cat['length'])//12))
    worst=0.
    for j in sample:
        x=trace_spatial_path(links,nt,E,t,cat['idx'][j],cat['sign'][j],cat['length'][j]);
        y=trace_spatial_path(trial,nt,E,t,cat['idx'][j],cat['sign'][j],cat['length'][j]);
        worst=max(worst,abs(x-y))
    return worst

def run(kind,seed,inputs,out):
    g,lat=setup_geometry(kind,20,3.5)
    src=Path(inputs)/f'{kind}_nt20_seed{seed}.npz'
    with np.load(src,allow_pickle=False) as z:
        links=z['links'];settings=json.loads(str(z['settings_json'].item()));sw=int(z['sweeps'])
        assert settings['spatial_geometry_hash']==g['graph_hash'] and sw>=10000
    cat=catalogue(g);obs=measurement(links,g,cat);err=gauge_test(links,g,cat)
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(out/f'{kind}_seed{seed}_stage19_pilot.npz',obs=obs,
         lengths=cat['length'],areas=cat['areas'],kinds=cat['kind'],sizes=np.array(cat['sizes']))
    rep={'geometry':kind,'seed':seed,'checkpoint_sweeps':sw,'counts':{str(s):int(np.sum(cat['kind']==i)) for i,s in enumerate(cat['sizes'])},
         'path_lengths':{str(s):[int(np.min(cat['length'][cat['kind']==i])),int(np.max(cat['length'][cat['kind']==i]))] for i,s in enumerate(cat['sizes'])},
         'max_trace_gauge_error':err,'obs_shape':list(obs.shape),'admit_scalar_mass':False,
         'input_name':src.name,'geometry_hash':g['graph_hash']}
    (out/f'{kind}_seed{seed}_validation.json').write_text(json.dumps(rep,indent=2))
    print(json.dumps(rep,indent=2));return rep

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--inputs',default='/mnt/data');p.add_argument('--output',default='stage19_outputs');p.add_argument('--kind',choices=['square','penrose'],required=True);p.add_argument('--seed',type=int,default=101)
 a=p.parse_args();run(a.kind,a.seed,a.inputs,a.output)
