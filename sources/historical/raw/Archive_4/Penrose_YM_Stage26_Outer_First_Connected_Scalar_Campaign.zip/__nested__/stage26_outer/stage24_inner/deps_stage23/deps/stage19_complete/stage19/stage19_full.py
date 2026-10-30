#!/usr/bin/env python3
"""Deterministic anchored face-cluster projection: engineering test, NOT mass fitting."""
import sys,time,json,argparse,hashlib
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
VENDOR=ROOT/'vendor'
sys.path[:0]=[str(VENDOR),str(VENDOR/'ym_stage13/deps/ym_stage7'),str(VENDOR/'ym_stage13/deps/ym_stage6/source_stage5')]
from stage7_checkpointed import setup_geometry
from stage4_smearing_flux import measure_scalar_groups

def neighbors(sp):
    ne=int(sp['F']); owner={};adj=[set() for _ in range(ne)]
    for f,row in enumerate(sp['face_idx']):
        for e in row:
            e=int(e)
            if e in owner:
                g=owner[e];adj[f].add(g);adj[g].add(f)
            else:owner[e]=f
    return [tuple(sorted(x)) for x in adj]

def boundary(sp, faces):
    edges={}
    for f in faces:
        for eid,sign in zip(sp['face_idx'][f],sp['face_sign'][f]):
            eid=int(eid);sign=int(sign)
            if eid in edges:
                if edges[eid]!=-sign:return None
                del edges[eid]
            else:edges[eid]=sign
    outgoing={}
    for eid,sign in edges.items():
        u,v=map(int,sp['edges'][eid]);a,b=(u,v) if sign==1 else (v,u)
        if a in outgoing:return None
        outgoing[a]=(b,eid,sign)
    if not outgoing:return None
    start=min(outgoing);u=start;path=[]
    while u in outgoing:
        v,e,s=outgoing.pop(u);path.append((e,s));u=v
        if u==start:break
    if u!=start or outgoing:return None
    return path

def full_catalogue(sp,sizes=(3,5,8)):
    """Each face contributes exactly one deterministic connected cluster per family.
    Anchor weighting counts face-rooted environments, NOT distinct loop shapes.
    """
    adj=neighbors(sp); F=int(sp['F']);groups=[];kinds=[];areas=[];anchors=[];orient=[];skipped={}
    edge_vec=np.asarray(sp['edge_vectors']);fa=np.asarray(sp['face_areas'])
    for typ,nf in enumerate(sizes):
        lost=0
        for root in range(F):
            cluster={root};queue=[root];q=0
            while len(cluster)<nf and q<len(queue):
                u=queue[q];q+=1
                for v in adj[u]:
                    if v not in cluster:
                        cluster.add(v);queue.append(v)
                        if len(cluster)==nf:break
            if len(cluster)!=nf:
                lost+=1;continue
            path=boundary(sp,sorted(cluster))
            if path is None:
                lost+=1;continue
            vec=np.array([edge_vec[e] for e,s in path]);length=np.linalg.norm(vec,axis=1)
            angle=np.arctan2(vec[:,1],vec[:,0]);z=np.sum(length*np.exp(4j*angle))
            theta=float((np.angle(z)/4)%(np.pi/2)) if abs(z)>1e-10 else float('nan')
            groups.append(path);kinds.append(typ);anchors.append(root)
            areas.append(float(fa[list(cluster)].sum()));orient.append(theta)
        skipped[str(nf)]=lost
    n=len(groups);maxlen=max(map(len,groups));ids=np.full((n,maxlen),-1,np.int32);sg=np.zeros((n,maxlen),np.int8)
    for j,path in enumerate(groups):
        for k,(e,s) in enumerate(path):ids[j,k]=e;sg[j,k]=s
    return {'idx':ids,'sign':sg,'length':np.array([len(p) for p in groups],np.int64),
            'kind':np.array(kinds,np.int64),'area':np.array(areas),'orientation':np.array(orient),
            'anchor':np.array(anchors,np.int64),'sizes':list(sizes),'skipped':skipped}

def weighted_bin_measure(links,sp,cat,mask):
    ii=np.flatnonzero(mask); c=cat
    if len(ii)==0:raise ValueError('empty area/orientation bin')
    return measure_scalar_groups(links,20,int(sp['E']),np.ascontiguousarray(c['idx'][ii].astype(np.int64)),
       np.ascontiguousarray(c['sign'][ii].astype(np.int64)),c['length'][ii],np.zeros(len(ii),np.int64),1)[:,0]

def run(kind,seed,inputs,output,benchmark=(128,1024),full=True):
    t0=time.perf_counter();sp,lat=setup_geometry(kind,20,3.5)
    geomsec=time.perf_counter()-t0;t0=time.perf_counter();cat=full_catalogue(sp)
    catsec=time.perf_counter()-t0
    src=Path(inputs)/f'{kind}_nt20_seed{seed}.npz'
    with np.load(src,allow_pickle=False) as f:
        links=f['links'];sw=int(f['sweeps']);settings=json.loads(str(f['settings_json'].item()))
    if settings['spatial_geometry_hash']!=sp['graph_hash'] or sw<10000:raise ValueError('incompatible checkpoint')
    from stage19_pilot import gauge_test
    subset={k:np.concatenate([np.flatnonzero(cat['kind']==i)[:k] for i in range(3)]) for k in benchmark}
    subset['all']=np.arange(len(cat['kind']))
    times={};obs={}
    for tag,indices in subset.items():
        if tag=='all' and not full:continue
        t0=time.perf_counter()
        obs[str(tag)]=measure_scalar_groups(links,20,int(sp['E']),
             np.ascontiguousarray(cat['idx'][indices].astype(np.int64)),
             np.ascontiguousarray(cat['sign'][indices].astype(np.int64)),cat['length'][indices],cat['kind'][indices],3)
        times[str(tag)]=time.perf_counter()-t0
    # Deterministic area and orientation bins, no misleading cross-geometry area equivalence.
    summary={};area=np.asarray(cat['area']);theta=np.asarray(cat['orientation'])
    for i,nface in enumerate(cat['sizes']):
        sel=cat['kind']==i;x=area[sel]
        summary[str(nface)]={'anchors':int(sel.sum()),'area_range':[float(x.min()),float(x.max())],
                            'area_quantiles':np.quantile(x,[0,.25,.5,.75,1]).tolist(),
                            'orientation_defined_fraction':float(np.mean(np.isfinite(theta[sel]))),
                            'unique_boundaries':None}
    err=gauge_test(links,sp,cat,nt=20)
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(output/f'{kind}_seed{seed}_full_projection.npz',**{'obs_'+k:v for k,v in obs.items()},
                        sizes=np.array(cat['sizes']),area=area,orientation=theta,kind=cat['kind'],anchor=cat['anchor'])
    rep={'geometry':kind,'seed':seed,'sweep':sw,'graph_hash':sp['graph_hash'], 'geometry_seconds':geomsec,
         'catalogue_seconds':catsec,'measurement_seconds':times,'loops':len(area), 'counts':summary,
         'rejected_anchor_counts':cat['skipped'],'max_gauge_error':err,
         'exact_root_coverage':all(int(np.sum(cat['kind']==i))==int(sp['F']) for i in range(3)),
         'caveat':'exact face-root average of deterministic rooted clusters, not full shape/rotation orbit; orientation diagnostic only; NOT glueball mass evidence'}
    (output/f'{kind}_seed{seed}_report.json').write_text(json.dumps(rep,indent=2))
    print(json.dumps(rep,indent=2),flush=True)
    return rep

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--kind',choices=('square','penrose'),required=True);p.add_argument('--seed',type=int,default=101)
 p.add_argument('--inputs',default='/mnt/data');p.add_argument('--output',default='results');p.add_argument('--no-full',action='store_true')
 a=p.parse_args();run(a.kind,a.seed,a.inputs,a.output,full=not a.no_full)
