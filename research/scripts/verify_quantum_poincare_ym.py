#!/usr/bin/env python3
"""SU(2) interacting one-loop quantum ground-state Dirichlet identity.
This verifies finite exact operator formulas by converged quadrature / spectral
truncation. NOT a 3D lattice, nor a physical continuum mass-gap proof.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh

nodes,ww=leggauss(600)
theta=np.pi*(nodes+1)/2
haar=ww*np.sin(theta)**2
haar/=haar.sum()

checks=0
for alpha in (0.6,1.,1.7):
 for beta in (0.8,2.,3.,5.):
  M=48
  H=np.diag([alpha*n*(n+2)/4+beta for n in range(M)])
  for n in range(M-1):H[n,n+1]=H[n+1,n]=-beta/2
  energy,C=eigh(H)
  gs=C[:,0]
  if gs[0]<0:gs=-gs
  # Characters χ_n(θ) = sin((n+1)θ)/sinθ; class Haar basis.
  char=np.sin(theta[:,None]*(np.arange(M)+1))/np.sin(theta[:,None])
  omg=char@gs
  den=haar*omg**2
  assert abs(den.sum()-1)<1e-10
  O=1-np.cos(theta)
  mean=den@O
  var=den@((O-mean)**2)
  kinetic_dir=alpha/4 * (den@np.sin(theta)**2)
  # Multiply (O-mean)Ω in character basis; use χ1χn=χn−1+χn+1.
  psi=np.zeros(M)
  psi += (1-mean)*gs
  psi[1:]-=.5*gs[:-1]
  psi[:-1]-=.5*gs[1:]
  quantum_dir=psi@(H-energy[0]*np.eye(M))@psi
  assert abs(kinetic_dir-quantum_dir)<1e-9,(alpha,beta,kinetic_dir,quantum_dir)
  assert abs(var-np.sum(psi*psi))<1e-9
  assert kinetic_dir/var>=energy[1]-energy[0]-1e-9
  checks+=3
print('PASS',checks,'interacting SU2 radial quantum Dirichlet / variational Poincare checks')
print('NOTE: finite conjugation-invariant one-loop SU2 rotor, not 3D PF/cubic YM or physical mass gap.')