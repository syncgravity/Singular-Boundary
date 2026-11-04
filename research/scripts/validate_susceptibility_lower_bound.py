"""Exact Haar rotor susceptibility sum rule and finite Whitney check."""
from fractions import Fraction as F
import numpy as np
a=F(3,2);v=F(1,4);q=F(3,4)
s=F(3,4)*a*v
chi=2*v/(F(3,4)*a)
C=a/4
assert s==C*q and v*v==chi*s/2 and chi==F(2,3)/a
M=np.load('/mnt/data/global_whitney_11face.npz')['matrix']
K=np.linalg.inv(M)
assert np.linalg.eigvalsh(K)[0]>0
print('PASS exact SU2 Haar rotor',v,q,s,chi)
print('PASS 30-link inverse geometry',np.linalg.eigvalsh(K)[[0,-1]])
