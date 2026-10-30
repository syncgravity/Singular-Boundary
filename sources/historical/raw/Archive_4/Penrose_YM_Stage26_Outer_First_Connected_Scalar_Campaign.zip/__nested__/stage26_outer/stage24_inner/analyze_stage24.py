#!/usr/bin/env python3
"""Diagnostic analyses; never promote inner replicates to outer configurations."""
import argparse,json
from pathlib import Path
import numpy as np

def within_field(path):
    with np.load(path,allow_pickle=False) as z:
        con=z['conditional'].copy();one=z['onepoint'].copy();dire=z['direct_product'].copy()
        burns=z['burns'].tolist();depths=z['depths'].tolist();seconds=z['seconds'].copy();sweeps=z['sweeps'].tolist()
    # Expected shape: outer,offset,burn,rep,depth,lag,4,4.
    assert con.ndim==8 and one.shape[:5]==con.shape[:5]
    lag4_aux=con[...,2,3,3]
    stats=[]
    for bi,burn in enumerate(burns):
        for ki,k in enumerate(depths):
            y=lag4_aux[:,:,bi,:,ki]
            stats.append(dict(burn=burn,depth=k,mean=float(y.mean()),within_field_replica_sd=float(y.std(axis=2,ddof=1).mean()),
                mean_seconds_per_replica=float(seconds[:,:,bi,:].mean()),
                paired_difference_to_direct=float((y.mean(axis=2)-dire[:,:,2,3,3]).mean())))
    return dict(source=str(path),n_outer=len(sweeps),sweeps=sweeps,n_inner_replicates=con.shape[3],statistics=stats,
        observation_note='One-point series and unsubtracted products only; no connected physical correlator admitted')

def independent_chain_connected(paths,kind=None):
    """Prototype chain-independent vacuum product. Requires at least two seeds per geometry;
    retains outer means as units and offers no reliable uncertainty without enough chains.
    """
    entries=[]
    for path in paths:
        with np.load(path,allow_pickle=False) as z:
            keys=z['sweeps'].copy();ones=z['onepoint'].copy();prods=z['conditional'].copy();direct=z['direct_timeslice'].copy()
        label=path.stem.split('_');geometry=label[0];seed=int(label[1].replace('seed',''))
        if kind and geometry!=kind:continue
        # pooled over outer,offset,replica for point estimate only. Must cluster by outer in uncertainties.
        entries.append((geometry,seed,ones.mean(axis=(0,1,2,3))[-1],prods.mean(axis=(0,1,2,3))[-1]))
    out={}
    for geo in sorted(set(e[0] for e in entries)):
        rows=[e for e in entries if e[0]==geo]
        seeds=[r[1] for r in rows]
        if len(set(seeds))<2:
            out[geo]={'status':'NOT_ESTIMABLE: independent-chain disconnected subtraction requires >=2 distinct seeds'};continue
        # one-point scalar vacuum: average time slices, per channel
        vacuum=np.array([r[2].mean(axis=0) for r in rows])
        cross=np.mean([np.outer(vacuum[i],vacuum[j]) for i in range(len(rows)) for j in range(len(rows)) if i!=j],axis=0)
        connected=np.mean([r[3] for r in rows],axis=0)-cross[None]
        out[geo]={'seeds':seeds,'cross_chain_connected_lag4_aux':float(connected[2,3,3]),
                  'status':'EXPLORATORY ONLY: no robust bootstrap or thermalization guarantee'}
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('files',nargs='+');p.add_argument('--out',default='STAGE24_DIAGNOSTICS.json');a=p.parse_args()
    paths=[Path(x) for x in a.files];report={'inner': [within_field(p) for p in paths], 'connected':independent_chain_connected(paths),
       'limitations':['Inner replicas are conditional samples, never independent outer configurations',
                      'Outer ensemble and autocorrelation remain to be validated',
                      'Products formed from different conditioned slabs require converged inner chains']}
    Path(a.out).write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
if __name__=='__main__':main()
