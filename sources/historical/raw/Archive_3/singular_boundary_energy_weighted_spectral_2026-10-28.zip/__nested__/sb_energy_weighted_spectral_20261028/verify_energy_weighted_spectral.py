#!/usr/bin/env python3
"""Exact rational and deterministic Hermitian matrix checks for EW-1..EW-10.

These are certificate/regression checks, not a proof of a Yang--Mills mass gap.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp
import numpy as np

# Abstract positive physical spectral laws with m1=1, m3 <= h^-2.
for h in [F(1,2), F(1,5), F(1,10)]:
    laws = {
        'finite': [(F(1), F(1))],
        'uv': [(F(1)/h, h)],
        'soft': [(h, F(1)/h)],
    }
    for name, law in laws.items():
        variance = sum(w for E, w in law)
        m1 = sum(E*w for E, w in law)
        m2 = sum(E*E*w for E, w in law)
        m3 = sum(E**3*w for E, w in law)
        assert m1 == 1 and m3 <= h**-2
        assert variance*m2 >= m1**2
        assert sum((h*E)**2 * E*w for E, w in law) == h*h*m3
        assert sum(E*w/(h*E) for E, w in law) == variance/h
        if name == 'finite':
            assert variance == 1 and (h*law[0][0]) == h
        elif name == 'uv':
            assert variance == h and (h*law[0][0]) == 1
            eps, R, c, K = F(1,4), F(2), F(1), F(1)
            band_sigma = sum(E*w for E, w in law if eps <= h*E <= R)
            band_mu = sum(w for E, w in law if eps <= h*E <= R)
            assert band_sigma >= c/2 and band_mu >= c*h/(2*R)
        else:
            assert variance == 1/h and h*law[0][0] == h*h

# Finite-dimensional noncommuting two-source physical spectral Gram measure.
h = F(1,5)
energies = [F(2), F(5)]
coeff = [[F(1), F(2)], [F(3), -F(1)]]  # mode x source
sigmas = [sp.Matrix([[energies[k]*coeff[k][i]*coeff[k][j] for j in range(2)] for i in range(2)]) for k in range(2)]
assert all(sigma.is_positive_semidefinite for sigma in sigmas)
M = sum(sigmas, sp.zeros(2))
C1 = [M[i,i] for i in range(2)]
C3 = [sum((h*energies[k])**2*sigmas[k][i,i] for k in range(2)) for i in range(2)]
assert all(C1[i] > 0 and C3[i]>0 for i in range(2))
assert all(sum((h*energies[k])**2 * sigmas[k][i,i] for k in range(2)) == C3[i] for i in range(2))

# Explicit nonnegative Gram/OS reflection positivity at two positive time arguments.
for t in [(0.0,0.75),(0.2,1.7)]:
    K = np.block([[sum(float(sigmas[k][i,j])*np.exp(-float(h*energies[k])*(t[a]+t[b])) for k in range(2)) for j in range(2) for b in range(2)] for i in range(2) for a in range(2)])
    # Ordering (a,i) in rows and (b,j) in columns, equivalent positive Gram form.
    G = np.zeros((4,4))
    for a in range(2):
        for i in range(2):
            for b in range(2):
                for j in range(2):
                    G[2*a+i,2*b+j]=sum(float(sigmas[k][i,j])*np.exp(-float(h*energies[k])*(t[a]+t[b])) for k in range(2))
    assert np.linalg.eigvalsh(G).min() > -1e-10

# Original canonical 3-rhombus Z^5 spatial incidence, not temporal Q14.
seed = [
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def edges(face):
    return {tuple(sorted((v,w))) for v,w in combinations(face,2) if sum(abs(x-y) for x,y in zip(v,w)) == 1}
face_edges = [edges(face) for face in seed]
assert len(set.union(*face_edges)) == 10
assert max(sum(e in fe for fe in face_edges) for e in set.union(*face_edges)) == 2
print('PASS: exact three spectral trichotomy witnesses; EW inverse moment and UV band; matrix Gram reflection positivity; 3-face spatial fixture')
print('LIMIT: pure spectral certificates do NOT establish actual Penrose vacuum variance or mass gap')
