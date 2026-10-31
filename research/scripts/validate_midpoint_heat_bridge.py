import numpy as np
from scipy.linalg import expm
L=np.array([[1.,-1.],[-1.,1.]])
V=np.diag([.7,-.3]);p=np.diag([1.,-1.]);b=.8

def bridge(H,t,s,x=0):
 w,U=np.linalg.eigh(H)
 kt=expm(-t*H);k2=expm(-2*t*H)
 nu=kt[x,:]**2/k2[x,x]
 C=np.exp(2*s*w[0])*expm(-2*s*H)[x,x]/U[x,0]**2-1
 z=np.exp(-2*(t-s)*(w[1]-w[0]))*C
 err=np.sqrt(z/(1+z));tv=.5*sum(abs(nu-U[:,0]**2))
 assert abs(sum(nu)-1)<1e-12 and tv<=err+1e-12
 return nu,err,U[:,0]**2
for t in (.25,1.,2.,5.):
 nu0,e0,m0=bridge(L+V,t,.25)
 nub,eb,mb=bridge(L+V-b*p,t,.25)
 assert np.all(nub>=np.exp(-4*b*t)*nu0-1e-12)
 assert np.all(nub<=np.exp(4*b*t)*nu0+1e-12)
 assert np.all(mb>=np.exp(-4*b*t)*(m0-e0)-eb-1e-12)
 print(t,e0,eb)
print('PASS midpoint bridge spectral mixing and local coupling comparison')
