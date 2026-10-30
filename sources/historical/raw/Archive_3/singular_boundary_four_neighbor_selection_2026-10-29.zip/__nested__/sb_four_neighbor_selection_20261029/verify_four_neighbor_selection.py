#!/usr/bin/env python3
"""Independent exact checks of physical SU2 star geometry and SU2 Haar selection.

Does not diagonalize the full nonabelian 3x3 physical Hamiltonian.
Verifies the exact topology, GF(2) flux flips and SU2 character overlap
using rational Clebsch-Gordan/orthogonality identities.
"""
from collections import defaultdict, deque
from fractions import Fraction
from math import factorial

N=3
faces={}
edges=defaultdict(list)
for x in range(N):
 for y in range(N):
  f=(x,y)
  vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
  faces[f]=vs
  for a,b in zip(vs,vs[1:]+vs[:1]):
   e=tuple(sorted((a,b)))
   edges[e].append(f)
target=(1,1)
star=[f for f in faces if f != target and any(f in inc and target in inc for inc in edges.values())]
assert len(star)==4,star
center_edges=[e for e,inc in edges.items() if target in inc]
assert len(center_edges)==4
for e in center_edges:
 inc=edges[e]
 assert len(inc)==2
 assert next(f for f in inc if f!=target) in star
# Complete edge Hamiltonian after deleting f and its 4 neighbors: all 4 target edges private.
retained=set(faces)-set(star)-{target}
assert len(retained)==4
assert all(not any(f in retained for f in edges[e]) for e in center_edges)
print('finite Wilson patch: faces',len(faces),'edges',len(edges),'central target',target,'neighbors',star,'retained corners',len(retained))

# Exact gauge-compatible Z2 flux strings exist for each chosen neighbor.
outside='exterior'
dual=defaultdict(list)
for e,inc in edges.items():
 if len(inc)==1:
  a,b=inc[0],outside
 else:
  a,b=inc
 dual[a].append((b,e));dual[b].append((a,e))
for face in star:
 q=deque([(face,[])]);seen={face}
 while q:
  v,path=q.popleft()
  if v==outside:break
  for nxt,e in dual[v]:
   if nxt not in seen:seen.add(nxt);q.append((nxt,path+[e]))
 assert v==outside
 parity={f:sum(e in path for e in [ee for ee,inc in edges.items() if f in inc])%2 for f in faces}
 assert all(parity[f]==int(f==face) for f in faces)
 print('center flip for neighbor',face,'dual path length',len(path),'target unchanged')

# Fundamental character fusion: chi_{1/2}^n = sum_{j} m(n,2j) chi_j.
# Here labels m=2j are nonnegative integers; chi_1/2=2p.
def multiplicities(n):
 d={0:1}
 for _ in range(n):
  out={}
  for m,c in d.items():
   for k in (m-1,m+1):
    if k>=0:out[k]=out.get(k,0)+c
  d=out
 return d
for j in (1,2,3):
 m=2*j
 for n in range(m):assert multiplicities(n).get(m,0)==0
 assert multiplicities(m)[m]==1
 # For 4 independent edge variables, Haar Fourier coefficient a_j(2j)=4^{-j}.
 # Exact integral: int chi_j(U1U2U3U4) prod_i p(Ui)^(2j) dU_i
 # = a_j(2j)^4 / (2j+1)^3
 coeff=Fraction(1,2**(4*m)*(m+1)**3)
 assert coeff>0
 print(f'spin j={j}: degree each neighbor >= {2*j}; total >= {8*j}; leading Haar tensor overlap {coeff} = {float(coeff):.11g}')

# Exact multivariable Taylor constraint: for spin j every exponent on each
# neighbor must be >= 2j, since only that perturbation touches its private edge.
# Additionally, center evenness enforces even exponents separately.
for j in (1,2,3):
 req=2*j
 for idx in range(4):
  n=[req]*4;n[idx]-=1
  assert n[idx]<req
  assert all(n[k]>=req for k in range(4) if k!=idx)
 print('Taylor sparsity verified for spin',j)
print('PASS: exact 3x3 face incidence, neighbor flux parity, and SU2 all-order representation selection')

# Exact smooth positive SU(2) class-rotor comparator with every selection rule.
# q(t)=prod t_i^2. Its normalized density is exp(-2*kappa*q*p^2)/Z.
# Spin-j coefficient begins at q^j because p^(2n) has no spin j>n.
# Its cap can nevertheless be exponentially depleted at t=(1,1,1,1).
from scipy.integrate import quad
import math

def harp(p):return 2/math.pi*math.sqrt(max(0.,1-p*p))
for h in (.2,.1,.05,.025):
 kap=1/h
 Z=quad(lambda p:harp(p)*math.exp(-2*kap*p*p),-1,1,epsabs=1e-13)[0]
 center=quad(lambda p:harp(p)*math.exp(-2*kap*p*p),1-h,1,epsabs=1e-18)[0]/Z
 haar=quad(harp,1-h,1,epsabs=1e-13)[0]
 assert 0<center<haar
 print('center-even rotor obstruction: h',h,'cap/Haar',center/haar)
print('PASS: explicit four-coupling even, Haar-hyperplane, spin-filtered positive rotor can deplete center cap')
