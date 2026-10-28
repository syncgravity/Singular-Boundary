#!/usr/bin/env python3
"""Read-only finite canonical Z5 Penrose boundary-distance certificate.
Uses three historical Q14 canonical seed rhombi; no simulation.
"""
import itertools,json
from collections import Counter
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]],
]
def d(a,b):return sum(abs(x-y) for x,y in zip(a,b))
def face_edges(v):
 v=[tuple(x) for x in v]
 es={tuple(sorted((a,b))) for a,b in itertools.combinations(v,2) if d(a,b)==1}
 assert len(es)==4
 return es
def midpoint(e):return tuple(a+b for a,b in zip(e[0],e[1]))
def main():
 fs=[face_edges(f) for f in seed]
 edges=sorted(set().union(*fs)); ix={e:i for i,e in enumerate(edges)}
 xs=[midpoint(e) for e in edges]
 assert len(set(xs))==len(xs)
 assert max(Counter(e for f in fs for e in f).values())<=2
 fidx=[{ix[e] for e in f} for f in fs]
 for f in fidx:assert all(d(xs[a],xs[b])==2 for a,b in itertools.combinations(f,2))
 n=0;cross=0;gap=0
 for mask in range(1,1<<len(edges)):
  inside={i for i in range(len(edges)) if mask>>i&1}
  outside=set(range(len(edges)))-inside
  touching=[f for f in fidx if f&inside and f&outside]
  X=set().union(*touching) if touching else set()
  for y in inside:
   n+=1
   if not X or not outside:continue
   cross+=1
   du=min(d(xs[y],xs[z]) for z in outside)
   dx=min(d(xs[y],xs[z]) for z in X)
   assert dx>=du-2
   gap=max(gap,du-dx)
 assert n==5120 and cross==5110 and gap==2
 print(json.dumps(dict(seed_faces=3,unique_links=len(edges),subset_site_checks=n,
  cases_with_crossing=cross,max_distance_loss=gap,all_passed=True,
  spectral_gap_verified=False),indent=2))
if __name__=="__main__":main()
