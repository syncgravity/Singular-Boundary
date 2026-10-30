#!/usr/bin/env python3
"""Serial, capped Stage18 scalar launcher; resumes each independent seed."""
import argparse,subprocess,sys,os
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--inputs',required=True);p.add_argument('--output',required=True)
p.add_argument('--target-sweeps',type=int,default=12000);p.add_argument('--chunk',type=int,default=100)
p.add_argument('--thin',type=int,default=10);p.add_argument('--kinds',nargs='+',choices=['square','penrose'],default=['square','penrose'])
p.add_argument('--seeds',nargs='+',type=int,default=[101,211,307,419]);a=p.parse_args()
if a.target_sweeps<10000 or a.chunk<1 or a.thin<1:p.error('invalid target/chunk/thin')
for kind in a.kinds:
 for seed in a.seeds:
  state=Path(a.output)/f'{kind}_seed{seed}'/'restart.npz'
  if state.exists():
   import numpy as np
   with np.load(state,allow_pickle=False) as z:now=int(z['sweeps'])
  else:
   source=Path(a.inputs)/f'{kind}_nt20_seed{seed}.npz'
   if not source.exists():raise FileNotFoundError(source)
   import numpy as np
   with np.load(source,allow_pickle=False) as z:now=int(z['sweeps'])
  while now<a.target_sweeps:
   cmd=[sys.executable,str(Path(__file__).with_name('stage18_scalar_run.py')),
    '--kind',kind,'--seed',str(seed),'--inputs',str(a.inputs),'--output',str(a.output),
    '--target-sweeps',str(a.target_sweeps),'--chunk',str(a.chunk),'--thin',str(a.thin)]
   print('RUNNING',kind,seed,now,'->',min(now+a.chunk,a.target_sweeps),flush=True)
   subprocess.run(cmd,check=True)
   with np.load(Path(a.output)/f'{kind}_seed{seed}'/'restart.npz',allow_pickle=False) as z:nxt=int(z['sweeps'])
   if nxt<=now:raise RuntimeError('no forward progress')
   now=nxt
print('TARGET REACHED for all requested chains',flush=True)
