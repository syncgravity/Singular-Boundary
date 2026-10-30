"""Gauge symmetry and physical displacement checks for bounded Stage 7 observables."""
import numpy as np
from stage2_rational_torus import build_torus
from stage3_periodic_pilot import square_torus
from stage7_measurement import build_measurement_plan,measure_configuration
from stage7_checkpointed import rng_state,initialize
from wilson_torus import mul

def dag(q):
 r=q.copy();r[1:]*=-1;return r

def gauge_transform(sp,links,nt,seed):
 V,E=sp['V'],sp['E']
 g=initialize(nt*V,rng_state('gauge',seed))
 out=links.copy()
 for t in range(nt):
  for e,(u,v) in enumerate(sp['edges']):
   out[t*E+e]=mul(mul(g[t*V+u],links[t*E+e]),dag(g[t*V+v]))
  for v in range(V):
   link=nt*E+t*V+v
   out[link]=mul(mul(g[t*V+v],links[link]),dag(g[((t+1)%nt)*V+v]))
 return out

def test_one(sp):
 nt=4
 plan=build_measurement_plan(sp)
 for path,meta in zip(zip(plan[-1]['idx'],plan[-1]['sign'],plan[-1]['length']),plan[-1]['meta']):
  idx,sg,l=path
  vec=np.sum(sp['edge_vectors'][idx[:l]]*sg[:l,None],axis=0)
  assert np.max(np.abs(vec-np.asarray(meta['physical_displacement'])))<1e-10
 links=initialize(nt*(sp['E']+sp['V']),rng_state('links',110))
 a,b,c=measure_configuration(links,nt,sp,plan,levels=(0,2,6))
 gt=gauge_transform(sp,links,nt,120)
 x,y,z=measure_configuration(gt,nt,sp,plan,levels=(0,2,6))
 err=float(max(np.max(abs(a-x)),np.max(abs(b-y)),np.max(abs(c-z))))
 assert a.shape==(nt,9) and b.shape==(nt,6) and c.shape==(3,len(plan[-1]['length']),nt//2)
 assert err<1e-11,err
 print('PASS',sp['spatial_kind'],'gauge residual',err, 'path count',len(plan[-1]['length']))
 return err
if __name__=='__main__':
 test_one(build_torus(5));test_one(square_torus(13,14,61.70899448216604))
