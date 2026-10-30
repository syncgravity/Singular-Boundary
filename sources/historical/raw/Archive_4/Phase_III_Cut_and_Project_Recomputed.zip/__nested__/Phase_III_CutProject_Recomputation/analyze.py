import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json, math, argparse
from pathlib import Path
from collections import defaultdict
import numpy as np
import arviz as az
base=Path(__file__).parent
parser=argparse.ArgumentParser();parser.add_argument('--chains-dir',default=str(base/'chains_dense'));parser.add_argument('--output',default=str(base/'diagnostics.json'));args=parser.parse_args()
files=sorted(Path(args.chains_dir).glob('*.json'))
settings=defaultdict(list)
for file in files:
    c=json.loads(file.read_text()); p=c['setup']
    settings[(p['radius'],p['beta'],p['offset'])].append(c)
rows=[]
for key, chains in sorted(settings.items()):
    chains.sort(key=lambda z:z['setup']['chain'])
    n=min(len(c['measurements']) for c in chains)
    row={'radius':key[0], 'beta':key[1], 'offset':key[2], 'graph':chains[0]['geometry'],
         'chains':len(chains),'draws_per_chain':n, 'raw_draws':len(chains)*n,
         'all_chains_completed': all(z['sweeps']==z['setup']['burn']+z['setup']['thin']*z['setup']['target'] for z in chains),
         'mean_proposal_acceptance': float(np.mean([c['accept_sum']/c['sweeps'] for c in chains]))}
    for var in ('plaquette','lambda0','lambda2','gap'):
        z=np.array([[d[var] for d in c['measurements'][:n]] for c in chains],dtype=float)
        row[var]={'mean':float(z.mean()), 'sd':float(z.std(ddof=1)),
                  'ess_bulk':float(az.ess(z,method='bulk')),
                  'ess_tail':float(az.ess(z,method='tail',prob=(0.05,0.95))),
                  'rhat_rank':float(az.rhat(z,method='rank')),
                  'mcse_mean':float(az.mcse(z,method='mean')),
                  'mcse_over_sd':float(az.mcse(z,method='mean')/z.std(ddof=1))}
    row['diagnostics_gate']=all(row[v]['ess_bulk']>=400 and row[v]['ess_tail']>=400 and row[v]['rhat_rank']<1.01
         for v in ('plaquette','lambda0'))
    rows.append(row)
output={'protocol':{'geometry':'independent Z5 window membership and basis-step faces','beta_values':[1,2],
 'offset':0,'burn_sweeps':100,'thin_sweeps':3,'raw_draws_per_setting':800,
 'target_ess_bulk':400,'target_ess_tail':400,'target_rank_rhat':'< 1.01',
 'warning':'Rhat/ESS do not prove stationarity or isolate quasiperiodic causation; one offset is insufficient for offset robustness.'},
 'settings':rows,'total_checkpoint_files':len(files),'total_retained_draws':sum(r['raw_draws'] for r in rows)}
Path(args.output).write_text(json.dumps(output,indent=2))
for r in rows:
    print('R',r['radius'],'beta',r['beta'],'raw',r['raw_draws'],'accepted',r['mean_proposal_acceptance'],'gate',r['diagnostics_gate'])
    for v in ('plaquette','lambda0','gap'):
        q=r[v]
        print(' ',v,'mean',round(q['mean'],7),'mcse',round(q['mcse_mean'],7),'rhat',round(q['rhat_rank'],5),'essBulk',round(q['ess_bulk'],1),'essTail',round(q['ess_tail'],1))
