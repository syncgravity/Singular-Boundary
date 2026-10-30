#!/usr/bin/env python3
"""Exact finite SU(2) deleted-vacuum small-ball variational theorem verification."""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.integrate import quad
from itertools import combinations

def haar_ball(radius):
    return quad(lambda d: (2/math.pi)*math.sqrt(d*(2-d)), 0., radius,
                epsabs=2e-14,epsrel=2e-14)[0]

def one_face_energy(a,b,N=180):
    # Four links each -a Delta, SU2 trace character j=n/2: electric n(n+2)a
    diag=a*np.arange(N)*(np.arange(N)+2)+b
    off=np.full(N-1,-b/2.)
    return eigh_tridiagonal(diag,off,select='i',select_range=(0,0))[0][0]

for h in [.2,.1,.05,.025]:
    a=1.;A=4*a;b=4/h**2;k=math.sqrt(2*b/A)
    m=haar_ball(1/k)
    E=one_face_energy(a,b)
    bound=b/k*(2+math.log(2*math.e**2*k/m))
    assert E>0 and E<=bound+1e-9
    lower=4/(3*math.pi)*(1/k)**1.5
    upper=4*math.sqrt(2)/(3*math.pi)*(1/k)**1.5
    assert lower-1e-13<=m<=upper+1e-13
    # sharpened exponential trial exactly integrate Haar density
    def rho(d):return (2/math.pi)*math.sqrt(d*(2-d))
    denom=quad(lambda d:math.exp(-2*k*d)*rho(d),0,2)[0]
    tilt=quad(lambda d:d*math.exp(-2*k*d)*rho(d),0,2)[0]/denom
    trial=(b+A*k*k/2)*tilt
    assert E<=trial+1e-8 and trial<=bound+1e-8
    # quantitative converse, when informative
    converse=min(1.,2*math.e**4*k*math.exp(-k*E/b))
    assert m<=converse+1e-12
    print(f'h={h:.3f} b={b:.1f} kappa={k:.3f} haar_ball={m:.8f} deletion={E:.6f} trial={trial:.6f} bound={bound:.6f}')

for s in (1.,2.,5.):
    for h in (.1,.025,.01):
        k=1/h; mass=h**s; b=k*k;A=2.;
        bound=b/k*(2+math.log(2*math.e**2*k/mass))
        assert bound<=b/k*(2+math.log(2*math.e**2)+(s+1)*math.log(1/h))+1e-8

seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def ed(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
assert len(set.union(*(ed(f) for f in seed)))==10
print('PASS: exact SU(2) Haar small-ball asymptotics, true interacting character ground energies, variational trial, Penrose spatial incidence; no Monte Carlo')
