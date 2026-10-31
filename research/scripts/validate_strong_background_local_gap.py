"""Strong-background torus: local Fourier gap survives collapsing global gap."""
import numpy as np
from scipy.linalg import eigh
a=0.35;n=35;m=np.arange(-n,n+1)
for B in (0.,10.,50.,100.):
 H0=np.diag(m.astype(float)**2+B)
 for j in range(len(m)-2):H0[j,j+2]=H0[j+2,j]=-B/2
 w=eigh(H0,eigvals_only=True,subset_by_index=(0,1))
 H1=H0+np.diag(2*a*m+np.ones(len(m)))
 one=eigh(H1,eigvals_only=True,subset_by_index=(0,0))[0]
 local_gap=one-w[0]
 assert local_gap>=1-a*a-1e-8
 print('B',B,'background_gap',w[1]-w[0],'local_sector_gap',local_gap)
print('PASS magnetic-strength-independent local sector gap')
