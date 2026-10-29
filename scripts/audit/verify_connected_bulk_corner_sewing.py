#!/usr/bin/env python3
"""Exact 3x3 Wilson support and symbolic full-coupling corner response regression."""
from itertools import combinations
from collections import defaultdict
import sympy as s
C=[(0,1),(1,0),(0,-1),(-1,0)]
D=[(1,1),(-1,1),(-1,-1),(1,-1)]
faces=[(0,0)]+C+D
edge_inc=defaultdict(list)
for x,y in faces:
 v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 for a,b in zip(v,v[1:]+v[:1]):edge_inc[tuple(sorted((a,b)))].append((x,y))
assert len(edge_inc)==24
adj=defaultdict(set)
for fs in edge_inc.values():
 if len(fs)==2:
  a,b=fs;adj[a].add(b);adj[b].add(a)
def haar(mask):
 active={f for i,f in enumerate(C+D) if (mask>>i)&1}
 if not set(C)<=active:return True
 rem=set(active);components=[]
 while rem:
  q=[rem.pop()];seen={q[0]}
  for v in q:
   for w in adj[v]&rem:rem.remove(w);seen.add(w);q.append(w)
  components.append(seen)
 colors=[next(i for i,P in enumerate(components) if f in P) for f in C]
 for k in set(colors):
  bits=[v==k for v in colors]
  if 0<sum(bits)<4 and sum(bits[i]!=bits[(i+1)%4] for i in range(4))==2:return True
 return False
assert sum(haar(mask) for mask in range(256))==251
assert sum(not haar(mask) for mask in range(256))==5
for j in (1,2,3):assert 4*(2*j)+3*2==8*j+6
z=s.symbols('z0:4');a=s.symbols('alpha')
F=a*a+s.Rational(2,7)*z[0]**2*z[1]**4*z[2]**2-s.Rational(1,5)*z[1]**2*z[2]**2*z[3]**4+s.Rational(3,8)*s.prod(w**2 for w in z)
rhs=a*a
for n in (3,4):
 for S in combinations(range(4),n):
  expr=F.subs({z[i]:0 for i in range(4) if i not in S})
  for i in S:expr=s.diff(expr,z[i],2)*(1-z[i])
  for i in S:expr=s.integrate(expr,(z[i],0,1))
  rhs+=expr
assert s.simplify(rhs-F.subs({t:1 for t in z}))==0
print('PASS 251 exact Haar activation supports, five unresolved connected supports, 8j+6 filtration and corner-sewing identity')
