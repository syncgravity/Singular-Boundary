#!/usr/bin/env python3
"""Exact SU2 Wilson quartic remainder; signed shared-edge covariance audit. No sampling."""
import sympy as s
import numpy as np
from scipy.linalg import eigh
from itertools import combinations
h,r,a,beta=s.symbols("h r a beta",positive=True)
z=s.sqrt(h)*r/2
assert s.simplify(s.series(1-s.cos(z),h,0,4).removeO()-(h*r*r/8-h*h*r**4/384+h**3*r**6/46080))==0
t1,t2,c,u,v=s.symbols("t1 t2 c u v",positive=True)
mgf=(1-2*t1*u-2*t2*v+4*(t1*t2-c*c)*u*v)**(-s.Rational(3,2))
co=s.factor(s.diff(mgf,u,2,v,2).subs({u:0,v:0})-225*t1*t1*t2*t2)
assert s.simplify(co-600*t1*t2*c*c-120*c**4)==0
assert s.simplify((600*4*a/beta*105*a/(32*beta))*(beta/384)**2-875*a*a/16384)==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
faces=[edges(f) for f in seed];E=set.union(*faces)
assert len(E)==10 and max(sum(e in f for f in faces) for e in E)==2
def check(M):
 w,U=eigh(M);assert w.min()>0 and w.max()<8.0000001
 root=(U*np.sqrt(w))@U.T;S=np.sqrt(2.)*root;t=np.diag(S);Q=S**2
 cov=600*np.outer(t,t)*Q+120*Q**2
 for q in [np.ones(len(t)),(-1.)**np.arange(len(t)),np.linspace(-1,1,len(t))]:
  n=q@q;z=q@cov@q
  assert 7875*n-1e-7<=z<=46080*n+1e-6
 return np.linalg.eigvalsh(root**2).min()
for n in (3,25,100):
 if n==3: M=np.diag([4.]*3)-np.diag([1.]*2,1)-np.diag([1.]*2,-1)
 else:
  N=int(np.sqrt(n));M=np.eye(n)*4
  for i in range(N):
   for j in range(N):
    k=i*N+j
    if i+1<N:M[k,k+N]=M[k+N,k]=-1
    if j+1<N:M[k,k+1]=M[k+1,k]=-1
 print('faces',n,'min K',check(M))
print('PASS: exact cosine expansion, three-color Wick, signed covariance, Penrose spatial seed; no Monte Carlo')
