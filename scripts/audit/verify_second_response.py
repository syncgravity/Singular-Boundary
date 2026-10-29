#!/usr/bin/env python3
"""Exact SU2 finite character and parity-resolved second response audit.
No Monte Carlo. Original source archives unmodified.
"""
import sympy as s
from itertools import combinations
z=(-1,-1,-1,-1,-1)
seed=[[z,(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[z,(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[z,(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
F=[frozenset(x) for x in seed]
p=(3,2,1,0,4)
def r(x):return tuple(x[i] for i in p)
assert [F.index(frozenset(r(v) for v in f)) for f in F]==[0,2,1]
def edges(f):return {tuple(sorted((a,b))) for a,b in combinations(f,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
E=[edges(f) for f in F]
assert len(set.union(*E))==10 and not(E[1]&E[2])
a=s.symbols('a',positive=True)
P=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,s.Rational(1,2)],[0,s.Rational(1,2),0]])
def curvature(energies,A):
 n=len(energies);v=s.eye(n)[:,0];G=s.diag(*([0]+[1/x for x in energies[1:]]));X=A*v;Y=G*X;var=(X.T*X)[0];S=A*A*v-var*v
 t1=4*(S.T*G*A*Y)[0];t2=2*(Y.T*(A*A-var*s.eye(n))*Y)[0];t3=-8*(X.T*Y)[0]**2
 return tuple(s.simplify(t) for t in (var,t1,t2,t3,t1+t2+t3))
v1=curvature([0,3*a,8*a],P)
A=s.Matrix(s.kronecker_product(P,s.eye(3))-s.kronecker_product(s.eye(3),P))
E0=[0,3*a,8*a];v3=curvature([i+j for i in E0 for j in E0],A)
assert v1[0]==s.Rational(1,4) and v1[-1]==-1/(32*a*a)
assert v3[0]==s.Rational(1,2) and v3[-1]==-1/(16*a*a)
q,d1,d2=s.symbols('q d1 d2',positive=True)
T=s.Matrix([[0,1,0],[1,0,q],[0,q,0]])
vv=curvature([0,d1,d2],T)
assert s.simplify(vv[-1]-(4*q*q/(d1*d2)+2*(q*q-4)/d1**2))==0
print('PASS: genuine 3-face seed symmetry and SU2 electric second response')
print('PASS: one-rhombus even sector, abstract sign indefinite 3-level response')
print('No simulations; nonlinear uniform continuum response remains OPEN')
