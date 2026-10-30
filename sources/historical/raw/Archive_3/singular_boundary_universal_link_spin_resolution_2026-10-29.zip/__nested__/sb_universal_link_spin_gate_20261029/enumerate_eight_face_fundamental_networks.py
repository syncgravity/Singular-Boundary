#!/usr/bin/env python3
"""EXACT complete Gauss-invariant graph spin-network dimension with link spins
j_e in {0,1/2} on eight-face square-rhombus open disk.
Each Eulerian 1-cycle determines edge spins; at each four-valent occupied
vertex the SU2 invariant intertwiner multiplicity is 2, otherwise 1.
This does not compute magnetic/kinetic recoupling matrix entries.
"""
from collections import Counter,defaultdict
from itertools import product
cells=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
verts=sorted(set(v for x,y in cells for v in ((x,y),(x+1,y),(x+1,y+1),(x,y+1))))
faces=[];edges=set()
for x,y in cells:
 v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 es={tuple(sorted((a,b))) for a,b in zip(v,v[1:]+v[:1])}
 faces.append(es);edges|=es
edges=sorted(edges);idx={e:i for i,e in enumerate(edges)}
face_masks=[sum(1<<idx[e] for e in es) for es in faces]
assert len(cells)==8 and len(edges)==22 and len(verts)==15
counter=Counter(); parity={0:Counter(),1:Counter()};seen=set(); rows=[]
target=cells.index((1,1))
for s in range(256):
 mask=0
 for k,m in enumerate(face_masks):
  if (s>>k)&1:mask^=m
 assert mask not in seen
 seen.add(mask)
 deg=Counter()
 for i,(a,b) in enumerate(edges):
  if (mask>>i)&1: deg[a]+=1;deg[b]+=1
 assert all(deg[v]%2==0 for v in verts)
 assert max(deg.values(),default=0)<=4
 four=sum(deg[v]==4 for v in verts)
 mult=2**four
 sector=(s>>target)&1
 parity[sector][four]+=mult
 counter[four]+=1
 rows.append((s,sector,mask,four,mult))
assert len(seen)==256
Dplus=sum(parity[0].values());Dminus=sum(parity[1].values());total=Dplus+Dminus
print('Eight-face open disk: V,E,F',len(verts),len(edges),len(faces),'cycle rank',len(edges)-len(verts)+1)
print('Eulerian link-spin configurations',len(seen),'four-intertwiner multiplicity distribution',dict(sorted(counter.items())))
print('Complete physical j_e<=1/2 spin-network Hilbert dimension',total)
print('Target center parity sectors even',Dplus,'odd',Dminus)
print('Exact center flux dimensions tracked by face-boundary coefficient, not state-dependent gauge choice')
# The 35-dimensional prior Ritz subspace has 35 vectors and is strictly incomplete
assert Dplus>=35 and total>35
import json
with open('/mnt/data/sb_universal_link_spin_gate_20261029/FUNDAMENTAL_NETWORK_DIMENSIONS.json','w') as f:json.dump({"vertices":len(verts),"edges":len(edges),"faces":len(faces),"eulerian_edge_spin_assignments":len(seen),"intertwiner_four_vertex_occurrence_histogram":dict(sorted(counter.items())),"all_sector_dimension":total,"center_even_dimension":Dplus,"center_odd_dimension":Dminus},f,indent=2)
print('PASS exact SU2 spin-1/2 graph enumeration; magnetic recoupling and ground spectrum NOT calculated')
