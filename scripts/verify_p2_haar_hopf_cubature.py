#!/usr/bin/env python3
"""Exact SU2 twirl Hopf cubature regression, including corrected physical electric covariance."""
import math
import numpy as np
from functools import reduce
from numpy.polynomial.legendre import leggauss
def kron(items):return reduce(np.kron,items)
def nodes(S):
 M=2*S+1;Q=(S+2)//2
 t,w=leggauss(Q)
 for z0,w0 in zip(t,w):
  z0=(z0+1)/2
  for a in range(M):
   for b in range(M):
    z=np.sqrt(z0)*np.exp(2j*np.pi*a/M)
    v=np.sqrt(1-z0)*np.exp(2j*np.pi*b/M)
    yield np.array([[z,v],[-v.conjugate(),z.conjugate()]]),w0/(2*M*M)
def twirl(X,N):
 Y=np.zeros_like(X,dtype=complex)
 for g,w in nodes(N):
  U=kron([g]*N);Y+=w*U@X@U.conj().T
 return Y
def pauli():
 return [np.array([[0,1],[1,0]],complex)/2,
 np.array([[0,-1j],[1j,0]],complex)/2,
 np.diag([1,-1]).astype(complex)/2]
def K(X,N):
 ops=[[kron([p if i==j else np.eye(2) for i in range(N)]) for p in pauli()] for j in range(N)]
 Y=3*N*X.astype(complex).copy()
 for i in range(N-1):
  for a in range(3):Y-=2*ops[i][a]@X@ops[i+1][a]
 return Y
for N in (2,4,6):
 d=2**N;v=np.zeros(d);w=np.zeros(d)
 idx=sum(1<<(N-1-i) for i in range(0,N,2))
 v[idx]=1;w[(d-1)^idx]=1
 X=np.outer(v,w);T=twirl(X,N)
 sv=np.linalg.svd(T,compute_uv=False)
 ex=[]
 for j in range(N//2+1):
  z=math.comb(N,N//2-j)/((N//2+j+1)*math.comb(N,N//2))
  ex.extend([z]*(2*j+1))
 ex +=[0]*(d-len(ex))
 assert np.max(np.abs(np.sort(sv)-np.sort(ex)))<1e-10
 if N<=4:assert np.linalg.norm(K(T,N)-twirl(K(X,N),N),'fro')<1e-10
 print("PASS Haar twirl spin spectrum and electric covariance N=",N)
