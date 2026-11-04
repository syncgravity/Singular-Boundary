import numpy as np
def mul(q,r):
 return np.r_[q[0]*r[0]-q[1:]@r[1:],q[0]*r[1:]+r[0]*q[1:]+np.cross(q[1:],r[1:])]
def inv(q):return np.r_[q[0],-q[1:]]
def rot(q,v):
 w=q[0];a=q[1:]
 return (w*w-a@a)*v+2*a*(a@v)+2*w*np.cross(a,v)
W=np.array([0.,0.,0.,1.]); z=W[1:]
for U,expected in [(np.array([1.,0.,0.,0.]),.7),(np.array([0.,1.,0.,0.]),.3),(np.array([np.sqrt(.5),np.sqrt(.5),0.,0.]),.5)]:
 V=mul(inv(U),W)
 assert abs(mul(U,V)[0])<1e-12
 g1=-z/2;g2=-rot(inv(U),z)/2
 q=g1@g1+g2@g2+0.8*(g1@g2)
 assert abs(q-expected)<1e-12
 print('p',mul(U,V)[0],'Gamma',q)
print('PASS nonclosed anisotropic SU2 radial diffusion at fixed trace')
