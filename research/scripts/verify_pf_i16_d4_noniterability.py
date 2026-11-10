#!/usr/bin/env python3
"""PF-I16: independent exact beta-integral and radial quadrature scaling test on R^6.
Flat local-chart constants are NOT claimed to be the original gauge metric constants."""
from math import pi
from scipy.integrate import quad
from scipy.special import beta

S=pi**3;d=6;k=4
def f(r): return (1-r*r)**k if r<1 else 0
def grad(r):return 2*k*r*(1-r*r)**(k-1) if r<1 else 0
def I(fn):return S*quad(lambda r:r**5*fn(r),0,1,epsabs=1e-13,epsrel=1e-13)[0]
J4=I(lambda r:grad(r)**4)
J43=I(lambda r:grad(r)**(4/3))
Jc=I(lambda r:f(r)*grad(r)**2)
assert abs(J4/(S/2*(2*k)**4*beta(5,13))-1)<2e-12
assert abs(J43/(S/2*(2*k)**(4/3)*beta(11/3,5))-1)<2e-12
assert abs(Jc/(S/2*(2*k)**2*beta(4,11))-1)<2e-12
C=Jc/(J4**.5*J43**.75)
for eps in (.2,.1,.05,.025,.0125,.00625):
    amplitude=eps**(-.5)/J4**.25
    D4=amplitude*eps**(.5)*J4**.25
    D43=amplitude*eps**(3.5)*J43**.75
    numerator=amplitude**3*eps**4*Jc
    lower=numerator/D43
    assert abs(D4-1)<1e-12 and abs(lower/(C*eps**(-.5))-1)<1e-12
    print(f'eps={eps:.6f}: D4(input)={D4:.8f}, dual lower bound={lower:.10f}')
print('PASS 6D chart scaling; C=%.14f'%C)
