#!/usr/bin/env python3
"""Center-even Haar witness and independent-portal response checks; not a Penrose simulation."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
pi=math.pi
def haar(fn):return quad(lambda u:2/pi*math.sin(u)**2*fn(u),0,pi,epsabs=1e-12)[0]
p2=haar(lambda u:math.cos(u)**2);p4=haar(lambda u:math.cos(u)**4)
assert abs(p2-.25)<1e-12 and abs(p4-.125)<1e-12
assert abs(16*p4-8*p2+1-1)<1e-12
assert abs(16*(p2-p4)-2)<1e-12
n=np.arange(90,dtype=float)
for b in (1.,10.,100.):
 ev,V=eigh_tridiagonal(n*(n+2)+b,np.full(89,-b/2))
 omega=V[:,0]
 pO=np.zeros(90)
 pO[:-1]+=.5*omega[1:];pO[1:]+=.5*omega[:-1]
 W=b*(omega-pO);W-=omega*np.dot(omega,W)
 coef=V.T@W
 susc=np.sum(coef[1:]**2/(ev[1:]-ev[0]))
 assert susc>0
 print('continuous SU2 rotor b',b,'driver self-susceptibility',susc)
print('PASS Haar spin-one Rayleigh 2A_f; portal driver susceptibility nonzero; exact cross-response vanishes by tensor-sector proof')
