import math
import numpy as np
from scipy.linalg import eigh
M=np.load('/mnt/data/global_whitney_11face.npz')['matrix']
gamma=3/(8*np.linalg.eigvalsh(M)[-1]); B0=9*3/32000; b=3/32000
lower=gamma-B0
err0=math.sqrt(B0/gamma);errb=math.sqrt(b/lower)
def cap(delta):
 t=math.acos(1-delta)
 return 2/math.pi*(t-math.sin(t)*math.cos(t))
assert lower>0
for d in (.1,.2,.3):print(d,max(0,cap(d)-err0-errb))
rng=np.random.default_rng(522)
for i in range(300):
 a=rng.uniform(.1,5)
 T=np.diag([0,a,2*a,4*a])
 V=np.diag(np.r_[0.,rng.uniform(-.3,.3,size=3)])
 B=np.linalg.norm(V,ord=2)
 w=eigh(T+V,eigvals_only=True)
 if a>B:assert w[1]-w[0]>=a-B-1e-12
print('PASS finite magnetic perturbation gap tests')
