#!/usr/bin/env python3
"""Stage 25 diagnostic on Stage 24-format results. Not a mass measurement.

Comparison across independent inner replicas. The one outer field is the unit
of outer sampling: do NOT interpret the replica t-statistic as gauge-ensemble inference.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np

def inspect(path):
    path=Path(path)
    with np.load(path,allow_pickle=False) as z:
        x=z['conditional'].copy(); o=z['onepoint'].copy(); d=z['direct_product'].copy()
        b=z['burns'].copy(); k=z['depths'].copy(); seconds=z['seconds'].copy(); err=z['cache_error'].copy()
        sweeps=z['sweeps'].copy(); offsets=z['offsets'].copy()
    if x.ndim!=8 or x.shape[-3:]!=(9,4,4):raise ValueError('unexpected conditional array shape')
    if o.shape!=x.shape[:-3]+(20,4):raise ValueError('one-point dimensions differ')
    if not np.isfinite(x).all() or not np.isfinite(o).all():raise ValueError('nonfinite measurements')
    if len(b)<2 or x.shape[3]<4 or len(k)<2:raise ValueError('expected >=2 burns, >=4 replicas, >=2 depths')
    if np.max(err)>1.e-9:raise ValueError('plaquette-cache inconsistency')
    # Report full 9x4 channel product panel; show more interpretable diagonal by default.
    rows=[]
    for ki, depth in enumerate(k):
        for lag in range(9):
            for channel in range(4):
                # pooled outer/offset only for descriptive diagnostic; not independent replicates
                a=x[:,:,0,:,ki,lag,channel,channel].mean(axis=(0,1))
                c=x[:,:,-1,:,ki,lag,channel,channel].mean(axis=(0,1))
                mean_a=float(a.mean());mean_c=float(c.mean());
                sd_a=float(a.std(ddof=1));sd_c=float(c.std(ddof=1));
                # shift/noise ratio is an informal diagnostic, not a hypothesis test or p-value
                denom=float(np.sqrt(sd_a**2/len(a)+sd_c**2/len(c)))
                rows.append(dict(lag=lag+2,channel=channel,depth=int(depth),burn_short=int(b[0]),burn_long=int(b[-1]),
                                 mean_short=mean_a,mean_long=mean_c,abs_burn_shift=abs(mean_a-mean_c),
                                 replica_sd_short=sd_a,replica_sd_long=sd_c,
                                 shift_over_replica_noise=(abs(mean_a-mean_c)/denom if denom else None),
                                 paired_direct=float(d[:,:,lag,channel,channel].mean())))
    # One-point means shifts between burn conditions; time-averaged per replica.
    one_rows=[]
    for ki,depth in enumerate(k):
        for channel in range(4):
            p=o[:,:,0,:,ki,:,channel].mean(axis=(0,1,3))
            q=o[:,:,-1,:,ki,:,channel].mean(axis=(0,1,3))
            one_rows.append(dict(channel=channel,depth=int(depth),short=float(p.mean()),long=float(q.mean()),
                                 abs_burn_shift=float(abs(p.mean()-q.mean())),sd_short=float(p.std(ddof=1)),sd_long=float(q.std(ddof=1))))
    out=dict(filename=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),outer_configs=int(x.shape[0]),
             offsets=offsets.tolist(),burns=b.tolist(),depths=k.tolist(),inner_replicas=int(x.shape[3]),
             sweep_end=int(sweeps[-1]),seconds=float(seconds.sum()),max_cache_error=float(err.max()),
             products=rows,onepoints=one_rows,
             warnings=['Inner replicas are not independent outer fields and cannot establish physical estimator unbiasedness.',
                       'Longer burn-in must be evaluated against replica noise; this is not a guaranteed convergence proof.',
                       'K=12 and K=32 are nested averages from the same inner Markov stream, not independent depths.',
                       'No connected scalar mass or cost-adjusted outer variance can be established with one outer field.'])
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('files',nargs='+');p.add_argument('--out',default='STAGE25_INNER_AUDIT.json');a=p.parse_args()
    r=[inspect(p) for p in a.files]
    Path(a.out).write_text(json.dumps(dict(results=r),indent=2,allow_nan=False))
    for v in r:
        print(v['filename'],'outer',v['outer_configs'],'replicas',v['inner_replicas'],'seconds',round(v['seconds'],1))
        for depth in v['depths']:
            t=[x for x in v['products'] if x['lag']==4 and x['channel']==3 and x['depth']==depth][0]
            print(f'  auxiliary lag 4 K={depth}: burn shift {t["abs_burn_shift"]:.6g}, noise units {t["shift_over_replica_noise"]:.3g}')
    print('Saved',a.out)
if __name__=='__main__':main()
