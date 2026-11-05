#!/usr/bin/env python3
"""Five-state SU2 corrected-electric MPO: local nearest-neighbor Liouville action.
Test against independent direct corrected K for genuine output spin tuples.
The complete actual-source/product-transfer checks are in the linked Library ZIP.
"""
from functools import reduce
from math import sqrt
import numpy as np
kron=lambda x:reduce(np.kron,x)
def spin(n):
 j=n/2;U=np.zeros((n+1,n+1),complex)
 for k in range(n):
  z=j-k-1;U[k,k+1]=sqrt((j-z)*(j+z+1))
 return [(U+U.conj().T)/2,(U-U.conj().T)/(2j),np.diag(np.arange(n,-n-1,-2)/2)]
def transfer_mpo(deg,local):
 D=sum(n*(n+2) for n in deg)
 states={0:np.array([[1.+0j]])}
 for n,M in zip(deg,local):
  new={}
  for state,left in states.items():
   transitions=[(state,M)] if state in (0,4) else []
   if state==0:
    transitions +=[(a+1,(2/D)*spin(n)[a]@M) for a in range(3)]
   elif 1<=state<=3:
    transitions=[(4,M@spin(n)[state-1])]
   for out,block in transitions:
    piece=np.kron(left,block)
    new[out]=new.get(out,np.zeros_like(piece))+piece
  states=new
 return states[4]
def independent_T(deg,local):
 X=kron(local);D=sum(n*(n+2) for n in deg)
 out=np.zeros_like(X)
 for i in range(len(deg)-1):
  for a in range(3):
   L=kron([spin(n)[a] if j==i else np.eye(n+1) for j,n in enumerate(deg)])
   R=kron([spin(n)[a] if j==i+1 else np.eye(n+1) for j,n in enumerate(deg)])
   out+=(2/D)*L@X@R
 return out
rng=np.random.default_rng(77)
for ds in ([2,1],[4,1],[1,2,1,1],[1,4,1,1],[1,1,3,1]):
 local=[rng.normal(size=(n+1,n+1))+1j*rng.normal(size=(n+1,n+1)) for n in ds]
 got=transfer_mpo(ds,local);expect=independent_T(ds,local)
 assert np.linalg.norm(got-expect,'fro')<1e-9
 print('PASS exact corrected SU2 five-state electric MPO',ds,'difference',np.linalg.norm(got-expect,'fro'))
print('The MPO has virtual states idle, pending x/y/z, done independent of strip width.')
