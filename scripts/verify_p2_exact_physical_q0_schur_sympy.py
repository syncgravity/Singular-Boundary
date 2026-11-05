#!/usr/bin/env python3
"""Exact symbolic SU2 corrected original-link Poisson q0 Schur traces, N=2 m=3."""
from sympy import Matrix,eye,zeros,Rational,sqrt,I,kronecker_product,simplify,trace
from sympy.physics.wigner import clebsch_gordan
def spin(n):
 j=Rational(n,2);up=zeros(n+1)
 for k in range(n):
  z=j-k-1;up[k,k+1]=sqrt((j-z)*(j+z+1))
 return ((up+up.T)/2,(up-up.T)/(2*I),Matrix.diag(*[j-k for k in range(n+1)]))
def K(F,degrees):
 a,b=degrees;D=sum(n*(n+2) for n in degrees)
 return D*F-2*sum((kronecker_product(x,eye(b+1))*F*kronecker_product(eye(a+1),y) for x,y in zip(spin(a),spin(b))),zeros(F.rows))
def cg(a,b,L):
 A=zeros((a+1)*(b+1),L+1)
 for i in range(a+1):
  for j in range(b+1):
   for k in range(L+1):
    A[i*(b+1)+j,k]=clebsch_gordan(Rational(a,2),Rational(b,2),Rational(L,2),Rational(a-2*i,2),Rational(b-2*j,2),Rational(L-2*k,2))
 return A
def source_block(F,m,l):
 C=cg(1,m,l);U=kronecker_product(C,eye(2));T=zeros(4*(m+1))
 for i in range(2):
  for j in range(2):
   for k in range(m+1):
    T[(i*(m+1)+k)*2+j,(i*2+j)*(m+1)+k]=1
 return U.T*T*kronecker_product(F,eye(m+1))*T.T*U
X=zeros(4);X[1,2]=1;m=3
for l,expected in ((2,[Rational(5,4),-Rational(5,2)]),(4,[Rational(7,2),-Rational(9,4)])):
 B=source_block(X,m,l)
 Z=(source_block(K(X,[1,1]),m,l)+m*(m+2)*B-K(B,[l,1]))/2
 vals=[]
 for L in (l-1,l+1):
  C=cg(l,1,L);vals.append(simplify(trace(C*C.T*Z)))
 assert vals==expected,(l,vals,expected)
 print('PASS exact rational source traces',l,vals,'Schur S1',sum(abs(x) for x in vals))
print('Scope: actual corrected physical q=0 output N=2,m=3; NOT N=m² or complete inverse.')
