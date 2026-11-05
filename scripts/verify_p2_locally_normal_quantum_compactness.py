#!/usr/bin/env python3
"""Finite-dimensional trace-norm local quantum compactness and consistency checks.
Analytic theorem uses compact SU2 one-site Casimir resolvent and original-link energy bound.
This finite model checks structural trace-ideal steps, not interacting ground dynamics.
"""
import numpy as np
rng=np.random.default_rng(532)
checks=0
for d in (8,16,32,64):
 for _ in range(12):
  Z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
  rho=Z@Z.conj().T;rho/=np.trace(rho).real
  E=float(np.dot(np.diag(rho).real,np.arange(d)**2))
  for cut in (2,4,8):
   P=np.diag([1]*min(d,cut)+[0]*max(0,d-cut))
   eps=float(np.trace((np.eye(d)-P)@rho).real)
   assert eps<=E/cut**2+1e-10
   assert np.linalg.norm(rho-P@rho@P,'nuc')<=2*np.sqrt(max(0,eps))+eps+1e-9
   checks+=1
N=5;psi=rng.normal(size=2**N)+1j*rng.normal(size=2**N)
psi/=np.linalg.norm(psi)
v=psi.reshape([2]*N).reshape(2,2,8)
rho01=np.einsum('abc,dec->abde',v,v.conj()).reshape(4,4)
rho0=np.einsum('abcb->ac',rho01.reshape(2,2,2,2))
assert np.isclose(np.trace(rho0),1) and np.linalg.eigvalsh(rho0).min()>-1e-10
assert np.linalg.norm(rho01-np.diag(np.diag(rho01)))>1e-5
print('PASS',checks,'spectral-tail/trace-norm compression tests and off-diagonal local partial trace')
print('Theorem: uniform finite-window Casimir energy and compact resolvent => locally normal subsequential quantum states')
print('NOT a proof of the infinite-volume quantum ground-state inequality or gap')
