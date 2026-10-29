#!/usr/bin/env python3
"""Deterministic SU2 reflection-seam cone and five connected 3x3 geometries audit.
This is not a numerical diagonalization of a many-link Wilson Hamiltonian.
"""
import math
import numpy as np
from scipy.linalg import expm
I=np.eye(2,dtype=complex)
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1])]
def U(i):
 a=np.array([math.sin(.9+i),math.cos(1.4+2*i),math.sin(.7+3*i)])
 a/=np.linalg.norm(a);th=.3+.241*i
 return math.cos(th)*I+1j*math.sin(th)*sum((a[k]*s[k] for k in range(3)),np.zeros((2,2),complex))
def chi(j,v):
 p=np.clip(np.trace(v).real/2,-1,1);theta=math.acos(p);d=int(2*j+1)
 if theta<1e-7:return d
 if math.pi-theta<1e-7:return d*(-1)**(2*j)
 return math.sin(d*theta)/math.sin(theta)
P=[U(i) for i in range(12)]
K={}
for j in (.5,1,1.5,2,3):
 G=np.array([[chi(j,a@b.conj().T) for b in P] for a in P])
 assert np.linalg.eigvalsh(G).min()>-1e-9
 K[j]=G
W=np.exp(1.13*K[.5]/2)
assert np.linalg.eigvalsh(W).min()>-1e-9
rng=np.random.default_rng(17)
adj=rng.uniform(.01,.15,(len(P),len(P)));adj=(adj+adj.T)/2
np.fill_diagonal(adj,0)
A=np.diag(adj.sum(axis=1))-adj
S=expm(-.008*A);R=np.ones_like(W)
for it in range(200):
 R=S@(W*R)@S;R/=np.linalg.norm(R)
 assert np.linalg.eigvalsh(R).min()>-1e-10
for j,G in K.items():
 score=np.sum(R*R*G)/len(P)**2
 assert score>=-1e-10
def check(missing=None,anti=False):
 N=3;cells={(x,y) for x in range(N) for y in range(N)}
 if missing is not None:cells.remove(missing)
 rf=(lambda v:(N-v[1]-1,N-v[0]-1)) if anti else (lambda v:(v[1],v[0]))
 rv=(lambda v:(N-v[1],N-v[0])) if anti else (lambda v:(v[1],v[0]))
 assert all(rf(f) in cells for f in cells)
 E=set()
 for x,y in cells:
  vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
  for a,b in zip(vs,vs[1:]+vs[:1]):E.add(tuple(sorted((a,b))))
 assert all(tuple(sorted((rv(a),rv(b)))) in E for a,b in E)
 assert not any(tuple(sorted((rv(a),rv(b))))== (a,b) for a,b in E)
 return len(cells),len(E)
assert check()==(9,24)
for m,anti in [((0,0),False),((2,2),False),((0,2),True),((2,0),True)]:
 assert check(m,anti)==(8,22)
a=math.acos(1-.001);H=lambda z:(z-math.sin(2*z)/2)/math.pi
assert abs(H(a/2)/(.001**1.5)-math.sqrt(2)/(6*math.pi))<1e-4
print('PASS SU2 PSD characters and crossing Wilson kernels, positive-Hilbert-Schmidt Trotter, all five reflection-symmetric connected supports, Haar cap constant')
