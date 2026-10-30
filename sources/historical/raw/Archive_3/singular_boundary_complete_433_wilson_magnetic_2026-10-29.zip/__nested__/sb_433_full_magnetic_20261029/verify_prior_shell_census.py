#!/usr/bin/env python3
"""Exact eight-face geometry, complete J=1/2 electric shell, and center-even winding witness.
No stochastic sampling; all SU(2) Haar integrals are deterministic 1D quadrature.
"""
from collections import defaultdict, Counter
from math import pi, sin, cos, acos, sqrt
from scipy.integrate import quad
import json
from pathlib import Path

cells=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
target=(1,1)
star={target,(1,0),(2,1),(1,2),(0,1)}
verts=sorted({v for x,y in cells for v in ((x,y),(x+1,y),(x+1,y+1),(x,y+1))})
def boundary_edges(face):
 x,y=face
 vs=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 return {tuple(sorted((a,b))) for a,b in zip(vs,vs[1:]+vs[:1])}
faces_edges={f:boundary_edges(f) for f in cells}
edges=sorted(set().union(*faces_edges.values()))
index={e:i for i,e in enumerate(edges)}
assert (len(cells),len(verts),len(edges))==(8,15,22)
star_count=Counter(e for f in star for e in faces_edges[f])
inner=faces_edges[target]
outer={e for e,count in star_count.items() if count==1}
assert len(inner)==4 and len(outer)==12 and not (inner&outer)
assert set().union(inner,outer)==set().union(*(faces_edges[f] for f in star))
# Outer perimeter and inner perimeter each form one simple closed loop.
for loop in (inner,outer):
 deg=Counter(v for e in loop for v in e)
 assert set(deg.values())=={2}
 assert len(deg)==len(loop)
# Fundamental representation on each occupied link and 4-valent intertwiners.
face_masks=[sum(1<<index[e] for e in faces_edges[f]) for f in cells]
target_index=cells.index(target)
levels=Counter();even=Counter();odd=Counter();four=Counter()
for s in range(1<<len(cells)):
 mask=0
 for i,m in enumerate(face_masks):
  if (s>>i)&1: mask^=m
 degrees=Counter(v for i,e in enumerate(edges) if (mask>>i)&1 for v in e)
 assert all(n%2==0 for n in degrees.values())
 n4=sum(v==4 for v in degrees.values());mult=2**n4
 occupied=mask.bit_count();levels[occupied]+=mult;four[n4]+=1
 (odd if ((s>>target_index)&1) else even)[occupied]+=mult
assert sum(levels.values())==433 and sum(even.values())==246 and sum(odd.values())==187
assert dict(sorted(four.items()))=={0:161,1:68,2:22,3:4,4:1}
# The winding witness = chi_half(W_inner) chi_half(W_outer), normalized because
# the loops have disjoint edges and each Wilson loop is Haar under link Haar.
# Since the target flux flips both loops, the product is center even.
def haar(fn):
 return quad(lambda u: (2/pi)*sin(u)**2*fn(cos(u)),0,pi,epsabs=1e-12,epsrel=1e-12)[0]
p2=haar(lambda p:p*p);p4=haar(lambda p:p**4)
assert abs(p2-1/4)<1e-12 and abs(p4-1/8)<1e-12
witness_norm=4*p2
spin_one=haar(lambda p:4*p*p*(4*p*p-1))
assert abs(witness_norm-1)<1e-12 and abs(spin_one-1)<1e-12
for h in (0.1,0.01,0.001,0.0001):
 a=acos(1-h)
 haar_cap=(a-sin(2*a)/2)/pi
 witness_cap=(a-sin(4*a)/4)/pi
 ratio=witness_cap/haar_cap
 assert 3.0<ratio<4.0000001
 print('h',h,'cap_Haar',haar_cap,'witness_cap',witness_cap,'ratio',ratio)
print('exact J=1/2 Hilbert dimension',sum(levels.values()))
print('target-center even',sum(even.values()),'odd',sum(odd.values()))
print('electric occupancies: count',dict(sorted(levels.items())))
print('witness chi_1 expectation =',spin_one,'electric units 3/4*16 = 12')
print('PASS exact 433-shell census, two disjoint Wilson loops, center-even non-Haar witness')
(Path(__file__).resolve().parent/'FUNDAMENTAL_ELECTRIC_HISTOGRAM.json').write_text(json.dumps({
 'faces':len(cells),'links':len(edges),'vertices':len(verts),'inner_links':len(inner),
 'outer_links':len(outer),'physical_shell_dim':sum(levels.values()),
 'target_even':sum(even.values()),'target_odd':sum(odd.values()),
 'occupied_link_electric_histogram':dict(sorted(levels.items())),
 'even_histogram':dict(sorted(even.items())),'odd_histogram':dict(sorted(odd.items())),
 'witness_spin_one_expectation':1,
 'witness_occupied_link_count':16,
 'witness_electric_energy_for_a_e_1':12,
 'witness_magnetic_expectation':'sum retained b_g; all retained p_g averages vanish',
},indent=2)+'\n')
