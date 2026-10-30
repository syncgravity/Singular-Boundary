#!/usr/bin/env python3
"""Deterministic exact incidence, gauge quotient and Cheeger bound verification.

Checks the canonical three-face spatial Z^5 Penrose seed; it is not the Q14
spacetime certificate. Symbolic algebra is not a numerical proof of the
continuum and no Monte Carlo simulations are performed.
"""
from itertools import combinations
from collections import Counter
import sympy as s

SEED=[
 [(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)],
]

def canon_edge(a,b):return tuple(sorted((a,b)))
def neighbors(a,b):return sum(abs(x-y) for x,y in zip(a,b)) == 1
faces=[{canon_edge(a,b) for a,b in combinations(f,2) if neighbors(a,b)} for f in SEED]
edges=sorted(set().union(*faces));vertices=sorted({v for e in edges for v in e})
F,E,V=len(faces),len(edges),len(vertices)
assert (V,E,F)==(8,10,3)
inc=Counter(e for face in faces for e in face)
assert max(inc.values())==2 and sorted(inc.values()).count(2)==2
# Orient faces consistently: the shared edge signs must oppose each other.
# Enumerate 4-cycle vertex permutations with deterministic lexicographic tie break.
cycles=[]
for vs,es in zip(SEED,faces):
    cands=[]
    for perm in __import__('itertools').permutations(vs[1:]):
        cycle=[vs[0],*perm]
        if all(canon_edge(a,b) in es for a,b in zip(cycle,cycle[1:]+cycle[:1])):
            cands.append(cycle)
    assert cands
    cycles.append(min(cands))
B=s.zeros(F,E)
for fi,cy in enumerate(cycles):
    for a,b in zip(cy,cy[1:]+cy[:1]):
        edge=canon_edge(a,b)
        B[fi,edges.index(edge)] = 1 if (a,b)==edge else -1
# Choose each face sign by a spanning walk of dual adjacency.
orient={0:1}
while len(orient)<F:
    progressed=False
    for f in range(F):
        if f not in orient: continue
        for g in range(F):
            if g in orient or f==g:continue
            shared=faces[f]&faces[g]
            if not shared:continue
            assert len(shared)==1
            e=edges.index(next(iter(shared)))
            orient[g]=-orient[f]*B[f,e]*B[g,e]
            progressed=True
    assert progressed
for f,v in orient.items(): B[f,:]*=v
D=s.zeros(E,V)
for ei,(a,b) in enumerate(edges):
    D[ei,vertices.index(a)]=-1
    D[ei,vertices.index(b)]=1
assert B*D==s.zeros(F,V)
assert D.rank()==V-1 and B.rank()==F
assert E==(V-1)+F

W=B*B.T
adj=s.zeros(F,F)
for f in range(F):
    for g in range(F):
        if f!=g and faces[f]&faces[g]:adj[f,g]=1
assert W==4*s.eye(F)-adj
assert s.simplify(W.charpoly().as_expr()-(s.Symbol('lambda')-4)*((s.Symbol('lambda')-4)**2-2))==0
assert set(W.eigenvals().keys())=={s.Integer(4),4-s.sqrt(2),4+s.sqrt(2)}
# Nonzero Hessian eigenvalues in the link Euclidean metric for b_f=b.
b=s.symbols('b',positive=True)
H=b*B.T*B/4
assert H.rank()==F and E-H.rank()==V-1
# With exactly one discarded face, 1 physical scalar null direction,
# in addition to 7 gauge directions; SU(2) triples all dimensions.
for f in range(F):
    Bgood=B[[g for g in range(F) if g!=f],:]
    assert Bgood.rank()==F-1
    assert E-Bgood.rank()-(V-1)==1
# Exact comparison on the finite seed (h=1, b=1):
sigma=s.sin(s.pi/5)
cheeger_lb=s.pi*sigma/(2*F)
assert s.N(4-s.sqrt(2)-cheeger_lb)>0
# Source fluctuation/gauge obstruction verified algebraically; no quantum claim.
print('PASS canonical seed (V,E,F)=', (V,E,F))
print('PASS B d0=0, ranks d0=7 / d1=3, 3 purely gauge-reduced modes')
print('PASS face Dirichlet dual graph matrix and eigenvalues 4, 4±sqrt(2)')
print('PASS magnetic flat Hessian rank 3 per Lie algebra, gauge nullity 7')
print('PASS deleting each face creates exactly 1 extra physical zero mode per Lie algebra')
print('PASS conservative planar Cheeger seed lower bound; no simulation')
