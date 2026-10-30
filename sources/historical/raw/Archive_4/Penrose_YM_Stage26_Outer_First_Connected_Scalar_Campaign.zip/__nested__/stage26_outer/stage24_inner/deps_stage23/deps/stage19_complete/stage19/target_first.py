#!/usr/bin/env python3
"""Target-first geometry-dependent rooted scalar-loop pilot. Not an admitted physical operator."""
import argparse, hashlib, json, time
from pathlib import Path
import numpy as np
from stage19_full import setup_geometry, neighbors, boundary
from stage19_symmetry import score
from matched_basis import weighted_observe

SIZES=(2,3,4,5,6,7,8,10,12,15)

def grow(adj, root, n, variant):
    cluster={int(root)}; frontier=set(adj[int(root)])
    while len(cluster)<n and frontier:
        p=min(frontier,key=lambda x:(score(int(root),variant,int(x)),int(x)))
        frontier.remove(p)
        if p not in cluster:
            cluster.add(p);frontier.update(set(adj[p])-cluster)
    return tuple(sorted(cluster)) if len(cluster)==n else None

def rooted_candidates(sp, roots, sizes=SIZES, variants=3):
    adj=neighbors(sp);vec=np.asarray(sp['edge_vectors']);areas=np.asarray(sp['face_areas']);rows=[]
    for root in roots:
        seen=set()
        for n in sizes:
            for variant in range(variants):
                faces=grow(adj,int(root),int(n),variant)
                if faces is None or faces in seen:continue
                path=boundary(sp,faces)
                if path is None:continue
                seen.add(faces)
                indices=np.array([e for e,s in path],dtype=int)
                vv=vec[indices];ll=np.linalg.norm(vv,axis=1);angle=np.arctan2(vv[:,1],vv[:,0]);per=ll.sum();area=areas[list(faces)].sum()
                # Rotation/reflection invariant edge-angle multipole magnitudes.
                h2=np.abs(np.sum(ll*np.exp(2j*angle))/per)
                h4=np.abs(np.sum(ll*np.exp(4j*angle))/per)
                rows.append((int(root),int(n),int(variant),float(area),float(per),float(4*np.pi*area/per**2),float(h2),float(h4),path))
    return rows

def features(rows):
    return np.array([[np.log(r[3]),np.log(r[4]),r[5]] for r in rows],float)

def choose_target(first,second):
    from scipy.spatial import cKDTree
    fa,fb=features(first),features(second)
    scale=np.maximum(np.std(np.vstack((fa,fb)),axis=0),[.08,.08,.04])
    # Balanced, geometry-only targets. Bidirectional closest pairs, then sorted by mismatch;
    # each target has one feasible observed loop on each regulator.
    ia=cKDTree(fa/scale);ib=cKDTree(fb/scale)
    d1,j1=ib.query(fa/scale);d2,j2=ia.query(fb/scale)
    pairs={(i,int(j)):float(d) for i,(j,d) in enumerate(zip(j1,d1))}
    for j,(i,d) in enumerate(zip(j2,d2)):
        pairs[(int(i),j)]=min(pairs.get((int(i),j),float('inf')),float(d))
    ranked=sorted([(d,i,j) for (i,j),d in pairs.items()])
    return ranked,scale

def match(first,second,per_geometry=24,maximum_distance=1.5):
    """Predeclared physical targets; selection uses geometry only, never gauge values.

    Each target requests area, perimeter, compactness. Retains only a feasible
    jointly close pair and uses distinct roots. Targets are defined *before*
    the square/Penrose candidate catalogues are inspected.
    """
    from scipy.spatial import cKDTree
    scale=np.array([.25,.25,.12],float)
    # Prespecified physical area/perimeter targets (coordinate units of Stage 7).
    targets=[]
    for area in (1.0,1.4,1.9,2.5,3.2,4.0):
        for perimeter in (4.5,5.5,6.5,8.,9.5,11.5,14.):
            compact=4*np.pi*area/perimeter**2
            if .20<=compact<=.85:
                targets.append((np.log(area),np.log(perimeter),compact))
    aa=features(first);bb=features(second)
    ta=cKDTree(aa/scale);tb=cKDTree(bb/scale)
    candidates=[]
    for k,target in enumerate(targets):
        target=np.asarray(target)/scale
        da,ia=ta.query(target,k=min(12,len(first)))
        db,ib=tb.query(target,k=min(12,len(second)))
        for i,d1 in zip(np.atleast_1d(ia),np.atleast_1d(da)):
            for j,d2 in zip(np.atleast_1d(ib),np.atleast_1d(db)):
                disparity=np.linalg.norm((aa[i]-bb[j])/scale)
                if disparity<=maximum_distance:
                    candidates.append((float(max(d1,d2)+disparity),int(k),int(i),int(j),float(disparity)))
    chosen=[];ra=set();rb=set();tt=set()
    for _,k,i,j,d in sorted(candidates):
        if k in tt or first[i][0] in ra or second[j][0] in rb:continue
        chosen.append((i,j,d));ra.add(first[i][0]);rb.add(second[j][0]);tt.add(k)
        if len(chosen)==per_geometry:break
    return chosen,scale,len(targets)

def pack(rows,select):
    vals=[rows[i] for i in select];long=max(len(x[8]) for x in vals)
    idx=np.full((len(vals),long),-1,np.int32);sg=np.zeros_like(idx,dtype=np.int8)
    for k,r in enumerate(vals):
        for l,(e,s) in enumerate(r[8]):idx[k,l]=e;sg[k,l]=s
    return {'idx':idx,'sign':sg,'length':np.array([len(r[8]) for r in vals],np.int64),
       'area':np.array([r[3] for r in vals]),'perimeter':np.array([r[4] for r in vals]),
       'faces':np.array([r[1] for r in vals]),'anchor':np.array([r[0] for r in vals]),
       'features':features(vals)}

def run(out,seed=101,nroots=128,nmatch=24,variants=3,measure=True):
    out=Path(out);out.mkdir(exist_ok=True,parents=True);t=time.perf_counter();data={}
    for kind in ('square','penrose'):
        sp,_=setup_geometry(kind,20,3.5)
        roots=np.unique(np.linspace(0,int(sp['F'])-1,nroots,dtype=np.int64))
        rows=rooted_candidates(sp,roots,variants=variants)
        data[kind]={'sp':sp,'rows':rows,'roots':roots}
    pairs,scale,target_count=match(data['square']['rows'],data['penrose']['rows'],nmatch)
    if not pairs:raise ValueError('No matched targets found')
    report={'requested_root_sample':nroots,'requested_targets':nmatch,'actual_targets':len(pairs),'predeclared_physical_targets':target_count,'features':['log(area)','log(perimeter)','compactness'],
      'feature_scales':scale.tolist(),'geometry_only':True,'full_volume_control_preserved':True,
      'pilot_subset_not_zero_momentum_projector':True,'construction_seconds':time.perf_counter()-t,
      'limitations':['Finite root subset: production requires a full-anchor target-constrained construction',
       'Rotation/reflection invariant descriptors, not explicit full point-group orbit averaging',
       'Matched descriptors do not prove equivalent lattice regulators or continuum operators',
       'Single snapshot cannot establish connected temporal overlap or mass']}
    sq=data['square']['rows'];pe=data['penrose']['rows']
    report['pairs']=[{'square_anchor':sq[i][0],'penrose_anchor':pe[j][0], 'square_faces':sq[i][1],'penrose_faces':pe[j][1],
        'distance':float(d),'square_area':sq[i][3],'penrose_area':pe[j][3],
        'square_perimeter':sq[i][4],'penrose_perimeter':pe[j][4]} for i,j,d in pairs]
    for kind,indices in (('square',[i for i,j,d in pairs]),('penrose',[j for i,j,d in pairs])):
        sp=data[kind]['sp'];packed=pack(data[kind]['rows'],indices)
        # Unchanged deterministic full-volume family control from existing engineering package.
        from stage19_full import full_catalogue
        full=full_catalogue(sp,sizes=(3,5,8))
        report[kind]={'graph_hash':sp['graph_hash'],'candidates':len(data[kind]['rows']),
            'root_sample_count':len(data[kind]['roots']),'matched_distinct_roots':len(np.unique(packed['anchor'])),
            'selected_face_counts':{str(int(x)):int(np.sum(packed['faces']==x)) for x in np.unique(packed['faces'])},
            'full_control_counts':[int(np.sum(full['kind']==i)) for i in range(3)],
            'full_control_complete':all(np.sum(full['kind']==i)==sp['F'] for i in range(3))}
        if measure:
            fn=Path('/mnt/data')/f'{kind}_nt20_seed{seed}.npz'
            with np.load(fn,allow_pickle=False) as f:
                import json as _json
                s=_json.loads(str(f['settings_json'].item()))
                if s['spatial_geometry_hash']!=sp['graph_hash']:raise ValueError('geometry mismatch')
                links=f['links']
            # Binary weights target-only, family 0; control measurement separate, full coverage.
            obs=weighted_observe(links,20,int(sp['E']),packed['idx'].astype(np.int64),packed['sign'].astype(np.int64),packed['length'],
                                 np.ones(len(indices))/len(indices),np.zeros(len(indices),dtype=np.int64),1)
            control=weighted_observe(links,20,int(sp['E']),full['idx'].astype(np.int64),full['sign'].astype(np.int64),full['length'],
                                    np.ones(len(full['length']))/len(full['length']),full['kind'],3)
            np.savez_compressed(out/f'{kind}_seed{seed}_pilot.npz',matched=obs,full_volume_control=control,**packed)
            report[kind]['matched_timeslice_mean']=float(obs.mean())
            report[kind]['full_volume_control_timeslice_means']=control.mean(axis=0).tolist()
    (out/'TARGET_FIRST_REPORT.json').write_text(json.dumps(report,indent=2,allow_nan=False))
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='results');p.add_argument('--seed',type=int,default=101);p.add_argument('--roots',type=int,default=128);p.add_argument('--targets',type=int,default=24);p.add_argument('--variants',type=int,default=3);p.add_argument('--no-measure',action='store_true')
    a=p.parse_args();r=run(a.output,a.seed,a.roots,a.targets,a.variants,not a.no_measure)
    print(json.dumps({k:r[k] for k in ['actual_targets','construction_seconds','square','penrose']},indent=2))
