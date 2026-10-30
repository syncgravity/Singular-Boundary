import tempfile
from pathlib import Path
import numpy as np
from stage7_checkpointed import (initialize,get_plaquettes,sweep,rng_state,process)
from stage7_large_torus import assemble_vectorized
from stage3_periodic_pilot import square_torus
from stage2_rational_torus import build_torus

def test_mcmc_consistency():
 for sp in [build_torus(5),square_torus(13,14,61.70899448216604)]:
  a=(sp['physical_area']/sp['F'])**.5
  l=assemble_vectorized(sp,4,3.5,a)
  st=rng_state('test',102)
  links=initialize(l['L'],st)
  assert np.max(np.abs(np.linalg.norm(links,axis=1)-1))<1e-12
  links2=links.copy();st2=st.copy()
  pf=get_plaquettes(links,l['fi'],l['sg']);pf2=pf.copy()
  counts=[sweep(links,pf,l['fi'],l['sg'],l['beta'],l['adj'],l['degree'],st,.95) for _ in range(5)]
  for _ in range(2):sweep(links2,pf2,l['fi'],l['sg'],l['beta'],l['adj'],l['degree'],st2,.95)
  for _ in range(3):sweep(links2,pf2,l['fi'],l['sg'],l['beta'],l['adj'],l['degree'],st2,.95)
  assert np.array_equal(links,links2)
  assert np.array_equal(pf,pf2)
  assert np.array_equal(st,st2)
  assert np.max(np.abs(pf-get_plaquettes(links,l['fi'],l['sg'])))<1e-9
  assert min(counts)>0
  print('PASS exact restart, cache, group SU2:',sp['spatial_kind'])

if __name__=='__main__':test_mcmc_consistency()


def test_Haar_init():
 st=rng_state('haar',4409)
 u=initialize(120000,st)
 m=np.mean(u**2,axis=0)
 assert max(abs(m-.25))<.004,m
 assert max(abs(u.mean(axis=0)))<.01
 print('PASS Haar quaternion first and second moments:',m)

if __name__=='__main__':test_Haar_init()
