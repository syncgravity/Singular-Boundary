#!/usr/bin/env python3
"""Deterministic finite two-rhombus strong-field SU2 tangent-limit constants.
Checks exact algebra and sixth-dimensional quadrature; does not replace proof.
"""
from itertools import combinations, permutations, product
import math
import numpy as np
import sympy as sy
from numpy.polynomial.hermite_e import hermegauss

faces0 = [
 [(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)],
]
def ekey(a,b): return tuple(sorted((a,b)))
def edges(face):
 return {ekey(a,b) for a,b in combinations(face,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
F=[edges(f) for f in faces0]
E=sorted(set.union(*F));V=sorted({v for e in E for v in e})
assert len(E)==10 and len(V)==8
F2=F[:2]; E2=sorted(F2[0]|F2[1]);V2={v for e in E2 for v in e}
assert len(E2)==7 and len(V2)==6 and len(F2[0]&F2[1])==1
B=sy.zeros(2,7)
for i,face in enumerate(faces0[:2]):
  for e in F2[i]:B[i,E2.index(e)]=1
j=E2.index(next(iter(F2[0]&F2[1])))
B[1,j]=-1
assert B*B.T==sy.Matrix([[4,-1],[-1,4]])
Msy=sy.Matrix([[4,-1],[-1,4]])
assert Msy.eigenvals()=={sy.Integer(3):1,sy.Integer(5):1}
rad=sy.sqrt(sy.trace(Msy)+2*sy.sqrt(Msy.det()))
root=(Msy+sy.sqrt(Msy.det())*sy.eye(2))/rad
assert sy.simplify(root*root-Msy)==sy.zeros(2)
coeff=sy.simplify(sy.Rational(3,16)*root[0,1]**2)
assert sy.simplify(coeff-sy.Rational(3,32)*(4-sy.sqrt(15)))==0
var_diag=sy.simplify(sy.Rational(3,16)*root[0,0]**2)
assert sy.simplify(var_diag-sy.Rational(3,32)*(4+sy.sqrt(15)))==0
mean=sy.simplify(3*sy.sqrt(2)*root[0,0]/8)
assert sy.simplify(mean-3*sy.sqrt(2)*(sy.sqrt(3)+sy.sqrt(5))/16)==0

# Independent deterministic 6-D Gauss-Hermite: exact degree-four Gaussian moments.
nodes,weights=hermegauss(3);weights=weights/math.sqrt(2*math.pi)
for shared in [0.0,.25,1.0,2.5]:
 A1,A2=4.0,5.0
 M=np.array([[A1,-shared],[-shared,A2]])
 assert np.linalg.eigvalsh(M).min()>0
 e,U=np.linalg.eigh(M)
 sqrtM=(U*np.sqrt(e))@U.T
 Sigma=math.sqrt(2)*sqrtM
 ch=np.linalg.cholesky(Sigma)
 e1=e2=ed1d2=0.
 for indexes in product(range(3),repeat=6):
  w=np.prod([weights[i] for i in indexes]);z=np.array([nodes[i] for i in indexes])
  y=ch@z.reshape(3,2).T  # shape (2,3)
  d1=float(np.dot(y[0],y[0]))/8
  d2=float(np.dot(y[1],y[1]))/8
  e1+=w*d1;e2+=w*d2;ed1d2+=w*d1*d2
 calc=ed1d2-e1*e2
 exact=3/16*(sqrtM[0,1]**2)
 assert abs(calc-exact)<1e-13,(shared,calc,exact)
 print(f's={shared:>4g}  lim_b[b Cov(d1,d2)]={calc:.12f}  exact={exact:.12f}')

# One face check: M=4a -> b Var(d) -> 3a/4
assert sy.simplify(sy.Rational(3,16)*(2*sy.sqrt(sy.Symbol('a',positive=True)))**2 - sy.Rational(3,4)*sy.Symbol('a',positive=True))==0
print('equal-link C =',float(coeff),'diagonal =',float(var_diag),'\nPASS all exact SU2 spatial incidence and independent 6-D quadrature checks')
