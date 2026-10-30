#!/usr/bin/env python3
"""Diagnostic only: ensemble paired direct/conditional covariance and cost screening.
Outer configurations, not inner draws, determine sample count. Small ensemble does
not authorize variance or bias claims. Connected scalar estimates subtract a
common vacuum contribution, requiring additional independent ensemble means.
"""
import argparse,json
from pathlib import Path
import numpy as np

def audit(paths):
    groups={}
    for p in paths:
        with np.load(p,allow_pickle=False) as z:
            dep=z['depths'].tolist();d=z['direct'].copy();c=z['conditional'].copy();key=z['keys'].copy();tm=z['inner_seconds'].copy()
        kind=p.stem.split('_')[0]
        x=groups.setdefault(kind,{'records':[], 'depths':dep})
        if x['depths']!=dep:raise ValueError('depths do not agree')
        for k,v,cv,seconds in zip(key,d,c,tm):
            x['records'].append({'outer_key':(p.stem,int(k[0]),int(k[1])), 'direct':v[0], 'conditional':cv,'seconds':seconds})
    result={}
    for kind,g in groups.items():
        rows=g['records'];dd=np.array([r['direct'] for r in rows]);cc=np.array([r['conditional'] for r in rows]);sec=np.array([r['seconds'] for r in rows]);
        # one offset per outer preferred. More offsets require clustered bootstrap by outer id.
        unique={(r['outer_key'][0],r['outer_key'][1]) for r in rows}
        n=len(unique); nd=len(rows)
        if nd!=n:result[kind]={'n_unique_outer':n,'n_records':nd,'status':'multiple offsets: cluster by outer config before variance comparison'};continue
        diag=[]
        for j,k in enumerate(g['depths']):
            a=dd[:,2,3,3];b=cc[:,j,2,3,3] # lag4 and complete auxiliary diagonal
            da=a-b
            diag.append({'depth':k,'direct_mean':float(a.mean()),'conditional_mean':float(b.mean()),
              'paired_difference':float(da.mean()),'paired_difference_se':float(da.std(ddof=1)/np.sqrt(n)) if n>1 else None,
              'direct_variance':float(a.var(ddof=1)) if n>1 else None,
              'conditional_variance':float(b.var(ddof=1)) if n>1 else None,
              'variance_ratio':float(a.var(ddof=1)/b.var(ddof=1)) if n>1 and b.var(ddof=1)>0 else None,
              'inner_seconds_per_outer':float(sec.mean())})
        result[kind]={'n_unique_outer':n,'n_records':nd,'lag4_auxiliary':diag,
             'admissible':False,'reason':'Requires outer equilibration, tau_int, inner burn/depth convergence, and replicated cost-adjusted variances'}
    return result
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('files',nargs='+');a.add_argument('--out',default='STAGE23_SCREEN.json');v=a.parse_args()
    r=audit([Path(x) for x in v.files]);Path(v.out).write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
