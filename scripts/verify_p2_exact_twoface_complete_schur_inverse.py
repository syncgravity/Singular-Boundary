#!/usr/bin/env python3
"""Exact full corrected-original-link SU2 N=2,m=3 physical response in Schur traces.
Uses independent already-committed exact physical source/CG module.
"""
from sympy import Matrix,Rational,simplify,trace
from verify_p2_exact_physical_q0_schur_sympy import electric,cg,block,X
m=3
for l,expected,Kexpected,res in (
 (2,[Rational(5,4),-Rational(5,2)],Matrix([[Rational(35,3),Rational(2,3)],[Rational(4,3),Rational(28,3)]]),
  Matrix([Rational(10,81),-Rational(185,648)])),
 (4,[Rational(7,2),-Rational(9,4)],Matrix([[Rational(144,5),Rational(4,5)],[Rational(6,5),Rational(121,5)]]),
  Matrix([Rational(173,1392),-Rational(23,232)]))):
 Ls=(l-1,l+1);P=[cg(l,1,L)*cg(l,1,L).T for L in Ls]
 B=block(X,m,l)
 Y=(block(electric(X,[1,1]),m,l)+15*B-electric(B,[l,1]))/2
 v=Matrix([simplify(trace(p*Y)) for p in P])
 k=Matrix(2,2,lambda i,j:simplify(trace(P[i]*electric(P[j],[l,1]))/(Ls[j]+1)))
 x=k.inv()*v
 assert list(v)==expected and k==Kexpected and x==res
 print('PASS exact physical l',l,'source',v.T,'electric',k,'inverse traces',x.T,'S1',sum(abs(i) for i in x))
 step=v/(l*(l+2)+3);partial=Matrix([0,0]);H=k-(l*(l+2)+3)*Matrix.eye(2)
 for q in range(6):
  partial+=step
  err=sum(abs(simplify(x[i]-partial[i])) for i in range(2))
  print('  q',q,'exact S1 error',err)
  step=-H*step/(l*(l+2)+3)
R=2*(Rational(9,256)*Rational(265,648)+Rational(25,256)*Rational(311,1392))
assert R==Rational(38695,534528)
print('PASS EXACT physical weighted extensive 2-site original-link response',R,'~',R.evalf(13))
print('LIMIT: N=2,m=3 exact physical full inverse, NOT joint N~m²')
