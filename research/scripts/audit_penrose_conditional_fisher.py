"""Original M5 inverse-Whitney conditional Fisher coefficient sanity checks.
Rehydrate global_whitney_11face.npz from Library into current directory first.
"""
from pathlib import Path
import hashlib, numpy as np
from scipy.integrate import quad
from math import pi, sin, cos, exp
p=Path(__file__).resolve().parent/"global_whitney_11face.npz"
assert hashlib.sha256(p.read_bytes()).hexdigest()=="d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf"
z=np.load(p);ids=list(map(int,z["edge_ids"]));K=np.linalg.inv(z["matrix"]);e=ids.index(13)
ix=[ids.index(i) for i in [1,4,13,0]];s=np.array([1,1,-1,-1])
w=np.zeros(30);w[ix]=s/2;kappa=w@K@w
print("kappa",kappa,"off-face current coefficient l2",np.linalg.norm(np.delete(w@K,ix)))
print("edge13 metric row off-diagonal l2",np.linalg.norm(np.delete(K[e],e)))
print("Schur edge13 coefficient",1/z["matrix"][e,e])
for lam in (.5,2.,5.):
 B=quad(lambda u:2*lam*abs(cos(u)*sin(u)),0,pi)[0]
 assert abs(B-2*lam)<1e-10
 Z=quad(lambda u:2/pi*sin(u)**2*exp(-2*lam*cos(u)**2),0,pi)[0]
 assert exp(-2*B)<exp(-2*lam)/Z
 print("lambda",lam,"B",B,"lower ratio",exp(-2*B))
print("PASS")
