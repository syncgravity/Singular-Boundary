import numpy as np
from scipy.linalg import expm
L=np.array([[1.,-1.],[-1.,1.]])
V=np.diag([.7,-.3]); p=np.diag([1.,-1.]); b=.8
for t in (.25,1.,2.,5.):
 A=expm(-t*(L+V)); B=expm(-t*(L+V-b*p))
 assert np.all(B>=np.exp(-b*t)*A-1e-12)
 assert np.all(B<=np.exp(b*t)*A+1e-12)
 A=A/A.sum(axis=1,keepdims=True);B=B/B.sum(axis=1,keepdims=True)
 ratio=B/A
 assert ratio.min()>=np.exp(-2*b*t)-1e-12
 assert ratio.max()<=np.exp(2*b*t)+1e-12
 print(t,ratio.min(),ratio.max())
print('PASS finite-time local semigroup comparison')
