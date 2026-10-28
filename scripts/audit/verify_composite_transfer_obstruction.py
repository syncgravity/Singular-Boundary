#!/usr/bin/env python3
"""Exact rational positive-transfer counterexample. Not SU(2) Wilson dynamics."""
from fractions import Fraction as F
import json
states=[(F(x),F(y)) for x in (-1,1) for y in (-1,1)]
one=[F(1)]*4;x=[q[0] for q in states];y=[q[1] for q in states];xy=[a*b for a,b in states]
def act(T,v):return [sum((r[j]*v[j] for j in range(4)),F(0)) for r in T]
out=[]
for rho in [F(3,4),F(99,100),F(9999,10000)]:
 T=[[(1+rho*xy[i]*xy[j])/4 for j in range(4)] for i in range(4)]
 assert all(z>0 for row in T for z in row)
 assert act(T,one)==one and act(T,x)==[F(0)]*4 and act(T,y)==[F(0)]*4
 assert act(T,xy)==[rho*z for z in xy]
 out.append({'rho':str(rho),'min_entry':str(min(z for row in T for z in row)),'coordinate_decay_n1':'0','composite_decay_n1':str(rho)})
print(json.dumps({'cases':out,'uniform_gap_as_rho_to_one':False,'simulation':False},indent=2))
