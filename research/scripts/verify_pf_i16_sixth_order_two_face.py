#!/usr/bin/env python3
"""PF-I16: exact degree-six quantum energy on two shared-edge SU(2) source faces.
Full standalone exact + generalized-eigenvalue verifier is in the PF-I16 Library ZIP.
This program independently reconstructs the exact rational polynomial recurrence.
"""
import sympy as s
from math import factorial
from functools import lru_cache
from itertools import product
x,y,z=s.symbols("x y z")
@lru_cache(None)
def sphere(a):
    if any(v%2 for v in a):return s.S.Zero
    v=s.S.One
    for q in a:
        for j in range(q//2):v*=s.Rational(2*j+1,2)
    for j in range(sum(a)//2):v/=j+2
    return v
@lru_cache(None)
def moment(i,j,k):
    out=s.S.Zero
    for a in range(k+1):
        for b in range(k-a+1):
            for c in range(k-a-b+1):
                d=k-a-b-c
                coeff=s.Rational(factorial(k),factorial(a)*factorial(b)*factorial(c)*factorial(d))
                out+=coeff*(-1)**(b+c+d)*sphere((i+a,b,c,d))*sphere((j+a,b,c,d))
    return out
def mean(p):
    return sum(v*moment(*m) for m,v in s.Poly(s.expand(p),x,y,z).terms())
def K(p):
    return s.expand(3*x*s.diff(p,x)+3*y*s.diff(p,y)+s.Rational(9,2)*z*s.diff(p,z)
     -(1-x*x)*s.diff(p,x,2)-(1-y*y)*s.diff(p,y,2)
     -s.Rational(3,2)*(1-z*z)*s.diff(p,z,2)
     -(z-x*y)*s.diff(p,x,y)/2
     -s.Rational(3,2)*(y-x*z)*s.diff(p,x,z)
     -s.Rational(3,2)*(x-y*z)*s.diff(p,y,z))
basis=sorted([(a,b,c) for c in range(4) for a in range(7) for b in range(7) if a+b+2*c<=6],key=lambda a:(sum(a),a))
assert len(basis)==50
polys=[x**a*y**b*z**c for a,b,c in basis]
pos={m:i for i,m in enumerate(basis)}
M=s.zeros(50)
for j,v in enumerate(polys):
    for m,c in s.Poly(K(v),x,y,z).terms():M[pos[m],j]=c
one=s.Matrix([int(m==(0,0,0)) for m in basis])
M=(M+one*s.Matrix([[moment(*m) for m in basis]])).inv()
def solve(p):
    rhs=s.zeros(50,1)
    for m,c in s.Poly(s.expand(p),x,y,z).terms():rhs[pos[m]]+=c
    result=s.expand(sum((M*rhs)[j]*polys[j] for j in range(50)))
    assert s.expand(K(result)-p)==0
    assert mean(result)==0
    return result
wave=[{0:s.S.One}]; energies=[{}]
for n in range(1,7):
    psi={};e={}
    for j in range(n+1):
        rhs=x*wave[n-1].get(j,0)+y*wave[n-1].get(j-1,0)
        for order in range(2,n):
            for power,co in energies[order].items():
                rhs+=co*wave[n-order].get(j-power,0)
        e[j]=-mean(rhs)
        rhs=s.expand(rhs+e[j])
        psi[j]=solve(rhs) if rhs!=0 else s.S.Zero
    wave.append(psi);energies.append(e)
    print('order',n,'energy',e)
assert energies[2][0]==-s.Rational(1,12)
assert energies[4][2]==-s.Rational(1,8424)
assert energies[6][0]==-s.Rational(289,4976640)
assert energies[6][2]==energies[6][4]==s.Rational(22285,3027787776)
assert all(v==0 for n in (1,3,5) for v in energies[n].values())
print("PASS: exact independent b,c coefficients through degree six")
