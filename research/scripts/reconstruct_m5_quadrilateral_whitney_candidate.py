"""Candidate quadrilateral Whitney/Nedelec edge mass for the archived M5 geometry.
Requires penrose_causal_study.py and wilson_torus.py on PYTHONPATH.
This is NOT validated as the historical global Whitney matrix.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
A=Approximant(M=5)
F=[0,1,3,2,4,154,150,11,10,7,8]
fi,_,_=penrose_faces(A)
E=sorted(set(map(int,fi[F].flat)));where={e:i for i,e in enumerate(E)}
M=np.zeros((len(E),len(E)))
x,w=leggauss(4);x=(x+1)/2;w=w/2
for f in F:
 v0,v1,v2,v3,aa,bb=A.faces[f]
 J=A.Qpar[:,[aa,bb]]
 assert abs(np.linalg.det(J))>1e-10
 pairs=[(v0,v1),(v1,v2),(v2,v3),(v3,v0)]
 index=[];sgn=[]
 for u,v in pairs:
  matches=[(eid,1 if (s,t)==(u,v) else -1) for eid,(s,t,k) in enumerate(A.edges) if (s,t)==(u,v) or (s,t)==(v,u)]
  assert len(matches)==1
  eid,sign=matches[0];index.append(where[eid]);sgn.append(sign)
 local=np.zeros((4,4))
 for u,wu in zip(x,w):
  for v,wv in zip(x,w):
   ref=np.array([[1-v,0],[0,u],[-v,0],[0,-(1-u)]])
   physical=ref@np.linalg.inv(J)
   local+=wu*wv*abs(np.linalg.det(J))*(physical@physical.T)
 for i in range(4):
  for j in range(4):M[index[i],index[j]]+=sgn[i]*sgn[j]*local[i,j]
eig=np.linalg.eigvalsh(M)
assert len(E)==30 and eig[0]>0 and np.allclose(M,M.T)
print('eigen min/max',eig[0],eig[-1],'edge13',M[where[13],where[13]])
np.savez_compressed('m5_whitney_candidate.npz',matrix=M,edge_ids=np.array(E),eigenvalues=eig)
