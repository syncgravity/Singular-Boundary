#!/usr/bin/env python3
"""Finite diagonal-Z5 quotient calibration, NOT authenticated Penrose/3D SU2.
Full 3375-check C5/D5 and sourced-window diagnostics in Library audit ZIP.
"""
import itertools, math, cmath
from collections import Counter
w=cmath.exp(2j*math.pi/5)
steps=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1))
checks=0
def proj(x,k):
 return sum(x[j]*w**(k*j) for j in range(4))
def rotate(x):
 a=list(x)+[0];b=a[1:]+a[:1];return tuple(t-b[4] for t in b[:4])
def mirror(x):
 a=list(x)+[0];b=[a[(-j)%5] for j in range(5)]
 return tuple(t-b[4] for t in b[:4])
def accept(x):
 z1,z2=proj(x,1),proj(x,2)
 if abs(z1)>5: return False
 return all((z2*cmath.exp(-2j*math.pi*j/10)).real<=1.65*math.cos(math.pi/10)+1e-12 for j in range(10))
V={x for x in itertools.product(range(-6,7),repeat=4) if accept(x)}
edges=set()
for x in V:
 for step in steps:
  y=tuple(a+b for a,b in zip(x,step))
  if y in V:edges.add(tuple(sorted((x,y))))
deg=Counter()
for x,y in edges:deg[x]+=1;deg[y]+=1
assert len(V)==231 and len(edges)==610
for x in V:
 y=rotate(x);z=mirror(x)
 assert y in V and z in V and mirror(z)==x
 assert abs(proj(z,1)-proj(x,1).conjugate())<1e-10
 assert abs(proj(z,2)-proj(x,2).conjugate())<1e-10
 assert deg[z]==deg[x]
 checks+=5
for i,st in enumerate(steps):
 assert abs(proj(st,1)-w**i)<1e-12
 checks+=1
for p in itertools.product(range(-2,3),repeat=4):
 z1,z2=proj(p,1),proj(p,2)
 for k in (1,2):
  base=proj(p,k)
  m=list(p)+[0]
  assert abs(sum((m[j]+3)*w**(k*j) for j in range(5))-base)<1e-11
  checks+=1
for x in [(1,2,-3,4,0),(0,0,0,0,0)]:
 for j in range(5):
  b=list(x); b[j]+=1
  assert sum(b)==sum(x)+1
  checks+=1
print(f"PASS {checks} quotient and dihedral calibration tests; V={len(V)} E={len(edges)} mean_degree={2*len(edges)/len(V):.6f}")
print("NOT source window/acceptance and NOT physical 3D geometry.")
