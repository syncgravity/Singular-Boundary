#!/usr/bin/env python3
"""C5 source-model identity regression; not a 3D Yang–Mills regulator."""
import math
import numpy as np
N=5
j=np.arange(N)
P0=np.ones((N,N))/N
P1=(2/N)*np.cos(2*np.pi*(j[:,None]-j[None,:])/N)
P2=(2/N)*np.cos(4*np.pi*(j[:,None]-j[None,:])/N)
I=np.eye(N)
checks=0
def check(c):
 global checks
 assert c
 checks+=1
for p,r in ((P0,1),(P1,2),(P2,2)):
 check(np.allclose(p,p.T));check(np.allclose(p@p,p));check(abs(np.trace(p)-r)<1e-12)
for a,b in ((P0,P1),(P0,P2),(P1,P2)):
 check(np.allclose(a@b,0))
check(np.allclose(P0+P1+P2,I))
C=np.roll(I,1,axis=0)
for p in (P0,P1,P2):check(np.allclose(C@p,p@C))
for m in I:
 z1=sum(m[k]*np.exp(2j*np.pi*k/5) for k in range(5))
 z2=sum(m[k]*np.exp(4j*np.pi*k/5) for k in range(5))
 check(abs(abs(z1)**2+abs(z2)**2-2)<1e-12)
 check(abs(m@(P1+P2)@m-.8)<1e-12)
theta=4*math.pi/5
rot=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]],dtype=complex)
wick=np.diag([1,1j])
check(np.max(np.abs((wick.conj().T@rot@wick).imag))>0.1)
print(f'PASS {checks} C5 projector and metric normalization tests')
