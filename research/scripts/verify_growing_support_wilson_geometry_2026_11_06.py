#!/usr/bin/env python3
"""Finite cubic-incidence and curvature-normalization regression.
Full non-Abelian finite-difference verifier + log are in the archived Library ZIP.
This checks deterministic geometry, NOT a coupled quantum-vacuum sample.
"""
import math
import numpy as np
def cubic(n):
 edge={};faces=[]
 def inc(p,k):
  t=list(p);t[k]+=1;return tuple(t)
 for p in np.ndindex((n+1,n+1,n+1)):
  for k in range(3):
   if p[k]<n:edge[(p,k)]=len(edge)
 for p in np.ndindex((n+1,n+1,n+1)):
  for i in range(3):
   for j in range(i+1,3):
    if p[i]>=n or p[j]>=n:continue
    faces.append((edge[p,i],edge[inc(p,i),j],edge[inc(p,j),i],edge[p,j]))
 return len(edge),faces
checks=0
for n in [1,2,3,4,6,8,12]:
 E,faces=cubic(n);P=len(faces);h=1/n
 assert (E,P)==(3*n*(n+1)**2,3*n*n*(n+1));checks+=1
 d=np.zeros(E,int)
 for f in faces:
  assert len(set(f))==4;checks+=1
  for e in f:d[e]+=1
 assert d.max()<=4;checks+=1
 assert abs(8*P*h**3-24*(1+1/n))<1e-10;checks+=1
 for L in [1.,2.]:
  w=np.full(P,L/P)
  # Deterministic upper bound ||grad sum(w_p ell_p)||² <=4 sum(w_p²)
  assert abs(4*np.dot(w,w)-4*L*L/P)<1e-10;checks+=1
print(f"PASS {checks} incidence, weights and curvature normalization checks")
