#!/usr/bin/env python3
"""Proof companion: exact SU2 deleted-face Haar small-ball inequalities.
Full character-basis numerical verifier and logs are in the companion ZIP.
"""
import math
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
import numpy as np
for h in [0.2,0.1,0.05,0.025]:
 b=4/h**2;A=4.;k=(2*b/A)**0.5
 mass=quad(lambda d:2/math.pi*(d*(2-d))**0.5,0,1/k)[0]
 N=180;n=np.arange(N);E=eigh_tridiagonal(n*(n+2)+b,np.full(N-1,-b/2),select='i',select_range=(0,0))[0][0]
 upper=b/k*(2+math.log(2*math.e**2*k/mass))
 assert 4/(3*math.pi)*k**-1.5 <=mass<=4*2**0.5/(3*math.pi)*k**-1.5
 assert 0<E<=upper
 print(h,mass,E,upper)
print('PASS exact Haar and interacting SU2 character-basis variational bound')
