#!/usr/bin/env python3
"""Exact static covariance and coherent-mode fixtures; no gauge-field sampling."""
from fractions import Fraction as F
from itertools import product
import json
# Verify independent Rademacher sign covariance removal.
C=[[F(3,8) if i==j else F(1,8) for j in range(3)] for i in range(3)]
w=[F(1),F(2),F(3)]
vals=[]
for signs in product((-1,1),repeat=3):
    vals.append(sum((F(signs[i]*signs[j])*w[i]*w[j]*C[i][j] for i in range(3) for j in range(3)),F(0)))
assert sum(vals,F(0))/8==sum((w[i]**2*C[i][i] for i in range(3)),F(0))
res=[]
for m in (2,3,4,8,16,64):
    h=F(1,m);N=m*m;q=h*h
    var=4*h*h*N*N*q*(1-q)
    signvar=4*h*h*N*q*(1-q)
    assert var==4*(1-h*h)
    res.append({"h":str(h),"smooth_var":str(var),"sign_avg_var":str(signvar),"mean_deficit":str(2*q)})
print(json.dumps({"rademacher_identity":"PASS","coherent_fixture":res,"no_simulation":True},indent=2))
