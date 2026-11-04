"""Verify original M5 non-tree chord sector-Sobolev cap certificate.

For the full proof, see R3_PROTECTED_CHORD_SECTOR_SOBOLEV_RELATIVE_CAP_2026-10-30.md.
The independent radial rotor eigensolve is a specialization, not the 30-link
interacting Penrose ground state. Original Whitney NPZ must be restored from Library.
"""
import hashlib, math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.special import eval_chebyu

p=Path(__file__).resolve().parent/"global_whitney_11face.npz"
assert hashlib.sha256(p.read_bytes()).hexdigest()=="d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf"
z=np.load(p);ids=list(map(int,z["edge_ids"]));M=z["matrix"];e=ids.index(13)
K=np.linalg.inv(M);B=[i for i in range(len(ids)) if i!=e]
schur=K[e,e]-K[e,B]@np.linalg.solve(K[np.ix_(B,B)],K[B,e])
assert abs(schur-1/M[e,e])<1e-11

g2_squared=1.
c=g2_squared/(2*M[e,e]);half_gap=.75*c
S=4*math.pi/math.sqrt(6)
print("M13,13",M[e,e],"c",c,"spinhalf gap",half_gap,"safe Sobolev S",S)
for b in (3/32000,.01,.05,.1):
 rho=abs(b)/half_gap
 lower=max(0.,math.sqrt(max(0.,1-rho*rho))-S*abs(b)/c)**2 if rho<1 else 0.
 N=40
 H=np.diag([c*n*(n+2)/4 for n in range(N+1)]).astype(float)
 for j in range(N):H[j,j+1]=H[j+1,j]=-b/2
 _,vec=eigh(H,subset_by_index=[0,0])
 q=vec[:,0];q=q if q[0]>0 else -q
 ps=np.linspace(-1,1,1601)
 density=q@np.stack([eval_chebyu(j,ps) for j in range(N+1)])
 assert np.min(density)>0
 actual=float(np.min(density**2))
 assert actual>=lower-1e-10
 print("b",b,"rho",rho,"theorem coefficient",lower,"radial rotor minimum",actual)
print("PASS: original M5 Schur identity, explicit uniform cap certificate and SU2 radial rotor specialization")
