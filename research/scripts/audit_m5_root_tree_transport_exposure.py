"""Audit actual M5 rooted-tree paths and inverse-Whitney coupled-edge exposure."""
import sys,collections,numpy as np
sys.path.insert(0,'/mnt/data/penrose_study_src')
from penrose_causal_study import Approximant
A=Approximant(M=5)
d=np.load('/mnt/data/global_whitney_11face.npz')
edges=list(map(int,d['edge_ids']));K=np.linalg.inv(d['matrix'])
adj=collections.defaultdict(list)
for e in edges:
 s,t,_=A.edges[e];adj[int(s)].append((int(t),e));adj[int(t)].append((int(s),e))
root=min(adj);parent={root:(None,None)};queue=collections.deque([root])
while queue:
 u=queue.popleft()
 for v,e in sorted(adj[u]):
  if v not in parent:parent[v]=(u,e);queue.append(v)
assert len(parent)==20
paths={}
for e in edges:
 src=int(A.edges[e][0]);path=set()
 while src!=root:
  src,pe=parent[src];path.add(pe)
 paths[e]=path
for target,expected in [(0,125),(1,151),(4,144),(13,0),(86,0),(88,0)]:
 exposed=[(edges[i],edges[j]) for i in range(30) for j in range(i+1,30)
          if edges[i]!=target and edges[j]!=target
          and target in (paths[edges[i]]^paths[edges[j]])
          and abs(K[i,j])>1e-6]
 assert len(exposed)==expected,(target,len(exposed))
 print(target,'tree',any(x==target for _,x in parent.values()),'exposed',len(exposed))
print('PASS deterministic M5 root-tree transport exposure')
