#!/usr/bin/env python3
"""Deterministic SU2 character positivity -> center ball lower probability certificates.
No Monte Carlo; finite quadrature, exact character integrals, and explicit Fourier tail.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_jacobi

def haar_cap(a):
    return (a-math.sin(2*a)/2)/math.pi

def b_char(j,r):
    d=2*j+1
    if j==0: return haar_cap(r)
    return (math.sin((d-1)*r)/(d-1)-math.sin((d+1)*r)/(d+1))/math.pi

def mollifier(t):
    if t<=.25:return 1.
    if t>=.5:return 0.
    x=4*(t-.25)
    a=math.exp(-1/x)
    b=math.exp(-1/(1-x))
    return b/(a+b)

def phi(u,r):return mollifier(u/r)

def coeff(j,a):
    d=2*j+1
    return 2/math.pi*quad(lambda u: phi(u,a)*math.sin(u)*math.sin(d*u), 0,a/2,epsabs=1e-13,limit=500)[0]

def masses(a):
    H=2/math.pi*quad(lambda u: phi(u,a)*math.sin(u)**2,0,a/2,epsabs=1e-14)[0]
    N=2/math.pi*quad(lambda u: phi(u,a)**2*math.sin(u)**2,0,a/2,epsabs=1e-14)[0]
    return H,N

for r in (0.2,0.5,1.0):
    for j in (0,.5,1,1.5,2,3,6):
        q=2/math.pi*quad(lambda u: math.sin(u)*math.sin((2*j+1)*u),0,r,epsabs=1e-14)[0]
        assert abs(q-b_char(j,r))<1e-12,(j,r,q,b_char(j,r))
    a=r; B=haar_cap(a/2)
    assert B>0 and B<haar_cap(a)
    # The constant Haar marginal has all higher coefficients zero.
    assert haar_cap(a)>= B

for a,J in [(1.,60),(.5,100),(.3,160)]:
    A,N=masses(a)
    vals=np.array([coeff(k/2,a) for k in range(2*J+1)])
    tail=max(0.,N-sum(vals*vals))
    lower=max(0.,(A*A-tail)/N)
    assert tail<A*A/2,(a,J,tail,A*A)
    assert lower>0
    print(f'smooth bump a={a:.3f} spin cutoff J={J}: A={A:.8g}, norm2={N:.8g}, tail={tail:.3g}, certified cap>={lower:.8g}, Haar cap={haar_cap(a):.8g}')

# Nonnegativity of the character coefficients is a genuine *additional* hypothesis.
# A strictly positive center-even density can have a negative spin-1 coefficient.
p,w=roots_jacobi(256,.5,.5)
w=2*w/math.pi
for kappa in (1.,5.,20.):
    z=np.dot(w,np.exp(-kappa*p*p))
    moment=np.dot(w,np.exp(-kappa*p*p)*(4*p*p-1))/z
    assert moment<0
    print(f'center-avoiding smooth SU2 rotor kappa={kappa:g}: <chi_spin1>={moment:.9g} < 0')
print('PASS exact group-character cap identity; Fourier minorization and finite-spin tail; sign obstruction. No Monte Carlo.')
