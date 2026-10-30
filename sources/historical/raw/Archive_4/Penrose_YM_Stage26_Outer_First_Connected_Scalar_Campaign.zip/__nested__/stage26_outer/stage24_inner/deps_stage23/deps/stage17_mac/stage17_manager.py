#!/usr/bin/env python3
"""Mac-safe 1-2 worker scheduling for independent Stage 17 chains."""
import argparse,concurrent.futures,fcntl,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
SEEDS=(101,211,307,419)

def main():
 p=argparse.ArgumentParser();p.add_argument('--inputs',required=True);p.add_argument('--output',required=True)
 p.add_argument('--workers',type=int,choices=[1,2],default=1);p.add_argument('--chunk',type=int,default=100)
 p.add_argument('--passes',type=int,default=1);p.add_argument('--max-hours',type=float,default=0.)
 p.add_argument('--pairs',type=int,default=600);p.add_argument('--thin',type=int,default=10)
 p.add_argument('--lags',type=int,nargs='+',default=list(range(2,11)));p.add_argument('--kinds',nargs='+',choices=['square','penrose'],default=['square','penrose'])
 p.add_argument('--seeds',type=int,nargs='+',default=list(SEEDS));a=p.parse_args()
 if a.chunk<=0 or a.passes<0 or a.max_hours<0 or a.passes==0 and a.max_hours==0:p.error('invalid budget')
 out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
 lock=(out/'.stage17_manager.lock').open('a+')
 try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError:raise SystemExit('Stage 17 manager is already running')
 items=[(k,s) for k in a.kinds for s in a.seeds];deadline=time.monotonic()+a.max_hours*3600 if a.max_hours else float('inf')
 def task(pair):
  k,s=pair;cmd=[sys.executable,str(HERE/'stage17_measure.py'),'--kind',k,'--seed',str(s),'--inputs',str(Path(a.inputs).resolve()),'--output',str(out),'--chunk',str(a.chunk),'--thin',str(a.thin),'--pairs',str(a.pairs),'--lags',*map(str,a.lags)]
  env=os.environ.copy();env.update({n:'1' for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','NUMBA_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS')})
  r=subprocess.run(cmd,env=env,capture_output=True,text=True)
  if r.returncode:raise RuntimeError(f'{k} {s}: {r.stderr[-2000:]} {r.stdout[-1000:]}')
  return r.stdout.strip()
 try:
  iteration=0
  while a.passes==0 or iteration<a.passes:
   if time.monotonic()>=deadline:break
   with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
    inflight={};iterator=iter(items)
    while True:
     while len(inflight)<a.workers and time.monotonic()<deadline:
      try:item=next(iterator)
      except StopIteration:break
      inflight[pool.submit(task,item)]=item
     if not inflight:break
     done,_=concurrent.futures.wait(inflight,return_when=concurrent.futures.FIRST_COMPLETED)
     for f in done:
      print(f.result(),flush=True);del inflight[f]
   iteration+=1
 finally:fcntl.flock(lock,fcntl.LOCK_UN);lock.close()
if __name__=='__main__':main()
