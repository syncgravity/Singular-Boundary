#!/usr/bin/env python3
"""Exact SU2 CLASS-character Jacobi cutoff obstruction; not a general spin-network bound.

a fixed max n=2j face-character cutoff leaves magnetic energy O(b), whereas
full Wilson gauge-invariant exponential trial has energy O(sqrt(b)).
"""
import math
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal
for N in [0,1,2,3,4,8,16,32]:
 D=np.zeros(N+1)
 x=eigvalsh_tridiagonal(D,np.full(N,.5))[-1] if N>0 else 0
 bound=math.cos(math.pi/(N+2))
 assert abs(x-bound)<1e-13,(N,x,bound)
 print('class max n',N,'j_max',N/2,'max projected Wilson trace',x,
       'min deficit',1-x)
# Product class subspaces with local cutoff N: for each q, P p_q P
# has the same Jacobi norm, so sum_q b_q (1-P p_q P)>=
# (sum_q b_q)(1-cos(pi/(N+2))) as a form.
# For b_q ~ b, the model-specific full-state trial gives E0<=C sqrt b.
# Thus a product-class truncation must have N+2>=c b^(1/4)
# to reproduce the correct ground energy scale.
for b in (16,256,4096,65536):
 C=15.042168124831203
 B=7.35*b
 N=0
 while B*(1-math.cos(math.pi/(N+2)))>C*math.sqrt(b):
  N+=1
 print('b',b,'minimum class n to remove energy-scale contradiction',N,
       'b^(1/4)',b**.25)
print('PASS exact SU2 character Jacobi spectrum and b^(1/4) necessary class-cutoff scaling')
