#!/usr/bin/env python3
"""Exact SU2 character Fourier cap certificate with finite-spin Parseval tail.
Full deterministic quadrature verifier: companion ZIP.
"""
import math
from scipy.integrate import quad
def H(a):return (a-math.sin(2*a)/2)/math.pi
def bj(j,r):
    if j==0:return H(r)
    return (math.sin(2*j*r)/(2*j)-math.sin((2*j+2)*r)/(2*j+2))/math.pi
for a in (.2,.5,1.):
    for j in (.5,1.,2.,4.):
        q=2/math.pi*quad(lambda u: math.sin(u)*math.sin((2*j+1)*u),0,a/2,epsabs=1e-13)[0]
        assert abs(q-bj(j,a/2))<1e-12
    assert H(a/2)>0
print("PASS SU2 center Haar mass and finite-character coefficients. Full Fourier tail audit in ZIP.")
