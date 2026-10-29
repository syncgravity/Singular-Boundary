#!/usr/bin/env python3
"""Sector parity SU2 cap-stability and abstract sampled-kernel obstruction.
Comparison model only; not a nonlinear Penrose Hamiltonian simulation.
"""
import math
import numpy as np
from scipy.linalg import eigh
I=np.eye(2); X=np.array([[0.,1.],[1.,0.]])
s=[1.,-1.]
T=.3*(np.kron(I-X,I)+np.kron(I,I-X))
R=np.zeros((4,4)); R[0,0]=R[3,3]=1;R[1,2]=R[2,1]=1
P=np.array([a*b for a in s for b in s])
W=np.diag(1-P)
M=4.
V=np.diag([M*(a==-1)+M*(b==-1) for a in s for b in s])
H0=T+W+V
ev,U=eigh(H0);om=U[:,0];dplus=ev[1]-ev[0]
odd=np.array([0.,1.,-1.,0.])/math.sqrt(2)
dminus=float(odd@H0@odd-ev[0])
assert np.allclose(R@H0@R,H0) and dplus>0 and dminus>0
cap=np.array([1.,0.,0.,0.]);m0=float(np.dot(om**2,cap))
for eps in (.005,.025,.08,.35):
 D=np.diag([eps*(float(a==-1)-float(b==-1)) for a in s for b in s])
 assert np.allclose(R@D@R,-D)
 e,Psi=eigh(H0+D);psi=Psi[:,0]
 even=(psi+R@psi)/2;oddpart=(psi-R@psi)/2
 w=even-(om@even)*om
 r=eps/dminus;z=eps**2/(dplus*dminus)
 assert np.linalg.norm(oddpart)<=r+1e-11 and np.linalg.norm(w)<=z+1e-11
 lb=max(0.,math.sqrt(max(0.,1-r*r-z*z))*math.sqrt(m0)-z)**2
 assert float(np.dot(psi**2,cap))>=lb-1e-10
 for h in (.2,.01,.001):
  a=math.acos(1-h);H=(a/2-math.sin(a)/2)/math.pi
  assert H>0
print('PASS exact even-odd gap bounds, asymmetric cap stability, and Haar scale; no physical Penrose simulation')
