#!/usr/bin/env python3
"""Read-only canonical Penrose seed SU(2) boundary check. No Monte Carlo."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def edges(z):
 z=list(map(tuple,z))
 return {tuple(sorted((u,v))) for u,v in combinations(z,2) if sum(abs(a-b) for a,b in zip(u,v))==1}
faces=[edges(s) for s in seed]; E=sorted(set().union(*faces))
assert len(E)==10 and all(len(x)==4 for x in faces)
def qmul(x,y):
 a,u=x[0],x[1:];b,v=y[0],y[1:]
 c=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
 return (a*b-sum((i*j for i,j in zip(u,v)),F(0)),)+tuple(a*j+b*i-t for i,j,t in zip(u,v,c))
def inv(q):return (q[0],)+tuple(-z for z in q[1:])
def d(q):return 1-q[0]
Q=[(F(1),F(0),F(0),F(0)),(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),
 (F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
assert all(sum(v*v for v in q)==1 for q in Q)
def loop(edges,link):
 degrees=Counter(x for e in edges for x in e)
 assert set(degrees.values())=={2}
 start=min(degrees);cur=start;prev=None;result=Q[0];steps=0
 while True:
  neighbors=sorted(y if x==cur else x for x,y in edges if cur in (x,y))
  dest=neighbors[0] if prev is None else next(y for y in neighbors if y!=prev)
  edge=tuple(sorted((cur,dest))); val=link[edge]
  result=qmul(result,val if edge==(cur,dest) else inv(val))
  steps+=1;prev,cur=cur,dest
  if cur==start:break
  assert steps<=len(edges)
 assert steps==len(edges)
 return result
patches=[]
for mask in range(1,8):
 ids=[i for i in range(3) if mask>>i&1]
 found={ids[0]}
 while True:
  n=found|{i for i in ids if any(faces[i]&faces[j] for j in found)}
  if n==found:break
  found=n
 if len(found)!=len(ids):continue
 count=Counter(e for i in ids for e in faces[i])
 bound={e for e,z in count.items() if z==1}
 assert len(bound)==2*len(ids)+2
 patches.append((ids,bound))
assert len(patches)==6
for case in range(7):
 links={e:Q[(i*(case+1)+case*case+2*i*i)%len(Q)] for i,e in enumerate(E)}
 delta=[d(loop(f,links)) for f in faces]
 for ids,bound in patches:
  assert d(loop(bound,links))<=len(ids)*sum(delta[j] for j in ids)
print(json.dumps({"seed_faces":3,"seed_links":10,"disk_patches":6,
 "exact_rational_boundary_checks":42,"all_passed":True,
 "physical_spectral_gap_proved":False,"monte_carlo":False},indent=2))
