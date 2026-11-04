import numpy as np
from math import pi,acos,sqrt
from scipy.linalg import expm
from scipy.special import eval_chebyu
for t in (1.,2.,4.):
 x=np.cos(np.linspace(0,pi,3001))
 k=sum((n+1)*eval_chebyu(n,x)*np.exp(-t*n*(n+2)/4) for n in range(71))
 assert k.min()>0
 print(t,k.min()/k.max())
delta=.1
c=(2/pi)*(acos(1-delta)-(1-delta)*sqrt(2*delta-delta**2))
assert abs(c-.037386073468498655)<1e-12
T=np.array([[1.,-1.],[-1.,1.]])
V=np.diag([.4,-.2]);B=.4;t=1.2
ke=expm(-t*T);kh=expm(-t*(T+V))
assert np.all(kh>=np.exp(-t*B)*ke-1e-13)
assert np.all(kh<=np.exp(t*B)*ke+1e-13)
print('PASS finite model kernel domination and SU2 rotor electric heat contrasts')
