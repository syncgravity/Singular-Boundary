"""Stage 8 bounded, genuinely independently seeded, restartable warmup campaign.

This script changes NO Wilson physics relative to Stage 7. The existing --burn
and --thin scheduling are inherited from its checkpointed engine. Absence of
post-burn observables is never interpreted as physics. Segments remain atomic.
"""
import argparse,json,time
from pathlib import Path
from stage7_checkpointed import process

def run(root:Path, seeds, target, increment, burn=1000, thin=10, nt=20, beta=3.5):
    root=Path(root); root.mkdir(parents=True,exist_ok=True)
    rows=[]
    for name in ('square','penrose'):
        for seed in seeds:
            cp=root/f'{name}_nt{nt}_seed{seed}.npz'
            start=time.monotonic()
            result=process(cp,kind=name,seed=seed,nt=nt,beta=beta,
              total_sweeps=target,burn=burn,thin=thin,limit=increment,
              verify=True,measure=True)
            row={'kind':name,'seed':seed,'sweeps':result['completed_sweeps'],
                 'n_postburn_samples':result['n_postburn_samples'],
                 'elapsed_seconds':round(time.monotonic()-start,2),
                 'cache_error':result['cache_error'],
                 'checkpoint_sha256':result['checkpoint_sha256']}
            rows.append(row)
            print('CHECKPOINT',json.dumps(row,sort_keys=True),flush=True)
    (root.parent/'stage8_run_summary.json').write_text(json.dumps(rows,indent=2))
    return rows

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint-root',default='checkpoints')
    ap.add_argument('--seeds',type=int,nargs='+',default=[101,211,307,419])
    ap.add_argument('--target',type=int,default=10000)
    ap.add_argument('--increment',type=int,default=20)
    ap.add_argument('--burn',type=int,default=1000)
    ap.add_argument('--thin',type=int,default=10)
    args=ap.parse_args()
    run(Path(args.checkpoint_root),args.seeds,args.target,args.increment,args.burn,args.thin)
