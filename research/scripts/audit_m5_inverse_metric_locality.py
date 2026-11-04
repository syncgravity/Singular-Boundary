"""Compute spatial coupling tails of the original archived M5 inverse Whitney mass.
Restore the original NPZ and geometry archive from ChatGPT Library first.
"""
from pathlib import Path
import hashlib, collections, numpy as np
p=Path("global_whitney_11face.npz")
expected="d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf"
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
z=np.load(p); ids=[int(x) for x in z["edge_ids"]]; M=z["matrix"]; K=np.linalg.inv(M)
n=len(ids); a,bb=np.linalg.eigvalsh(M)[[0,-1]]
rho=(bb-a)/(bb+a)
neighbors=[{j for j in range(n) if j!=i and abs(M[i,j])>1e-12} for i in range(n)]
dist=np.full((n,n),999,dtype=int)
for i in range(n):
 dist[i,i]=0; q=collections.deque([i])
 while q:
  u=q.popleft()
  for v in neighbors[u]:
   if dist[i,v]==999:
    dist[i,v]=dist[i,u]+1; q.append(v)
assert np.all(dist<999)
assert np.all(np.abs(K)<=rho**dist/a+1e-10)
print("a",a,"b",bb,"rho",rho,"mass offdiag pairs",sum(map(len,neighbors))//2)
for d in sorted(set(dist.ravel())):
 if d:
  vals=np.abs(K[dist==d]);print("distance",d,"count",len(vals),"maximum",vals.max(),"bound",rho**d/a)
print("PASS")
