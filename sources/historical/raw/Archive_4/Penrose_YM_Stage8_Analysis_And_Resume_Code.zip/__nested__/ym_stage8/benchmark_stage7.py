"""Full M55 2+1D SU2 Wilson hot-start update, deliberately non-thermalized.
Only algorithm feasibility and runtime are reported; no physical observables.
"""
import sys,time,os,json,hashlib,argparse
import numpy as np
from numba import njit
from stage7_large_torus import pair,assemble_vectorized
from stage6_multilevel import plaquettes, update_sweeps_inplace
from wilson_torus import face_trace_scalar

@njit
def init_field(n,seed):
 np.random.seed(seed)
 U=np.empty((n,4),np.float64)
 for i in range(n):
  q=np.random.randn(4)
  U[i]=q/np.sqrt(np.dot(q,q))
 return U

@njit
def init_random(seed):np.random.seed(seed)


def run(kind,nt=20,sweeps=2,seed=541):
 tp=time.monotonic()
 sp=pair()[0 if kind=='penrose' else 1]
 a=(sp['physical_area']/sp['F'])**.5
 lat=assemble_vectorized(sp,nt,3.5,a)
 tp=time.monotonic()-tp
 # compile on a small model prior to timing production updates, if needed
 from stage2_rational_torus import build_torus
 little=build_torus(5)
 la=assemble_vectorized(little,4,3.5,(little['physical_area']/little['F'])**.5)
 u0=init_field(la['L'],120);p0=plaquettes(u0,la['fi'],la['sg'])
 init_random(121)
 _=update_sweeps_inplace(u0,p0,la['fi'],la['sg'],la['beta'],la['adj'],la['degree'],np.arange(la['L'],dtype=np.int32),1,.95)
 # expensive part
 start=time.monotonic()
 u=init_field(lat['L'],seed);pf=plaquettes(u,lat['fi'],lat['sg'])
 init=time.monotonic()-start
 init_random(seed+3001)
 live=np.arange(lat['L'],dtype=np.int32)
 stats=[]
 for z in range(sweeps):
  t=time.monotonic()
  accepted=update_sweeps_inplace(u,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],live,1,.95)
  elapsed=time.monotonic()-t
  means=pf.reshape(nt,sp['F']+sp['E'])
  stats.append({'sweep':z+1,'seconds':elapsed,'acceptance':accepted/lat['L'],
     'spatial_plaquette':float(means[:,:sp['F']].mean()),
     'temporal_plaquette':float(means[:,sp['F']:].mean())})
  print(kind,'sweep',z+1, 'seconds',round(elapsed,2),'acc',round(accepted/lat['L'],3),flush=True)
 resid=float(np.max(np.abs(plaquettes(u,lat['fi'],lat['sg'])-pf)))
 print('CACHED PLAQUETTE ERROR',resid,flush=True)
 assert resid<1e-9
 # one hot-start field is not equilibrated nor an independent measurement
 report={'geometry':kind,'V':sp['V'],'F':sp['F'],'nt':nt,'L':lat['L'],
   'beta_ref':3.5,'initial_state':'independent Haar SU2 on every link',
   'geometry_build_seconds':tp,'initialization_seconds':init,
   'sweeps':stats,'cache_max_error':resid,'measured_physics':'NONE: warmup only; no equilibrated ensemble',
   'estimated_sweep_time':float(np.median([r['seconds'] for r in stats]))}
 out='/mnt/data/ym_stage7/M55_'+kind+'_hot_start_benchmark.json'
 with open(out,'w') as f:json.dump(report,f,indent=2)
 return report

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--geometry',default='penrose');ap.add_argument('--sweeps',type=int,default=2);a=ap.parse_args()
 run(a.geometry,sweeps=a.sweeps)
