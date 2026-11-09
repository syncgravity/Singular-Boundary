#!/usr/bin/env python3
"""PF-I16 source-rhombus cut combinatorics and one-loop information limit."""
from itertools import combinations
import numpy as np
from scipy.linalg import eigh_tridiagonal
from numpy.polynomial.legendre import leggauss
from math import pi
edges={'a':(0,3),'b':(3,4),'c':(0,1),'s':(1,4),
       'd':(4,5),'e':(1,2),'f':(2,5)}
faces=[{'a','b','c','s'},{'s','d','e','f'}]
def is_forest(S):
    par={v:v for e in edges.values() for v in e}
    def root(x):
        while par[x]!=x: x=par[x]
        return x
    for name in S:
        x,y=edges[name]; x,y=root(x),root(y)
        if x==y: return False
        par[x]=y
    return True
for k in range(4):
    assert all(is_forest(S) for S in combinations(edges,k))
assert all(not is_forest(f) for f in faces)
def n_cross(S):
    S=set(S)
    return sum(bool(S&f and f-S) for f in faces)
assert n_cross({'s'})==2 and n_cross({'a'})==1
assert abs(n_cross({'s'})/(2*9)-1/9)<1e-15
assert abs(n_cross({'a'})/(2*9)-1/18)<1e-15
x,w=leggauss(600); theta=(x+1)*pi/2; hw=w*np.sin(theta)**2
n=np.arange(36,dtype=float)
chars=np.sin((n[:,None]+1)*theta[None,:])/np.sin(theta)[None,:]
for b in (.1,.05,.02,.01,.005,.002):
    _,vec=eigh_tridiagonal(n*(n+2)+b,np.full(len(n)-1,-b/2))
    rho=(vec[:,0]@chars)**2; rho/=hw@rho
    info=float(hw@(rho*np.log(rho)))
    assert abs(info/b**2-1/18)<4e-5
    print(f'b={b:.3g}: I/b^2={info/b**2:.12g}')
print('PASS forest/cut/character information checks')
