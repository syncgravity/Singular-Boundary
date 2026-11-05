"""Corrected original-link SU2 local CG tensor engine, P-73.
Doubled-spin fusion labels. Constructs genuine collar source coefficients and
reduced electric operator without full Fourier or dense coupled-generator matrices.
The FULL invariant matrix can still grow exponentially with strip width.
"""
from functools import lru_cache
from math import sqrt
import numpy as np
from sympy import Rational
from sympy.physics.wigner import clebsch_gordan

@lru_cache(None)
def cg(a,ma,b,mb,c,mc):
 if ma+mb!=mc:return 0.
 return float(clebsch_gordan(Rational(a,2),Rational(b,2),Rational(c,2),
                             Rational(ma,2),Rational(mb,2),Rational(mc,2)))

def paths(deg):
 p=[(deg[0],)]
 for n in deg[1:]:p=[x+(j,) for x in p for j in range(abs(x[-1]-n),x[-1]+n+1,2)]
 return p

@lru_cache(None)
def tensors(deg,path):
 t=[];n=deg[0];first=np.zeros((1,n+1,n+1))
 for k in range(n+1):first[0,k,k]=1
 t.append(first)
 for i in range(1,len(deg)):
  prev=path[i-1];cur=path[i];n=deg[i];A=np.zeros((prev+1,n+1,cur+1))
  for k in range(prev+1):
   ma=prev-2*k
   for j in range(n+1):
    mb=n-2*j;mc=ma+mb
    if abs(mc)<=cur and (cur-mc)%2==0:
     A[k,j,(cur-mc)//2]=cg(prev,ma,n,mb,cur,mc)
  t.append(A)
 return tuple(t)

def spin(n):
 j=n/2;up=np.zeros((n+1,n+1),complex)
 for k in range(n):
  z=j-k-1;up[k,k+1]=sqrt((j-z)*(j+z+1))
 return [(up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(np.arange(n,-n-1,-2)/2)]

def matrix_element(deg,pa,ma,pb,mb,site,O):
 A=tensors(tuple(deg),tuple(pa));B=tensors(tuple(deg),tuple(pb))
 e=np.ones((1,1),complex)
 for i,(a,b) in enumerate(zip(A,B)):
  w=O if i==site else np.eye(deg[i]+1)
  e=np.einsum('ab,ajc,bkd,jk->cd',e,a.conj(),b,w,optimize=True)
 return e[(pa[-1]-ma)//2,(pb[-1]-mb)//2]

def product_overlap(deg,p,M,vecs):
 e=np.ones(1,complex)
 for v,A in zip(vecs,tensors(tuple(deg),tuple(p))):
  e=np.einsum('a,ajb,j->b',e,A.conj(),v,optimize=True)
 return e[(p[-1]-M)//2]

def physical_collar_terms(N,m,ell,j):
 a=[np.eye(2,dtype=complex)[:,i%2] for i in range(N)]
 b=[np.eye(2,dtype=complex)[:,1-i%2] for i in range(N)]
 C=np.zeros((2,m+1,ell+1),complex)
 for i in range(2):
  for k in range(m+1):
   for h in range(ell+1):C[i,k,h]=cg(1,1-2*i,m,m-2*k,ell,ell-2*h)
 deg=[1]*N;deg[j]=ell
 def compress(v,k):
  out=[x.copy() for x in v]
  out[j]=v[j]@C[:,k,:]
  return out
 terms=[];delta=(3+m*(m+2)-ell*(ell+2))/2
 for k in range(m+1):terms.append((delta,compress(a,k),compress(b,k)))
 for i in (j-1,j):
  if not (0<=i<N-1):continue
  for h in range(3):
   inp=spin(1)[h];out1=spin(deg[i])[h];out2=spin(deg[i+1])[h]
   for k in range(m+1):
    u=compress(a,k);v=compress(b,k)
    u[i]=out1@u[i];v[i+1]=out2@v[i+1]
    terms.append((1.,u,v))
    u=[x.copy() for x in a];v=[x.copy() for x in b]
    u[i]=inp@u[i];v[i+1]=inp@v[i+1]
    terms.append((-1.,compress(u,k),compress(v,k)))
 assert len(terms)<=13*(m+1)
 return terms

def projected_source_coordinates(deg,labels,terms):
 pp=sorted({p for p,q in labels}|{q for p,q in labels})
 out=np.zeros(len(labels),complex)
 for c,u,v in terms:
  aa={};bb={}
  for p in pp:
   for M in range(p[-1],-p[-1]-1,-2):
    aa[p,M]=product_overlap(deg,p,M,u)
    bb[p,M]=product_overlap(deg,p,M,v)
  for i,(p,q) in enumerate(labels):
   out[i]+=c*sum(aa[p,M]*bb[q,M].conjugate()
                 for M in range(p[-1],-p[-1]-1,-2))
 return out

def electric_restricted_local(deg):
 pp=paths(deg);labels=[(p,q) for p in pp for q in pp if p[-1]==q[-1]]
 D=sum(n*(n+2) for n in deg)
 local=[spin(n) for n in deg]
 @lru_cache(None)
 def gamma(i,a,p,mp,q,mq):
  if abs(mp-mq)>2:return 0j
  return matrix_element(deg,p,mp,q,mq,i,local[i][a])
 K=np.zeros((len(labels),len(labels)),complex)
 for col,(p,q) in enumerate(labels):
  J=p[-1]
  for row,(r,s) in enumerate(labels):
   if p==r and q==s:K[row,col]+=D
   L=r[-1]
   for i in range(len(deg)-1):
    for a in range(3):
     for mp in range(J,-J-1,-2):
      for mr in range(L,-L-1,-2):
       if abs(mr-mp)>2:continue
       x=gamma(i,a,r,mr,p,mp)
       if x!=0:
        K[row,col]-=2/(J+1)*x*gamma(i+1,a,q,mp,s,mr)
 return labels,K
