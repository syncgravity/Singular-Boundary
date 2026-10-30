#!/usr/bin/env python3
"""Deterministic exact checks for shared-edge Gaussian tangent spectral moments (no Monte Carlo)."""
import sympy as s
from itertools import combinations,permutations
F0=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edge(a,b):return tuple(sorted((a,b)))
def adj(a,b):return sum(abs(x-y) for x,y in zip(a,b))==1
fs=[{edge(a,b) for a,b in combinations(f,2) if adj(a,b)} for f in F0]
E=sorted(set.union(*fs)); V=sorted({v for e in E for v in e})
B=s.zeros(3,len(E))
for i,face in enumerate(F0):
    cycles=[]
    for tail in permutations(face[1:]):
        seq=[face[0],*tail]
        if all(edge(a,b) in fs[i] for a,b in zip(seq,seq[1:]+seq[:1])):cycles.append(seq)
    seq=min(cycles)
    for a,b in zip(seq,seq[1:]+seq[:1]):
        e=edge(a,b);B[i,E.index(e)]=1 if (a,b)==e else -1
M=B*B.T
D=s.zeros(len(E),len(V))
for i,(a,b) in enumerate(E):D[i,V.index(a)]=-1;D[i,V.index(b)]=1
assert len(V)==8 and len(E)==10 and B*D==s.zeros(3,8)
assert B.rank()==3 and D.rank()==7
assert s.expand(M.charpoly().as_expr())==s.expand((s.Symbol('lambda')-4)*((s.Symbol('lambda')-4)**2-2))
assert s.trace(M)==12 and s.trace(M*M)==52
h,a,b=s.symbols('h a b',positive=True)
v=3*a*h*s.trace(M)/(16*b)
m2=3*a*a*h*s.trace(M*M)/8
assert s.simplify(v-9*a*h/(4*b))==0
assert s.simplify(m2-39*a*a*h/2)==0
# Two independent Cartesian oscillator modes: sigma=1/2 sqrt(A/B), D=A/sigma.
A,Bp=s.symbols('A Bp',positive=True)
sigma=s.sqrt(A/Bp)/2; decay=s.simplify(A/sigma)
assert s.simplify(decay**2*sigma**2-A*A)==0
# 3 colors times Gaussian Var(z^2)=2 sigma^2 (sigma is a variance).
varmode=s.Rational(3)*h/64*(2*sigma**2)
m2mode=s.simplify((2*decay)**2*varmode)
assert s.simplify(m2mode-(3*h/8)*A*A)==0
assert s.simplify(varmode-(3*h/32)*sigma**2)==0
print('PASS: authentic Penrose 3-face, 10-edge incidence; Gaussian variance and spectral m2; no Monte Carlo')
