#!/usr/bin/env python3
"""Integrate strictly recovered 150 Penrose loops into versioned catalogue; never alter pilot cache."""
import sys,hashlib,json,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE/'stage18'),str(HERE/'stage18'/'stage17_mac'),str(HERE/'stage18'/'stage17_mac'/'ym_stage13'/'deps'/'ym_stage7'),str(HERE/'stage19')]
from stage7_checkpointed import setup_geometry
from stage19_full import neighbors,boundary
from target_first import grow
from full_anchor_targets import TARGETS,SCALE,THRESHOLD
from stage19_mc import pack,save,sha

def build(old,diagnostics,out):
    sp,_=setup_geometry('penrose',20,3.5)
    with np.load(old,allow_pickle=False) as z:cat={k:z[k].copy() for k in z.files}
    with np.load(diagnostics,allow_pickle=False) as z: miss=z['missing_anchor_ids'].copy(); sizes=z['new_search_size'].copy()
    assert int(cat['F'])==22808 and len(cat['roots'])==22658
    assert np.array_equal(miss,np.setdiff1d(np.arange(22808),cat['roots']))
    adj=neighbors(sp);area=np.asarray(sp['face_areas']);v=np.asarray(sp['edge_vectors'])
    targets=np.array([[np.log(a),np.log(p),4*np.pi*a/p**2] for a,p in TARGETS])
    paths=[];roots=[];distance=[];target=[];faces=[]
    for j,r in enumerate(miss):
        r=int(r); hint=int(sizes[j]); best=(float('inf'),None)
        # Recreate the strict recovery search, early accept only after exact descriptor evaluation.
        variants=12 if r==10550 else 8
        nf_list=sorted(set(([hint] if hint>0 else [])+list(range(2,26 if r==10550 else 20))))
        seen=set()
        for nf in nf_list:
            for variant in range(variants):
                fs=grow(adj,r,nf,variant)
                if fs is None or fs in seen:continue
                seen.add(fs);p=boundary(sp,fs)
                if p is None:continue
                ids=np.array([e for e,s in p],dtype=np.int64)
                ar=float(area[list(fs)].sum());per=float(np.linalg.norm(v[ids],axis=1).sum())
                feat=np.array([np.log(ar),np.log(per),4*np.pi*ar/per**2])
                d=np.linalg.norm((targets-feat)/SCALE,axis=1);idx=int(np.argmin(d))
                if float(d[idx])<best[0]:best=(float(d[idx]),(p,idx,nf))
            # A matching loop is enough, but prefer the best among hinted size / scanned sizes.
        if best[0]>THRESHOLD:raise RuntimeError(f'failed strict recovery root {r}: distance {best[0]}')
        p,k,nf=best[1];paths.append(p);roots.append(r);distance.append(best[0]);target.append(k);faces.append(nf)
        if (j+1)%25==0:print('RECOVERED',j+1,'/ 150',flush=True)
    idx,sign,length=pack(paths)
    n=max(cat['idx'].shape[1],idx.shape[1])
    def pad(x,width,fill):return np.pad(x,((0,0),(0,width-x.shape[1])),constant_values=fill)
    perm=np.argsort(np.r_[cat['roots'],roots]);
    cat['idx']=np.vstack([pad(cat['idx'],n,-1),pad(idx,n,-1)])[perm]
    cat['sign']=np.vstack([pad(cat['sign'],n,0),pad(sign,n,0)])[perm]
    for key,ext in [('length',length),('roots',roots),('distance',distance),('target',target),('faces',faces)]:cat[key]=np.r_[cat[key],ext][perm]
    assert np.array_equal(cat['roots'],np.arange(22808))
    assert np.all(cat['distance']<=THRESHOLD) and np.all(cat['length']>0)
    assert all(np.count_nonzero(cat['ckind']==k)==22808 for k in range(3))
    cat['coverage_version']=np.array('stage19_complete_22808_v1')
    save(out,**cat)
    with np.load(out,allow_pickle=False) as z:assert np.array_equal(z['roots'],np.arange(22808))
    report={'accepted':22808,'missing':0,'threshold':THRESHOLD,'original_accepted':22658,'newly_integrated':len(roots),'max_distance':float(np.max(cat['distance'])),'max_new_distance':float(max(distance)),'sha256':sha(out),'graph_hash':str(cat['graph_hash'].item())}
    Path(out).with_suffix('.json').write_text(json.dumps(report,indent=2));print('COMPLETE',json.dumps(report),flush=True)
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--old',default=str(HERE/'penrose_strict_catalogue.npz'));p.add_argument('--diagnostics',default=str(HERE/'missing_anchor_diagnostics.npz'));p.add_argument('--output',default=str(HERE/'penrose_complete_catalogue.npz'))
 a=p.parse_args();build(a.old,a.diagnostics,a.output)
