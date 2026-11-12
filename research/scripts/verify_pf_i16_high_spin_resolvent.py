#!/usr/bin/env python3
"""PF-I16: exact high-spin SU(2) character nonlinear growth and electric inverse."""
from math import pi,sqrt
import sympy as s
import numpy as np
from numpy.polynomial.legendre import leggauss
n,k=s.symbols('n k',integer=True,positive=True)
lam=n*(n+2)
exact=s.factor(s.summation((lam-2*k*(k+1))**2,(k,0,n)))
expected=n*(n+1)*(n+2)*(7*n*n+14*n+4)/15
assert s.simplify(exact-expected)==0
normalized=s.factor(exact/lam**2)
assert s.limit(normalized/n,n,s.oo)==s.Rational(7,15)
print('Exact polynomial:', exact)
print('Unit-H1 nonlinear forcing norm²:', normalized)
print('Inverse response norm limit:',sqrt(pi**2/48-3/16))
x,w=leggauss(1100)
th=(x+1)*pi/2
hw=w*np.sin(th)**2
for N in (1,2,4,8,16,32,64,128):
    energy=N*(N+2)
    chi=np.sin((N+1)*th)/np.sin(th)
    assert abs(float(hw@(chi*chi))-1)<1e-10
    modes=np.arange(N+1)
    amps=energy-2*modes*(modes+1)
    even=np.sin((2*modes[:,None]+1)*th[None,:])/np.sin(th)[None,:]
    gamma=amps@even
    norm2=float(hw@(gamma*gamma))
    assert abs(norm2/float(expected.subs(n,N))-1)<1e-9
    inver=amps[1:]/(4*modes[1:]*(modes[1:]+1)*energy)
    print(f'n={N:3d} nonlinear={sqrt(norm2)/energy:.8f} inverse={np.linalg.norm(inver):.8f}')
print('PASS: exact character identity, Haar checks and inverse smoothing')
