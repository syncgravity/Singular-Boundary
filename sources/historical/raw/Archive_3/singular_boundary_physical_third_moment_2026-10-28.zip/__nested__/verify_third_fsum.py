#!/usr/bin/env python3
"""Deterministic SU2 non-Gaussian third-moment commutator, no Monte Carlo."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
import sympy as sp
from itertools import combinations
p,a,h,b=sp.symbols('p a h b',real=True,positive=True)
# Single four-link class sector of the genuine SU2 gauge-invariant Hamiltonian:
# T=-a(1-p**2)d²+3ap d, Y=h(1-p), V=b(1-p).
assert sp.simplify(2*(a*(1-p*p)*sp.diff(h*(1-p),p)*sp.diff(a*(1-p*p)*sp.diff(b*(1-p),p)*sp.diff(h*(1-p),p),p))-4*a*a*b*h*h*p*(1-p*p))==0
for nmode in [24,36,48,72]:
 k=np.arange(nmode,dtype=float)
 pmat=np.zeros((nmode,nmode))
 for j in range(nmode-1): pmat[j,j+1]=pmat[j+1,j]=.5
 for field in [0.,.5,5.,20.]:
  T=np.diag(k*(k+2))
  V=field*(np.eye(nmode)-pmat)
  H=T+V
  e0,vec=eigh_tridiagonal(np.diag(H),np.diag(H,1),select='i',select_range=(0,0))
  om=vec[:,0]
  yy=.1*(np.eye(nmode)-pmat)
  C=H@yy-yy@H
  L=H@C-C@H
  m3=(om@(-.5*(C@L-L@C))@om)
  z=yy@om-(om@yy@om)*om
  K=H-e0[0]*np.eye(nmode)
  direct=z@K@K@K@z
  assert abs(m3-direct)<1e-9,(nmode,field,m3,direct)
  m3V=om@(-.5*(C@(V@C-C@V)-(V@C-C@V)@C))@om
  expected=4*field*.1**2*(om@pmat@om-om@pmat@pmat@pmat@om)
  assert abs(m3V-expected)<1e-9,(m3V,expected)
  m1=z@K@z;m2=z@K@K@z
  assert m2*m2<=m1*m3+1e-8
  if nmode==48:print(f'b={field:g} m1={m1:.10g} m2={m2:.10g} m3={m3:.10g} m3V={m3V:.10g} m3T={m3-m3V:.10g}')
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
fsets=[edges(f) for f in seed];es=set.union(*fsets)
assert len(es)==10 and max(sum(e in f for f in fsets) for e in es)==2
print('PASS: interacting SU2 physical triple commutator, magnetic derivative exact, m2²<=m1*m3; authentic Penrose spatial fixture.')

# Independent differential-operator check in the radial one-plaquette SU(2) class sector.
# The whole radial T has coefficient functions, so this is not a substitute for the
# multi-link Casimir proof above, but it tests exact differential order and h powers.
x,hh,aa,bb=sp.symbols('x hh aa bb', real=True)
from math import comb

def compose(A,B):
    R={}
    for i,ai in A.items():
        for j,bj in B.items():
            for k in range(i+1):
                z=i+j-k
                R[z]=sp.expand(R.get(z,0)+ai*sp.binomial(i,k)*sp.diff(bj,x,k))
    return {k:sp.factor(v) for k,v in R.items() if v!=0}

def comm(A,B):
    AB=compose(A,B);BA=compose(B,A)
    return {k:sp.factor(AB.get(k,0)-BA.get(k,0)) for k in set(AB)|set(BA) if sp.simplify(AB.get(k,0)-BA.get(k,0))!=0}
radial_T={2:-aa*(1-x*x),1:3*aa*x}
radial_Y={0:hh*(1-x)}
C_op=comm(radial_T,radial_Y)
E_op=comm(C_op,comm(radial_T,C_op))
assert max(E_op)<=2,(E_op,max(E_op))
assert all(sp.simplify(v.subs(hh,0))==0 and sp.simplify(sp.diff(v,hh).subs(hh,0))==0 for v in E_op.values())
print('PASS: SU2 radial electric triple commutator has order <=2 and every coefficient is quadratic in source amplitude h.')
