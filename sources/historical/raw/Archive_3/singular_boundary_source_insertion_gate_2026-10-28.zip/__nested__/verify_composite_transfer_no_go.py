#!/usr/bin/env python3
"""Exact rational positive-transfer counterexample: fast coordinate sources,
slow composite source. NOT an SU(2) Wilson model; no stochastic sampling.
"""
from fractions import Fraction as Q
import json
states=[(Q(x),Q(y)) for x in (-1,1) for y in (-1,1)]
one=[Q(1)]*4
x=[s[0] for s in states]
y=[s[1] for s in states]
xy=[a*b for a,b in states]

def dot(a,b):return sum((u*v for u,v in zip(a,b)),Q(0))/4

def matvec(K,v):return [sum((row[j]*v[j] for j in range(4)),Q(0)) for row in K]

def verify(rho):
    K=[[(Q(1)+rho*xy[i]*xy[j])/4 for j in range(4)] for i in range(4)]
    assert all(z>0 for row in K for z in row)
    assert all(sum(row)==1 for row in K)
    assert all(K[i][j]==K[j][i] for i in range(4) for j in range(4))
    assert matvec(K,one)==one
    assert matvec(K,x)==[Q(0)]*4
    assert matvec(K,y)==[Q(0)]*4
    assert matvec(K,xy)==[rho*q for q in xy]
    assert dot(x,x)==dot(y,y)==dot(xy,xy)==1
    assert dot(one,x)==dot(one,y)==dot(one,xy)==0
    assert dot(x,y)==dot(x,xy)==dot(y,xy)==0
    assert all(z>=0 for z in [Q(1),rho,Q(0),Q(0)])
    return dict(rho=str(rho),min_kernel_entry=str(min(z for row in K for z in row)),
        coordinate_correlator_n1='0',composite_correlator_n1=str(rho),
        composite_correlator_n2=str(rho*rho),spectrum=['1',str(rho),'0','0'])

if __name__=='__main__':
    print(json.dumps({'cases':[verify(Q(3,4)),verify(Q(99,100)),verify(Q(9999,10000))],
        'family_has_no_uniform_gap_as_rho_tends_to_one':True,
        'note':'Logical positive-transfer counterexample; not a lattice SU2 Wilson system',
        'simulations_run':False},indent=2))
