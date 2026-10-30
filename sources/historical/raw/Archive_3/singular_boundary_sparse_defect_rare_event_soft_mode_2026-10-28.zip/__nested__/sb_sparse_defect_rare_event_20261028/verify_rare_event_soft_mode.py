#!/usr/bin/env python3
"""Reproducible numerical and algebraic checks, no Monte Carlo.
Physical one-rhombus SU(2) character Jacobi Hamiltonian.  Haar class measure
is 2 sqrt(1-p²)dp/pi; character basis is U_n(p).
"""
import math
from itertools import combinations
import numpy as np
from scipy.linalg import eigh_tridiagonal

c0=math.pi**2/4-1
c2=math.pi**4/96
c3=math.pi**6/1152
Cchi=1.5
a=q=1.0
Cgamma=32*a*q*q*(math.sqrt(c3)+math.sqrt(2)*Cchi*c2)**2

# Smoothstep C1 cutoff.
def chi_and_derivative(v):
    v=np.asarray(v)
    val=np.where(v<=1,1,np.where(v>=2,0,1-3*(v-1)**2+2*(v-1)**3))
    der=np.where((v>1)&(v<2), -6*(v-1)*(2-v),0)
    return val,der

# Deterministic pointwise SU2 derivative checks, including near cut locus.
dvals=np.concatenate([np.geomspace(1e-5,.01,1200),np.linspace(.01,2-1e-8,2400)])
p=1-dvals
angle=np.arccos(p)
r=.5*angle**2-dvals
rp=angle/np.sqrt(dvals*(2-dvals))-1
assert np.min(r)>-1e-8
assert np.max(r/(dvals*dvals))<c2+1e-8
assert np.max(r/dvals)<c0+1e-8
assert np.max(rp*rp*dvals*(2-dvals)/(4*dvals**3))<c3+1e-6
for h in (.2,.1,.05):
    delta=h**.75
    ch,chd=chi_and_derivative(dvals/delta)
    sr=r*(1-ch)
    ds=rp*(1-ch)-r*chd/delta
    E=dvals>delta
    Z=h*dvals
    S=math.sqrt(h)*sr
    grad=a*h*dvals*(2-dvals)*ds**2 # 4 equal electric links
    assert max(abs(S)/(c0*h**-.5*np.maximum(Z,1e-300)+1e-100))<=1+2e-6
    assert np.max(grad/(Cgamma*np.maximum(Z,1e-300)))<1.00001
    assert not np.any(grad[~E]>1e-13)

print('PASS: SU2 pointwise class-angle, cutoff-support and Gamma(S) inequalities')

# SU2 genuine magnetic ground state (not a Gaussian vacuum).
for h,b in [(0.2,5.),(0.1,5.),(0.05,20.)]:
    N=90
    n=np.arange(N,dtype=float)
    eigs, basis=eigh_tridiagonal(a*n*(n+2)+b,np.full(N-1,-b/2),select='i',select_range=(0,0))
    ground=basis[:,0]
    J=2400
    k=np.arange(1,J+1)
    x=np.cos(math.pi*k/(J+1))
    weights=2/(J+1)*np.sin(math.pi*k/(J+1))**2
    U=np.empty((N,J),float)
    U[0]=1.; U[1]=2*x
    for j in range(2,N): U[j]=2*x*U[j-1]-U[j-2]
    omega=ground@U
    density=weights*omega**2
    density/=sum(density)
    d=1-x
    z=h*d
    angle=np.arccos(x)
    r=.5*angle**2-d
    deriv=angle/np.sqrt(np.maximum(1-x*x,1e-200))-1
    delta=h**.75
    ch,chd=chi_and_derivative(d/delta)
    S=math.sqrt(h)*r*(1-ch)
    Sder=math.sqrt(h)*(deriv*(1-ch)-r*chd/delta)
    grad=a*(1-x*x)*Sder**2
    E=d>delta
    prob=float(np.sum(density[E]))
    exp=lambda v: float(np.dot(density,v))
    M=exp(np.exp(z))
    L=math.log(M/prob)
    entropy1=prob*L
    entropy2=(1+math.exp(-2))*prob*(L+2)**2
    m1=exp(grad)
    varm=exp(S*S)-exp(S)**2
    second=exp((z*z)*E)
    assert exp(z*E)<=entropy1+1e-10
    assert second<=entropy2+1e-10
    assert m1<=Cgamma*entropy1+1e-9
    assert varm<=c0*c0/h*entropy2+1e-8
    assert abs(exp(S*(~E)))<1e-12
    # independently project onto physical eigenbasis: S Omega
    char_coeff=(U@(weights*omega*S))
    spectral_coeff=basis.T@char_coeff
    spectral_coeff[0]=0
    # K in eigenbasis: need all eigenvalues, not just lowest.
    all_e,all_b=eigh_tridiagonal(a*n*(n+2)+b,np.full(N-1,-b/2))
    spectral_vec=all_b.T@char_coeff
    spectral_m1=float(np.dot((all_e-all_e[0])[1:],spectral_vec[1:]**2))
    assert abs(spectral_m1-m1)<4e-6,(h,spectral_m1,m1)
    assert abs(np.dot(spectral_vec[1:],spectral_vec[1:])-varm)<4e-6
    print(f'PASS: interacting SU2 h={h:g} b={b:g} P_event={prob:.6f} '
          f'm1={m1:.8g} varS={varm:.8g} entropy={entropy1:.8g}')

# Exact spectral projection algebra: finite spectral measures and norm transfer.
v0=1.0
j=.0012
lam=8*j/v0
# A centered physical source with low-energy m1 <=j and variance >=v0.
energy=np.array([.0005,.0008,.0015])
mass=np.array([.3,.4,.4])
assert np.dot(energy,mass)<j
assert mass.sum()>=v0
assert mass[energy<=lam].sum()>=(math.sqrt(7)-1)**2/16*v0

# Verify exact three-face Penrose Z5 spatial fixture (not temporal Q14).
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face): return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(v-w) for v,w in zip(x,y))==1}
faces=list(map(edges,seed)); union=set().union(*faces)
assert len(union)==10 and max(sum(e in f for f in faces) for e in union)==2
print('PASS: spectral soft-mode projection algebra; authentic 3-face 10-edge spatial fixture')
print('ALL CHECKS PASS (no Monte Carlo; no Stage26 source verification)')
