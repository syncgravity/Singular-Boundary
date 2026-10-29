#!/usr/bin/env python3
"""SU2 deleted-orbit radial Fisher data processing: exact Haar witness and cap tests."""
import math
import numpy as np
from scipy.special import roots_jacobi
from scipy.integrate import quad
for n in (18,40,80):
    x,w=roots_jacobi(n,.5,.5)
    w=2*w/math.pi
    assert abs(sum(w)-1)<2e-14
    assert abs(np.dot(w,x))<2e-14
    assert abs(np.dot(w,x*x)-.25)<2e-14
    eps=.5
    Z=1+eps*eps/4
    assert abs(np.dot(w,(1+eps*x)**2)/Z-1)<1e-13
    eta2=eps*eps/(4+eps*eps)
    Jorb=3*eps*eps/(4*(4+eps*eps))
    assert abs(eta2-4*Jorb/3)<1e-15
    assert abs(eta2-1/17)<1e-15
    assert abs(Jorb-3/68)<1e-15
    Jrad=np.dot(w,(1-x*x)/4*(eps/math.sqrt(Z))**2)
    assert abs(Jrad-Jorb)<1e-14
for h in (.2,.05,.01,.001):
    cap=(math.acos(1-h)-(1-h)*math.sqrt(2*h-h*h))/math.pi
    exact=quad(lambda p:2/math.pi*math.sqrt(max(0,1-p*p)),1-h,1,epsabs=1e-14)[0]
    assert abs(cap-exact)<1e-11
print("PASS SU2 Haar character moments, gauge-invariant positive two-face witness, radial Fisher sharpness, center cap")
print("No Monte Carlo; no nonlinear Penrose vacuum inference.")
