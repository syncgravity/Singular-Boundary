#!/usr/bin/env python3
"""Common-support root-balanced matched scalar loop basis; geometry-only weights.
This is a restricted *descriptor-matched* operator, not equality of physical states.
"""
import json, argparse, hashlib, time
from pathlib import Path
import numpy as np
from numba import njit
from stage19_symmetry import many_shapes, weights, setup_geometry
from stage4_smearing_flux import trace_spatial_path

# Fixed *before inspecting gauge observables*, in physical coordinate units of Stage 7.
AREA = np.array([0,.8,1.2,1.6,2.,2.5,3.2,4.5,8.,np.inf])
COMPACT = np.array([0,.35,.50,.65,.8,1.01,np.inf])
PERIM = np.array([0,3.5,5.,6.5,8.,10.,13.,18.,np.inf])
ANISOTROPY = np.array([0,.35,.7,1.000001])

def descriptors(cat, sp):
    v=np.asarray(sp['edge_vectors']); out=np.empty((len(cat['length']),2))
    for i,n in enumerate(cat['length']):
        d=v[cat['idx'][i,:n]]; ll=np.linalg.norm(d,axis=1); angle=np.arctan2(d[:,1],d[:,0]);
        out[i,0]=abs(np.dot(ll,np.exp(2j*angle)))/ll.sum()
        out[i,1]=abs(np.dot(ll,np.exp(4j*angle)))/ll.sum()
    return out

def labels(cat, sp, detail=False):
    a=descriptors(cat,sp)
    components=[cat['family'],np.searchsorted(AREA,cat['area'],side='right')-1,
        np.searchsorted(COMPACT,cat['compactness'],side='right')-1,
        np.searchsorted(PERIM,cat['perimeter'],side='right')-1]
    if detail: components += [np.searchsorted(ANISOTROPY,a[:,0],side='right')-1,
                              np.searchsorted(ANISOTROPY,a[:,1],side='right')-1]
    return np.column_stack(components).astype('int16'),a

def construct(a,spa,b,spb,detail=False):
    xa,da=labels(a,spa,detail); xb,db=labels(b,spb,detail)
    root_a=weights(a)/len(a['sizes']);root_b=weights(b)/len(b['sizes'])
    ua,inv_a=np.unique(xa,axis=0,return_inverse=True)
    ub,inv_b=np.unique(xb,axis=0,return_inverse=True)
    ka=[tuple(x) for x in ua];kb=[tuple(x) for x in ub]
    wa=np.bincount(inv_a,weights=root_a,minlength=len(ua));wb=np.bincount(inv_b,weights=root_b,minlength=len(ub))
    ma=dict(zip(ka,range(len(ka))));mb=dict(zip(kb,range(len(kb))))
    common=sorted(set(ma)&set(mb)); pa=np.zeros(len(a['length']));pb=np.zeros(len(b['length']))
    # Partial coupling: equal UNNORMALIZED probability in each accepted joint descriptor cell.
    # Conditional normalization on common support then gives exactly equal bin mass.
    support=0.;entries=[]
    for key in common:
        ia,ib=ma[key],mb[key];amount=min(wa[ia],wb[ib]);support+=amount
        pa[inv_a==ia]=root_a[inv_a==ia]*amount/wa[ia]
        pb[inv_b==ib]=root_b[inv_b==ib]*amount/wb[ib]
        entries.append({'bin':list(map(int,key)),'square_original_mass':float(wa[ia]),
          'penrose_original_mass':float(wb[ib]),'coupled_mass':float(amount),
          'square_count':int(np.sum(inv_a==ia)),'penrose_count':int(np.sum(inv_b==ib))})
    if support<=0:raise ValueError('No common shape-descriptor support')
    pa/=support;pb/=support
    # Compare matched bin probabilities at machine precision.
    err=max(abs(pa[inv_a==ma[k]].sum()-pb[inv_b==mb[k]].sum()) for k in common)
    def diagnostics(w,prior,cat):
        counts=[]
        for fam in range(len(cat['sizes'])):counts.append(float(w[cat['family']==fam].sum()))
        accepted=w>0
        return {'retained_prior_mass':float(prior[accepted].sum()),'positive_paths':int(accepted.sum()),
          'effective_path_count':float(1./np.sum(w*w)),'per_family_weight':counts,
          'anchor_coverage':float(len(np.unique(cat['anchor'][accepted]))/cat['F']),
          'max_path_weight':float(w.max())}
    report={'descriptor_configuration':{'area_edges':AREA.tolist()[:-1]+['inf'],
       'compactness_edges':COMPACT.tolist()[:-1]+['inf'],
       'perimeter_edges':PERIM.tolist()[:-1]+['inf'],
       'anisotropy_edges':ANISOTROPY.tolist(),'use_anisotropy':bool(detail)},
       'matched_cells':len(common),'common_support_mass':float(support),
       'max_joint_bin_probability_error':float(err),
       'square':diagnostics(pa,root_a,a),'penrose':diagnostics(pb,root_b,b),
       'bin_weights':entries,
       'interpretation':'Common-support, descriptor-histogram-matched restricted scalar operator. Not a full-volume unbiased scalar projector; not C4/C5 representation equivalence; not renormalized physics matching.'}
    return pa,pb,report

@njit
def weighted_observe(links, nt, E, idx, sign, length, w, family, nfamily):
    out=np.zeros((nt,nfamily),np.float64);norm=np.zeros(nfamily)
    for j in range(len(length)): norm[family[j]]+=w[j]
    for t in range(nt):
        for j in range(len(length)):
            if w[j]>0:out[t,family[j]]+=w[j]*(1.-trace_spatial_path(links,nt,E,t,idx[j],sign[j],length[j]))
    for k in range(nfamily):
        if norm[k]>0:out[:,k]/=norm[k]
    return out

def measure(src, sp,cat,w):
    with np.load(src,allow_pickle=False) as f:
        links=f['links'];settings=json.loads(str(f['settings_json'].item()));sweep=int(f['sweeps'])
    if settings['spatial_geometry_hash']!=sp['graph_hash'] or sweep<10000:raise ValueError('Checkpoint geometry or sweep mismatch')
    return weighted_observe(links,20,int(sp['E']),np.ascontiguousarray(cat['idx'].astype(np.int64)),
       np.ascontiguousarray(cat['sign'].astype(np.int64)),np.ascontiguousarray(cat['length']),
       np.ascontiguousarray(w),np.ascontiguousarray(cat['family']),len(cat['sizes']))

def run(input_dir,output,seed=101,detail=False):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    t=time.perf_counter();sps={};cats={}
    for kind in ('square','penrose'):
        sps[kind],_=setup_geometry(kind,20,3.5)
        cats[kind]=many_shapes(sps[kind],variants=2)
    wa,wb,report=construct(cats['square'],sps['square'],cats['penrose'],sps['penrose'],detail=detail)
    report['catalogue_seconds']=round(time.perf_counter()-t,3)
    for kind,w in [('square',wa),('penrose',wb)]:
        cat=cats[kind];sp=sps[kind]
        fp=Path(input_dir)/f'{kind}_nt20_seed{seed}.npz'
        t=time.perf_counter();obs=measure(fp,sp,cat,w);elapsed=time.perf_counter()-t
        digest=hashlib.sha256(w.tobytes()).hexdigest()
        np.savez_compressed(output/f'{kind}_seed{seed}_matched_observable.npz',
            scalar=obs,weights=w,area=cat['area'],perimeter=cat['perimeter'],compactness=cat['compactness'],
            family=cat['family'],anchor=cat['anchor'],graph_hash=np.array(sp['graph_hash']),
            weight_sha256=np.array(digest))
        report[kind]['measurement_seconds']=round(elapsed,3)
        report[kind]['operator_mean']=obs.mean(axis=0).tolist()
        report[kind]['weight_sha256']=digest
    (output/'MATCHED_BASIS_REPORT.json').write_text(json.dumps(report,indent=2,allow_nan=False))
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--inputs',default='/mnt/data');p.add_argument('--output',default='results');p.add_argument('--seed',type=int,default=101);p.add_argument('--anisotropy-bins',action='store_true')
    a=p.parse_args();r=run(a.inputs,a.output,a.seed,a.anisotropy_bins)
    print(json.dumps({k:r[k] for k in ('matched_cells','common_support_mass','max_joint_bin_probability_error','square','penrose')},indent=2))
