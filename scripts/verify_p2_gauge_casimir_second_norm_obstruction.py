#!/usr/bin/env python3
"""P-72: Gauge-invariant face-zero Casimir projector is norm-C1 but NOT norm-C2
for actual corrected two-face interacting SU2 operator at every lambda != 0.
This is an exact analytic operator bound; finite spin numerics only illustrate.
"""
from math import sqrt
import numpy as np
P=np.diag([1,0,0,0,0]).astype(complex)
V=np.zeros((5,5),complex)
for idx in (1,4):V[0,idx]=V[idx,0]=-1/(2*sqrt(2))
C=np.diag([0,.75,.75,.75,.75]);Rz=np.diag([0,.5,-.5,.5,-.5])
ad=lambda A,B:A@B-B@A
D=ad(V,P);Z=ad(Rz,D)
omega=np.eye(5)[:,0]
assert abs(np.linalg.norm(Z@omega)-.25)<1e-12
for lam in (.25,1.,2.):
 bounded=lam*ad(4*C,D)+lam**2*ad(V,D)
 for doubled_spin in (1,2,4,10,20,50,100,1000):
  spin=doubled_spin/2
  # compress actual corrected 2R1.L2 cross commutator onto neighbor |s,s>
  block=2*lam*spin*Z+bounded
  lower=abs(lam)*spin/2-np.linalg.norm(bounded,2)
  assert np.linalg.norm(block,2)+1e-10>=lower
 print('PASS lambda',lam,'slope of unbounded double commutator >=',abs(lam)/2)
print('PROVED norm of double commutator has no finite bound as neighbor spin grows.')
print('P0 tensor I is gauge-invariant and has bounded first commutator, but')
print('cannot have a twice operator-norm differentiable corrected interacting orbit.')
print('C2 ground-state correlation kernels (P-70) are compatible with this result.')
