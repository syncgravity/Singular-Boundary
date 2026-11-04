import numpy as np
M=np.load('/mnt/data/global_whitney_11face.npz')['matrix']
c=1/(2*np.linalg.eigvalsh(M)[-1])
gamma=3*c/4-9*3/32000
assert gamma>0.3386
H=np.array([[0.,1.],[1.,2.]])
w,v=np.linalg.eigh(H)
assert 2-w[0]>2.4 and abs(v[1,0])>0.38
print('PASS',gamma,abs(v[1,0]))
