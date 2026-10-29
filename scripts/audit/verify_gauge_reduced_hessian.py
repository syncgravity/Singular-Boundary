#!/usr/bin/env python3
import sympy as s
from itertools import combinations,permutations
faces0=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edge(a,b):return tuple(sorted((a,b)))
def adjacent(a,b):return sum(abs(x-y) for x,y in zip(a,b))==1
faces=[{edge(a,b) for a,b in combinations(f,2) if adjacent(a,b)} for f in faces0]
E=sorted(set.union(*faces));V=sorted({v for e in E for v in e});B=s.zeros(3,len(E))
for i,vs in enumerate(faces0):
 cs=[]
 for perm in permutations(vs[1:]):
  seq=[vs[0],*perm]
  if all(edge(a,b) in faces[i] for a,b in zip(seq,seq[1:]+seq[:1])):cs.append(seq)
 seq=min(cs)
 for a,b in zip(seq,seq[1:]+seq[:1]):
  k=edge(a,b);B[i,E.index(k)]=1 if (a,b)==k else -1
for i in [1,2]:
 shared=next(iter(faces[0]&faces[i]));j=E.index(shared)
 B[i,:]*=-B[0,j]*B[i,j]
D=s.zeros(len(E),len(V))
for i,(a,b) in enumerate(E):D[i,V.index(a)]=-1;D[i,V.index(b)]=1
assert len(V)==8 and len(E)==10 and B*D==s.zeros(3,8)
assert B.rank()==3 and D.rank()==7
W=B*B.T
assert set(W.eigenvals())=={s.Integer(4),4-s.sqrt(2),4+s.sqrt(2)}
assert all(B[[j for j in range(3) if j!=i],:].rank()==2 for i in range(3))
print("PASS exact original spatial seed rank/gauge kernel and dual eigenvalues; no Monte Carlo")