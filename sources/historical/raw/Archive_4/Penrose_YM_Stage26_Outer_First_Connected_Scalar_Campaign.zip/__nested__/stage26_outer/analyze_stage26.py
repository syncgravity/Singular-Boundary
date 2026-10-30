#!/usr/bin/env python3
"""Outer-level audit: records are independent statistical units only after autocorrelation assessment.
Connected estimates use cross-chain disconnected vacuum products; no mass fits.
"""
import argparse,json
from pathlib import Path
import numpy as np

def inspect(root):
    out={}
    for kind in ('square','penrose'):
        groups={}
        for seed in (101,211,307,419):
            files=sorted((Path(root)/f'{kind}_seed{seed}').glob('outer_*.npz'))
            data=[]
            for f in files:
                with np.load(f,allow_pickle=False) as z:
                    data.append((int(z['sweep']),int(z['offset']),z['direct_timeslice'].copy(),z['direct_product'].copy(),z['conditional'].copy(),z['conditional_onepoint'].copy(),z['pair_counts'].copy(),float(z['inner_seconds'].sum())))
            if not data:continue
            sweeps=np.array([d[0] for d in data]); offsets=np.array([d[1] for d in data]); k=data[0][4].shape[0]
            if len(set(sweeps))!=len(sweeps):raise ValueError('duplicate sweeps')
            if any(d[4].shape!=(k,9,4,4) or d[5].shape!=(k,20,4) for d in data):raise ValueError('shape mismatch')
            groups[seed]=data
        item={'chains':{str(seed):{'n_outer':len(d),'sweep_start':d[0][0],'sweep_end':d[-1][0], 'offsets':sorted(set(x[1] for x in d)),'inner_seconds':float(sum(x[7] for x in d))} for seed,d in groups.items()},'scientific_gate':'Pending outer autocorrelation, independent chain agreement, covariance/uncertainty and bias tests'}
        if len(groups)>=2:
            means={seed:np.mean([x[2].mean(axis=0) for x in d],axis=0) for seed,d in groups.items()}
            # Unbiased disconnected cross-chain point for the zero-time-translation-averaged scalar mean.
            keys=list(groups)
            vac=np.mean([np.outer(means[i],means[j]) for i in keys for j in keys if i!=j],axis=0)
            # Each recorded cross-slab product averages valid pairs at that offset.
            cond=np.mean([x[4].mean(axis=0) for d in groups.values() for x in d],axis=0)
            dr=np.mean([x[3] for d in groups.values() for x in d],axis=0)
            item['exploratory_point_estimates']={'direct_connected_diagonal':np.diagonal(dr-vac,axis1=-2,axis2=-1).tolist(),'conditional_connected_diagonal':np.diagonal(cond-vac,axis1=-2,axis2=-1).tolist(),'warning':'No uncertainty estimates. Cross-slab pair selection varies with offset; bias from finite inner equilibration unresolved.'}
        out[kind]=item
    return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--results',default='stage26_results');p.add_argument('--out',default='STAGE26_AUDIT.json');a=p.parse_args()
 result=inspect(a.results);Path(a.out).write_text(json.dumps(result,indent=2));print('Saved',a.out)
