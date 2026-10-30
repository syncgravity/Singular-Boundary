"""Audit effective local blocks from a supplied 30-link Whitney NPZ."""
import sys
import numpy as np
file=sys.argv[1] if len(sys.argv)>1 else "global_whitney_11face.npz"
d=np.load(file); M=d["matrix"]; ids=list(map(int,d["edge_ids"]))
assert M.shape==(30,30) and np.linalg.eigvalsh(M)[0]>0
K=np.linalg.inv(M)
reference={ (0,86):(0.6311719708357876,1.6848697857079034), (1,88):(1.3176740386402281,1.18741201978661), (4,372):(0.9247357057985095,1.7110577880440834), (13,26):(1.242265570819589,1.2855792798087755)}
for pair,(c0,l0) in reference.items():
 I=[ids.index(e) for e in pair]; B=[j for j in range(30) if j not in I]
 C=K[np.ix_(I,B)]
 eff=K[np.ix_(I,I)]-C@np.linalg.solve(K[np.ix_(B,B)],C.T)
 c=np.linalg.norm(C,2);l=np.linalg.eigvalsh(eff)[0]
 assert l>0 and abs(c-c0)<1e-9 and abs(l-l0)<1e-9
 print(pair,c,l)
print("PASS four local/background block numerical audits")
