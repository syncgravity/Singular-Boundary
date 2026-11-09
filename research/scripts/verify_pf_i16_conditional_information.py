#!/usr/bin/env python3
"""PF-I16 conditional-information calibration on one source SU(2) rhombus."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh_tridiagonal

n_max = 70
x,w=leggauss(1200)
theta=(x+1)*math.pi/2
weights=w*(math.pi/2)*(2/math.pi)*np.sin(theta)**2
n=np.arange(n_max,dtype=float)
characters=np.sin((n[:,None]+1)*theta[None,:])/np.sin(theta)[None,:]
assert abs(sum(weights)-1)<2e-13
assert abs(float(np.dot(weights,characters[1]*characters[1]))-1)<2e-13

for b in (0.,.01,.1,.71,1.,4.,16.):
    diag=n*(n+2)+b
    off=np.full(n_max-1,-b/2)
    _,vec=eigh_tridiagonal(diag,off)
    coeff=vec[:,0]
    if coeff[0]<0: coeff=-coeff
    psi=coeff@characters
    rho=np.maximum(psi*psi,1e-300)
    rho/=float(weights@rho)
    information=float(weights@(rho*np.log(rho)))
    kinetic=float(np.dot(coeff*coeff,n*(n+2))/4)
    total_variation=float(.5*(weights@np.abs(rho-1)))
    assert information>=-1e-11
    assert information<=4*kinetic+2e-10
    assert kinetic<=2*b+2e-10
    assert total_variation<=math.sqrt(max(0,information)/2)+5e-11
    assert total_variation<=min(1.,math.sqrt(2*kinetic))+5e-11
    print('b=%.3f T_e=%.10f I_e=%.10f TV=%.10f' %
          (b,kinetic,information,total_variation))
print('PASS: SU(2) Haar quadrature, LSI, Pinsker, local variational checks')
