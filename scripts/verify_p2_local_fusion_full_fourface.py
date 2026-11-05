#!/usr/bin/env python3
"""P-73: full corrected N=4 physical Poisson source and electric inverse
using only local CG fusion tensor contractions, no dense Fourier operator.
Every expected number independently verified in P-71; not N~m² full inverse.
"""
import numpy as np
from p2_local_fusion_source_engine import (paths,electric_restricted_local,
                                           physical_collar_terms,projected_source_coordinates)
refs={
 (3,0,2):.315418175781805,(3,1,2):.36359897782139905,
 (3,0,4):.20982992815863935,(3,1,4):.20684394535827635,
 (4,0,3):.35594459456305333,(4,1,3):.4000978537658875,
 (4,0,5):.23884701092254476,(4,1,5):.237518340874363}
for m in (3,4):
 half=0.
 for j in (0,1):
  for ell in (m-1,m+1):
   deg=[1]*4;deg[j]=ell
   labels,K=electric_restricted_local(deg)
   source=projected_source_coordinates(deg,labels,physical_collar_terms(4,m,ell,j))
   x=np.linalg.solve(K,source)
   assert np.linalg.norm(K@x-source)<1e-11
   nuclear=0.
   for L in {p[-1] for p in paths(deg)}:
    pp=[p for p in paths(deg) if p[-1]==L]
    block=np.array([[x[labels.index((p,q))] for q in pp] for p in pp])
    nuclear+=np.linalg.norm(block,'nuc')
   assert abs(nuclear-refs[(m,j,ell)])<2e-10
   half+=(ell+1)**2/(4*(m+1)**3)*nuclear
   print('PASS actual corrected local-fusion source/inverse N=4,m,j,ell',m,j,ell,
         'invariant dimension',len(labels),'S1',nuclear)
 total=2*half  # reflection symmetry independently checked at all four sites in archived suite
 assert abs(total-{3:.1291250095339979,4:.1169833273515}[m])<2e-9
 print('PASS full physical four-face first-moment response',m,total)
print('Not a polynomial-width all-fusion-path algorithm or N~m² complete inverse.')
