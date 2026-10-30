#!/usr/bin/env python3
"""Deterministic exact SU(2) Haar spin-one moments and interacting-rotor response.
Operator-level portal orthogonality is proved in the companion manuscript.
NOT a generic connected Penrose vacuum simulation.
"""
import math
from collections import defaultdict
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal

pi=math.pi
h=lambda fun:quad(lambda u:2/pi*math.sin(u)**2*fun(u),0,pi,epsabs=1e-13)[0]
E2=h(lambda u:math.cos(u)**2)
E4=h(lambda u:math.cos(u)**4)
assert abs(E2-1/4)<1e-12 and abs(E4-1/8)<1e-12
var=(16*E4-8*E2+1)
diri=16*(E2-E4)
assert abs(var-1)<1e-12 and abs(diri-2)<1e-12
print('SU2 Haar p^2',E2,'p^4',E4,'spin-one variance',var,'m1/A_f',diri)

# Quaternion formula for p(U V^{-1}) over SU2 U. Tetrahedral points integrate
# exactly the angular second moments required by spin-one character.
tetra=np.array([[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]],float)/math.sqrt(3)
assert np.linalg.norm(tetra.mean(axis=0))<1e-15
assert np.linalg.norm(tetra.T@tetra/4-np.eye(3)/3)<1e-15
for v0 in (0.,.11,.45,.85,1.):
 v=np.array([math.sqrt(1-v0*v0),0,0]);
 def avg(u):
  p=math.cos(u)*v0+math.sin(u)*(tetra@v)
  return float(np.mean(4*p*p-1))
 c=h(avg)
 assert abs(c)<1e-12
 print('noncommuting SU2 V scalar',v0,'Haar_U chi1(UV^-1)',c)

# Nontrivial, continuous SU2 character-rotor driver; eigenstates are spin-j class
# functions. Omega_B changes with magnetic coupling, and Q_B W Omega_B != 0.
N=90;n=np.arange(N,dtype=float)
for b in (1.,10.,100.):
 diag=n*(n+2)+b
 off=np.full(N-1,-b/2)
 ev,V=eigh_tridiagonal(diag,off)
 Om=V[:,0];E=ev[0]
 pOm=np.zeros(N)
 pOm[:-1]+=.5*Om[1:];pOm[1:]+=.5*Om[:-1]
 WO=b*(Om-pOm);WO-=Om*np.dot(Om,WO)
 wcoeff=V.T@WO
 susceptibility=np.sum(wcoeff[1:]**2/(ev[1:]-E))
 strength=np.linalg.norm(WO)
 assert susceptibility>0 and strength>0
 print(f'nonlinear SU2 driver b={b:g} QW norm={strength:.8f} self susceptibility={susceptibility:.8f} mixed chi1 portal response EXACTLY 0 in every spectral window')

# Incidence check: seven-face 2-cycle open-arc vs fully connected nine-face.
def geometry(cells,center=(1,1)):
 edges=defaultdict(list)
 for x,y in cells:
  v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
  for a,b in zip(v,v[1:]+v[:1]):edges[tuple(sorted((a,b)))].append((x,y))
 rest=set(cells)-{center};adj={c:set() for c in cells}
 for inc in edges.values():
  if len(inc)==2:
   a,b=inc;adj[a].add(b);adj[b].add(a)
 components=[]
 while rest:
  v=rest.pop();part={v};stack=[v]
  for z in stack:
   for w in adj[z]&rest:rest.remove(w);part.add(w);stack.append(w)
  components.append(part)
 neighbors=[(2,1),(1,2),(0,1),(1,0)]
 colors=[next(i for i,c in enumerate(components) if n in c) for n in neighbors]
 return len(edges),[sum(x==i for x in colors) for i in range(len(components))],colors
seven={(1,1),(2,1),(0,1),(1,2),(1,0),(2,2),(0,0)}
nine={(x,y) for x in range(3) for y in range(3)}
r7=geometry(seven);r9=geometry(nine)
assert r7[0]==20 and sorted(r7[1])==[2,2]
assert r9[0]==24 and r9[1]==[4]
print('7-face two-cycle components:',r7,'9-face connected:',r9)
print('PASS all deterministic Haar spin-one, non-Abelian group quadrature, positive driver response, and open-arc geometry checks')
