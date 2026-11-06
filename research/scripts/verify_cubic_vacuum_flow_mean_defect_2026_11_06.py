#!/usr/bin/env python3
"""Deterministic calibration for R3 quantum-vacuum-to-flow mean-defect theorem.
Not a simulation of the interacting vacuum or nonlinear flow."""
import math
from scipy.special import ive

def ratio(t):
    return ive(2, 2*t)/ive(1, 2*t)

checks=0
for n in range(1,101):
    E=3*n*(n+1)**2
    P=3*n*n*(n+1)
    assert abs(E/P-(n+1)/n)<1e-14
    assert 1<E/P<=2
    checks+=2

for t in [0.01,0.1,0.5,1,2,5,10,30,100,300,1000]:
    r=ratio(t)
    assert 0<r<1
    assert 0<=1-r<=3/(2*t)+1e-12
    assert 1-r**4<=6/t+1e-12
    checks+=3

for n in [1,2,4,8,16,32]:
    E=3*n*(n+1)**2
    P=3*n*n*(n+1)
    for g2 in [0.1,0.3,1.0,2.0]:
        h=1/n
        alpha=g2/(2*h)
        beta=2/(g2*h)
        t=4*math.sqrt(beta*P/(alpha*E))
        r=ratio(t)
        trial=alpha*E*3*t*r/8 + beta*P*(1-r**4)
        bound=3*math.sqrt(alpha*beta*E*P)
        assert trial<=bound*(1+1e-13)
        assert bound/beta/P <= (3*g2/2)*math.sqrt(E/P)*(1+1e-13)
        checks+=2
print(f"PASS: {checks} assertions")
