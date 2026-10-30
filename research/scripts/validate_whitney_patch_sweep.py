"""Verify patch-independent Whitney assembly lower bound on finite M5 geometry."""
import os,sys,numpy as np
from collections import defaultdict,deque
if os.environ.get("PENROSE_STUDY_SRC"):sys.path.insert(0,os.environ["PENROSE_STUDY_SRC"])
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
A=Approximant(M=5);fi,_,_=penrose_faces(A); v=A.Qpar@np.eye(5)
edge_map={}
for i,(u,w,_) in enumerate(A.edges):
 edge_map[int(u),int(w)]=(i,1);edge_map[int(w),int(u)]=(i,-1)
q=np.array([[2/3,1/6,1/6],[1/6,2/3,1/6],[1/6,1/6,2/3]])
ed=((0,1),(1,2),(2,3),(0,3),(0,2))
local=[];ids=[];neighbor=defaultdict(set);byedge=defaultdict(list)
for f in A.faces:
 u,ua,uab,ub,di,dj=map(int,f);verts=(u,ua,uab,ub);a,b=v[:,di],v[:,dj]
 X=np.array([[0,0],a,a+b,b]);M=np.zeros((5,5))
 for tri in ((0,1,2),(0,2,3)):
  p=X[list(tri)];g=np.linalg.inv(np.column_stack((np.ones(3),p)))[1:,:].T
  area=abs(np.linalg.det(np.column_stack((p[1]-p[0],p[2]-p[0]))))/2
  W=np.zeros((5,3,2))
  for z,(s,t) in enumerate(ed):
   if s in tri and t in tri:
    si,ti=tri.index(s),tri.index(t)
    for j,l in enumerate(q):W[z,j]=l[si]*g[ti]-l[ti]*g[si]
  M+=area/3*np.einsum('iqk,jqk->ij',W,W)
 S=M[:4,:4]-np.outer(M[:4,4],M[4,:4])/M[4,4]
 oriented=[edge_map[verts[s],verts[t]] for s,t in ed[:4]]
 ei=np.array([e for e,_ in oriented]);sg=np.array([z for _,z in oriented])
 local.append(S*np.outer(sg,sg));ids.append(ei)
 for e in ei:byedge[int(e)].append(len(local)-1)
for faces in byedge.values():
 if len(faces)==2:
  a,b=faces;neighbor[a].add(b);neighbor[b].add(a)
order=[];seen=set();todo=deque([0])
while todo:
 f=todo.popleft()
 if f in seen:continue
 seen.add(f);order.append(f);todo.extend(sorted(neighbor[f]-seen))
assert len(order)==188
local_min=min(np.linalg.eigvalsh(m)[0] for m in local)
assert local_min>0
for n in (11,25,50,100,150,187,188):
 fs=order[:n]; edges=sorted({int(e) for f in fs for e in ids[f]})
 lookup={e:i for i,e in enumerate(edges)}
 H=np.zeros((len(edges),len(edges)))
 for f in fs:
  ii=[lookup[e] for e in ids[f]]
  H[np.ix_(ii,ii)]+=local[f]
 eig=np.linalg.eigvalsh(H)
 assert eig[0]>=local_min-1e-10
 print(n,len(edges),format(eig[0],'.12f'),format(eig[-1],'.12f'))
print('PASS tile minimum',format(local_min,'.12f'))
