#!/usr/bin/env python3
"""Independent deterministic regression of double self-weighted cap-response constants.
Full numerical Haar convolution and rotor quadrature verifier is in the archived proof ZIP.
"""
import math
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
import numpy as np

def phi(t,a):
    x=t/a
    if x<=.25: return 1.
    if x>=.5: return 0.
    z=4*(x-.25)
    return (1-10*z**3+15*z**4-6*z**5)**2

for a in (.4,.7,1.):
    alpha=quad(lambda t:2/math.pi*math.sin(t)**2*phi(t,a),0,a/2,epsabs=1e-12)[0]
    nu=quad(lambda t:2/math.pi*math.sin(t)**2*phi(t,a)**2,0,a/2,epsabs=1e-12)[0]
    assert 0<nu<=alpha
    print("cap",a,alpha,nu)

n=np.arange(110,dtype=float)
for b in (4.,25.,100.):
    eig,_=eigh_tridiagonal(n*(n+2)+b,np.full(len(n)-1,-b/2),select="i",select_range=(0,0))
    deletion=float(eig[0])
    assert 0<deletion<=3/(2*math.sqrt(2))*math.sqrt(4*b)
    print("coupling",b,"deletion",deletion)

for h in (.2,.1,.05,.025):
    a=math.acos(1-h)
    alpha=quad(lambda t:2/math.pi*math.sin(t)**2*phi(t,a),0,a/2)[0]
    b=4/h**2
    uv=math.sqrt(a)*b**.75/(h**(-11/8))**2
    assert 100<uv/alpha<150
print("PASS: Haar bump scaling, interacting deletion-energy comparison, h^-11/8 cutoff")
