import collections
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
A=Approximant(M=5)
F=[0,1,3,2,4,154,150,11,10,7,8]
fi,_,_=penrose_faces(A)
E=sorted(set(int(e) for f in F for e in fi[f]));adj=collections.defaultdict(list)
for e in E:
 u,v,_=A.edges[e];adj[int(u)].append((int(v),e));adj[int(v)].append((int(u),e))
root=min(adj);q=collections.deque([root]);parent={root:(None,None)}
while q:
 u=q.popleft()
 for v,e in sorted(adj[u]):
  if v not in parent:parent[v]=(u,e);q.append(v)
T={e for _,e in parent.values() if e is not None}
assert len(T)==19 and len(E)==30 and 13 not in T and 4 in T
assert list(map(int,fi[0]))==[1,4,13,0]
assert list(map(int,fi[10]))==[13,18,26,12]
assert [f for f in F if f!=0 and 13 in fi[f]]==[10]
assert len((T-{4})|{13})==19
print('PASS actual M5 root tree edge4 -> edge13 exchange')
