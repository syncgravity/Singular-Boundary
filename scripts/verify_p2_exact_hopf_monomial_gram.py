#!/usr/bin/env python3
"""Exact Wigner SU2 projected tensor-Gram overlap: rational times sqrt(rational).
No numerical quadrature or exponentially sized Clebsch-Gordan basis.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt
from collections import defaultdict

def term(n,l,k,bar=False):
 d=defaultdict(int)
 for s in range(max(0,l-k),min(l,n-k)+1):
  a=n-k-s;b=k-l+s;c=l-s;f=s
  e=(c,f,a,b) if bar else (a,b,c,f)
  d[e]+=(-1)**s*comb(n-k,s)*comb(k,l-s)
 return {e:v for e,v in d.items() if v}

def mul(a,b):
 d=defaultdict(int)
 for x,u in a.items():
  for y,v in b.items():
   e=tuple(x[k]+y[k] for k in range(4))
   d[e]+=u*v
 return {e:v for e,v in d.items() if v}

def overlap(deg,ket,bra,L):
 a=sum(n-2*k for n,k in zip(deg,ket))
 b=sum(n-2*k for n,k in zip(deg,bra))
 if abs(a)>L or abs(b)>L or (L-a)%2 or (L-b)%2:return F(0),F(1)
 la=(L-a)//2;lb=(L-b)//2
 rad=F(comb(L,lb),comb(L,la));pol={(0,0,0,0):1}
 for n,i,j in zip(deg,ket,bra):
  pol=mul(pol,term(n,i,j))
  rad*=F(comb(n,j),comb(n,i))
 pol=mul(pol,term(L,la,lb,True))
 val=F(0)
 for (z,v,zb,vb),co in pol.items():
  if z==zb and v==vb:
   val+=co*F(factorial(z)*factorial(v),factorial(z+v+1))
 return (L+1)*val,rad

def value(pair):return float(pair[0])*sqrt(float(pair[1]))
for d,a,b,L,expected in [
 ([1,1],[0,1],[1,0],0,-.5),
 ([1,1],[0,1],[1,0],2,.5),
 ([1,1,1],[0,0,1],[0,1,0],1,-1/3),
 ([1,2,1],[0,1,0],[1,0,0],2,-1/sqrt(8)),
 ([1,3,1],[0,1,1],[1,0,0],3,-.4)]:
 out=overlap(d,a,b,L)
 assert abs(value(out)-expected)<1e-12
 print('PASS small mixed-weight SU2 Wigner projector',d,L,out)
for m in (3,4,5,6,10,20):
 N=m*m;l=m+1;deg=[1]*(N-1)+[l]
 a=[0]*N;b=[0]*N;a[0]=1;b[-1]=1
 out=overlap(deg,a,b,sum(deg))
 assert out==(F(1,sum(deg)),F(l))
 print('PASS N=m^2',N,'m',m,'exact maximal-spin tensor Gram sqrt',l,'/',sum(deg))
print('PASS exact factorial/Beta tensor-Gram through 400 faces')
print('WARNING: these are basis-pair Gram tests, not actual corrected q-Poisson sources or full inverse')
