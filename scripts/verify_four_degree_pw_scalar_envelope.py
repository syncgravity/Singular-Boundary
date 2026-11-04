#!/usr/bin/env python3
"""Exact-rational output-channel audit of the all-four-degree scalar envelope.
The all-degree theorem is analytic. This is a reproducibility regression.
"""
from fractions import Fraction
from itertools import product
max_seen=(Fraction(0),None)
checks=0
for p,q,r,s in product(range(1,17),repeat=4):
    P,Q,R,T=(z*(z+2) for z in (p,q,r,s))
    A=1+max(p,q); B=1+max(r,s)
    for l in range(abs(q-r),q+r+1,2):
        c=P+T+l*(l+2); W=1+max(p,l,s)
        e=Fraction(W,A*B)*(Fraction(1,2)+Fraction(5*(P+Q+R+T),4*c))
        assert e<6,(p,q,r,s,l,e)
        assert c>=6 and W<=A+B
        assert q<=r+l and r<=q+l
        assert Fraction(Q,A*B)<=Fraction(3+l,2)
        assert Fraction(R,A*B)<=Fraction(3+l,2)
        checks+=1
        if e>max_seen[0]:max_seen=(e,(p,q,r,s,l))
assert 6*25>144   # sqrt(6)>12/5, since 6>144/25.
assert Fraction(29,8)+Fraction(25,12)<6 # 29/8+5/sqrt(6)<6
print('PASS',checks,'exact-rational output-channel and component inequalities')
print('Largest sampled envelope:',*max_seen)
print('PASS all-spin algebraic constant 29/8 + 5/sqrt(6) < 6')
