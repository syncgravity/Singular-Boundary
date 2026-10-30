"""Absolute physical-area and orientation stratified full face-root projection."""
import json,time
from pathlib import Path
import numpy as np
from stage19_full import setup_geometry,full_catalogue
from stage4_smearing_flux import measure_scalar_groups

# Common, geometry-independent area edges in calibrated spatial-length units squared.
AREA_EDGES=np.array([0,1.0,1.4,1.8,2.2,2.6,3.0,np.inf])
ORIENT_EDGES=np.linspace(0,np.pi/2,5)

def groups(cat):
    a=np.asarray(cat['area']);o=np.asarray(cat['orientation']);f=np.asarray(cat['kind'])
    if not np.isfinite(o).all():raise ValueError('undefined boundary orientation')
    ab=np.searchsorted(AREA_EDGES,a,side='right')-1
    ob=np.minimum(np.searchsorted(ORIENT_EDGES,o,side='right')-1,3)
    triples=np.stack([f,ab,ob],axis=1)
    keys,inv=np.unique(triples,axis=0,return_inverse=True)
    counts=np.bincount(inv,minlength=len(keys))
    assert counts.sum()==len(a)
    return inv.astype(np.int64),keys,counts

def measure(links,sp,cat):
    inv,keys,counts=groups(cat)
    vals=measure_scalar_groups(links,20,int(sp['E']),
       np.ascontiguousarray(cat['idx'].astype(np.int64)),
       np.ascontiguousarray(cat['sign'].astype(np.int64)),cat['length'],inv,len(keys))
    # each root has equal weight; global family measurement is count-weighted bin mean
    for f in range(3):
        m=keys[:,0]==f
        weighted=(vals[:,m]*counts[m]).sum(axis=1)/counts[m].sum()
        direct=measure_scalar_groups(links,20,int(sp['E']),
           np.ascontiguousarray(cat['idx'][cat['kind']==f].astype(np.int64)),
           np.ascontiguousarray(cat['sign'][cat['kind']==f].astype(np.int64)),
           cat['length'][cat['kind']==f],np.zeros(int(np.sum(cat['kind']==f)),np.int64),1)[:,0]
        if not np.allclose(weighted,direct,atol=2e-12):raise AssertionError('bin normalization mismatch')
    return vals,keys,counts

def run(kind,seed=101,inputs='/mnt/data',output='results'):
    sp,_=setup_geometry(kind,20,3.5);cat=full_catalogue(sp)
    with np.load(Path(inputs)/f'{kind}_nt20_seed{seed}.npz',allow_pickle=False) as z: links=z['links']
    t=time.perf_counter();vals,keys,counts=measure(links,sp,cat);sec=time.perf_counter()-t
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(out/f'{kind}_seed{seed}_area_orientation.npz',observables=vals,keys=keys,counts=counts,
                        area_edges=AREA_EDGES,orientation_edges=ORIENT_EDGES)
    rep={'geometry':kind,'seed':seed,'occupied_bins':len(keys),'total_roots':int(counts.sum()),'seconds':sec,
         'bin_counts':[{ 'family':int(k[0]),'area_bin':int(k[1]),'orientation_bin':int(k[2]),'count':int(c)} for k,c in zip(keys,counts)],
         'strict_geometry_match_warning':'bin labels are comparable but underlying cluster shapes remain regulator-dependent'}
    (out/f'{kind}_seed{seed}_area_orientation.json').write_text(json.dumps(rep,indent=2));print(kind,len(keys),sec)

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--kind',choices=('square','penrose'),required=True);p.add_argument('--seed',type=int,default=101);p.add_argument('--inputs',default='/mnt/data');p.add_argument('--output',default='results')
 a=p.parse_args();run(a.kind,a.seed,a.inputs,a.output)
