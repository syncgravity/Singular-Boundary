#!/usr/bin/env python3
"""Exact two-level cycle sign and Gaussian magnetic submodularity; deterministic."""
import numpy as np
import sympy as s
from scipy.linalg import sqrtm

g,u,t=s.symbols('g u t',positive=True)
E=g+u+t-s.sqrt((g+u)**2+t**2)
assert s.simplify(s.diff(E,t,u)-t*(g+u)/((g+u)**2+t**2)**s.Rational(3,2))==0
assert s.simplify(s.diff(E,u,2)+t*t/((g+u)**2+t**2)**s.Rational(3,2))==0
assert s.simplify(s.diff(E,t,2)+(g+u)**2/((g+u)**2+t**2)**s.Rational(3,2))==0
assert s.simplify(s.diff(E,t).subs(t,0)-1)==0

sx=np.array([[0.,1.],[1.,0.]]);sz=np.diag([1.,-1.]);iden=np.eye(2)
for gg in [.3,1.,7.]:
 for uu in [.1,1.,5.]:
  for tt in [.2,1.,9.]:
   H=(gg+uu)*(iden-sx)+tt*(iden-sz)
   eig=np.linalg.eigvalsh(H)[0]
   assert abs(eig-float(E.subs({g:gg,u:uu,t:tt})))<1e-11
   assert float(s.diff(E,t,u).subs({g:gg,u:uu,t:tt}))>0

# Rebuild the canonical three-face Z^5 Penrose spatial incidence (not Q14 temporal).
from itertools import combinations, permutations
faces0=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edge(x,y):return tuple(sorted((x,y)))
def neighboring(x,y):return sum(abs(i-j) for i,j in zip(x,y))==1
face_edges=[{edge(x,y) for x,y in combinations(face,2) if neighboring(x,y)} for face in faces0]
edgelist=sorted(set.union(*face_edges))
assert len(edgelist)==10 and all(len(f)==4 for f in face_edges)
B=np.zeros((3,len(edgelist)))
for i,vertices in enumerate(faces0):
 cycles=[]
 for perm in permutations(vertices[1:]):
  cycle=[vertices[0],*perm]
  if all(edge(x,y) in face_edges[i] for x,y in zip(cycle,cycle[1:]+cycle[:1])):
   cycles.append(cycle)
 cycle=min(cycles)
 for x,y in zip(cycle,cycle[1:]+cycle[:1]):
  e=edge(x,y); B[i,edgelist.index(e)]=1 if (x,y)==e else -1
for i,j in [(0,1),(0,2)]:
 common=next(iter(face_edges[i]&face_edges[j]));k=edgelist.index(common)
 B[j]*=-B[i,k]*B[j,k]
M=B@B.T
assert np.allclose(np.diag(M),[4,4,4])
assert np.allclose(np.linalg.eigvalsh(M),[4-np.sqrt(2),4,4+np.sqrt(2)])

def gauss_E(mag):
 A=np.asarray(sqrtm(M),dtype=float)@np.diag(mag)@np.asarray(sqrtm(M),dtype=float)
 return 3/(2*np.sqrt(2))*np.sqrt(np.clip(np.linalg.eigvalsh(A),0,None)).sum()
for vec in ([.5,2.,3.],[2.,.1,4.],[10.,8.,.4]):
 vec=np.array(vec,dtype=float); dh=1e-3
 for f in range(3):
  for j in range(3):
   if f==j: continue
   e=np.eye(3)
   mix=(gauss_E(vec+dh*e[f]+dh*e[j])-gauss_E(vec+dh*e[f]-dh*e[j])-gauss_E(vec-dh*e[f]+dh*e[j])+gauss_E(vec-dh*e[f]-dh*e[j]))/(4*dh**2)
   assert mix <1e-5, (vec,f,j,mix)

# Validate formula for second mixed derivative by positive matrix resolvent quadrature.
from scipy.integrate import quad
vec=np.array([1.3,3.1,.6]);root=np.asarray(sqrtm(M),dtype=float)
A=root@np.diag(vec)@root
for f,j in [(0,1),(0,2),(1,2)]:
 vf,vj=root[:,f],root[:,j]
 def ff(theta):
  # z=tan²(theta), z^(-1/2) dz =2sec²(theta) dtheta
  z=np.tan(theta)**2
  r=np.linalg.solve(A+z*np.eye(3),vj)
  return 2/np.cos(theta)**2*(vf@r)**2
 integral=quad(ff,0,np.pi/2,epsabs=1e-11)[0]
 actual=-3/(4*np.sqrt(2)*np.pi)*integral
 eps=1e-3;e=np.eye(3)
 numeric=(gauss_E(vec+eps*e[f]+eps*e[j])-gauss_E(vec+eps*e[f]-eps*e[j])-gauss_E(vec-eps*e[f]+eps*e[j])+gauss_E(vec-eps*e[f]-eps*e[j]))/(4*eps**2)
 assert abs(actual-numeric)<1e-6,(actual,numeric)

# Nonuniform Gaussian face deletion bound including positive cycle closure.
for face in range(3):
 Af=M[face,face];b=9.
 original=np.array([4.,7.,6.]);original[face]=0.
 for scale in [0.,.1,.5,1.]:
  base=scale*original
  delta=gauss_E(base+b*np.eye(3)[face])-gauss_E(base)
  assert delta<=3/(2*np.sqrt(2))*np.sqrt(Af*b)+1e-7
print('PASS: positive-resolvent gaussian submodularity, 3-face Penrose seed, exact center-parity two-level opposite sign.')
print('No Monte Carlo; no nonlinear SU2 mixed-sign inference.')
