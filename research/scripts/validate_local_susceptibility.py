import numpy as np
for t,d in [(0.1,0),(1,0.4),(0.3,5)]:
 H=np.array([[0.,-t],[-t,d]])
 p=np.diag([0.,1.])
 ev,U=np.linalg.eigh(H)
 g=U[:,0]; m=g@p@g; phi=(p-m*np.eye(2))@g
 var=phi@phi
 first=phi@(H-ev[0]*np.eye(2))@phi
 chi=2*(phi@U[:,1])**2/(ev[1]-ev[0])
 assert abs(var**2-first*chi/2)<1e-12
 assert abs(var-(g@(p@p)@g-m*m))<1e-12
 print(t,d,'variance',var,'first moment',first,'susceptibility',chi,'moment',1-g@(p@p)@g)
print('PASS two-state spectral identity and missing mean obstruction')
