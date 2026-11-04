#!/usr/bin/env python3
"""Exact original-link SU(2) three-face non-character recoupling audit.
No sampling and no claim about high-spin tame inequalities. Requires SymPy.
"""
import sympy as s
v=s.symbols('a0:4 b0:4 c0:4');A=v[:4];B=v[4:8];C=v[8:12]
def mul(a,b):
 x,y,z,w=a;X,Y,Z,W=b
 return (x*X-y*Y-z*Z-w*W,x*Y+y*X+z*W-w*Z,x*Z-y*W+z*X+w*Y,x*W+y*Z-z*Y+w*X)
E=[(0,s.Rational(1,2),0,0),(0,0,s.Rational(1,2),0),(0,0,0,s.Rational(1,2))]
def X(f,k,side,i):
 h=(A,B,C)[k];d=mul(E[i],h) if side=='L' else mul(h,E[i])
 return sum(s.diff(f,x)*y for x,y in zip(h,d))
def K(f):
 return s.expand(-4*sum(X(X(f,k,'L',i),k,'L',i) for k in range(3) for i in range(3))
                 +2*sum(X(X(f,k,'R',i),k+1,'L',i) for k in range(2) for i in range(3)))
def direct(f,g):
 return s.expand(4*sum(X(f,k,'L',i)*X(g,k,'L',i) for k in range(3) for i in range(3))
   -sum(X(f,k,'R',i)*X(g,k+1,'L',i)+X(g,k,'R',i)*X(f,k+1,'L',i)
         for k in range(2) for i in range(3)))
def avgB(f):
 out=0
 for ex,co in s.Poly(f,v).terms():
  spins=ex[4:8]
  t=1 if sum(spins)==0 else s.Rational(1,4) if sum(spins)==2 and max(spins)==2 else 0
  if t:out+=co*t*s.prod(v[k]**ex[k] for k in list(range(4))+list(range(8,12)))
 return s.expand(out)
def chk(f):assert s.expand(f)==0
F=mul(A,B)[0];G=mul(B,C)[0]
chk(K(F)-s.Rational(9,2)*F);chk(K(G)-s.Rational(9,2)*G)
T=s.expand((F*K(G)+G*K(F)-K(s.expand(F*G)))/2)
chk(T-direct(F,G))
KT=K(T);chk(K(KT)-16*KT+60*T)
H=s.expand((16*T-KT)/60);chk(K(H)-T)
T6=s.expand((10*T-KT)/4);T10=s.expand((KT-6*T)/4)
chk(K(T6)-6*T6);chk(K(T10)-10*T10);chk(H-T6/6-T10/10)
R=s.expand(A[0]*C[0]+sum(A[i]*C[i] for i in range(1,4)))
chk(K(R)-6*R);chk(avgB(T)-s.Rational(3,8)*R)
chk(avgB(H)-R/16);chk(avgB(T10))
print('PASS exact original-link K, direct Gamma, K^-1, K=6/10, and physical marginal')
print('Source monomials:',len(s.Poly(T,v).terms()),'response monomials:',len(s.Poly(H,v).terms()))
