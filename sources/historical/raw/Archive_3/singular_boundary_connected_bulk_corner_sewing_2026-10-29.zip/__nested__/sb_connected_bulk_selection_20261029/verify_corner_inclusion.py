#!/usr/bin/env python3
"""Exact symbolic verification of the four-corner even-interaction response identity.
No numerical lattice-vacuum claim.
"""
import sympy as s
x=s.symbols('x0:4', real=True)
a=s.symbols('alpha', positive=True)
# Every nonconstant term contains at least three distinct even corner powers.
F=a*a + s.Rational(2,7)*x[0]**2*x[1]**4*x[2]**2 -s.Rational(1,5)*x[1]**2*x[2]**2*x[3]**4 + s.Rational(3,8)*s.prod(t**2 for t in x) + s.Rational(1,19)*s.prod(t**4 for t in x)
assert all(s.simplify(F.subs({x[i]:0 for i in range(4) if i not in inds})-a*a)==0 for inds in [(),(0,), (1,2), (0,3)])

rhs=a*a
for mask in range(1<<4):
    inds=[i for i in range(4) if mask>>i&1]
    if len(inds)<3:continue
    y=F.subs({x[k]:0 for k in range(4) if k not in inds})
    for k in inds:y=s.diff(y,x[k],2)*(1-x[k])
    for k in inds:y=s.integrate(y,(x[k],0,1))
    rhs+=y
assert s.simplify(rhs-F.subs({v:1 for v in x}))==0
print('PASS exact full-coupling 3-corner + 4-corner second-derivative interaction formula')

# A positive (but not physical) even comparator where the endpoint is Haar while
# the unnormalized one-sided mixed response is positive of arbitrarily high size.
# All four neighboring variables have 2 factors, and 3 corners have >=2 factors.
r=s.symbols('r0:4',real=True)
y=s.symbols('y0:4',real=True)
M=s.symbols('M',positive=True)
G=a*a*(1+M*s.prod(t*t*(1-t*t) for t in r)*s.prod(y[i]**2 for i in (0,1,2)))
assert s.simplify(G.subs({t:1 for t in r+y})-a*a)==0
assert s.simplify(G.subs({t:0 for t in r[:1]})-a*a)==0
assert s.simplify(G.subs({y[1]:0})-a*a)==0
H=G
for t in r:H=s.diff(H,t,2)
# At r_i=1, the four second derivatives are negative, product positive.
# At r=(1,1,1,0), three negative, one positive, hence integrand negative.
negvalue=s.simplify(H.subs({r[0]:1,r[1]:1,r[2]:1,r[3]:0,y[0]:1,y[1]:1,y[2]:1}))
assert negvalue<0
print('PASS smooth positive comparator: signed endpoint response cancels but adverse-part budget nonzero')
