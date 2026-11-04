#!/usr/bin/env python3
"""Independent SU2 N=2 physical original-link one-Haar HS source verifier."""
import math
from itertools import product
import numpy as np
from numpy.polynomial.legendre import leggauss
from sympy import S
from sympy.physics.wigner import clebsch_gordan
def spin(n):
 j=n/2;v=np.arange(j,-j-1,-1);up=np.zeros((n+1,n+1),complex)
 for k in range(n):
  z=v[k+1];up[k,k+1]=math.sqrt((j-z)*(j+z+1))
 return ((up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(v))
def rep(n,g):
 out=np.zeros((n+1,n+1),complex)
 for k in range(n+1):
  for l in range(n+1):
   out[l,k]=math.sqrt(math.comb(n,k)/math.comb(n,l))*sum(math.comb(n-k,r)*math.comb(k,l-r)*g[1,0]**r*g[0,0]**(n-k-r)*g[0,1]**(k-l+r)*g[1,1]**(l-r) for r in range(max(0,l-k),min(l,n-k)+1))
 return out
def haar(f,S):
 M=2*S+1;Q=(S+2)//2;t,w=leggauss(Q);z=0j
 for x,weight in zip(t,w):
  x=(x+1)/2
  for a in range(M):
   u=math.sqrt(x)*np.exp(2j*np.pi*a/M)
   for b in range(M):
    v=math.sqrt(1-x)*np.exp(2j*np.pi*b/M)
    g=np.array([[u,v],[-v.conjugate(),u.conjugate()]])
    z+=weight/(2*M*M)*f(g)
 return z
def K(X,degrees):
 D=sum(n*(n+2) for n in degrees)
 left,right=spin(degrees[0]),spin(degrees[1])
 return D*X-2*sum(np.kron(a,np.eye(degrees[1]+1))@X@np.kron(np.eye(degrees[0]+1),b) for a,b in zip(left,right))
def cg(m,l):
 C=np.zeros((2*(m+1),l+1),complex)
 for i,j,k in product(range(2),range(m+1),range(l+1)):
  C[i*(m+1)+j,k]=float(clebsch_gordan(S(1)/2,S(m)/2,S(l)/2,S(1-2*i)/2,S(m-2*j)/2,S(l-2*k)/2))
 return C
def block(F,m,l):
 C=cg(m,l);U=np.kron(C,np.eye(2)).reshape(2*(m+1)*2,(l+1)*2)
 T=np.zeros((4*(m+1),4*(m+1)),complex)
 for i,j,k in product(range(2),range(2),range(m+1)):
  old=(i*2+j)*(m+1)+k;new=(i*(m+1)+k)*2+j
  T[new,old]=1
 A=T@np.kron(F,np.eye(m+1))@T.conj().T
 return U.conj().T@A@U
v=np.zeros(4,complex);w=np.zeros(4,complex);v[1]=1;w[2]=1
X=np.outer(v,w.conj())
F=haar(lambda g:np.kron(g,g)@X@np.kron(g,g).conj().T,2)
for l,expected in ((2,75/32),(4,125/32)):
 Z=(block(K(X,[1,1]),3,l)+15*block(X,3,l)-K(block(X,3,l),[l,1]))/2
 Y=(block(K(F,[1,1]),3,l)+15*block(F,3,l)-K(block(F,3,l),[l,1]))/2
 h=haar(lambda g:np.vdot(Z,np.kron(rep(l,g),g)@Z@np.kron(rep(l,g),g).conj().T),1+l)
 actual=np.linalg.norm(Y,'fro')**2
 assert abs(h.real-actual)<1e-8 and abs(actual-expected)<1e-8,(l,h,actual,expected)
 print('PASS physical q0 one-Haar source l=',l,'HS squared=',actual)
