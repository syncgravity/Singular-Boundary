#!/usr/bin/env python3
"""Corrected original-link SU(2) shared-face Neumann inverse, S1-norm tests."""
from itertools import product
from math import sqrt
import numpy as np
def spin(n):
 j=n/2;m=np.arange(j,-j-1,-1);p=np.zeros((n+1,n+1),complex)
 for k in range(n):
  a=m[k+1];p[k,k+1]=sqrt((j-a)*(j+a+1))
 return ((p+p.conj().T)/2,(p-p.conj().T)/(2j),np.diag(m).astype(complex))
rng=np.random.default_rng(20261104);count=0
for m,n in product(range(1,8),repeat=2):
 d1=m+1;d2=n+1;E=m*(m+2)+n*(n+2)
 S=sqrt(m*(m+2)*n*(n+2))/4
 assert S<=E/8
 a=spin(m);b=spin(n)
 A=[np.kron(x,np.eye(d2)) for x in a]
 B=[np.kron(np.eye(d1),x) for x in b]
 def D(x):return -sum((A[k]@x@B[k] for k in range(3)),np.zeros_like(x))
 def K(x):return E*x+2*D(x)
 for rankone in (False,True):
  f=rng.normal(size=(d1,d1))+1j*rng.normal(size=(d1,d1))
  g=rng.normal(size=(d2,d2))+1j*rng.normal(size=(d2,d2))
  if rankone:
   f=np.outer(f[:,0],f[0,:]);g=np.outer(g[:,0],g[0,:])
  X=np.kron(f,g);source=-D(X);answer=np.zeros_like(X)
  step=source/E
  for _ in range(128):
   answer+=step;step=-2*D(step)/E
   if np.linalg.norm(step,'fro')<1e-13:break
  assert np.linalg.norm(K(answer)-source,'fro')<1e-10*max(1,np.linalg.norm(source,'fro'))
  ratio=np.linalg.norm(answer,'nuc')/(np.linalg.norm(f,'nuc')*np.linalg.norm(g,'nuc'))
  assert ratio<=S/(E-2*S)+1e-9
  assert ratio<=1/6+1e-9
  count+=1
assert count==98
print("PASS",count,"actual two-face original-link superoperator inverse/nuclear tests")
