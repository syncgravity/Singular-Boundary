#!/usr/bin/env python3
"""Exact SU(2) shared-link mixed f-sum and center-even Markov countermodel.

No Monte Carlo, no Penrose ground-state simulation.  SU(2) derivative tests use
fixed deterministic pseudorandom noncommuting matrices for algebraic identity.
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp
from scipy.linalg import eigh

sig=[np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]],complex),
     np.diag([1,-1]).astype(complex)]
tau=[1j*s/2 for s in sig]
rng=np.random.default_rng(20261029)
def su2():
    q=rng.normal(size=4);q=q/np.linalg.norm(q)
    return q[0]*np.eye(2)+1j*sum((q[k+1]*sig[k] for k in range(3)),np.zeros((2,2),complex))
def p(A):return float(np.trace(A).real/2)
maxerr=0.;npos=0;nneg=0
for _ in range(128):
    U,X,Y=su2(),su2(),su2()
    f=p(U@X);g=p(U.conj().T@Y)
    df=np.array([np.trace(t@U@X).real/2 for t in tau])
    dg=np.array([-np.trace(U.conj().T@t@Y).real/2 for t in tau])
    left=float(df@dg);right=(p(X@Y)-f*g)/4
    err=abs(left-right);maxerr=max(err,maxerr)
    assert err<1e-13
    assert abs(p(X@Y)-f*g)<=np.sqrt(max(0,1-f*f)*max(0,1-g*g))+1e-13
    npos+=left>0;nneg+=left<0
assert npos>10 and nneg>10
print('SU2 exact shared-link Fierz: 128 noncommuting checks, max abs error',f'{maxerr:.3g}')
print('SU2 local gradient signs:',npos,'positive,',nneg,'negative')

# Reversible six-state, nearest-neighbor graph diffusion.  Only link 2--3 is weak.
z=sp.symbols('z',positive=True)
L=sp.zeros(6)
for i in range(5):
    c=z if i==2 else sp.Integer(1)
    L[i,i]+=c;L[i+1,i+1]+=c;L[i,i+1]-=c;L[i+1,i]-=c
P=sp.ones(6,6)/6
G=(L+P).inv()-P
mom1=sp.factor(L[0,2]/6)
mom_minus1=sp.factor(G[0,2]/6)
assert mom1==0
assert sp.simplify(mom_minus1-(1/(24*z)-sp.Rational(1,27)))==0
print('Six-state Markov exact mixed first moment:',mom1)
print('Six-state Markov exact inverse-energy mixed moment:',mom_minus1)

# Build exact center-even, positivity-improving 12-state model (two identical
# copies connected by a second independent positive Markov laplacian).
C2=np.array([[0,1],[1,0]],dtype=float)
L2=np.eye(2)-C2
for eps in (F(1,4),F(1,16),F(1,64),F(1,256)):
    K6=np.array(L.subs(z,sp.Rational(eps.numerator,eps.denominator)),dtype=float)
    K=np.kron(K6,np.eye(2))+np.kron(np.eye(6),L2)/5
    center=np.kron(np.eye(6),C2)
    assert np.allclose(center@K,K@center)
    ev,V=eigh(K)
    assert abs(ev[0])<1e-10 and ev[1]>.0
    om=np.ones(12)/np.sqrt(12)
    assert abs(np.abs(V[:,0]@om)-1)<1e-10
    O=np.diag(np.repeat([1.,0.,0.,0.,0.,0.],2))
    W=np.diag(np.repeat([0.,0.,1.,0.,0.,0.],2))
    assert np.allclose(center@O,O@center) and np.allclose(center@W,W@center)
    Q=np.eye(12)-np.outer(om,om)
    f=Q@O@om;w=Q@W@om
    m1=f@K@w
    score=np.sum((V[:,1:].T@f)*(V[:,1:].T@w)/ev[1:])
    exact=float(mom_minus1.subs(z,sp.Rational(eps.numerator,eps.denominator)))
    assert abs(m1)<1e-12 and abs(score-exact)<1e-9
    # The driver has nonzero overlap with every center-even excited eigenmode,
    # so its cyclic subspace contains the *entire* center-even excited sector.
    center_even=(np.kron(np.eye(6),C2)+np.eye(12))/2
    even_exc=np.einsum('ij,jk->ik',V[:,1:],np.eye(11))
    weights=V[:,1:].T@w
    evencols=np.array([np.linalg.norm(center_even@V[:,i])>.999999 for i in range(1,12)])
    assert np.all(np.abs(weights[evencols])>1e-8)
    projection=V[:,1:][:,evencols]@(weights[evencols]*0+V[:,1:][:,evencols].T@f)
    assert abs(np.linalg.norm(projection)/np.linalg.norm(f)-1)<1e-9
    ms_o=f@K@f;ms_w=w@K@w
    assert abs(ms_o-1/6)<1e-10 and abs(ms_w-(1+float(eps))/6)<1e-10
    print('center-even Markov eps',str(eps),'gap',f'{ev[1]:.6g}',
          'mixed m1',f'{m1:.2g}','mixed inverse m-1',f'{score:.8g}',
          'source/driver fsum',f'{ms_o:.5f}',f'{ms_w:.5f}')
print('PASS: exact SU2 local mixed fsum, local sign freedom, and center-even diffusion inverse-moment obstruction')
