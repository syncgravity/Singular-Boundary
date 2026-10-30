"""One-link mixing control: exact SU(2) heatbath versus local Metropolis.
Conditional links in different time-slices at the same site have no shared plaquettes.
This local experiment says nothing about equilibration of the remaining slab DOFs.
"""
import json,time
from pathlib import Path
import numpy as np
from numba import njit
from stage16_multihit import _field,exact_su2_mean,exact_su2_heatbath
from wilson_torus import mul
from corrected_2p1_pilot import run_chain
from stage13_transport import small_square
HERE=Path(__file__).resolve().parent

@njit
def _metropolis_link(h,start,n,seed,angle=.95):
 np.random.seed(seed)
 q=start.copy();arr=np.empty((n,4));acc=0
 for i in range(n):
  axis=np.random.randn(3);axis/=np.sqrt(np.dot(axis,axis))
  th=np.random.random()*angle
  dq=np.array([np.cos(th),np.sin(th)*axis[0],np.sin(th)*axis[1],np.sin(th)*axis[2]])
  qp=mul(dq,q)
  if np.log(np.random.random())<np.dot(qp-q,h):q=qp;acc+=1
  arr[i]=q
 return arr,acc/n

def compare(n=6000):
 sp,lat=small_square(nt=15,nx=8,ny=8)
 U,_,_,cache=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],665,220,2,2,.95)
 if cache>1e-9:raise AssertionError('gauge cache')
 links=U[-1];eid=lat['nt']*sp['E']+13
 h=_field(links,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],eid)
 expected=exact_su2_mean(h)
 t=time.perf_counter();met,accept=_metropolis_link(h,links[eid],n,181,.95);mt=time.perf_counter()-t
 rng=np.random.default_rng(181)
 t=time.perf_counter();hb=np.array([exact_su2_heatbath(h,rng) for _ in range(n)]);ht=time.perf_counter()-t
 axis=h/np.linalg.norm(h)
 out={}
 for name,arr,cost in [('metropolis',met,mt),('exact_heatbath',hb,ht)]:
  projection=arr@axis
  ac1=np.corrcoef(projection[1:],projection[:-1])[0,1]
  out[name]={'projected_mean':float(projection.mean()),'target_mean':float(expected@axis),
    'mean_error':float(projection.mean()-expected@axis),
    'lag1_autocorrelation':float(ac1), 'seconds':cost}
 out['metropolis']['acceptance']=float(accept)
 result={'conditional_field_norm':float(np.linalg.norm(h)), 'n_samples':n,
   'one_link_fixed_neighborhood':True,'remaining_slab_equilibration':'NOT TESTED',
   'note':'exact multihit uses analytic mean, no heatbath samples required; heatbath is an optional exact single-link Gibbs draw',
   'results':out}
 (HERE/'HEATBATH_MIXING.json').write_text(json.dumps(result,indent=2))
 return result
if __name__=='__main__':print(json.dumps(compare(),indent=2))
