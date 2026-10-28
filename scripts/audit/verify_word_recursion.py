#!/usr/bin/env python3
"""Read-only exact checks of SU2 character recursion and Wilson trace algebra."""
from fractions import Fraction as F
import sympy as s
from itertools import product
import json
theta,a=s.symbols('theta a',positive=True)
energies=[]
for n in range(7):
    y=s.sin((n+1)*theta)
    assert s.simplify(-a*s.diff(y,theta,2)-a*y-a*n*(n+2)*y)==0
    energies.append(n*(n+2))
paths={}
for steps in range(6):
    d={0:1}
    for _ in range(steps):
        nxt={}
        for j,c in d.items():
            nxt[j+1]=nxt.get(j+1,0)+c
            if j:nxt[j-1]=nxt.get(j-1,0)+c
        d=nxt
    assert sum(d.values())<=2**steps
    paths[steps]=d
def mul(x,y):
    a,u=x[0],x[1:];b,v=y[0],y[1:]
    dot=sum((i*j for i,j in zip(u,v)),F(0))
    cross=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
    return (a*b-dot,)+tuple(a*j+b*i-c for i,j,c in zip(u,v,cross))
def inv(x):return (x[0],)+tuple(-v for v in x[1:])
def tr(x):return 2*x[0]
Z=F(0);I=(F(1),Z,Z,Z);X=(Z,F(1),Z,Z);Y=(Z,Z,F(1),Z)
S=[I,X,Y,(Z,Z,Z,F(1)),(F(3,5),F(4,5),Z,Z),(F(5,13),Z,F(12,13),Z)]
for x,y in product(S,repeat=2):
    assert tr(x)*tr(y)==tr(mul(x,y))+tr(mul(x,inv(y)))
print(json.dumps({'electric_energies_over_a':energies,'paths':paths,
'trace_pairs_checked':len(S)**2,'stochastic_simulation':False,'physical_gap_proved':False},indent=2))
