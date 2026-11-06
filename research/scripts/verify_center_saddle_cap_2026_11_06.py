#!/usr/bin/env python3
"""Regression checks for center-sign Hessians and Haar cap asymptotics; not a proof of stable manifolds."""
import math
import numpy as np
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import eigsh
from scipy.integrate import quad

def incidence(n):
    links={};faces=[];r=[];c=[];v=[]
    def plus(p,k):
        z=list(p);z[k]+=1;return tuple(z)
    for x in range(n+1):
     for y in range(n+1):
      for z in range(n+1):
       p=(x,y,z)
       for k in range(3):
        if p[k]<n:links[(p,k)]=len(links)
    for x in range(n+1):
     for y in range(n+1):
      for z in range(n+1):
       p=(x,y,z)
       for i in range(3):
        for j in range(i+1,3):
         if p[i]>=n or p[j]>=n:continue
         row=len(faces);faces.append((p,i,j))
         for a,k,sgn in [(p,i,1),(plus(p,i),j,1),(plus(p,j),i,-1),(p,j,-1)]:
          r.append(row);c.append(links[(a,k)]);v.append(sgn)
    return coo_matrix((v,(r,c)),shape=(len(faces),len(links))).tocsr()

checks=0
for n in [2,3,4,5]:
 B=incidence(n);degree=np.asarray(B.power(2).sum(axis=0)).ravel()
 assert degree.max()==4;checks+=1
 e=int(np.flatnonzero(degree==4)[0]);sign=np.where(B.getcol(e).toarray().ravel()!=0,-1,1)
 assert np.count_nonzero(sign==-1)==4;checks+=1
 H=B.T@diags(sign/4)@B
 assert abs(H[e,e]+1)<1e-13;checks+=1
 assert eigsh(H,k=1,which='SA')[0][0]<-1+1e-8;checks+=1
for delta in [1e-6,1e-4,0.001,0.01,0.1,0.5]:
 theta=math.acos(1-delta);vol=(theta-math.sin(theta)*math.cos(theta))/math.pi
 integral=quad(lambda t:2*math.sin(t)**2/math.pi,0,theta)[0]
 assert abs(vol-integral)<1e-12;checks+=1
print('PASS',checks,'exact-incidence and cap checks')
