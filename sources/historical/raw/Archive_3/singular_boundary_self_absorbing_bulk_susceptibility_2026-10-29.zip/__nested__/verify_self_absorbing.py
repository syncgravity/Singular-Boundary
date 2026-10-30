#!/usr/bin/env python3
"""Deterministic proof checks for SU2 coupling-integrated f-sum and cutoff.

The SU2 one-face character-basis calculation checks the f-sum and
Hellmann-Feynman integration. It is NOT a simulation of a growing Penrose vacuum.
"""
import math
from itertools import combinations
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal
from numpy.polynomial.legendre import leggauss

# 1. SU2 class geometry and exact cutoff exponent
p, A, b, h, m, L = sp.symbols('p A b h m L', positive=True)
d = 1-p
assert sp.simplify(1-p*p - (2*d - d*d)) == 0
assert sp.simplify(A/4*(2*d-d*d) - A/4*(1-p*p)) == 0
lam = L*h**(-sp.Rational(5,4))*m**sp.Rational(1,4)
assert sp.simplify((h**-6*m)/lam**4 - h**-1/L**4) == 0
# One-face exact coefficient; general many-face Cauchy has twice this constant.
af, ag, bf, bg = sp.symbols('af ag bf bg', positive=True)
ct = bg*sp.sqrt(af*ag*bf/2)/lam**2
assert sp.simplify(ct**2 - af*ag*bf*bg**2/(2*lam**4)) == 0
# Sharp quadratic root after maximum/Young absorption
bb, nn, cc = sp.symbols('bb nn cc', nonnegative=True)
root = (cc+sp.sqrt(cc**2+4*(bb+nn)))/2
assert sp.simplify(root**2-(bb+nn+cc*root)) == 0
for x in (0,.2,3.,100.):
    for v in (0.2,1.,5.):
        for w in (.1,1.,7.):
            if x <= v+w*math.sqrt(x):
                assert x <= 2*v+w*w+1e-10
# 2. Original 3-face Z5 Penrose spatial incidence
seed = [
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def edge(a,b): return tuple(sorted([a,b]))
def face_edges(face):
    return {edge(a,b) for a,b in combinations(face,2) if sum(abs(x-y) for x,y in zip(a,b)) == 1}
face_sets = list(map(face_edges, seed))
union = set.union(*face_sets)
assert len(union) == 10
assert max(sum(ed in faces for faces in face_sets) for ed in union) <= 2
# Select an adjacent magnetic neighbor on every interior face (a complete square grid fixture).
def grid_faces(n):
    out = []
    for i in range(n):
        for j in range(n):
            out.append({edge((i,j),(i+1,j)),edge((i+1,j),(i+1,j+1)),
                        edge((i+1,j+1),(i,j+1)),edge((i,j+1),(i,j))})
    return out
for n in (3,5,10):
    fs=grid_faces(n)
    for k,f in enumerate(fs):
        shared = [g for g in range(len(fs)) if g!=k and len(f&fs[g])==1]
        if len(shared)==4:
            g=shared[0]
            assert any(sum(e in ff for j,ff in enumerate(fs) if j!=g)==1 for e in f)
            # With g deleted, target has a private magnetic edge.
# 3. Genuine interacting SU2 one-face ground state and integrated f-sum
n_char=100
a=1.
J=np.arange(n_char,dtype=float)
P=np.diag(np.full(n_char-1,.5),1)+np.diag(np.full(n_char-1,.5),-1)
dmat=np.eye(n_char)-P
xg,wg=leggauss(55)

def ground(coupling):
    ev,V=eigh_tridiagonal(a*J*(J+2)+coupling,np.full(n_char-1,-coupling/2),select='i',select_range=(0,0))
    return ev[0],V[:,0]

for mag in (4.,25.,100.):
    energy,omega=ground(mag)
    exact_m1=float((dmat@omega)@((np.diag(a*J*(J+2)+mag)-mag*P)-energy*np.eye(n_char))@(dmat@omega))
    direct_m1=a*(1-float(omega@P@P@omega))
    assert abs(exact_m1-direct_m1)<2e-9,(mag,exact_m1,direct_m1)
    integrated_deficit=0.
    integrated_fsum=0.
    for xx,ww in zip(xg,wg):
        t=mag*(xx+1)/2
        en,ps=ground(t)
        integrated_deficit+=ww*(float(ps@dmat@ps))*mag/2
        integrated_fsum+=ww*(a*(1-float(ps@P@P@ps)))*mag/2
    assert abs(integrated_deficit-energy)<2e-8,(mag,energy,integrated_deficit)
    assert integrated_fsum <= 2*a*integrated_deficit+1e-9
    print(f'Nonlinear SU2 one-face b={mag:.0f}:  ΔE={energy:.9f}, ∫m1={integrated_fsum:.9f}, (A/2)ΔE={2*a*energy:.9f}')
# 4. Asymptotic cutoff comparison
for smallh in (.2,.1,.05,.025):
    ab_max=2.;betamax=4.;nn=1
    lam=float(smallh**(-1.25))
    err=(4*ab_max)**2*(betamax*smallh**-2)**3/(2*lam**4)
    assert abs(err*smallh - 8*ab_max**2*betamax**3) <1e-8
    print(f'h={smallh:.3f}, single-neighbor cutoff={lam:.4g}, UV absorption h×bound={err*smallh:.3f}')
print('PASS exact SU2 fsum, integrated source moment, single-neighbor graph, spectral cutoff algebra; no Monte Carlo')
