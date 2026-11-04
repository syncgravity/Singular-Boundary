"""Actual M5 gauge-orbit chart transition: depends on original Library-restored archive.
Requires `validate_actual_m5_two_tree_wilson_forms.py` in same working directory.
"""
import runpy,collections,numpy as np
from pathlib import Path
base=Path(__file__).resolve().parent
m=runpy.run_path(str(base/"validate_actual_m5_two_tree_wilson_forms.py"))
rng=np.random.default_rng(541)
unit=m["unit"];A=m["A"];ids=m["edge_ids"];mul=m["mul"];inv=m["inv"]
def fix(U,tree):
 ad=collections.defaultdict(list)
 for e in tree:
  u,v,_=A.edges[e];i=m["edge_index"][e]
  ad[int(u)].append((int(v),U[i]));ad[int(v)].append((int(u),inv(U[i])))
 h={m["root"]:unit};queue=collections.deque([m["root"]])
 while queue:
  u=queue.popleft()
  for v,x in ad[u]:
   if v not in h:h[v]=mul(h[u],x);queue.append(v)
 assert len(h)==20
 X=U.copy()
 for i,e in enumerate(ids):
  u,v,_=A.edges[e];X[i]=mul(mul(h[int(u)],U[i]),inv(h[int(v)]))
 for e in tree: assert np.linalg.norm(X[m["edge_index"][e]]-unit)<1e-10
 return X
def energy(U,tree):
 G=m["grads"](U);V=m["transports"](tree,U)
 D=np.array([m["rot"](V[i],G[i]) for i in range(30)])
 return float(np.einsum("ia,ij,ja->",D,m["K"],D))
for i in range(5):
 U=rng.normal(size=(30,4));U/=np.linalg.norm(U,axis=1)[:,None]
 X,Y=fix(U,m["T1"]),fix(U,m["T2"])
 assert abs(m["obs"](X)-m["obs"](Y))<1e-10
 a,b=energy(U,m["T1"]),energy(U,m["T2"])
 assert abs(a-energy(X,m["T1"]))<2e-8
 assert abs(b-energy(Y,m["T2"]))<2e-8
 if i==0:
  print("tree1",a,"tree2",b,"difference",b-a)
  assert abs(a-b)>1e-5
print("PASS 5 orbit-chart invariance and nonidentity checks")
