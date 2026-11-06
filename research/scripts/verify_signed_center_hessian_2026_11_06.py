#!/usr/bin/env python3
"""Deterministic cubic SU(2) signed-center Hessian checks, not a vacuum simulation."""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from math import cos

def complex3(n):
    edges={}
    for x in range(n+1):
      for y in range(n+1):
        for z in range(n+1):
          q=(x,y,z)
          for k in range(3):
            if q[k]<n: edges[(q,k)]=len(edges)
    row=[];col=[];val=[]
    def up(q,k):
      qq=list(q);qq[k]+=1;return tuple(qq)
    p=0
    for x in range(n+1):
      for y in range(n+1):
        for z in range(n+1):
          q=(x,y,z)
          for i in range(3):
            for j in range(i+1,3):
              if q[i]>=n or q[j]>=n:continue
              for qq,k,sgn in [(q,i,1),(up(q,i),j,1),(up(q,j),i,-1),(q,j,-1)]:
                row.append(p);col.append(edges[(qq,k)]);val.append(sgn)
              p+=1
    return sp.coo_matrix((val,(row,col)),shape=(p,len(edges))).tocsr(),edges

tests=0
for n in (2,3,4,5):
  B,edges=complex3(n)
  assert B.shape==(3*n*n*(n+1),3*n*(n+1)**2);tests+=1
  assert np.all(B.power(2).sum(axis=1).A1==4);tests+=1
  assert np.max(B.power(2).sum(axis=0).A1)==4;tests+=1
  e=next(k for (q,d),k in edges.items() if all(0<q[t]<n for t in range(3)))
  assert B.getcol(e).count_nonzero()==4;tests+=1
  z=np.ones(B.shape[1]);z[e]=-1
  signs=np.prod(np.where(B.toarray()!=0,z[None,:],1),axis=1)
  assert np.sum(signs==-1)==4;tests+=1
  H=(B.T@sp.diags(signs/4)@B).tocsr()
  assert abs(H[e,e]+1)<1e-12;tests+=1
  eig=eigsh(H,k=1,which="SA")[0][0]
  assert eig<=-1+1e-8;tests+=1
  for t in (.001,.01,.1):
    second=4*(2*cos(t/2)-2)/t**2
    assert abs(second+1)<t*t/40+1e-8;tests+=1
  print(f"n={n}, E={B.shape[1]}, P={B.shape[0]}, min Hessian eigenvalue={eig:.9f}")
assert tests==40
print("PASS",tests,"deterministic assertions")
