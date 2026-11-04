"""Exact SU2 connector-link Haar sector obstruction, with Haar quaternion Monte Carlo."""
import numpy as np
c=.3
K=np.array([[1.,0.,0.],[0.,1.,c],[0.,c,1.]])
assert np.linalg.eigvalsh(K)[0]>0
rng=np.random.default_rng(524);n=150000
q=rng.normal(size=(n,3,4))
q/=np.linalg.norm(q,axis=2,keepdims=True)
e,f,g=q[:,0],q[:,1],q[:,2]
w=e[:,0];v=e[:,1:];u=g[:,1:]
rot=(w*w-np.sum(v*v,axis=1))[:,None]*u+2*v*np.einsum('ij,ij->i',v,u)[:,None]+2*w[:,None]*np.cross(v,u)
dot=np.einsum('ij,ij->i',f[:,1:],rot)
measured=np.mean((-.5*c*dot)**2)
expected=3*c*c/64
assert abs(measured-expected)<.0012
print('PASS SPD gauge-invariant transporter model')
print('offsector squared norm Monte Carlo',measured,'exact',expected)
