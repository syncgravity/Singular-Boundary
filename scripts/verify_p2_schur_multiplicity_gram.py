#!/usr/bin/env python3
"""Exact SU2 Schur multiplicity trace norm versus Haar twirl, two fundamental faces."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from math import sqrt
# |up down> = (|triplet M0> + |singlet>)/sqrt(2)
updn=np.array([0,1,0,0],complex)
dnu=np.array([0,0,1,0],complex)
trip=np.array([0,1/sqrt(2),1/sqrt(2),0],complex)
sing=np.array([0,1/sqrt(2),-1/sqrt(2),0],complex)
Pt=np.eye(4)-np.outer(sing,sing.conj())
Ps=np.outer(sing,sing.conj())
for ket,bra,target in [(updn,updn,.5*Ps+(1/6)*Pt),
                        (updn,dnu,-.5*Ps+(1/6)*Pt)]:
 X=np.outer(ket,bra.conj())
 nodes,weights=leggauss(4);nodes=(nodes+1)/2;weights=weights/2
 out=np.zeros((4,4),complex); M=9
 for t,w in zip(nodes,weights):
  for a in range(M):
   for b in range(M):
    z=sqrt(t)*np.exp(2j*np.pi*a/M)
    v=sqrt(1-t)*np.exp(2j*np.pi*b/M)
    g=np.array([[z,v],[-v.conjugate(),z.conjugate()]])
    U=np.kron(g,g)
    out+=w/M**2*(U@X@U.conj().T)
 assert np.linalg.norm(out-target,'fro')<1e-12
 # Exact multiplicity coefficients: singlet +-1/2, triplet 1/2.
 assert abs(np.linalg.norm(out,'nuc')-1)<1e-12
print('PASS two-face physical SU2 Haar/Schur multiplicity S1 identities')
print('Extended N=2,3,4 complex weight-pure tests: conversation audit ZIP')
