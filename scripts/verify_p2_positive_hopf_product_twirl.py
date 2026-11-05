#!/usr/bin/env python3
"""P-75 constructive positive Haar SU2 Hopf cubature, fixed spin-sector product rank-one."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
def rep(g,n):
 a,b,c,d=g[0,0],g[0,1],g[1,0],g[1,1]
 out=np.zeros((n+1,n+1),complex)
 for k in range(n+1):
  for h in range(n+1):
   z=0j
   for rr in range(max(0,h-k),min(h,n-k)+1):
    t=h-rr
    z+=math.comb(n-k,rr)*math.comb(k,t)*a**(n-k-rr)*c**rr*b**(k-t)*d**t
   out[h,k]=z*math.sqrt(math.comb(n,k)/math.comb(n,h))
 return out
def twirl(ds,u,v):
 S=sum(ds);M=2*S+1;Q=S+1
 nodes,w=leggauss(Q)
 out=np.zeros((math.prod(n+1 for n in ds),)*2,complex)
 ph=np.exp(2j*np.pi*np.arange(M)/M)
 for t,weight in zip((nodes+1)/2,w/2):
  for aa in ph:
   for bb in ph:
    a=math.sqrt(t)*aa;b=math.sqrt(1-t)*bb
    g=np.array([[a,b],[-b.conjugate(),a.conjugate()]])
    x=np.array([1+0j]);y=x.copy()
    for n,ui,vi in zip(ds,u,v):
     D=rep(g,n);x=np.kron(x,D@ui);y=np.kron(y,D@vi)
    out+=weight/M**2*np.outer(x,y.conjugate())
 return out
for ds in ([1,1],[1,1,1,1],[2,1,1]):
 u=[np.eye(n+1)[:,i%2] for i,n in enumerate(ds)]
 v=[np.eye(n+1)[:,1-i%2] for i,n in enumerate(ds)]
 X=twirl(ds,u,v);a=.87;b=1j*np.sqrt(1-a*a)
 g=np.array([[a,b],[-b.conjugate(),a.conjugate()]])
 U=np.array([[1+0j]])
 for n in ds:U=np.kron(U,rep(g,n))
 assert np.linalg.norm(U@X@U.conj().T-X)<3e-12
 if ds==[1,1]:
  singlet=np.array([0,1,-1,0])/np.sqrt(2)
  P=np.outer(singlet,singlet);T=np.eye(4)-P
  original=np.outer(np.kron(*u),np.kron(*v))
  expected=np.trace(P@original)*P+np.trace(T@original)*T/3
  assert np.linalg.norm(X-expected)<1e-12
 print('PASS exact Hopf positive cubature degrees',ds,'nodes',(sum(ds)+1)*(2*sum(ds)+1)**2)
print('Analytic exactness: phase Fourier cutoff <=2S, remaining t polynomial degree <=S.')
print('Tests are finite numerical diagnostics, not complete high-width inversions.')
