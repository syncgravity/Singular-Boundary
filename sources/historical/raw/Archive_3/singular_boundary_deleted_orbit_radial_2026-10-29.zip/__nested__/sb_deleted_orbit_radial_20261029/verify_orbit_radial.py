#!/usr/bin/env python3
"""Deterministic SU(2) Haar and radial orbital Fisher checks. No Monte Carlo."""
import math
import numpy as np
from scipy.special import roots_jacobi
from scipy.integrate import quad
# SU2 p density (2/pi)*sqrt(1-p*p); Jacobi alpha=beta=1/2 quadrature.
for n in (18,40,80):
    x, w = roots_jacobi(n, 0.5, 0.5)
    w = (2/math.pi) * w
    assert abs(sum(w)-1) < 2e-14
    assert abs(np.dot(w,x)) < 2e-14
    assert abs(np.dot(w,x*x)-.25)<2e-14
    eps=0.5
    Z=1+eps*eps/4
    # Normalized positive SU2 diagonal-conjugation invariant two-face state
    # psi(U,V)=(1+eps*p(U V^-1))/sqrt(Z).
    assert 1-eps>0
    norm=np.dot(w,(1+eps*x)**2)/Z
    assert abs(norm-1)<1e-13
    eta2=eps*eps/(4+eps*eps)
    orbit_j=3*eps*eps/(4*(4+eps*eps))
    assert abs(eta2-4*orbit_j/3)<1e-15
    assert abs(eta2-1/17)<1e-15
    assert abs(orbit_j-3/68)<1e-15
    # Radial class state Omega(p)=const*(1+eps*p) saturates contraction
    denom=Z
    fisher=np.dot(w,(1-x*x)/4*(eps/math.sqrt(denom))**2)
    assert abs(fisher-orbit_j)<1e-14
    # Witness above has exactly constant marginal and radial Fisher zero.
for h in (0.2,0.05,0.01,0.001):
    cap=(math.acos(1-h)-(1-h)*math.sqrt(2*h-h*h))/math.pi
    cap_integral=quad(lambda p:2/math.pi*math.sqrt(max(0,1-p*p)),1-h,1,epsabs=1e-14)[0]
    assert abs(cap-cap_integral)<1e-11
    print('h',h,'Haar cap',cap,'ratio to h^3/2',cap/h**1.5)
# Symbolic exponent logic and annular band: threshold Jorb=o(h^1/2).
for h in (.2,.1,.05,.02):
    sample_jorb=h
    c_h=(math.acos(1-h)-(1-h)*math.sqrt(2*h-h*h))/math.pi
    assert (sample_jorb**0.5)*c_h**(-1/6) <= 2*h**.25
print('PASS normalized strictly positive SU2 witness, radial contraction, Haar cap and O(h^1/2) threshold')
