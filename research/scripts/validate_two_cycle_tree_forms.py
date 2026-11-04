import numpy as np
rng=np.random.default_rng(535)
def mul(q,r):return np.r_[q[0]*r[0]-q[1:]@r[1:],q[0]*r[1:]+r[0]*q[1:]+np.cross(q[1:],r[1:])]
def inv(q):return np.r_[q[0],-q[1:]]
def rot(q,v):
 w=q[0];x=q[1:];return (w*w-x@x)*v+2*x*(x@v)+2*w*np.cross(x,v)
def ran():
 q=rng.normal(size=4);return q/np.linalg.norm(q)
def obs(Q):
 a,b,c,d=Q
 w=mul(mul(a,b),inv(c));z=mul(mul(a,d),inv(c))
 return mul(w,z)[0]
def grads(Q):
 eps=1e-6;out=[]
 for i in range(4):
  v=[]
  for j in range(3):
   axis=np.eye(3)[j];q=np.r_[np.cos(eps/2),np.sin(eps/2)*axis]
   u=[x.copy() for x in Q];t=[x.copy() for x in Q]
   u[i]=mul(q,u[i]);t[i]=mul(inv(q),t[i])
   v.append((obs(u)-obs(t))/(2*eps))
  out.append(v)
 return np.array(out)
K=np.eye(4);K[0,3]=K[3,0]=.3
assert np.linalg.eigvalsh(K)[0]>.6
maxdiff=0.
for j in range(100):
 Q=[ran() for _ in range(4)];a,b,c,d=Q;g=grads(Q)
 V1=[np.array([1.,0,0,0]),a,np.array([1.,0,0,0]),a]
 V2=[np.array([1.,0,0,0]),mul(c,inv(b)),np.array([1.,0,0,0]),mul(c,inv(b))]
 D1=np.array([rot(v,g[i]) for i,v in enumerate(V1)])
 D2=np.array([rot(v,g[i]) for i,v in enumerate(V2)])
 q1=np.einsum('ia,ij,ja->',D1,K,D1)
 q2=np.einsum('ia,ij,ja->',D2,K,D2)
 maxdiff=max(maxdiff,abs(q1-q2))
 if j<3:print(j,q1,q2,q1-q2)
assert maxdiff>.1
print('PASS two-cycle gauge-invariant tree-form difference:',maxdiff)
