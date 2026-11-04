"""Check finite M5 one-edge Schur coefficients; operator gap proven analytically."""
import numpy as np
z=np.load('/mnt/data/global_whitney_11face.npz')
M=z['matrix']; ids=list(map(int,z['edge_ids'])); K=np.linalg.inv(M)
b=3/32000
for edge in (86,88,372,26):
 i=ids.index(edge); rest=[j for j in range(len(ids)) if j!=i]
 sch=K[i,i]-K[i,rest]@np.linalg.solve(K[np.ix_(rest,rest)],K[rest,i])
 assert abs(sch-1/M[i,i])<1e-10
 gamma=3/(8*M[i,i]); assert b<gamma
 print(edge,'M_ee',M[i,i],'gap',gamma,'coupled response',b/(gamma-b))
print('PASS M5 matrix Schur identities; functional diamagnetism analytic')
