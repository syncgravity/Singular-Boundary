"""Validate Haar SU2 exponential trial and exact local-Dirichlet response structure."""
import numpy as np
from scipy.special import roots_jacobi

x,w=roots_jacobi(200,0.5,0.5)
w=w/w.sum()
def tilted(t):
    z=np.exp(2*t*(x-1))
    law=w*z/np.dot(w,z)
    return np.dot(law,x),np.dot(law,1-x*x)
for b in (1,10,100,10000):
    t=np.sqrt(b)
    m,q=tilted(t)
    lower=m-(t*t/(4*b))*q
    assert 0<lower<1
    print('b=',b,'m>=',format(lower,'.9f'))
assert tilted(100)[0]>0.99
print('PASS SU2 Haar exponential variational response checks')
