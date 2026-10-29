#!/usr/bin/env python3
"""Double-deleted neighbor parity and finite comparator; non-Penrose surrogate."""
import numpy as np
from scipy.linalg import eigh
S=np.diag([1.,-1.,1.]);H0=np.diag([0.,2.,3.])
O=np.array([[1.,0.,.3],[0.,0.,0.],[.3,0.,.5]])
assert np.linalg.eigvalsh(O).min()>=-1e-12
for sign in (-1,1):
 B=np.array([[0.,1.,0.],[1.,0.,5.*sign],[0.,5.*sign,0.]])
 assert np.allclose(S@B@S,-B) and np.allclose(S@O@S,O)
 def F(t):
  ev,V=eigh(H0-t*B)
  return float(V[:,0]@O@V[:,0])
 assert abs(F(.001)-F(-.001))<1e-12
 second=(F(.001)-2*F(0)+F(-.001))/1e-6
 assert (second>0)==(sign>0)
 print('sign',sign,'second derivative',second)
print('PASS endpoint parity and unfixed second-order sign')
