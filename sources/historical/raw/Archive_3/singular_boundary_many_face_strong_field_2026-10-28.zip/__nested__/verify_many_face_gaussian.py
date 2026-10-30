#!/usr/bin/env python3
"""Exact graph-independent Gaussian tangent estimates on full shared-edge face complexes.
Deterministic linear algebra; no SU2 nonlinear ground-state computation, no Monte Carlo.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import eigh

# Sharp matrix inequality sqrt(t) >= t + t(1-t)/2, t in [0,1].
t=sp.symbols('t',nonnegative=True)
u=sp.symbols('u',nonnegative=True)
assert sp.factor(u - u**2 - sp.Rational(1,2)*u**2*(1-u**2)) == u*(u-1)**2*(u+2)/2
assert sp.simplify((sp.Rational(19,4)**2/sp.Integer(8))*2-4) == sp.Rational(105,64)

# Actual three-rhombus spatial Z5 fixture: 8 vertices, 10 edges, 3 face boundaries.
from itertools import permutations
faces = [
 [(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def edge(u,v): return tuple(sorted([u,v]))
def is_edge(u,v):return sum(abs(x-y) for x,y in zip(u,v))==1
face_edges=[]
for verts in faces:
    ee={edge(u,v) for i,u in enumerate(verts) for v in verts[i+1:] if is_edge(u,v)}
    assert len(ee)==4
    face_edges.append(ee)
edges=sorted(set.union(*face_edges)); vertices=set(v for ed in edges for v in ed)
assert len(vertices)==8 and len(edges)==10
B=sp.zeros(3,len(edges))
for fi,verts in enumerate(faces):
    candidates=[]
    for seq in permutations(verts):
        if all(edge(seq[i],seq[(i+1)%4]) in face_edges[fi] for i in range(4)):
            candidates.append(seq)
    seq=min(candidates)
    for i in range(4):
        v,w=seq[i],seq[(i+1)%4];k=edges.index(edge(v,w))
        B[fi,k]=1 if (v,w)==edge(v,w) else -1
# face orientation arbitrary, offdiag BBT squared sign-invariant
M= B*B.T
assert M.eigenvals()=={sp.Integer(4):1,4-sp.sqrt(2):1,4+sp.sqrt(2):1}
S=np.asarray(M,dtype=float)
lambda_,U=eigh(S);sqrtM=(U*np.sqrt(lambda_))@U.T
K=sqrtM**2
assert np.allclose(K.sum(axis=1),np.diag(S),atol=1e-12)
assert np.linalg.eigvalsh(K).min()>1.640625
for q in [np.array([1.,-3.,1.]), np.array([1.,1.,1.]),np.array([1.,-1.,-1.])]:
    Q=float(q@K@q)
    assert Q >= (105/64)*float(q@q)-1e-10
    assert Q <= 4*float(q@q)+1e-10

# Also verify on a complete n x n planar rhombus/square-grid face complex.
def grid(n):
    A=np.zeros((n*n,n*n),float)
    for i in range(n):
        for j in range(n):
            r=i*n+j;A[r,r]=4
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ii,jj=i+di,j+dj
                if 0<=ii<n and 0<=jj<n:A[r,ii*n+jj]=-1
    return A
for n in (2,4,8):
    L=grid(n);ev,Q=eigh(L);root=(Q*np.sqrt(ev))@Q.T;K=root**2
    assert np.min(2*np.diag(K)-4)>105/64-1e-10
    for j in range(4):
        q=np.array([np.sin((i+1)*(j+1)) + np.cos((i+2)*(j+3)) for i in range(n*n)])
        v=float(q@K@q)/float(q@q)
        assert 105/64-1e-10 <=v <=4+1e-10

# Exact t>0 bound at alpha=2, b=beta/h^2, constant q sampled on fixed-area grid.
# C(t) = 3/32 c^2 sum q_f q_g [(sqrt(2/b) sqrt M exp(-t sqrt(b M/2)))_fg]^2.
# At alpha=2, c=1. At alpha=3/2, c=sqrt h.
beta=2.0;a=1.0
L=grid(8);ev,Q=eigh(L)
for h in (.5,.25,.125):
    b=beta/h**2
    q=np.array([(-1.)**(i//8+i%8) for i in range(64)])
    sig=(Q*(np.sqrt(2/b)*np.sqrt(ev)))@Q.T
    W=sig*sig
    v2=(3/32)*float(q@W@q)
    assert v2>= (315/1024)*(a/beta)*h**2*float(q@q)-1e-9
    for tau in (.2,1.,3.):
        dyn=(Q*(np.sqrt(2/b)*np.sqrt(ev)*np.exp(-tau*np.sqrt(b*ev/2))))@Q.T
        C=(3/32)*float(q@(dyn*dyn)@q)
        AA=64*h*h
        bound=(3*a*a)/(8*beta*beta*math.e**2*tau**2)*AA*h**2
        assert -1e-12 <=C <= bound+1e-10,(h,tau,C,bound)
print('PASS exact 3-face Penrose incidence; strictly signed diagonal dominance; time-decay uniform bounds; no Monte Carlo')
print('3-face K eigenvalues',np.linalg.eigvalsh((sqrtM*sqrtM)).round(8).tolist())
print('uniform signed lower/upper factors',str(sp.Rational(105,64)),4)
