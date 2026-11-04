"""Radial SU2 heat-kernel uniform bounds and a global-normalization stress test.
The matrix-derived kappa is for archived M5 edge metric without overall coupling.
"""
import math
from scipy.integrate import quad
kappa=2.362228738429273
for t in (0.3,0.5,1.0):
 S=sum((n+1)**2*math.exp(-kappa*n*(n+2)*t) for n in range(1,500))
 assert 0<S<1
 coeff=((1-S)/(1+S))**2
 print('time',t,'S',S,'certified kernel ratio squared',coeff)
def Z(lam):
 return quad(lambda p:2/math.pi*math.sqrt(1-p*p)*math.exp(-2*lam*p*p),-1,1,epsabs=1e-12)[0]
for lam in (0.5,1.,5.):
 I=Z(lam/2)/math.sqrt(Z(lam))
 assert 0<I<=1
 print('spectator lambda',lam,'I',I,'30-fold global L1 squared',I**60)
print('PASS radial spectral kernel inequality and product spectator test')
