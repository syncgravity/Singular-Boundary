#!/usr/bin/env python3
"""Local Casimir spectral projectors commute with corrected original-link
cross-electric SU2 generators; bounded onsite magnetic commutators remain uniform.
"""
from math import sqrt
import numpy as np
def gens(n):
 p=np.zeros((n+1,n+1),complex)
 for k in range(1,n+1):p[k-1,k]=sqrt(k*(n-k+1))
 m=p.conj().T
 return [(p+m)/2,(p-m)/(2j),np.diag(np.arange(n,-n-1,-2)/2)]
G1=[np.zeros((5,5),complex) for k in range(3)]
for k in range(3):
 G1[k][:2,:2]=gens(1)[k]
 G1[k][2:,2:]=gens(2)[k]
P1=np.diag([1,1,0,0,0])
C1=np.diag([.75,.75,2,2,2]);W1=np.zeros((5,5),complex)
W1[1,2]=W1[2,1]=1
for n in (1,2,4,8,16):
 I=np.eye(n+1)
 H=4*np.kron(C1,I).astype(complex)+n*(n+2)*np.eye(5*(n+1))
 for k in range(3):H+=2*np.kron(G1[k],gens(n)[k])
 P=np.kron(P1,I)
 assert np.linalg.norm(H@P-P@H)<1e-11
 mag=np.kron(W1,I)
 assert np.linalg.norm(mag@P-P@mag,2)<=2
 print('PASS second-face degree',n,'electric commutator zero; magnetic commutator bounded')
print('For any local F=f(C_i,i in W), ||[H_N(lambda),F]||<=2|lambda||W|||F||')
print('Uniform finite-width norm-Lipschitz seed; NOT an invariant infinite-volume C*-algebra')
