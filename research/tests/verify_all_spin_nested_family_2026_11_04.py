#!/usr/bin/env python3
"""Exact all-spin two-face nested SU2 PW regression. Requires SymPy.
Run beside verify_nested_pw_2026_11_04.py."""
from fractions import Fraction
import sympy as sp
import verify_nested_pw_2026_11_04 as physical

def block(n, sign):
    l=n+sign; dplus=Fraction(l,4); E=l*(l+2)+3
    alpha=-n if sign==1 else n+2
    beta=Fraction(-1 if sign==1 else 1,n+1)
    plus=(alpha+beta*dplus)/(E+2*dplus)
    if not l: return 2*abs(plus),(plus,Fraction(0))
    dminus=Fraction(-(l+2),4)
    minus=(alpha+beta*dminus)/(E+2*dminus)
    A=(dplus*minus-dminus*plus)/(dplus-dminus)
    B=(plus-minus)/(dplus-dminus)
    return (l+2)*abs(plus)+l*abs(minus),(A,B)

def rat(n):
    return sum(2*(n+s+1)*(1+max(n+s,1))*block(n,s)[0]
               for s in (-1,1))/Fraction(64*(n+1)**3)

n=sp.symbols("n",positive=True,integer=True)
bp=(n+2)*(8*n**3+32*n**2+39*n-3)/((2*n**2+7*n+9)*(2*n**2+9*n+13))
bm=n*(8*n**3+16*n**2+7*n+17)/((2*n**2-n+3)*(2*n**2+n+3))
for N in range(1,513):
    assert sp.Rational(block(N,1)[0])==bp.subs(n,N)
    assert sp.Rational(block(N,-1)[0])==bm.subs(n,N)
    assert 0<rat(N)<=Fraction(1,16),N
assert rat(1)==Fraction(35,1024)
m=sp.symbols("m",nonnegative=True)
assert sp.expand(2*(2*n**2+7*n+9)*(2*n**2+9*n+13) -(n+2)*(8*n**3+32*n**2+39*n-3))==16*n**3+111*n**2+269*n+240
assert sp.expand((3*(2*n**2-n+3)*(2*n**2+n+3)-n*(8*n**3+16*n**2+7*n+17)).subs(n,m+1))==4*m**4+2*m**2+3*m+24
assert sp.limit(n*(2*(n+2)**2*bp+2*n**2*bm)/(64*(n+1)**3),n,sp.oo)==sp.Rational(1,8)

def sphere(f):
    a0,a=physical.a0,physical.a
    b0,b=physical.b0,physical.b
    f=sp.rem(sp.expand(f),a[2]**2-(1-a0**2-a[0]**2-a[1]**2),a[2])
    f=sp.rem(f,b[2]**2-(1-b0**2-b[0]**2-b[1]**2),b[2])
    return sp.factor(f)
for N in range(1,6):
    plus=sp.chebyshevu(N+1,physical.a0)
    minus=sp.chebyshevu(N-1,physical.a0)
    F=sp.chebyshevu(N,physical.a0)*physical.y
    x=physical.x
    G=sp.expand((F*physical.K(x)+x*physical.K(F)-physical.K(F*x))/2)
    expected=(-N*plus+(N+2)*minus)*physical.y-(physical.D(plus*physical.y)-physical.D(minus*physical.y))/(N+1)
    assert sphere(G-expected)==0,N
    answer=0
    for sign,chi in ((1,plus),(-1,minus)):
        _,(A,B)=block(N,sign)
        answer+=sp.Rational(A.numerator,A.denominator)*chi*physical.y+sp.Rational(B.numerator,B.denominator)*physical.D(chi*physical.y)
    assert sphere(physical.K(answer)-G)==0,N
print("PASS: 512 exact all-spin PW blocks, global rational bounds and 5 quaternion inverse regressions.")
