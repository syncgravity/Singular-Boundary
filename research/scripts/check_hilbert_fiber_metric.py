import numpy as np
z=np.load('/mnt/data/global_whitney_11face.npz');M=z['matrix'];K=np.linalg.inv(M);E=list(map(int,z['edge_ids']))
for edge in (13,26,86,88,372):
 i=E.index(edge);B=[j for j in range(30) if j!=i]
 s=K[i,i]-K[i,B]@np.linalg.solve(K[np.ix_(B,B)],K[B,i])
 assert abs(s-1/M[i,i])<1e-10
 print(edge,3/(8*M[i,i]))
print('PASS')
