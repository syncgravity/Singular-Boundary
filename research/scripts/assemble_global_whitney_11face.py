"""Assemble rhombus Whitney Schur matrices on eleven-face M5 open disk."""
import os,sys,numpy as np
if os.environ.get("PENROSE_STUDY_SRC"):sys.path.insert(0,os.environ["PENROSE_STUDY_SRC"])
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
A=Approximant(M=5); fi,sg,_=penrose_faces(A)
F=(0,1,3,2,4,154,150,11,10,7,8)
ids=sorted({int(e) for f in F for e in fi[f]})
idx={e:i for i,e in enumerate(ids)}
orient={(int(z),int(w)):(i,1) for i,(z,w,d) in enumerate(A.edges)}
orient.update({(int(w),int(z)):(i,-1) for i,(z,w,d) in enumerate(A.edges)})
quad=np.array([[2/3,1/6,1/6],[1/6,2/3,1/6],[1/6,1/6,2/3]])
tr=((0,1,2),(0,2,3));ee=((0,1),(1,2),(2,3),(0,3),(0,2))
v=A.Qpar@np.eye(5)
H=np.zeros((len(ids),len(ids)))
for f in F:
 u,ua,uab,ub,aa,bb=map(int,A.faces[f]); verts=(u,ua,uab,ub)
 a,b=v[:,aa],v[:,bb]; X=np.array([[0,0],a,a+b,b]); M=np.zeros((5,5))
 for tri in tr:
  P=X[list(tri)]; grad=np.linalg.inv(np.column_stack((np.ones(3),P)))[1:,:].T
  area=abs(np.linalg.det(np.column_stack((P[1]-P[0],P[2]-P[0]))))/2
  forms=np.zeros((5,3,2))
  for j,(s,t) in enumerate(ee):
   if s in tri and t in tri:
    si,ti=tri.index(s),tri.index(t)
    for k,l in enumerate(quad):forms[j,k]=l[si]*grad[ti]-l[ti]*grad[si]
  M+=area/3*np.einsum('iqk,jqk->ij',forms,forms)
 S=M[:4,:4]-np.outer(M[:4,4],M[4,:4])/M[4,4]
 ei,sign=zip(*(orient[(verts[s],verts[t])] for s,t in ee[:4]))
 S=S*np.outer(sign,sign)
 ii=[idx[e] for e in ei];H[np.ix_(ii,ii)]+=S
vals=np.linalg.eigvalsh(H)
assert H.shape==(30,30) and np.allclose(H,H.T) and vals[0]>0
assert abs(vals[0]-0.143174148694)<1e-9
assert abs(vals[-1]-1.10465934416)<1e-9
assert np.count_nonzero(abs(H-np.diag(H.diagonal()))>1e-10)==132
print("PASS SPD global matrix",vals[0],vals[-1])
