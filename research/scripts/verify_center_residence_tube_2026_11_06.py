#!/usr/bin/env python3
"""Deterministic regression for signed Hessian and finite-time residence envelope.
Not a simulation of coupled interacting quantum vacuum or nonlinear chart bounds.
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from scipy.integrate import solve_ivp

def incidence(n):
    edges={}; faces=[]; rows=[]; cols=[]; vals=[]
    for x in range(n+1):
      for y in range(n+1):
       for z in range(n+1):
        a=(x,y,z)
        for d in range(3):
         if a[d]<n: edges[(a,d)]=len(edges)
    def shift(a,k):
        b=list(a);b[k]+=1;return tuple(b)
    for x in range(n+1):
     for y in range(n+1):
      for z in range(n+1):
       a=(x,y,z)
       for i in range(3):
        for j in range(i+1,3):
         if a[i]>=n or a[j]>=n:continue
         p=len(faces);faces.append((a,i,j))
         for pos,d,sgn in [(a,i,1),(shift(a,i),j,1),(shift(a,j),i,-1),(a,j,-1)]:
            rows.append(p);cols.append(edges[(pos,d)]);vals.append(sgn)
    return sp.coo_matrix((vals,(rows,cols)),shape=(len(faces),len(edges))).tocsr()

checks=0
for n in range(2,7):
 B=incidence(n)
 assert B.shape==(3*n*n*(n+1),3*n*(n+1)*(n+1));checks+=1
 assert np.all(B.power(2).sum(axis=1).A1==4);checks+=1
 degree=B.power(2).sum(axis=0).A1
 assert degree.max()==4;checks+=1
 e=int(np.flatnonzero(degree==4)[0])
 center=np.where(B.getcol(e).toarray().ravel()!=0,-1.,1.)
 assert np.count_nonzero(center==-1)==4;checks+=1
 H=B.T@sp.diags(center/4)@B
 assert abs(H[e,e]+1)<1e-12;checks+=1
 lam=-eigsh(H,k=1,which='SA',tol=1e-9)[0][0]
 assert lam>=1-1e-8;checks+=1
 print('grid',n,'links',B.shape[1],'faces',B.shape[0],'unstable rate >=',round(lam,7))
for lam in [1.,1.25,1.75]:
 for c in [-0.5,0.,0.5]:
  r=0.1
  for x0 in np.linspace(-.095,.095,39):
   sol=solve_ivp(lambda t,y:lam*y+c*y*y,(0,3),[x0],rtol=2e-11,atol=2e-12,max_step=.02,dense_output=True)
   for T in [.2,.5,1.,2.,3.]:
    yy=sol.sol(np.linspace(0,T,81))[0]
    if np.max(np.abs(yy))>r+1e-8:continue
    width=r*np.exp(-lam*T)+(abs(c)/lam)*r*r*(1-np.exp(-lam*T))
    assert abs(x0)<=width+1e-8,(lam,c,x0,T,width)
    checks+=1
print('PASS',checks,'signed-Hessian and scalar residence checks')
