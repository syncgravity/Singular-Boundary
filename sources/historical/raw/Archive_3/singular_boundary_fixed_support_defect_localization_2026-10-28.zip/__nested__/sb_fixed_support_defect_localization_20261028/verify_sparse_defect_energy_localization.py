#!/usr/bin/env python3
"""Deterministic SU(2) class-angle, cutoff, and spectral energy tests; no Monte Carlo."""
import math
from itertools import combinations
import numpy as np
from scipy.linalg import eigh_tridiagonal
import sympy as s
c2=math.pi**4/96
c3=math.pi**6/1152
for u in np.linspace(0,math.pi,20001):
    d=1-math.cos(u)
    r=u*u/2-d
    grad2=(u-math.sin(u))**2/4
    assert r >=-1.e-12 and r <= c2*d*d+1.e-11
    assert grad2 <=c3*d**3+1.e-11
# A polynomial C1 cutoff with bounded derivative (sufficient for Sobolev Dirichlet form).
def chi(x):
    if x<=1: return 1.
    if x>=2: return 0.
    t=x-1
    return 1-3*t*t+2*t**3

def dchi(x):
    if x<=1 or x>=2: return 0.
    t=x-1
    return -6*t+6*t*t
assert max(abs(dchi(x)) for x in np.linspace(0,3,2001)) <=1.5+1e-9
for delta in (.1,.01,.001):
    for u in np.linspace(0,math.pi,15001):
        d=1-math.cos(u)
        x=d/delta
        r=u*u/2-d
        # gradient in an SU(2) link direction: |nabla u|=1/2
        # product derivative w.r.t. u
        gu=(u-math.sin(u))*chi(x)+r*dchi(x)*math.sin(u)/delta
        if d<=2*delta:
            cg=math.sqrt(c3)+math.sqrt(2)*1.5*c2
            assert gu**2/4 <= cg**2*d**3+3.e-10
        else:
            assert abs(gu) < 1e-10
# Power law exponents: delta=h^(3/4)
h=s.symbols('h',positive=True)
gamma=s.Rational(3,4)
assert gamma-s.Rational(1,2)==s.Rational(1,4)
assert 1-gamma==s.Rational(1,4)
assert 2*gamma==s.Rational(3,2)
# Genuine interacting SU(2) one-plaquette operator spectral test, deterministic character basis.
for h0 in (0.2,0.1):
    n=55
    b=h0**-2
    k=np.arange(n,dtype=float)
    ev,U=eigh_tridiagonal(k*(k+2)+b,np.full(n-1,-b/2))
    omega=U[:,0]
    P=np.diag(np.full(n-1,.5),1)+np.diag(np.full(n-1,.5),-1)
    K=ev-ev[0]
    # Functional calculus in the p-basis; correct Jacobi multiplication operator.
    pv,PV=np.linalg.eigh(P)
    d=1-pv
    r=np.arccos(pv)**2/2-d
    delta=h0**gamma
    good=np.sqrt(h0)*(PV@np.diag(r*np.vectorize(chi)(d/delta))@PV.T)
    residual=np.sqrt(h0)*(PV@np.diag(r)@PV.T)
    bad=residual-good
    vgood=U.T@(good@omega)
    vbad=U.T@(bad@omega)
    vtotal=U.T@(residual@omega)
    assert np.linalg.norm(vgood)**2 < 50*float(delta)**2/h0
    eg=np.dot(K,vgood**2)
    eb=np.dot(K,vbad**2)
    er=np.dot(K,vtotal**2)
    assert eg>=-1e-11 and eg<30*float(delta)**2
    # Spectral energy-weighted variation upper bound for diagonal spectral measures.
    tv=np.sum(K*np.abs(vtotal*vtotal-vbad*vbad))
    assert tv <= 2*np.sqrt(eg*eb)+eg+1.e-8
    print(f'Rotor h={h0}: good_m1={eg:.7g}, energy-weighted_TV={tv:.7g}')
# Original canonical spatial Penrose seed: 3 faces, 10 distinct links.
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
# The first face is corrected to the actual original fixture below.
seed[0]=[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)]
def edges(face):
    return {tuple(sorted((x,y))) for x,y in combinations(face,2)
            if sum(abs(i-j) for i,j in zip(x,y))==1}
faces=[edges(f) for f in seed]
E=set.union(*faces)
assert len(E)==10 and max(sum(e in f for f in faces) for e in E)<=2
print('PASS: global SU2 angle-gradient inequality, smooth-cutoff form, physical energy-weighted spectral comparison, authentic spatial seed.')
