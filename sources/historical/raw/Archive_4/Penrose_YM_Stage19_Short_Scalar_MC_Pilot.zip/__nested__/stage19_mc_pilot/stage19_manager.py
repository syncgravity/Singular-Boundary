#!/usr/bin/env python3
"""Serial short-run launcher; fixed absolute sweep target (no clock-based runaway)."""
import argparse,subprocess,sys
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--inputs',required=True);p.add_argument('--output',required=True)
p.add_argument('--cache',default='stage19_catalogues');p.add_argument('--target-sweeps',type=int,default=10100)
p.add_argument('--chunk',type=int,default=20);p.add_argument('--thin',type=int,default=10)
p.add_argument('--kinds',choices=['square','penrose'],nargs='+',default=['square','penrose'])
p.add_argument('--seeds',type=int,nargs='+',default=[101,211,307,419]);a=p.parse_args()
if a.target_sweeps<10000 or a.chunk<1 or a.thin<1:p.error('invalid target/chunk/thin')
for kind in a.kinds:
 for seed in a.seeds:
  src=Path(a.inputs)/f'{kind}_nt20_seed{seed}.npz'; od=Path(a.output)/f'{kind}_seed{seed}'
  if not src.is_file():raise FileNotFoundError(src)
  while True:
   inp=od/'restart.npz' if (od/'restart.npz').exists() else src
   with np.load(inp,allow_pickle=False) as z:now=int(z['sweeps'])
   if now>=a.target_sweeps:break
   print('RUNNING',kind,seed,now,'->',min(now+a.chunk,a.target_sweeps),flush=True)
   cmd=[sys.executable,str(Path(__file__).with_name('stage19_mc.py')),'--kind',kind,'--seed',str(seed),
        '--inputs',str(a.inputs),'--output',str(a.output),'--cache',str(a.cache),
        '--target-sweeps',str(a.target_sweeps),'--chunk',str(a.chunk),'--thin',str(a.thin)]
   subprocess.run(cmd,check=True)
   with np.load(od/'restart.npz',allow_pickle=False) as z:nxt=int(z['sweeps'])
   if nxt<=now:raise RuntimeError('no forward progress')
print('ALL REQUESTED CHAINS HAVE REACHED TARGET',a.target_sweeps)
