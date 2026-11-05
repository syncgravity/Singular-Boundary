#!/usr/bin/env python3
"""Genuine corrected SU2 q=0 Poisson collar maximal-spin source, exact rational CG.
Computes selected N=m² source traces without dense Fourier or numerical Haar.
NOT the full physical nuclear response or complete inverse.
"""
from sympy import Matrix,zeros,S,Rational,sqrt,I,binomial,simplify,conjugate
from sympy.physics.wigner import clebsch_gordan
from functools import lru_cache
@lru_cache(None)
def spin(n):
 j=Rational(n,2);up=zeros(n+1)
 for k in range(n):
  z=j-k-1
  up[k,k+1]=sqrt((j-z)*(j+z+1))
 return ((up+up.T)/2,(up-up.T)/(2*I),Matrix.diag(*[j-k for k in range(n+1)]))
@lru_cache(None)
def cg_arr(m,ell):
 return [[[clebsch_gordan(Rational(1,2),Rational(m,2),Rational(ell,2),Rational(1-2*i,2),Rational(m-2*k,2),Rational(ell-2*h,2)) for h in range(ell+1)] for k in range(m+1)] for i in range(2)]
def compressed(vec,j,k,arr):
 out=[v.copy() for v in vec]
 out[j]=Matrix([sum(vec[j][f]*arr[f][k][h] for f in (0,1)) for h in range(len(arr[0][0]))])
 return out
def poly(deg,ket):
 d={0:S.One}
 for n,vec in zip(deg,ket):
  nz=[(k,vec[k]*sqrt(binomial(n,k))) for k in range(n+1) if vec[k]!=0]
  nxt={}
  for a,u in d.items():
   for b,v in nz:nxt[a+b]=nxt.get(a+b,S.Zero)+u*v
  d=nxt
 return d
def maxspin_overlap(deg,ket,bra):
 a=poly(deg,ket);b=poly(deg,bra);L=sum(deg)
 return sum((u*conjugate(b[k])/binomial(L,k) for k,u in a.items() if k in b),S.Zero)
def actual_source(N,m,j,ell):
 a=[Matrix([1,0]) if i%2==0 else Matrix([0,1]) for i in range(N)]
 b=[Matrix([0,1]) if i%2==0 else Matrix([1,0]) for i in range(N)]
 deg=[1]*N;deg[j]=ell;arr=cg_arr(m,ell)
 value=S.Zero
 delta=Rational(3+m*(m+2)-ell*(ell+2),2)
 for k in range(m+1):
  value+=delta*maxspin_overlap(deg,compressed(a,j,k,arr),compressed(b,j,k,arr))
 for i in (j-1,j):
  if i<0 or i>=N-1:continue
  for h in range(3):
   Gin=spin(1)[h];GoutL=spin(deg[i])[h];GoutR=spin(deg[i+1])[h]
   for k in range(m+1):
    u=compressed(a,j,k,arr);v=compressed(b,j,k,arr)
    u[i]=GoutL*u[i];v[i+1]=GoutR*v[i+1]
    value+=maxspin_overlap(deg,u,v)
    u=[x.copy() for x in a];v=[x.copy() for x in b]
    u[i]=Gin*u[i];v[i+1]=Gin*v[i+1]
    value-=maxspin_overlap(deg,compressed(u,j,k,arr),compressed(v,j,k,arr))
 value=simplify(value)
 assert value.is_Rational,(N,m,j,ell,value)
 return value
cases={
 (10,3,0,2):-Rational(23,1540),(10,3,5,4):-Rational(1,132),
 (16,4,0,3):-Rational(361,875160),(16,4,8,5):-Rational(7,36465),
 (36,6,0,5):-Rational(12587,14102760256200),
 (100,10,0,9):-Rational(148349,1120902837901218187949766844514160),
 (400,20,0,19):-Rational(15503,61269470221931091170701758881844885546464537288625786274605224783664337944176829919193814195427635840644583267816575608800),
 (400,20,200,21):-Rational(421,4128395255430118762216332800848119668964158107781213694217447288994525628143343539793297480310957367357718348760021642212)
}
for p,expected in cases.items():
 got=actual_source(*p);assert got==expected,(p,got,expected)
 print('PASS exact corrected physical q0 maximal-spin source',p,got)
print('PASS',len(cases),'exact physical source checks up to N=400; complete response OPEN')
