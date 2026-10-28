#!/usr/bin/env python3
"""Read-only exact parity/connectedness test of three canonical Q14 seed rhombi."""
from itertools import combinations,product
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def dist(a,b):return sum(abs(x-y) for x,y in zip(a,b))
def edges(face):
 v=list(map(tuple,face))
 return {tuple(sorted((a,b))) for a,b in combinations(v,2) if dist(a,b)==1}
faces=[edges(f) for f in seed]
assert len(set().union(*faces))==10
assert len(faces[0]&faces[1])==len(faces[0]&faces[2])==1
assert len(faces[1]&faces[2])==0
def satisfies(a,b,seq):
 parity=faces[a]^faces[b]
 for j in seq: parity.symmetric_difference_update(faces[j])
 if parity:return False
 sets=[faces[a],faces[b]]+[faces[j] for j in seq]
 seen={0}
 while True:
  new=seen|{j for j in range(len(sets)) if any(sets[j]&sets[i] for i in seen)}
  if new==seen:break
  seen=new
 return len(seen)==len(sets)
for a,b,expected in ((0,1,2),(1,2,4)):
 first=next(n for n in range(7) if any(satisfies(a,b,seq) for seq in product(range(3),repeat=n)))
 assert first==expected
 print(f"pair ({a},{b}): first permitted order {first}")
print("Exact parity and connectedness fixture passed; no Monte Carlo.")
