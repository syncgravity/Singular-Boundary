#!/usr/bin/env python3
"""Symbolic exact Kato coefficients for SU2 one-rhombus source; no MCMC."""
import sympy as s
a=s.symbols('a',positive=True)
E=[0,3*a,8*a,15*a,24*a]; n=len(E)
V=s.eye(n); P2=s.zeros(n)
for j in range(n-1):V[j,j+1]=V[j+1,j]=-s.Rational(1,2)
P2[0,0]=s.Rational(1,4); P2[0,2]=P2[2,0]=s.Rational(1,4)
for j in range(1,n):
    P2[j,j]=s.Rational(1,2)
    if j+2<n:P2[j,j+2]=P2[j+2,j]=s.Rational(1,4)
def energy2(i):return s.simplify(sum((V[j,i]**2/(E[i]-E[j]) for j in range(n) if j!=i),s.Integer(0)))
def tangent(i):
    return s.Matrix([V[j,i]/(E[i]-E[j]) if j!=i else 0 for j in range(n)])
e0=s.eye(n)[:,0];e1=s.eye(n)[:,1]
overlap=s.simplify((tangent(1).T*P2*e0+e1.T*P2*tangent(0))[0])
assert energy2(0)==-1/(12*a)
assert energy2(1)==1/(30*a)
assert overlap==1/(15*a)
print({'ground_E2':str(energy2(0)),'first_excited_E2':str(energy2(1)),'p2_first_overlap':str(overlap),'simulation':False})
