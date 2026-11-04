#!/usr/bin/env python3
"""Exact finite checks of face-energy collar and exceptional history charging.
All-width analytical proof: research/audits/DIRECT_FACE_NESTED_CASIMIR_CLOSURE_2026-11-04.md
Full independent physical matrix verifier and hashes: companion conversation ZIP.
"""
from fractions import Fraction as Q
from random import Random
rng=Random(20261104)
t=Q(1,4)
count=0
for N in range(1,29):
 for _ in range(24):
  a=[rng.randrange(9) for i in range(N)]
  if not any(a):continue
  energies=[z*(z+2) for z in a];D=sum(energies)
  J=[(i,j) for i in range(N) for j in range(i,N)]
  W={j:Q(rng.randrange(1,30),rng.randrange(2,80)) for j in J}
  G=max(sum((W[j] for j in J if j[0]<=i<=j[1]),Q()) for i in range(N))
  q={j:sum(energies[j[0]:j[1]+1]) for j in J}
  exc=[j for j in J if 2*q[j]>D]
  assert sum((t**Q(j[1]-j[0]+1,2)*W[j] for j in exc),Q())<=G
  assert sum((Q(2+6*(j[1]-j[0]+1))*t**(j[1]-j[0]+1)*W[j] for j in exc),Q())<=4*G
  count+=2
  for i in range(N):
   assert sum((t**(j[1]-j[0]+1)*W[j] for j in J if j[0]-1<=i<=j[1]+1),Q())<=3*t*G
   count+=1
  for j in J:
   b=[0]*N;s=rng.randrange(1,8)
   for i in range(j[0],j[1]+1):b[i]=rng.randrange(1,s+1)
   edge=2*sum(a[i]*b[i] for i in range(N))
   for i in range(N+1):
    ids=[k for k in (i-1,i) if 0<=k<N]
    edge+=sum(a[k] for k in ids)*sum(b[k] for k in ids)
   collar=sum(a[max(0,j[0]-1):min(N,j[1]+2)])
   assert edge<=8*s*collar
   if 2*q[j]<=D: assert Q(3*edge,D)<=Q(24*s*collar,D)
   count+=1
assert count==108513,count
print("PASS",count,"exact rational face-Casimir/one-face collar/weighted exception checks")
print("At kappa=log(4): H_kappa=4, C_same=88/3, C_moment=6")
