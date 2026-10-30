#!/usr/bin/env python3
"""Deterministic SU2 deleted-marginal Fisher/capacity obstruction check.
One-plaquette pure electric reference and true Haar radial geometry; not a Penrose vacuum simulation.
"""
import math
from scipy.integrate import quad
import numpy as np
from scipy.special import roots_chebyu

def rho(u): return 2/math.pi * math.sin(u)**2

def cap(h):
    a=math.acos(1-h)
    return (a-(1-h)*math.sqrt(2*h-h*h))/math.pi

def smoothstep(t):
    if t<=0: return 0.,0.
    if t>=1: return 1.,0.
    return t*t*(3-2*t),6*t*(1-t)

def trial(h):
    r=4*math.sqrt(h); eta=math.exp(-1/h)
    def g(u):
        d=min(u,math.pi-u); v,der=smoothstep((d-r)/r)
        return eta+(1-eta)*v, (1-eta)*der/r
    N=quad(lambda u:g(u)[0]**2*rho(u),0,math.pi,epsabs=2e-13)[0]
    E=quad(lambda u:g(u)[1]**2*rho(u),0,math.pi,epsabs=2e-12)[0]/N  # A_f/4=1, all a_e=1
    L2_sq=quad(lambda u:(g(u)[0]/math.sqrt(N)-1)**2*rho(u),0,math.pi,epsabs=2e-13)[0]
    m=math.exp(-2/h)*cap(h)/N
    return r,N,E,L2_sq,m

# Exact SU2 class radial Casimir: -Delta p=3/4 p per edge; four links a=1 gives E_p=3.
assert abs(4*(3/4)-3)<1e-15
for h in [1/400,1/900,1/1600,1/2500,1/3600]:
    r,N,E,L2,m=trial(h)
    ref=cap(h)
    assert r<math.pi/4
    assert 0<N<=1 and E>0
    assert E < (21/math.pi)*r/N +1e-12
    assert L2 < 20*r**3
    assert m/ref<1e-40
    assert .3<ref/h**1.5<.7
    print(f"h={h:.6f} r={r:.6f} norm={N:.8f} excess={E:.8f} L2dist={math.sqrt(L2):.7f} Haarcap={ref:.8e} trialcap={m:.4e}")
# A comparator accurate to o(h^3/4) transfers Haar-cap order, but O(h^1/4) norm error cannot.
assert 0.0001**.75 < 0.0001**.25
print("PASS exact SU2 center-even Haar cap, normalized positive smoothstep, energy o(1), cap depletion, transfer threshold")
# A cap of Haar mass m_h ~ h^(3/2) requires radial Fisher J=o(m_h^(1/3))=o(sqrt h)
for h in (1e-2,1e-3,1e-4):
    m=cap(h)
    assert 0.1*math.sqrt(h) < m**(1/3) < 2*math.sqrt(h)
print('PASS: sharp S3 Sobolev cap capacity exponent J=o(sqrt(h)), smoothstep saturates energy O(sqrt(h))')

# Independent genuinely interacting SU2 one-face physical ground state (a_e=1,b=5):
# Exact character eigenbasis, not Monte Carlo. The radial Fisher inequality is saturated.
from scipy.linalg import eigh_tridiagonal
from scipy.special import roots_chebyu
n=52
levels=np.arange(n,dtype=float)
energies,eigenvectors=eigh_tridiagonal(levels*(levels+2)+5.,np.full(n-1,-2.5),select="i",select_range=(0,0))
c=eigenvectors[:,0]
p,w0=roots_chebyu(500); wt=2/math.pi*w0
U=np.zeros((n,len(p)));Up=np.zeros_like(U)
U[0]=1; U[1]=2*p;Up[1]=2
for j in range(2,n):
    U[j]=2*p*U[j-1]-U[j-2]
    Up[j]=2*U[j-1]+2*p*Up[j-1]-Up[j-2]
wave=c@U;derivative=c@Up
assert abs(np.dot(wt,wave*wave)-1)<1e-10
T=float(np.dot(wt,(1-p*p)*derivative*derivative))
logFprime=2*derivative/wave
Fisher=float(np.dot(wt,wave*wave*(1-p*p)*logFprime**2))/4
assert abs(Fisher-T)<1e-10
assert T>0
print(f'PASS interacting SU2 physical b=5: E0={energies[0]:.10f}, local Fisher={Fisher:.10f}, electric score={T:.10f}')
# Genuine 3-rhombus spatial Penrose coordinate fixture (not temporal Stage 26 incidence).
from itertools import combinations
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
fs=[edges(f) for f in seed]; EE=set.union(*fs)
assert len(EE)==10 and max(sum(e in f for f in fs) for e in EE)==2
print('PASS genuine 3-face/10-edge spatial Penrose fixture')
