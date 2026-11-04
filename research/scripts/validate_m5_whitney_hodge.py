import numpy as np
from penrose_causal_study import Approximant
a=Approximant(M=5); f=a.faces[0]; u=a.Qpar[:,int(f[4])]; v=a.Qpar[:,int(f[5])]
X=np.array([[0.,0.],u,u+v,v]); tris=((0,1,2),(0,2,3))
edges=((0,1),(1,2),(2,3),(0,3),(0,2))
quad=((2/3,1/6,1/6),(1/6,2/3,1/6),(1/6,1/6,2/3))
M=np.zeros((5,5))
for tri in tris:
 p=X[list(tri)]
 G=np.linalg.inv(np.array([[1,*p[0]],[1,*p[1]],[1,*p[2]]]))[1:,:].T
 area=abs(np.linalg.det(np.stack((p[1]-p[0],p[2]-p[0]),axis=1)))/2
 F=np.zeros((5,3,2))
 for i,(s,t) in enumerate(edges):
  if s in tri and t in tri:
   j=tri.index(s);k=tri.index(t)
   for z,lam in enumerate(quad): F[i,z]=lam[j]*G[k]-lam[k]*G[j]
 M+=area/3*np.einsum('iqk,jqk->ij',F,F)
assert min(np.linalg.eigvalsh(M))>0
S=M[:4,:4]-np.outer(M[:4,4],M[4,:4])/M[4,4]
assert min(np.linalg.eigvalsh(S))>0
assert np.count_nonzero(abs(S-np.diag(np.diag(S)))>1e-10)==12
print('PASS 5-edge Whitney SPD, 4-edge Schur SPD, 12 nonzero off-diagonal entries')
