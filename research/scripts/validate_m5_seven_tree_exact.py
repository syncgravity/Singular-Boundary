from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces

faces,signs,E=penrose_faces(Approximant(M=5))
S=(1,2,3,4,7,8,10)
support={g:set(map(int,faces[g])) for g in S}
adj={(a,b):next(iter(support[a]&support[b])) for a,b in combinations(S,2) if support[a]&support[b]}
assert adj=={(1,3):3,(1,8):14,(2,3):2,(2,4):5,(7,8):8,(7,10):12}
edges=tuple(adj)
def canon(blocks):return tuple(sorted(tuple(sorted(x)) for x in blocks))
@lru_cache(None)
def partitions(J):
    active=tuple((a,b) for a,b in edges if a in J and b in J)
    out=set()
    for mask in range(1<<len(active)):
        parent={v:v for v in J}
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        for i,(a,b) in enumerate(active):
            if mask>>i&1:parent[root(a)]=root(b)
        groups={}
        for v in J:groups.setdefault(root(v),[]).append(v)
        out.add(canon(groups.values()))
    return sorted(out,key=lambda p:(-len(p),p))
def merge(p,a,b):
    i=next(i for i,x in enumerate(p) if a in x)
    j=next(i for i,x in enumerate(p) if b in x)
    if i==j:return p
    return canon([x for k,x in enumerate(p) if k not in (i,j)]+[p[i]+p[j]])
def T(p):
    J={x for block in p for x in block}
    cuts=[(a,b) for a,b in edges if a in J and b in J and not any(a in q and b in q for q in p)]
    d=sum((F(3,4)*(2*len(q)+2) for q in p),F())+F(len(cuts),2)
    out={p:d}
    for a,b in cuts:out[merge(p,a,b)]=out.get(merge(p,a,b),F())-F(1,2)
    return out
coeff={frozenset():{():F(1)}}
for size in range(1,8):
    for Jtuple in combinations(S,size):
        J=frozenset(Jtuple);src={}
        for g in J:
            for p,c in coeff[J-{g}].items():
                q=canon(list(p)+[(g,)])
                src[q]=src.get(q,F())+c
        P=partitions(tuple(sorted(J)));sol={}
        for p in P:
            incoming=sum((c*T(q).get(p,F()) for q,c in sol.items()),F())
            sol[p]=(src.get(p,F())-incoming)/T(p)[p]
        check={}
        for p,c in sol.items():
            for q,d in T(p).items():check[q]=check.get(q,F())+c*d
        assert all(check.get(p,F())==src.get(p,F()) for p in P)
        coeff[J]=sol
full=coeff[frozenset(S)]
assert len(coeff)==128 and len(full)==64
assert full[canon([(g,) for g in S])]==F(58886977,206090632800)
assert full[(tuple(S),)]==F(13607484139435318199,2995402808330596135600128000)
print("PASS: 127 exact subset residuals, 64 final retained Wilson products; squarefree Q coefficient zero")
