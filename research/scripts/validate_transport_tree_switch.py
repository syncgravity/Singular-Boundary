"""Exact SU(2) quaternion transport coefficient difference for alternative trees."""
import numpy as np
def mul(q,r):
 w,v=q[0],q[1:];z,u=r[0],r[1:]
 return np.r_[w*z-np.dot(v,u),w*u+z*v+np.cross(v,u)]
def adj(q,v):
 w=q[0];a=q[1:]
 return (w*w-np.dot(a,a))*v+2*a*np.dot(a,v)+2*w*np.cross(a,v)
a=np.array([np.sqrt(.5),np.sqrt(.5),0.,0.])
b=np.array([np.sqrt(.5),0.,np.sqrt(.5),0.])
c=np.array([np.sqrt(.5),0.,0.,np.sqrt(.5)])
u=np.array([1.,0.,0.]);v=np.array([0.,1.,0.])
T1=np.dot(u,adj(mul(a,b),v));T2=np.dot(u,adj(c,v))
assert abs(T1-0.)<1e-12 and abs(T2+1.)<1e-12
print('PASS coefficient inequality',T1,T2,'not spectral inequivalence')
