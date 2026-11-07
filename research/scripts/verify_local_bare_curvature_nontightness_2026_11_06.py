#!/usr/bin/env python3
"""Haar cap, physical subcube face count, arbitrary-correlation fraction, scaling checks.
Analytic theorem uses interacting-vacuum per-link Fisher and SU2 Sobolev estimates;
this script does not sample the interacting vacuum.
"""
import math
import numpy as np
from scipy.integrate import quad
checks=0
CV=4*math.sqrt(2)/(3*math.pi)
for d in np.geomspace(1e-5,1,201):
    th=math.acos(1-d)
    v=(th-math.sin(th)*math.cos(th))/math.pi
    alt=quad(lambda t:(2/math.pi)*math.sqrt(max(0,2*t-t*t)),0,d,epsabs=1e-12)[0]
    assert abs(v-alt)<3e-11,(d,v,alt)
    assert alt<=CV*d**1.5*(1+1e-6),(d,alt,CV*d**1.5)
    checks+=2
for n in range(8,101):
    plane=sum(1 for a in range(n) if .25<=(a+.5)/n<=.75)
    normal=sum(1 for a in range(n+1) if .25<=a/n<=.75)
    N=3*plane*plane*normal
    assert N>=.08*n**3,(n,N/n**3)
    checks+=1
for m in range(1,51):
    x=np.arange(m+1)/m
    rng=np.random.default_rng(m)
    for _ in range(100):
        q=rng.random(m+1);q/=q.sum()
        E=float(np.dot(q,x));prob=float(q[x>=.25].sum())
        if E>=.5:assert prob>=(E-.25)/.75-1e-12
        checks+=1
for t in np.geomspace(1e-8,1e5,300):
    assert t/(t+32)>=min(1,t)/33-1e-14
    checks+=1
assert checks==5795,checks
print("PASS",checks,"deterministic checks")
