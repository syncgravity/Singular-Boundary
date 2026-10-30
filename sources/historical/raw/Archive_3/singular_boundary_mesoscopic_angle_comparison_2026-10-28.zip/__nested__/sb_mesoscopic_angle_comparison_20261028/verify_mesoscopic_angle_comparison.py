#!/usr/bin/env python3
"""Deterministic exact SU2 angle identities and interacting spectral-band certificate."""
import math
from itertools import combinations
import numpy as np
import sympy as s
from scipy.linalg import eigh_tridiagonal

pi=math.pi
c=pi*pi/4-1
assert c>0
for x in np.linspace(0,pi,10001):
    d=1-math.cos(float(x));q=float(x*x/2);r=q-d
    assert r >= -1e-11
    assert r <= c*d+1e-11
    assert r <= pi**4/96*d*d+1e-11
# Analytic power and coefficient identities (r<=c*d and d^2<=2d).
h,R,eta,beta,cf,ce=s.symbols('h R eta beta cf ce',positive=True)
upper=s.factor((2*c**2/beta)*(cf*R**2/h**2)*h**3*(ce*(R**2+R)/h**3+eta))
target=(2*c**2*cf/beta)*(ce*(R**4+R**3)/h**2+eta*R**2*h)
assert s.simplify(upper-target)==0
print('Analytic prefactor check: PASSED')
# Genuine finite SU2 one-plaquette physical Hamiltonian; χ_n(p)=U_n(p).
for h0 in [0.2,0.1,0.05]:
    b=1/h0**2
    nmax=70
    en,vecs=eigh_tridiagonal(np.arange(nmax)*(np.arange(nmax)+2)+b,np.full(nmax-1,-b/2))
    E0=float(en[0]); eta0= float(en[2]-E0) + 1e-8
    P=vecs[:,:3]
    num=2001
    idx=np.arange(1,num+1)
    x=np.cos(np.pi*idx/(num+1))
    w=2/(num+1)*np.sin(np.pi*idx/(num+1))**2
    U=np.zeros((nmax,num));U[0]=1.;U[1]=2*x
    for j in range(2,nmax): U[j]=2*x*U[j-1]-U[j-2]
    v= U.T@P
    r= (np.arccos(x)**2/2)-(1-x)
    # || delta B P ||^2 = maximal eigenvalue of P* multiplication (h r^2) P.
    obs=(v.T * (w*h0*r*r)) @v
    norm2=float(np.linalg.eigvalsh(obs)[-1])
    # one face, exterior removed, H_out=0 => Delta_D=E0
    bound=2*c*c*h0**3*(E0+eta0)
    assert norm2 <= bound+1e-9,(h0,norm2,bound)
    print(f'nonlinear SU2: h={h0:g}, ||ΔB P||²={norm2:.8f}, bound={bound:.8f}, ratio={norm2/bound:.6f}')
# Authentic 3-face 10-edge Z^5 spatial seed; not Stage26 temporal data.
faces=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,0,-1,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)] ]
# The first face above must match the canonical coordinate list (repair third vertex below).
faces[0]=[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)]
def edge(a,b):return tuple(sorted((a,b)))
def edges(f):return {edge(a,b) for a,b in combinations(f,2) if sum(abs(i-j) for i,j in zip(a,b))==1}
facets=[edges(f) for f in faces]; ee=set.union(*facets)
assert len(ee)==10 and max(sum(e in f for f in facets) for e in ee)==2
print('PASS: global angle bounds, nonlinear gauge-invariant spectral projection, original three-face spatial incidence')
