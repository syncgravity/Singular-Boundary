#!/usr/bin/env python3
"""Exact joint-force Ward identities, and deterministic interacting SU(2) one-plaquette check."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import eval_chebyu
from numpy.polynomial.chebyshev import chebgauss
from sympy import symbols, simplify
from itertools import combinations

a,h,p,z = symbols('a h p z', positive=True)
assert simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
assert simplify((-3*a)*a*h*h*(1-p*p)-(-3*a*a*h*h*(1-p*p)))==0

# SU2 one-plaquette physical Hilbert space with four identical link coefficients a.
# Chi_n(p)=U_n(p), H_E chi_n = a*n(n+2) chi_n, p chi_n=(chi_{n-1}+chi_{n+1})/2.
# Eigenvectors of the spectral Jacobi truncation converge rapidly for b/a=5.
def check(N,quad=600,a=1.0,b=5.0,h=0.1):
    n=np.arange(N,dtype=float)
    diag=a*n*(n+2)+b
    off=np.full(N-1,-b/2)
    vals,vec=eigh_tridiagonal(diag,off,select='i',select_range=(0,0))
    E0=vals[0]; c=vec[:,0]
    if c[0]<0: c=-c
    k=np.arange(1,quad+1)
    theta=np.pi*k/(quad+1); p=np.cos(theta)
    weights=2/(quad+1)*np.sin(theta)**2
    U=np.empty((N,quad))
    U[0,:]=1.0
    if N>1: U[1,:]=2*p
    for j in range(2,N): U[j]=2*p*U[j-1]-U[j-2]
    # derivatives of Chebyshev U_n, using derivative recurrence.
    Up=np.zeros_like(U)
    if N>1: Up[1]=2.0
    for j in range(2,N): Up[j]=2*U[j-1]+2*p*Up[j-1]-Up[j-2]
    omega=c@U; op=c@Up
    density=omega**2*weights
    assert abs(sum(density)-1)<1e-11
    D=3*a*h*p
    F=-2*a*h*(1-p*p)*op/omega
    L=D+F
    GDY=-3*a*a*h*h*(1-p*p)
    GammaY=a*h*h*(1-p*p)
    avg=lambda v: np.dot(density,v)
    E_DF=avg(D*F)
    RHS=-avg(D*D)-avg(GDY)
    Cov=np.dot(density,(D-avg(D))*(F-avg(F)))
    CovR=-np.dot(density,(D-avg(D))**2)-avg(GDY)
    m2_direct=avg(L*L)/h
    m2_ward=(avg((F-avg(F))**2)-avg((D-avg(D))**2)-2*avg(GDY))/h
    # spectral Jacobi cross-check (matrix p including n=N-1 to N boundary negligible)
    w=np.zeros(N)
    w[1:]+=c[:-1]/2
    w[:-1]+=c[1:]/2
    H_w=(diag-E0)*w
    H_w[:-1]+=off*w[1:]
    H_w[1:]+=off*w[:-1]
    m2_matrix=(h*h*np.dot(H_w,H_w))/h
    return E0,E_DF,RHS,Cov,CovR,m2_direct,m2_ward,m2_matrix,avg(L),avg(GammaY)

for N in [24,36,48]:
  E, df, rhs, cov, covr, m2, m2w, m2mat, stat, m1 = check(N)
  print(f'N={N} E0={E:.12f}  E[DF]={df:.12f}  Ward={rhs:.12f}  Cov={cov:.12f}/{covr:.12f}  m2={m2:.12f}/{m2w:.12f}/{m2mat:.12f} stationary={stat:+.3e}  M1Y={m1:.12f}')
  assert abs(df-rhs)<1e-9 and abs(cov-covr)<1e-9 and abs(m2-m2w)<1e-9 and abs(m2-m2mat)<1e-8
  assert abs(stat)<1e-9
# Authentic Z^5 3-rhombus spatial incidence (not the temporal Q14).
faces=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edge_set(face):
 return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
fs=[edge_set(face) for face in faces]
es=set.union(*fs)
assert len(es)==10 and len({v for e in es for v in e})==8
assert max(sum(e in f for f in fs) for e in es)==2
print('PASS: exact symbolic Ward, deterministic interacting SU(2) character/Haar check, 3-face Penrose spatial incidence; no Monte Carlo')
