#!/usr/bin/env python3
import sympy as s
L=s.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
assert set(L.eigenvals())=={4-s.sqrt(2),s.Integer(4),4+s.sqrt(2)}
I=s.eye(3); vals=list(L.eigenvals()); R=s.zeros(3)
for v in vals:
 p=I
 for w in vals:
  if w!=v:p=p*(L-w*I)/(v-w)
 R+=s.sqrt(v)*p
assert s.simplify(R*R-L)==s.zeros(3)
assert all(s.simplify(sum(R[i,j]**2 for j in range(3))-4)==0 for i in range(3))
print('Exact square-root incidence identities pass; no Monte Carlo')
