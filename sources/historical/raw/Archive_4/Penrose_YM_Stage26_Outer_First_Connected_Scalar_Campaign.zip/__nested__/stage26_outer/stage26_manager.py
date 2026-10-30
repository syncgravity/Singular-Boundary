#!/usr/bin/env python3
"""Sequential all-eight-chain launcher; invoke repeatedly to resume."""
import argparse,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--inputs',default='../ym_stage9/checkpoints');p.add_argument('--output',default='stage26_results');p.add_argument('--cache',default='stage24_inner/deps_stage23/deps/stage19_complete');p.add_argument('--target-sweeps',type=int,default=11000);p.add_argument('--stride',type=int,default=20);p.add_argument('--burn',type=int,default=96);p.add_argument('--depth',type=int,default=32);p.add_argument('--thin',type=int,default=3);p.add_argument('--reps',type=int,default=2);p.add_argument('--max-outer',type=int,default=0);p.add_argument('--kinds',nargs='+',default=['square','penrose']);p.add_argument('--seeds',type=int,nargs='+',default=[101,211,307,419]);a=p.parse_args()
for kind in a.kinds:
 for seed in a.seeds:
  cmd=[sys.executable,str(Path(__file__).with_name('stage26_outer.py')),'--kind',kind,'--seed',str(seed),'--checkpoint',str(Path(a.inputs)/f'{kind}_nt20_seed{seed}.npz'),'--output',a.output,'--cache',a.cache,'--target-sweeps',str(a.target_sweeps),'--stride',str(a.stride),'--burn',str(a.burn),'--depth',str(a.depth),'--thin',str(a.thin),'--reps',str(a.reps),'--max-outer',str(a.max_outer)]
  print('LAUNCH',kind,seed,flush=True);subprocess.run(cmd,check=True)
