#!/usr/bin/env python3
"""Verify exact rhombus shared-edge component topology supporting the open-arc Haar theorem.
Geometry check only; SU2 Haar open-path lemma is proved analytically.
"""
from collections import defaultdict
center=(0,0)
def analyze(cells):
 edge_faces=defaultdict(list);adj={c:set() for c in cells}
 for x,y in cells:
  v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
  for a,b in zip(v,v[1:]+v[:1]):edge_faces[tuple(sorted((a,b)))].append((x,y))
 for faces in edge_faces.values():
  assert len(faces)<=2
  if len(faces)==2:
   a,b=faces;adj[a].add(b);adj[b].add(a)
 rest=set(cells)-{center};components=[]
 while rest:
  s=rest.pop();stack=[s];cc={s}
  for x in stack:
   for y in adj[x]:
    if y in rest:rest.remove(y);cc.add(y);stack.append(y)
  components.append(cc)
 v=[(0,0),(1,0),(1,1),(0,1)]
 colors=[]
 for a,b in zip(v,v[1:]+v[:1]):
  f=edge_faces[tuple(sorted((a,b)))]
  colors.append(next(i for i,c in enumerate(components) if any(x in c for x in f if x!=center)))
 arcs=[]
 for i in range(len(components)):
  mask=[v==i for v in colors]
  if 0<sum(mask)<4 and sum(mask[j]!=mask[(j+1)%4] for j in range(4))==2:
   arcs.append(sum(mask))
 return len(edge_faces),len(components),sorted(arcs),colors
star={center,(1,0),(-1,0),(0,1),(0,-1)}
seven=star|{(1,1),(-1,-1)}
nine={(x,y) for x in (-1,0,1) for y in (-1,0,1)}
assert analyze(star)[:3]==(16,4,[1,1,1,1])
assert analyze(seven)[:3]==(20,2,[2,2])
assert analyze(nine)[:3]==(24,1,[])
for c in (star,seven,nine):print('faces',len(c),'edges/components/arcs/colors',analyze(c))
print('PASS: two-cycle non-bridge open-arc fixture and fully connected obstruction')
