import numpy as np
from scipy.linalg import eigh
P=np.diag([1.,-1.])
for a in (.2,1.,3.):
 H0=np.array([[0.,-a],[-a,0.]])
 w0,U0=eigh(H0);z=U0[:,0];gap=w0[1]-w0[0]
 assert abs(z@P@z)<1e-13
 for b in (.01,.1,.8,5.):
  _,U=eigh(H0-b*P);v=U[:,0]
  distance=np.sqrt(max(0.,1-(z@v)**2))
  assert distance<=np.sqrt(b/gap)+1e-12
  assert v[0]**2>=z[0]**2-np.sqrt(b/gap)-1e-12
print('PASS direct local ground-state comparison without semigroup time')
