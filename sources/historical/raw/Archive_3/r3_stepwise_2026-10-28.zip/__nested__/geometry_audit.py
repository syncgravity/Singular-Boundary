"""Exact combinatorial audit on a 2x2 spatial square grid, 3 temporal intervals.
CONTROL COMPLEX ONLY, NOT Penrose R3 geometry.
"""
import json
from collections import Counter,deque
from pathlib import Path
P=Path(__file__).parent
# undirected edges with canonical vertex ordering
edges={}; faces={}
def edge(u,v):
    k=tuple(sorted((u,v)))
    if k not in edges: edges[k]=len(edges)
    return edges[k]
def face(name,vs):
    seq=[edge(vs[i],vs[(i+1)%4]) for i in range(4)]
    faces[name]=seq
for t in range(4):
 for x in range(2):
  for y in range(2):
   face(f'S_{x}{y}_{t}',[(x,y,t),(x+1,y,t),(x+1,y+1,t),(x,y+1,t)])
for t in range(3):
 for x in range(2):
  for y in range(3):
   face(f'Tx_{x}{y}_{t}',[(x,y,t),(x+1,y,t),(x+1,y,t+1),(x,y,t+1)])
 for x in range(3):
  for y in range(2):
   face(f'Ty_{x}{y}_{t}',[(x,y,t),(x,y+1,t),(x,y+1,t+1),(x,y,t+1)])
# Example Q: all 4 temporal faces around the lower-left spatial plaquette in interval 1
Q={f'Tx_00_1',f'Tx_01_1',f'Ty_00_1',f'Ty_10_1'}
C=set(faces)-Q
usage={e:set() for e in edges.values()}
for f,ee in faces.items():
 for e in ee: usage[e].add(f)
leaf={f:[e for e in faces[f] if usage[e]=={f}] for f in Q}
# strict cavity-free but shared within Q: gives a bipartite matching test
free={f:[e for e in faces[f] if usage[e].isdisjoint(C)] for f in Q}
# each edge touching Q has non-Q cofaces (in this fully-coupled complex)
# collar: face adjacency via shared edges; count distance layers from Q
adj={f:set() for f in faces}
for fset in usage.values():
 for f in fset: adj[f].update(fset-{f})
dist={f:0 for f in Q};front=deque(Q)
while front:
 f=front.popleft()
 for g in adj[f]:
  if g not in dist: dist[g]=dist[f]+1;front.append(g)
summary={'model':'2x2 square spatial plaquettes with 3 temporal intervals; all spatial and temporal faces coupled','vertices':3*3*4,'edges':len(edges),'faces':len(faces),'spatial_faces':16,'temporal_faces':36,'inserted_faces':sorted(Q),'strict_leaf_edges_by_inserted_face':{f:len(v) for f,v in sorted(leaf.items())},'cavity_free_edges_by_inserted_face':{f:len(v) for f,v in sorted(free.items())},'collar_face_sizes':{str(r):sum(d<=r for d in dist.values()) for r in range(5)},'shared_with_cavity_edges':len({e for f in Q for e in faces[f] if usage[e]&C})}
(P/'geometry_result.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
