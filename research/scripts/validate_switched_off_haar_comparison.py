import math
import numpy as np
M=np.load('/mnt/data/global_whitney_11face.npz')['matrix']
gamma=3/(8*np.linalg.eigvalsh(M)[-1])
B0=9*3/32000
error=math.sqrt(B0/gamma)
def haarcap(delta):
 t=math.acos(1-delta)
 return 2/math.pi*(t-(1-delta)*math.sqrt(2*delta-delta*delta))
assert abs(gamma-0.3394711699872615)<1e-12
assert abs(error-0.04985462390154264)<1e-12
for d in (.1,.2,.3):
 c=haarcap(d)
 print(d,'Haar',c,'lower',max(0,c-error))
assert haarcap(.1)<error<haarcap(.2)
rng=np.random.default_rng(514)
for _ in range(500):
 q=rng.normal(size=2);q/=np.linalg.norm(q)
 theta=rng.uniform(-math.pi,math.pi)
 u=np.array([math.cos(theta),math.sin(theta)])
 assert abs((u@q)**2-u[0]**2)<=math.sqrt(max(0,1-q[0]**2))+1e-12
print('PASS 500 pure state probability contraction tests')
