"""R3-IR-553 local Poisson response regression plus original Whitney block audit."""
import hashlib,numpy as np
from scipy.linalg import eigh
from pathlib import Path
p=Path(__file__).resolve().parent/"global_whitney_11face.npz"
if not p.exists():p=Path("/mnt/data/tsb_recovery/global_whitney_11face.npz")
assert hashlib.sha256(p.read_bytes()).hexdigest()=="d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf"
z=np.load(p);ids=list(map(int,z["edge_ids"]));K=np.linalg.inv(z["matrix"])
face=[ids.index(i) for i in (1,4,13,0)];other=[i for i in range(30) if i not in face]
w=np.zeros(30);w[face]=np.array([1,1,-1,-1])/2
print("M5 kappa",w@K@w,"face/environment current l2",np.linalg.norm((w@K)[other]),"block norm",np.linalg.norm(K[np.ix_(face,other)],2))
L=np.array([[-1.,1.,0.],[1.,-2.,1.],[0.,1.,-1.]])
W=np.diag([-1.,0.,1.]);pi=np.ones(3)/3;A=-L
ev,Q=eigh(A);R=Q@np.diag([0. if x<1e-12 else 1/x for x in ev])@Q.T
u1=-R@np.diag(W);wrw=np.diag(W)*(R@np.diag(W))
u2=R@(wrw-np.dot(pi,wrw))
D=u1*u1+2*u2;D-=np.dot(pi,D)
print("u1",u1,"u2",u2,"second response",D)
assert np.allclose(u1,[1,0,-1]);assert np.allclose(u2,[1/9,-2/9,1/9])
for b in (.08,.04,.02,.01):
 e,v=eigh(A+b*W);q=np.abs(v[:,0]);q/=np.dot(pi,q)
 density=q*q/np.dot(pi,q*q);sym=(density+density[::-1])/2
 err=np.max(np.abs(sym-(1+b*b*D)))
 print("b",b,"err",err,"err/b4",err/b**4)
 assert err<2*b**4
print("PASS")
