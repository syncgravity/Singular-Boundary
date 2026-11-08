#!/usr/bin/env python3
"""Numerical class-Haar audit: PF-I16 source-rhombus infrared countermodel."""
import math
import numpy as np
from scipy.integrate import quad

def haar(fun):
    return quad(lambda p:(2/math.pi)*math.sqrt(max(0.,1-p*p))*fun(p),
                -1.,1.,epsabs=2e-12,epsrel=2e-12)[0]

assert abs(haar(lambda p:1.)-1)<1e-12
assert abs(haar(lambda p:p*p)-.25)<1e-12

for eps in [.5,.2,.1,.05,.02,.01]:
    Z=.25+eps*eps
    T=haar(lambda p:p*p*(1-p*p)/(p*p+eps*eps))/(4*Z)
    var=haar(lambda p:p*p)/Z
    energy=haar(lambda p:(1-p*p)*eps**4/(p*p+eps*eps)**2)/Z
    rayleigh=energy/var
    def lap_ratio(p):
        return (1-p*p)*eps*eps/(p*p+eps*eps)**2-3*p*p/(p*p+eps*eps)
    def potential(p):
        return 3*eps*eps/(p*p+eps*eps)+eps*eps*(1-p*p)/(p*p+eps*eps)**2
    for p in np.linspace(-1,1,101):
        assert potential(p)>=0
        assert abs(-lap_ratio(p)+potential(p)-3)<1e-10
    assert T<=1+1e-11
    assert abs(var-1/(1+4*eps*eps))<1e-10
    assert rayleigh<=4*eps*(1+1e-10)
    print(f'eps={eps:.3f} T_e={T:.9f} Var={var:.9f} Rayleigh={rayleigh:.9f} bound={4*eps:.9f}')
print('PASS: six SU(2) Haar quadratures and potential checks')
