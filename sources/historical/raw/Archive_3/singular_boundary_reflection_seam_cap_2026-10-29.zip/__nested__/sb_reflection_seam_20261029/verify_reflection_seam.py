#!/usr/bin/env python3
"""Deterministic SU2 character positivity and diagonal seam audit.
Finite kernel is a POSITIVITY MECHANISM comparator, not a Wilson multi-link diagonalization.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
from collections import defaultdict
I=np.eye(2,dtype=complex)
sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]

def U(i):
    a=np.array([math.sin(.9+i),math.cos(1.4+2*i),math.sin(.7+3*i)])
    a=a/np.linalg.norm(a);t=.3+.241*i
    return math.cos(t)*I+1j*math.sin(t)*sum((a[k]*sigma[k] for k in range(3)),np.zeros((2,2),complex))

def chi(j,Z):
    p=np.trace(Z).real/2
    p=max(-1.,min(1.,p))
    u=math.acos(p);d=int(2*j+1)
    if u<1e-7:return float(d)
    if math.pi-u<1e-7:return float(d*(-1)**(2*j))
    return math.sin(d*u)/math.sin(u)

points=[U(k) for k in range(12)]
chi_grams={}
for j in (0.5,1,1.5,2,3,5):
    G=np.array([[chi(j,x@y.conj().T) for y in points] for x in points])
    assert np.max(abs(G-G.T))<1e-11
    mineig=np.linalg.eigvalsh(G).min()
    assert mineig>-2e-9,(j,mineig)
    chi_grams[j]=G
    print('SU2 positive character kernel spin',j,'min eig',round(mineig,10))
p=lambda x:chi(.5,x)/2
K=np.array([[math.exp(1.13*p(x@y.conj().T)) for y in points] for x in points])
assert np.linalg.eigvalsh(K).min()>-1e-9
# A_+ : arbitrary real positive local electric kinetic + within-side Wilson potential.
rng=np.random.default_rng(17)
L=rng.uniform(0.01,.15,size=(len(points),len(points)))
L=(L+L.T)/2
np.fill_diagonal(L,0)
A=np.diag(L.sum(axis=1))-L+np.diag(np.arange(len(points))*.06)
S=expm(-.008*A)
R=np.ones_like(K)
for step in range(300):
    R=S@(K*R)@S
    R/=np.linalg.norm(R)
    m=np.linalg.eigvalsh(R).min()
    assert m>-2e-10,(step,m)
    assert np.max(abs(R-R.T))<2e-10
    assert (R>=-1e-11).all(),(step,R.min())
weights=np.ones(len(points))/len(points)
r2=R*R
assert np.linalg.eigvalsh(r2).min()>-2e-10
for j,G in chi_grams.items():
    corr=(weights[:,None]*weights[None,:]*r2*G).sum()
    assert corr>-1e-10,(j,corr)
    print('finite Hilbert-Schmidt cone character response spin',j,':',round(corr,10))

def reflection_patch(n,diag='main',missing=None):
    cells={(x,y) for x in range(n) for y in range(n)}
    if missing is not None:cells.remove(missing)
    def r(v):
        x,y=v
        return (y,x) if diag=='main' else (n-x,n-y)
    def rf(f):
        x,y=f
        return (y,x) if diag=='main' else (n-y-1,n-x-1)
    if diag=='anti':
        def r(v):
            x,y=v
            return (n-y,n-x)
    assert all(rf(f) in cells for f in cells)
    edge_set=set()
    for x,y in cells:
        vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
        for a,b in zip(vs,vs[1:]+vs[:1]):edge_set.add(tuple(sorted((a,b))))
    assert all(tuple(sorted((r(a),r(b)))) in edge_set for a,b in edge_set)
    fixed_edges=[e for e in edge_set if tuple(sorted((r(e[0]),r(e[1]))))==e]
    assert len(fixed_edges)==0, fixed_edges
    fixed_faces=[f for f in cells if rf(f)==f]
    print('patch',n,diag,'missing',missing,'faces',len(cells),'edges',len(edge_set),'fixed diagonal faces',fixed_faces)
    assert (n//2,n//2) in fixed_faces
    return len(cells),len(edge_set)
assert reflection_patch(3,'main')==(9,24)
for missing in ((0,0),(2,2)):
    assert reflection_patch(3,'main',missing)==(8,22)
for missing in ((0,2),(2,0)):
    assert reflection_patch(3,'anti',missing)==(8,22)
for delta in (.2,.05,.01,.001):
    a=math.acos(1-delta)
    H=lambda x:(x-math.sin(2*x)/2)/math.pi
    ratio=H(a/2)/delta**1.5
    assert abs(ratio-math.sqrt(2)/(6*math.pi))<.02,(delta,ratio)
    print('center-cap delta',delta,'H(a/2)',H(a/2),'ratio h^3/2',ratio)
print('PASS: exact SU2 PD character kernels, Wilson exponential Schur kernel, finite semigroup PSD preservation, 3x3 diagonal reflection pairs, Haar cap')
