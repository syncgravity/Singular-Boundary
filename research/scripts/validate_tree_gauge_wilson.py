import numpy as np
rng=np.random.default_rng(533)
def mul(q,r):return np.r_[q[0]*r[0]-np.dot(q[1:],r[1:]),q[0]*r[1:]+r[0]*q[1:]+np.cross(q[1:],r[1:])]
def inv(q):return np.r_[q[0],-q[1:]]
def rot(q,v):
 w=q[0];a=q[1:];return (w*w-a@a)*v+2*a*(a@v)+2*w*np.cross(a,v)
def randq():
 q=rng.normal(size=4);return q/np.linalg.norm(q)
def p(a,b,c):return mul(mul(a,b),c)[0]
def grad(a,b,c):
 out=[];eps=1e-6
 for k in range(3):
  g=np.zeros(3)
  for j in range(3):
   axis=np.zeros(3);axis[j]=1
   d=np.r_[np.cos(eps/2),np.sin(eps/2)*axis];d0=inv(d)
   x=[a,b,c];y=[a,b,c];x[k]=mul(d,x[k]);y[k]=mul(d0,y[k])
   g[j]=(p(*x)-p(*y))/(2*eps)
  out.append(g)
 return out
K=np.eye(3);K[0,2]=K[2,0]=.3
assert np.linalg.eigvalsh(K)[0]>0
maxdiff=0
for i in range(100):
 a,b,c=randq(),randq(),randq(); da,db,dc=grad(a,b,c)
 d1=np.array([da,rot(a,db),rot(mul(a,b),dc)])
 d2=np.array([da,rot(a,db),rot(inv(c),dc)])
 Q1=np.einsum('ia,ij,ja->',d1,K,d1)
 Q2=np.einsum('ia,ij,ja->',d2,K,d2)
 maxdiff=max(maxdiff,abs(Q1-Q2))
 if i==0:
  h0,h1,h2=randq(),randq(),randq()
  ag=mul(mul(h0,a),inv(h1));bg=mul(mul(h1,b),inv(h2));cg=mul(mul(h2,c),inv(h0))
  assert abs(p(a,b,c)-p(ag,bg,cg))<1e-12
assert maxdiff<1e-8
print('PASS gauge invariant Wilson triangle: two tree forms agree; maximum difference',maxdiff)
