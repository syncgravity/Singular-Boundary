"""Exact rational 10-cycle proper-subset forest recurrence."""
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
from collections import defaultdict
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
fi,sg,E=penrose_faces(Approximant(M=5))
S=(1,3,2,4,154,150,11,10,7,8)
links={g:set(map(int,fi[g])) for g in S}
edges=tuple(sorted((a,b) for a,b in combinations(S,2) if links[a]&links[b]))
assert len(edges)==10
def canon(blocks):return tuple(sorted(tuple(sorted(b)) for b in blocks))
@lru_cache(None)
def partinfo(J):
 present=[(a,b) for a,b in edges if a in J and b in J]
 assert len(present)<len(J)
 out=[]
 for mask in range(1<<len(present)):
  parent={v:v for v in J}
  def root(v):
   while parent[v]!=v:v=parent[v]
   return v
  for i,(a,b) in enumerate(present):
   if mask>>i&1:parent[root(a)]=root(b)
  groups=defaultdict(list)
  for v in J:groups[root(v)].append(v)
  out.append(canon(groups.values()))
 assert len(set(out))==len(out)
 return tuple(sorted(out,key=lambda p:(-len(p),p)))
def operator(p):
 J={x for block in p for x in block}
 cut=[(a,b) for a,b in edges if a in J and b in J and not any(a in v and b in v for v in p)]
 diagonal=sum((Q(3,4)*(2*len(b)+2) for b in p),Q())+Q(len(cut),2)
 r={p:diagonal}
 for a,b in cut:
  i=next(i for i,z in enumerate(p) if a in z)
  j=next(i for i,z in enumerate(p) if b in z)
  v=canon([z for k,z in enumerate(p) if k!=i and k!=j]+[p[i]+p[j]])
  r[v]=r.get(v,Q())-Q(1,2)
 return r
F={frozenset():{():Q(1)}}
for n in range(1,10):
 for subset in combinations(S,n):
  J=frozenset(subset);source=defaultdict(Q)
  for g in J:
   for p,c in F[J-{g}].items():
    source[canon(list(p)+[(g,)])]+=c
  P=partinfo(tuple(sorted(J)));res={}
  for p in P:
   inc=sum((c*operator(q).get(p,Q()) for q,c in res.items()),Q())
   res[p]=(source.get(p,Q())-inc)/operator(p)[p]
  check=defaultdict(Q)
  for p,c in res.items():
   for q,v in operator(p).items():check[q]+=c*v
  assert all(check[p]==source.get(p,Q()) for p in P)
  F[J]=res
assert len(F)==1023
print('PASS 1022 proper-subset recurrences')
