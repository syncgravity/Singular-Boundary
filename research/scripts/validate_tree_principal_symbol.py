import numpy as np
def mul(q,r):
 return np.r_[q[0]*r[0]-np.dot(q[1:],r[1:]),q[0]*r[1:]+r[0]*q[1:]+np.cross(q[1:],r[1:])]
def inv(q):return np.r_[q[0],-q[1:]]
def rotate(q,v):
 w=q[0];a=q[1:]
 return (w*w-np.dot(a,a))*v+2*a*np.dot(a,v)+2*w*np.cross(a,v)
I=np.array([1.,0.,0.,0.]);c=np.array([np.sqrt(.5),0.,0.,np.sqrt(.5)])
x=np.array([1.,0.,0.]);Kac=.3
Q1=2+2*Kac*np.dot(x,rotate(mul(I,I),x))
Q2=2+2*Kac*np.dot(x,rotate(inv(c),x))
assert abs(Q1-2.6)<1e-12 and abs(Q2-2.)<1e-12
assert 1-abs(Kac)>0
print('PASS root tree principal symbols',Q1,Q2)
