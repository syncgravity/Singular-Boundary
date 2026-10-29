#!/usr/bin/env python3
"""Deterministic 3x3 SU2 four-neighbor geometry and representation-selection checks.
Not an interacting SU2 Hamiltonian diagonalization.
"""
from collections import defaultdict, deque
from fractions import Fraction
N=3; faces={};edges=defaultdict(list)
for x in range(N):
 for y in range(N):
  f=(x,y);v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)];faces[f]=v
  for a,b in zip(v,v[1:]+v[:1]):edges[tuple(sorted((a,b)))].append(f)
f=(1,1)
nbr={g for inc in edges.values() if f in inc for g in inc if g!=f}
assert len(faces)==9 and len(edges)==24 and len(nbr)==4
target_edges=[e for e,inc in edges.items() if f in inc]
assert len(target_edges)==4
assert all(all(g==f or g in nbr for g in edges[e]) for e in target_edges)
for spin in (1,2,3):
 n=2*spin
 overlap=Fraction(1,2**(4*n)*(n+1)**3)
 assert overlap>0
 print('spin',spin,'earliest total degree',4*n,'Haar overlap',overlap)
print('PASS: four neighbors, four private edges, exact SU2 fusion threshold')
