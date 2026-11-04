import sys,collections,math,numpy as np
sys.path.insert(0,'/mnt/data/penrose_study_src')
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
A=Approximant(M=5);F=(0,1,3,2,4,154,150,11,10,7,8);fi,_,_=penrose_faces(A)
d=np.load('/mnt/data/global_whitney_11face.npz');ids=list(map(int,d['edge_ids']));M=d['matrix'];K=np.linalg.inv(M)
adj=collections.defaultdict(list)
for e in ids:
 u,v,_=A.edges[e];adj[int(u)].append((int(v),e));adj[int(v)].append((int(u),e))
root=min(adj);par={root:(None,None)};q=collections.deque([root])
while q:
 u=q.popleft()
 for v,e in sorted(adj[u]):
  if v not in par:par[v]=(u,e);q.append(v)
T={e for _,e in par.values() if e is not None}
assert 13 not in T and 13 in fi[0] and [f for f in F if f!=0 and 13 in fi[f]]==[10]
for e in ids:
 u=int(A.edges[e][0])
 while u!=root:
  u,pe=par[u];assert pe!=13
i=ids.index(13);B=[j for j in range(len(ids)) if j!=i]
sch=K[i,i]-K[i,B]@np.linalg.solve(K[np.ix_(B,B)],K[B,i])
assert abs(sch-1/M[i,i])<1e-10
gamma=3/(8*M[i,i]);b=3/32000;eps=b/(gamma-b)
for delta in (.1,.2,.3):
 theta=math.acos(1-delta);c=2/math.pi*(theta-math.sin(theta)*math.cos(theta))
 print(delta,'Haar',c,'deleted-face bound',max(0,c-eps))
assert abs(gamma-.4820924954982508)<1e-10
print('PASS M5 non-tree shared-link incidence and conditional finite-cap arithmetic')
