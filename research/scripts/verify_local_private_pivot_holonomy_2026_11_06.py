#!/usr/bin/env python3
"""Deterministic private-pivot geometry and Hilbert-norm contraction calibration.
Not a simulation of the interacting SU(2) vacuum or continuum flow.
"""
import math
import numpy as np
from itertools import combinations

def complex_faces(n):
 e={}; faces=[]
 def shift(x,i):
  y=list(x); y[i]+=1;return tuple(y)
 for x in np.ndindex((n+1,)*3):
  for i in range(3):
   if x[i]<n:e[x,i]=len(e)
 for x in np.ndindex((n+1,)*3):
  for i,j in combinations(range(3),2):
   if x[i]>=n or x[j]>=n:continue
   faces.append({e[x,i],e[shift(x,i),j],e[shift(x,j),i],e[x,j]})
 return len(e),faces

checks=0
for n in range(2,8):
 E,F=complex_faces(n)
 assert E==3*n*(n+1)**2 and len(F)==3*n*n*(n+1); checks+=1
 links_to_faces={a:[] for a in range(E)}
 for p,face in enumerate(F):
  assert len(face)==4;checks+=1
  for edge in face: links_to_faces[edge].append(p)
 star=next(p for p in links_to_faces.values() if len(p)==4)
 pivots=[next(e for e in F[p] if all(e not in F[q] for q in star if p!=q)) for p in star]
 assert len(set(pivots))==4;checks+=1
 for i,e in enumerate(pivots):
  assert e in F[star[i]] and all(e not in F[star[j]] for j in range(4) if i!=j);checks+=1
 print('n',n,'edges',E,'faces',len(F),'private star pivots',pivots)

for d in np.geomspace(1e-8,.3,120):
 theta=math.acos(1-d)
 vol=(theta-math.sin(theta)*math.cos(theta))/math.pi
 assert 0<vol<1;checks+=1
 for k in [1,2,4,8]:
  assert abs((vol**k)**(2/(3*k))-vol**(2/3))<1e-13;checks+=1

rng=np.random.default_rng(20261106)
for m in [2,3,8,31]:
 for j in range(500):
  f=rng.normal(size=m);df=rng.normal(size=m)
  der=np.dot(f,df)/np.linalg.norm(f)
  assert der*der <= np.dot(df,df)+1e-10;checks+=1
print('PASS',checks,'geometry/cap/Fisher-contraction checks')
