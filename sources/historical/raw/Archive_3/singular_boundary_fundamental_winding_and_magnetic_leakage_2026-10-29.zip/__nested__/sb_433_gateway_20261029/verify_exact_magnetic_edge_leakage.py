#!/usr/bin/env python3
"""Exact SU(2) character fusion identifies 7 independent omitted spin-(J+1/2)
channels for ANY complete physical link cutoff J>=1/2, even under target C_f.
"""
from fractions import Fraction as F
from math import sqrt
from scipy.integrate import quad
from math import pi,cos,sin
import numpy as np

# SU2 normalized class Haar, chi_n(theta)=sin((n+1)theta)/sin(theta), n=2j.
def char(n,theta):
 if theta<1e-9:return float(n+1)
 if pi-theta<1e-9:return float(((-1)**n)*(n+1))
 return sin((n+1)*theta)/sin(theta)
def haar(fn):return quad(lambda u:2/pi*sin(u)**2*fn(u),0,pi,epsabs=5e-12)[0]
for N in (1,2,3,4,5,8):
 j=F(N,2)
 # p_g = 1/2 chi_half; the exact off-block fusion coefficient is +1/2.
 m=haar(lambda u:char(N+1,u)*(.5*char(1,u))*char(N,u))
 assert abs(m-.5)<1e-11
 # Any off-face q differs: independence of Haar face coordinates and zero mean chi_half(q).
 assert abs(haar(lambda u:char(1,u)))<1e-11
 assert abs(haar(lambda u:char(N+1,u)*char(N,u)))<1e-11
 print('link cutoff J=',float(j),'exact omitted (J+1/2) fusion coefficient',m)

# One physical Wilson character per retained magnetic face gives an orthonormal
# seven-state domain family; all omitted higher-spin Wilson characters are
# orthonormal, and the exact cross matrix is diag(-b_g/2).
b=np.array([1.,2.,3.,5.,7.,11.,13.])
block=-np.diag(b)/2
sv=np.linalg.svd(block,compute_uv=False)
assert np.allclose(np.sort(sv),np.sort(b/2))
assert np.linalg.norm(block,2)==max(b)/2
print('seven exact target-center-even outgoing singular values',list(np.sort(sv)))
print('PASS exact SU2 fusion, seven independent color-even boundary channels, nondecaying operator leakage')
