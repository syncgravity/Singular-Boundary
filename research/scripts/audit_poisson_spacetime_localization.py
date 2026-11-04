"""Spacetime Poisson localization criterion + reflecting-chain countercheck."""
import math
import numpy as np
from scipy.integrate import quad
mu,v,lam=.7,1.4,.35
beta=mu*lam/(lam+mu*v)
for d in (0,2,5,10,20):
 f=lambda t:min(math.exp(-lam*t),math.exp(-mu*(d-v*t)))
 integral=quad(f,0,max(100,d/v+100))[0]
 upper=(1/(mu*v)+1/lam)*math.exp(-beta*d)
 assert integral<=upper*(1+1e-9)
 print(d,integral,upper)
for n in (16,32,64,128):
 D=np.diag(np.full(n,2.))-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1)
 D[0,0]=D[-1,-1]=1
 f=np.eye(n)[0]-np.ones(n)/n
 u=np.linalg.solve(D+np.ones((n,n))/n,f)
 q=np.linalg.solve(D+.1*np.eye(n),np.eye(n)[0])
 assert np.linalg.norm(D@u-f)<1e-8
 assert abs(u[0]-(n-1)*(2*n-1)/(6*n))<1e-9
 print(n,u[0],q[0],q[-1])
print('PASS')
