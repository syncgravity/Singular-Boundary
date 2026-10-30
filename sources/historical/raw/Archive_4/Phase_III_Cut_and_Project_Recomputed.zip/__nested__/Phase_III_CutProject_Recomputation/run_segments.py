"""Run all scheduled independent chains, each in short restartable chunks."""
from checkpoint_wilson import run_one
import sys,time,json
from pathlib import Path
out=Path(__file__).parent
start=time.perf_counter()
for R in (5., 6.5):
 for beta in (1.,2.):
  for c in range(4):
   while True:
    row=run_one(radius=R,offset=0,beta=beta,chain=c,burn=100,thin=3,target=200,
                module_sweeps=150,directory=str(out/'chains_certified'))
    print(json.dumps(row),flush=True)
    if row['done']:break
print('total_seconds',round(time.perf_counter()-start,3),flush=True)
