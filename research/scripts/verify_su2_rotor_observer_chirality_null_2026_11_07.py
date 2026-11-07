#!/usr/bin/env python3
"""Non-Penrose one-loop interacting SU2 gauge-class quantum rotor null.
Not the authentic PF 3D regulator or the coupled many-link SU2 vacuum.
Requires NumPy SciPy; fuller script and executed output in Library audit ZIP.
"""
import numpy as np
from scipy.linalg import eigh
from numpy.polynomial.legendre import leggauss
alpha,beta=1.,3.
loops=np.array([1,2,3,1,3,2,4,1,2,4,3,2,1])
nloops=13
x,w=leggauss(600);theta=(x+1)*np.pi/2
weight=w*np.sin(theta)**2
results=[]
for M in (10,16,24,32):
    H=np.diag([alpha*n*(n+2)/4+beta for n in range(M)])
    for n in range(M-1):H[n,n+1]=H[n+1,n]=-beta/2
    energies,V=eigh(H);psi0=V[:,0]
    if psi0[0]<0:psi0=-psi0
    B=np.sin(theta[:,None]*(np.arange(M)+1)[None,:])/np.sin(theta[:,None])
    wave=B@psi0
    density=weight*wave**2
    W=1-np.cos(theta[:,None]*loops[None,:])
    def T(a):return density@np.mean(W*W[:,(np.arange(nloops)+a)%nloops]*W[:,(np.arange(nloops)+3*a)%nloops],axis=1)
    D=float(T(5)-T(8))
    means=density@W
    v=(B.T@(weight[:,None]*wave[:,None]*(W-means))).T@V
    def C(a,t):return np.sum((v*np.exp(-t*(energies-energies[0])))*v[(np.arange(nloops)+a)%nloops])/nloops
    assert abs(density.sum()-1)<1e-10
    assert all(abs(C(5,t)-C(8,t))<1e-10 for t in (0.,.1,1.,2.))
    assert D>.027
    results.append(D)
assert abs(results[-1]-results[-2])<1e-11
print("PASS: interacting SU2 class-rotor false-positive nonzero Delta",results)
print("NOTE: arbitrary loop powers, not Penrose observer geometry.")
