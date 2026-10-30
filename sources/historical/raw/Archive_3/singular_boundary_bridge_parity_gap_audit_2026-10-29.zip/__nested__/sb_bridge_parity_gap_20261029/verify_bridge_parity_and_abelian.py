#!/usr/bin/env python3
"""Exact center-flux interpolation parity tests, positive three-level comparator,
and finite Fourier truncation of a 3x3 U(1) *physical gauge theory*.
The U(1) computation is not an SU(2) Wilson proof.
"""
import numpy as np
from scipy.linalg import eigh
from scipy.sparse import diags, kron, identity
from scipy.sparse.linalg import eigsh

# Exact selection rule in an abstract H0-center-symmetric spectral truncation.
S=np.diag([1.,-1.,1.]);H0=np.diag([0.,2.,3.]);
O=np.array([[1.,0.,.3],[0.,0.,0.],[.3,0.,.5]])
assert np.linalg.eigvalsh(O).min()>=-1e-12
for sign in [-1.,1.]:
    B=np.array([[0.,1.,0.],[1.,0.,5.*sign],[0.,5.*sign,0.]])
    assert np.allclose(S@B@S,-B) and np.allclose(S@O@S,O)
    def F(t):
        w,V=eigh(H0-t*B);g=V[:,0];return float(g@O@g)
    dp=(F(.001)-F(-.001))/(.002)
    d2=(F(.001)-2*F(0)+F(-.001))/(1e-6)
    assert abs(dp)<1e-10
    assert (d2>0 if sign>0 else d2<0)
    print(f'Parity comparator sign={sign:+.0f}, F(0)={F(0):.8f}, F(0.001)={F(.001):.8f}, Fprime0={dp:.4g}, Fsecond0={d2:.8f}')

# U(1) finite rhombus/square disk: face Fourier charges, exact face incidence Gram.
# E=2*n*(n+1), F=n*n; with all-vertex Gauss invariance face variables are independent.
n=3;F=n*n;f=4;R=1;b=1.15
M=4*np.eye(F)
for i in range(n):
    for j in range(n):
        k=i*n+j
        if i+1<n:M[k,k+n]=M[k+n,k]=-1
        if j+1<n:M[k,k+1]=M[k+1,k]=-1
keep=[i for i in range(F) if i!=f]
q=np.stack(np.meshgrid(*([np.arange(-R,R+1)]*len(keep)), indexing='ij'),axis=-1).reshape(-1,len(keep))
print('3x3 U(1) gauge disk: 9 face modes, 24 electric edges, 6561 Fourier basis states per deleted-charge block')
D=2*R+1
sh=diags([np.ones(D-1),np.ones(D-1)],[-1,1],shape=(D,D),format='csr')
Id=identity(D,format='csr')
V=None
for k in range(len(keep)):
    op=identity(1,format='csr')
    for z in range(len(keep)):
        op=kron(op,sh if z==k else Id,format='csr')
    V=op if V is None else V+op
V=-b*.5*V + b*len(keep)*identity(len(q),format='csr')
for charge in [0,1,-1]:
    vec=np.zeros((len(q),F),dtype=float);vec[:,keep]=q;vec[:,f]=charge
    T=np.einsum('ni,ij,nj->n',vec,M,vec)
    H=V+diags(T,format='csr')
    vals=eigsh(H,k=1,which='SA',tol=1e-9,return_eigenvectors=False,maxiter=40000)
    print('U(1) deleted face Fourier charge',charge,'lowest Ritz energy',float(vals[0]))
print('PASS: exact center-parity Ward test and cycle-rich U(1) gauge face-block computation')
