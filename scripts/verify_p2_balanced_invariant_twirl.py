#!/usr/bin/env python3
"""Exact Gauss balanced even-spin twirl: J^2 spectral-projector checks."""
from itertools import combinations
from math import comb
import sympy as s
for N in (2,4,6):
 masks=[sum(1<<i for i in ups) for ups in combinations(range(N),N//2)]
 pos={x:i for i,x in enumerate(masks)}
 D=len(masks)
 J=s.Rational(N*(4-N),4)*s.eye(D)
 for a,b in combinations(range(N),2):
  P=s.zeros(D)
  for col,x in enumerate(masks):
   y=x if (x>>a)&1==(x>>b)&1 else x^(1<<a)^(1<<b)
   P[pos[y],col]=1
  J+=P
 v=s.zeros(D,1);w=s.zeros(D,1)
 x=sum(1<<i for i in range(0,N,2))
 v[pos[x]]=1;w[pos[((1<<N)-1)^x]]=1
 probs=[]
 for j in range(N//2+1):
  P=s.eye(D)
  for k in range(N//2+1):
   if j!=k:P=P*(J-k*(k+1)*s.eye(D))/s.Rational(j*(j+1)-k*(k+1))
  P=P.applyfunc(s.factor)
  p=(v.T*P*v)[0];cross=(v.T*P*w)[0]
  assert P*P==P and cross*cross==p*p
  mu=comb(N,N//2-j)-(comb(N,N//2-j-1) if N//2-j-1>=0 else 0)
  assert p==s.Rational(mu,D)
  probs.append(p)
 assert sum(probs)==1
 print('PASS even width',N,'projected spin weights:',probs)
for N in range(2,202,2):
 assert sum(comb(N,N//2-j)-(comb(N,N//2-j-1) if N//2-j-1>=0 else 0) for j in range(N//2+1))==comb(N,N//2)
print('PASS all-even-width trace-class Gauss twirl multiplicities through width 200')
