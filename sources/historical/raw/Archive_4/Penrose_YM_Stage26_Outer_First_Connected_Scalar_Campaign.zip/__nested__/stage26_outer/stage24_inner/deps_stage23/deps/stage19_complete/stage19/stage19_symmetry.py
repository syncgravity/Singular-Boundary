#!/usr/bin/env python3
"""Root-stratified multiple-shape loop construction and geometry-aware matched screens.
An engineering improvement, NOT uniform sampling of the set of all lattice animals.
"""
import argparse, hashlib, json, time
from pathlib import Path
import numpy as np
from stage19_full import setup_geometry, neighbors, boundary
from stage4_smearing_flux import measure_scalar_groups

def score(root, variant, face):
    return ((face * 0x9e3779b185ebca87 + root * 0xc2b2ae3d27d4eb4f + variant * 0x165667b19e3779f9) & ((1<<64)-1))

def many_shapes(sp, sizes=(3,5,8), variants=4):
    adj=neighbors(sp); F=int(sp['F']); vec=np.asarray(sp['edge_vectors']);fa=np.asarray(sp['face_areas'])
    rows=[]; seen=[set() for _ in sizes]; dup=np.zeros((len(sizes),),dtype=int); invalid=np.zeros_like(dup)
    for family,n in enumerate(sizes):
        for root in range(F):
            for variant in range(variants):
                cluster={root};front=set(adj[root])
                while len(cluster)<n and front:
                    pick=min(front,key=lambda i:(score(root,variant,i),i))
                    front.remove(pick)
                    if pick in cluster:continue
                    cluster.add(pick);front.update(set(adj[pick])-cluster)
                if len(cluster)!=n or boundary(sp,sorted(cluster)) is None:
                    invalid[family]+=1
                    # Valid deterministic breadth-first fallback used by the validated Stage 19 pilot.
                    cluster={root}; queue=[root]; q=0
                    while len(cluster)<n and q<len(queue):
                        u=queue[q]; q+=1
                        for v in adj[u]:
                            if v not in cluster:
                                cluster.add(v); queue.append(v)
                                if len(cluster)==n:break
                key=tuple(sorted(cluster));path=boundary(sp,key)
                if path is None:invalid[family]+=1;continue
                if (root,key) in seen[family]:dup[family]+=1;continue
                seen[family].add((root,key))
                area=float(fa[list(cluster)].sum())
                path_ids=np.array([e for e,s in path],dtype=np.int32)
                per=float(np.linalg.norm(vec[path_ids],axis=1).sum())
                # intrinsic rotation/reflection-invariant compactness, 1 for round curves
                compact=4*np.pi*area/per**2
                rows.append((family,root,variant,path,area,per,compact,key))
    m=len(rows); L=max(len(x[3]) for x in rows)
    ids=np.full((m,L),-1,np.int32);sg=np.zeros((m,L),np.int8)
    for i,row in enumerate(rows):
        for j,(e,s) in enumerate(row[3]):ids[i,j]=e;sg[i,j]=s
    return {'idx':ids,'sign':sg,'length':np.array([len(x[3]) for x in rows],np.int64),
            'family':np.array([x[0] for x in rows],np.int64),'anchor':np.array([x[1] for x in rows],np.int64),
            'variant':np.array([x[2] for x in rows],np.int64), 'area':np.array([x[4] for x in rows]),
            'perimeter':np.array([x[5] for x in rows]),'compactness':np.array([x[6] for x in rows]),
            'face_keys':[x[7] for x in rows], 'duplicates':dup.tolist(),'invalid':invalid.tolist(),
            'sizes':list(sizes),'F':F,'variants':variants}

def weights(cat):
    # Within-root cluster deduplication with root-balanced total weight; each root contributes equally
    # within each family regardless of number of distinct valid variants.
    w=np.empty(len(cat['family']),float)
    for family in range(len(cat['sizes'])):
        ix=np.flatnonzero(cat['family']==family)
        count=np.bincount(cat['anchor'][ix],minlength=cat['F'])
        if np.any(count==0):raise ValueError('Missing root in family')
        w[ix]=1.0/(cat['F']*count[cat['anchor'][ix]])
    return w

def strata(a,b):
    # matched bins in absolute physical area and intrinsic compactness (not assumed same shape orbit)
    ab=np.array([0,0.8,1.2,1.6,2.0,2.5,3.2,4.5,8, np.inf]); cb=np.array([0,0.35,0.50,0.65,0.8,1.01,np.inf])
    def labels(x):
        return np.stack([x['family'],np.searchsorted(ab,x['area'],side='right')-1,
              np.searchsorted(cb,x['compactness'],side='right')-1],axis=1)
    x,y=labels(a),labels(b)
    common=set(map(tuple,x)) & set(map(tuple,y))
    maska=np.array([tuple(i) in common for i in x]);maskb=np.array([tuple(i) in common for i in y])
    wa,wb=weights(a),weights(b)
    results=[]
    for key in sorted(common):
        ma=np.all(x==key,axis=1);mb=np.all(y==key,axis=1)
        aw=float(wa[ma].sum());bw=float(wb[mb].sum())
        results.append({'key':list(map(int,key)),'square_count':int(ma.sum()),'penrose_count':int(mb.sum()),
                        'square_root_weight':aw,'penrose_root_weight':bw,'overlap_weight':min(aw,bw)})
    return {'square_covered_root_weight':float(wa[maska].sum()/len(a['sizes'])),
            'penrose_covered_root_weight':float(wb[maskb].sum()/len(b['sizes'])),
            'strata':results, 'area_edges':[None if not np.isfinite(v) else float(v) for v in ab],'compactness_edges':[None if not np.isfinite(v) else float(v) for v in cb],
            'warning':'Matching intrinsic bins does not establish identical loop distributions or renormalized physical scale.'}

def observe(links,sp,cat):
    # Disaggregated by family and raw shape variant; workhorse returns sums/count means per family.
    t=time.perf_counter()
    raw=measure_scalar_groups(links,20,int(sp['E']),np.ascontiguousarray(cat['idx'].astype(np.int64)),
             np.ascontiguousarray(cat['sign'].astype(np.int64)),cat['length'],cat['family'],len(cat['sizes']))
    return raw,time.perf_counter()-t

def run(args):
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True);cats={};links_by={};sp_by={};reports={}
    for kind in ('square','penrose'):
        t=time.perf_counter();sp,_=setup_geometry(kind,20,3.5)
        cat=many_shapes(sp,variants=args.variants);sec=time.perf_counter()-t
        src=Path(args.inputs)/f'{kind}_nt20_seed{args.seed}.npz'
        with np.load(src,allow_pickle=False) as z:
            links=z['links'];settings=json.loads(str(z['settings_json'].item()));sweep=int(z['sweeps'])
        assert settings['spatial_geometry_hash']==sp['graph_hash'] and sweep>=10000
        cats[kind]=cat;links_by[kind]=links;sp_by[kind]=sp
        w=weights(cat);rootcount=np.bincount(cat['anchor'][cat['family']==0],minlength=cat['F'])
        reports[kind]={'sweep':sweep,'graph_hash':sp['graph_hash'],'paths':len(cat['length']),
             'catalogue_seconds':sec,'duplicates':cat['duplicates'],'invalid':cat['invalid'],
             'root_multiplicity_range':[int(rootcount.min()),int(rootcount.max())],
             'root_normalization':[float(w[cat['family']==i].sum()) for i in range(3)],
             'areas':[float(cat['area'].min()),float(cat['area'].max())]}
        if args.measure:
            obs,elapsed=observe(links,sp,cat)
            reports[kind]['measurement_seconds']=elapsed
            np.savez_compressed(out/f'{kind}_seed{args.seed}_measure.npz',obs=obs,
                 area=cat['area'],perimeter=cat['perimeter'],compactness=cat['compactness'],
                 anchor=cat['anchor'],family=cat['family'],variant=cat['variant'],weights=w)
    matched=strata(cats['square'],cats['penrose'])
    result={'geometries':reports,'matching':matched,'variants':args.variants,
            'admit_mass':False,'admit_matched_operator':False,
            'limitations':['finite deterministic hash variants, not uniform all connected cluster shapes',
               'deduping clusters changes shape inclusion probabilities; root normalization only',
               'shape orientation or full symmetry-orbit averages not yet proven',
               'matched area/compactness bins may differ in finer shape distribution',
               'one checkpoint per geometry: no temporal connected correlator or mass overlap test']}
    (out/'STAGE19_SHAPE_MATCH.json').write_text(json.dumps(result,indent=2,allow_nan=False))
    print(json.dumps({'geometries':reports,'common_strata':len(matched['strata']),
          'matching_coverage':[matched['square_covered_root_weight'],matched['penrose_covered_root_weight']]},indent=2))
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--inputs',default='/mnt/data');p.add_argument('--output',default='results');p.add_argument('--seed',type=int,default=101)
    p.add_argument('--variants',type=int,default=4);p.add_argument('--measure',action='store_true');run(p.parse_args())
