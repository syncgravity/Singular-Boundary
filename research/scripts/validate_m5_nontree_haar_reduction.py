"""Reconstruct M5 open-disk root paths and verify non-tree free Haar fibers."""
import sys,collections,numpy as np
sys.path.insert(0,'/mnt/data/penrose_study_src')
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
A=Approximant(M=5);z=np.load('/mnt/data/global_whitney_11face.npz')
E=list(map(int,z['edge_ids']));F=(0,1,3,2,4,154,150,11,10,7,8)
fi,_,_=penrose_faces(A);adj=collections.defaultdict(list)
for e in E:
 s,t,_=A.edges[e]
 adj[int(s)].append((int(t),e));adj[int(t)].append((int(s),e))
root=min(adj);parent={root:(None,None)};q=collections.deque([root])
while q:
 u=q.popleft()
 for v,e in sorted(adj[u]):
  if v not in parent:parent[v]=(u,e);q.append(v)
tree={e for u,e in parent.values() if e is not None}
nontree=set(E)-tree
assert len(tree)==19 and len(nontree)==11
paths={}
for e in E:
 u=int(A.edges[e][0]);p=set()
 while u!=root:
  u,pe=parent[u];p.add(pe)
 paths[e]=p
for e in nontree:
 assert all(e not in paths[j] for j in E)
members={e:[f for f in F if e in fi[f]] for e in E}
free={e:fs[0] for e,fs in members.items() if len(fs)==1 and e in nontree}
assert free[86]==1 and free[88]==2
assert free[372]==4 and free[26]==10
print('root',root,'tree',len(tree),'non-tree',len(nontree))
print('free non-tree links:',sorted(free.items()))
print('PASS root-tree independent coefficients for all non-tree links')
