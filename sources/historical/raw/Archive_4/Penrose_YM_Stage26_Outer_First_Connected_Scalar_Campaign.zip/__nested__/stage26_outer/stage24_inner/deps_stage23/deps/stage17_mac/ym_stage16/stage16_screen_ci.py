"""Chain-stratified paired bootstrap for Stage 16 EXPLORATORY variance and bias screens."""
import json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent

def bootstrap_rows(data,n=2000,seed=1717):
 rng=np.random.default_rng(seed)
 results=[]
 for batch in data['design']['batch_sizes']:
  for lag in data['design']['lags']:
   rows=[r for r in data['rows'] if r['batch']==batch and r['lag']==lag]
   chains=sorted({r['seed'] for r in rows})
   D=np.array([r['direct'] for r in rows]);M=np.array([r['multihit'] for r in rows]);dist=np.asarray(rows[0]['r'])
   bychain={s:np.array([i for i,r in enumerate(rows) if r['seed']==s]) for s in chains}
   for rr in sorted(set(dist.tolist())):
    use=np.flatnonzero(np.isclose(dist,rr));d=D[:,use].mean(axis=1);m=M[:,use].mean(axis=1)
    boot_diff=[];boot_sd=[];boot_d=[];boot_m=[]
    for _ in range(n):
     # Resample chain identity and then entire per-chain samples (small chain count).
     selected=[]
     for s in rng.choice(chains,size=len(chains),replace=True):
      inds=bychain[s]
      selected.extend(rng.choice(inds,size=len(inds),replace=True).tolist())
     inds=np.array(selected)
     dd=d[inds];mm=m[inds]
     boot_diff.append(np.mean(mm-dd));boot_d.append(np.mean(dd));boot_m.append(np.mean(mm))
     boot_sd.append(dd.std(ddof=1)/mm.std(ddof=1) if mm.std(ddof=1)>0 else np.nan)
    results.append({'batch':batch,'lag':lag,'r':float(rr),'n_paths':int(len(use)),'n_outer':len(rows),
      'observed_direct':float(d.mean()),'observed_multihit':float(m.mean()),
      'paired_difference_CI95':np.quantile(boot_diff,[.025,.975]).tolist(),
      'direct_mean_CI95':np.quantile(boot_d,[.025,.975]).tolist(),
      'multihit_mean_CI95':np.quantile(boot_m,[.025,.975]).tolist(),
      'raw_SD_ratio_CI95':np.nanquantile(boot_sd,[.025,.975]).tolist()})
 return {'exploratory_only':True,'bootstrap_repetitions':n,'n_independent_outer_chains':4,
  'stationarity_certified':False,'outer_burn_certified':False,
  'note':'chain-identity and within-chain bootstrap; small N=4 chains, results illustrative not physical admission',
  'results':results}
if __name__=='__main__':
 o=bootstrap_rows(json.loads((HERE/'BENCHMARK.json').read_text()))
 (HERE/'BOOTSTRAP_SCREEN.json').write_text(json.dumps(o,indent=2))
 for r in o['results']:
  if r['batch']==128 and r['r'] in (1.,2.) and r['lag']==10:print(r)
