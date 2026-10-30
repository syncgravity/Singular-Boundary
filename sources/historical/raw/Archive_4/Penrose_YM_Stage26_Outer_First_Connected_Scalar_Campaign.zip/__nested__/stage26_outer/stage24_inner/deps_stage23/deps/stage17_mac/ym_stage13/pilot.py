"""Tiny-lattice smoke/precision study; NO physical measurements accepted."""
import json,time,numpy as np
from pathlib import Path
from stage13_transport import *
from corrected_2p1_pilot import run_chain

def main():
 sp,lat=small_square();nt=lat['nt'];E=sp['E'];V=sp['V']
 started=time.monotonic()
 outer,actions,accept,err=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],30303,200,96,6,.95)
 results=[]
 for i,u in enumerate(outer):
  result=conditioned_rectangle(u,lat,sp,0,1,[0],[1],inner=16,warm=16,spacing=2,seed=35000+i)
  result['action']=float(actions[i]);results.append(result)
  if (i+1)%4==0:print('outer',i+1,'/',len(outer),flush=True)
 d=np.array([r['initial_direct'] for r in results]);c=np.array([r['conditional'] for r in results]);ic=np.array([r['inner_direct_mean'] for r in results]);
 out={'geometry':'5x5 square nt15 only','physical_admission':False,'n_outer':len(outer),'inner':16,'conditional_warm_sweeps':16,
      'mean_direct':float(d.mean()),'mean_conditional':float(c.mean()),'mean_inner_direct':float(ic.mean()),
      'sd_direct':float(d.std(ddof=1)),'sd_conditional':float(c.std(ddof=1)),
      'std_ratio_descriptive':float(d.std(ddof=1)/c.std(ddof=1)) if c.std(ddof=1)>0 else None,
      'direct_vs_conditional_mean_diff_se':float((c-d).mean()/((c-d).std(ddof=1)/(len(d)**.5))) if (c-d).std(ddof=1)>0 else None,
      'max_cache_error':max(x['cache_error'] for x in results), 'seconds':time.monotonic()-started,
      'note':'16 outer configurations from one short chain. Deep inner equilibration, outer independence and cost-adjusted variance are not validated. Product of inner means is a finite-N conditional estimator with dependence from shared inner trajectory.'}
 Path(__file__).parent.joinpath('PILOT.json').write_text(json.dumps(out,indent=2))
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
