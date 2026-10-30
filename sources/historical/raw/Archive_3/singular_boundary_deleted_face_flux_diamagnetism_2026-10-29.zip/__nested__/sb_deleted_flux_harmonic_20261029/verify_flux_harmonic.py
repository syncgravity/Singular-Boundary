#!/usr/bin/env python3
"""Exact mixed-link SU(2) harmonic flux barrier around a deleted face.

The 3x3 all-square disk is an explicit surrogate for testing nonabelian holonomy;
Penrose three-face Z^5 seed is checked separately (not a temporal Q14 fixture).
No stochastic simulations and no statement about the nonlinear ground state.
"""
from __future__ import annotations
from itertools import combinations
from math import cos, sin, pi, sqrt, exp, factorial
import numpy as np
from scipy.linalg import eigvalsh, expm
from scipy.special import iv
from scipy.integrate import quad


def flux_matrix(theta: float):
    n=3
    faces=[(i,j) for i in range(n) for j in range(n) if (i,j)!=(1,1)]
    edges=set()
    for i,j in faces+[(1,1)]:
        edges.update((('h',i,j),('v',i+1,j),('h',i,j+1),('v',i,j)))
    edges=sorted(edges); idx={e:k for k,e in enumerate(edges)}
    C=np.zeros((len(faces),len(edges)),dtype=complex)
    # Dirac string: change central plaquette holonomy and keep all eight others exactly flat
    U={('h',1,2):1, ('h',1,3):1}
    for fi,(i,j) in enumerate(faces):
        walk=[(('h',i,j),1),(('v',i+1,j),1),(('h',i,j+1),-1),(('v',i,j),-1)]
        prefix=0
        for e,sign in walk:
            power=U.get(e,0)
            transporter_power=prefix if sign==1 else prefix-power
            C[fi,idx[e]]=sign*np.exp(2j*theta*transporter_power)
            prefix+=sign*power
        assert prefix==0,(i,j,prefix)
    M=C@C.conj().T
    assert np.linalg.norm(M-M.conj().T)<1e-12
    return M,C,faces,edges


def trace_root(M):
    lam=eigvalsh(M)
    assert lam.min() >1e-10,lam.min()
    return np.sqrt(lam).sum()

M0,C0,faces,edges=flux_matrix(0)
assert len(faces)==8 and len(edges)==24
assert np.allclose(np.diag(M0),4)
assert np.count_nonzero(np.triu(abs(M0)>1e-12,1))==8
expected=np.sort([4-2*cos(2*pi*k/8) for k in range(8)])
assert np.allclose(eigvalsh(M0),expected,atol=1e-12)
print('3x3 punctured disk: 8 remaining faces, 24 links, dual cycle C8')
print('L0 eigenvalues:',np.round(expected,12))

flux_diff=[]
for theta in [0,pi/12,pi/6,pi/4,pi/2,3*pi/4,pi]:
    M,_,_,_=flux_matrix(theta)
    Lphi=np.array([[4 if i==j else -np.exp(1j*2*theta) if (i,j)==(0,7) else -np.exp(-1j*2*theta) if (i,j)==(7,0) else -1 if (j==(i+1)%8 or i==(j+1)%8) else 0 for j in range(8)] for i in range(8)],dtype=complex)
    # Same spectrum, up to gauge rephasing, as a single twisted edge of C8
    assert np.allclose(eigvalsh(M),eigvalsh(Lphi),atol=1e-10)
    delta3=2*(trace_root(M)-trace_root(M0))
    assert delta3>=-1e-11
    flux_diff.append((theta,delta3))
    print(f'theta={theta:.9f}, three-color sqrt-trace difference={delta3:.12f}')
assert flux_diff[4][1]>4e-5
assert abs(flux_diff[-1][1])<1e-9

# Analytic heat trace: n e^-4t * [I_0(2t)+2 sum_{m>=1} I_{m*n}(2t) cos(m*phi)]
for t in [0.1,0.5,1.0,2.0,4.0]:
    th=pi/3
    M,_,_,_=flux_matrix(th)
    direct=np.trace(expm(-t*M0)).real-np.trace(expm(-t*M)).real
    fourier=2*8*exp(-4*t)*sum(iv(8*m,2*t)*(1-cos(2*m*th)) for m in range(1,20))
    assert abs(direct-fourier)<1e-11,(t,direct,fourier)
    assert direct>=-1e-12
    print('heat check t',t,'difference',f'{direct:.12g}')

# The uniform winding-loop bound, with a_- = beta_- = 1, a_+ beta_+=1,
# Dmax=4, and length of a fixed once-winding directed cycle <=40.
# For the 8-ring, chosen t in [1,2] bound is positive and <= exact difference.
length=8
low_const=(2/sqrt(pi))*quad(lambda t: t**(length-1.5)*exp(-4*t),1,2,epsabs=1e-30)[0]/factorial(length)
assert low_const>0
assert flux_diff[4][1]>=low_const
print('explicit universal C8 sqrt-trace lower coefficient',f'{low_const:.12g}')

# Actual historic Z^5 three-rhombus Penrose spatial seed incidence only
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def cell_edges(f):
    return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
sets=[cell_edges(f) for f in seed]
assert len(set.union(*sets))==10
assert max(sum(e in f for f in sets) for e in set.union(*sets))==2
print('PASS: covariant linearization, dual C8 holonomy, exact heat trace, square root flux barrier, original Penrose spatial incidence')
