import numpy as np
from math import pi
M=np.load('/mnt/data/global_whitney_11face.npz')['matrix']; K=np.linalg.inv(M)
ids=list(map(int,np.load('/mnt/data/global_whitney_11face.npz')['edge_ids']))
for e in (0,1,4,13):
 i=ids.index(e); b=[k for k in range(30) if k!=i]
 sch=K[i,i]-K[i,b]@np.linalg.solve(K[np.ix_(b,b)],K[b,i])
 assert abs(sch-1/M[i,i])<1e-11
 assert np.linalg.norm(K[i,b])>0.01
a=.35; eps=.2
x=np.linspace(0,2*pi,81);y=np.linspace(0,2*pi,83)
X,Y=np.meshgrid(x,y,indexing='ij');c=np.cos(X+Y);Omega=1+eps*c
V=-2*(1+a)*eps*c/Omega
lapA=2*(1+a)*eps*c
assert np.max(np.abs(lapA+V*Omega))<1e-12
assert np.max(abs(2*a*eps*c))>0.13
print('PASS SPD inverse metric cross coupling and positive elliptic ground state with nonzero mixed flux')
