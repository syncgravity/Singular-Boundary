#!/usr/bin/env python3
"""Exact rational checks for the source hierarchy; no Monte Carlo."""
from fractions import Fraction as F
from itertools import product
import json
def walsh(x,mask):
    z=F(1)
    for i,v in enumerate(x):
        if mask>>i&1:z*=v
    return z
out=[]
for k in (2,3,4):
    states=list(product((-1,1),repeat=k)); n=len(states)
    rho=F(9999,10000); delta=F(1,8); q=(1<<k)-1
    T=[[(delta if i==j else F(0))+(1-delta)*(1+rho*walsh(a,q)*walsh(b,q))/n for j,b in enumerate(states)] for i,a in enumerate(states)]
    assert all(min(row)>0 and sum(row)==1 for row in T)
    for mask in range(n):
        ev=F(1) if mask==0 else delta+(1-delta)*rho if mask==q else delta
        v=[walsh(a,mask) for a in states]
        assert [sum(T[i][j]*v[j] for j in range(n)) for i in range(n)]==[ev*z for z in v]
    out.append({'k':k,'slow_parity_eigenvalue':str(delta+(1-delta)*rho),'all_proper_nonconstant_eigenvalues':str(delta)})
print(json.dumps({'exact_hierarchy_checks':out,'monte_carlo':False,'physical_gap_proved':False},indent=2))
