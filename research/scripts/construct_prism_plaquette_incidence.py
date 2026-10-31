"""Construct all bottom/top horizontal and vertical Wilson plaquettes of six candidate
Penrose prisms; check rooted spanning-tree and selected-chord incidence.
Restore penrose_causal_study.py and wilson_torus.py from Library onto PYTHONPATH.
"""
import json,collections
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
result=[]
for m in (5,7,9,11,13,15):
 a=Approximant(m);fi,sg,_=penrose_faces(a)
 ef=collections.defaultdict(list)
 for f,es in enumerate(fi):
  for e in es:ef[int(e)].append(f)
 near=[set() for _ in a.faces]
 for faces in ef.values():
  for f in faces:near[f].update(set(faces)-{f})
 F={0};front={0}
 for _ in range(2):
  new=set().union(*(near[f] for f in front))-F;F|=new;front=new
 F=sorted(F);E=sorted({int(e) for f in F for e in fi[f]})
 V=sorted({int(v) for e in E for v in a.edges[e][:2]})
 ei={e:i for i,e in enumerate(E)};vi={v:i for i,v in enumerate(V)}
 ne,nv=len(E),len(V)
 plaquettes=[]
 for layer in (0,1):
  for f in F:
   plaquettes.append(("horizontal",layer,f,[layer*ne+ei[int(e)] for e in fi[f]]))
 for e in E:
  u,v=map(int,a.edges[e][:2])
  plaquettes.append(("vertical",None,e,[ei[e],2*ne+vi[v],ne+ei[e],2*ne+vi[u]]))
 chord=int(fi[0][0]);p={v:v for v in V}
 def root(v):
  while p[v]!=v:p[v]=p[p[v]];v=p[v]
  return v
 def add(e):
  u,v=map(int,a.edges[e][:2]);x,y=root(u),root(v)
  if x==y:return False
  p[x]=y;return True
 tree=set()
 for e in sorted({int(e) for e in fi[0]}-{chord}):
  assert add(e);tree.add(ei[e])
 for e in E:
  if e!=chord and add(e):tree.add(ei[e])
 assert len(tree)==nv-1
 tree|=set(range(2*ne,2*ne+nv))
 assert len(tree)==2*nv-1 and ei[chord] not in tree
 touching=[x for x in plaquettes if ei[chord] in x[3]]
 retained=[x for x in touching if not(x[0]=="horizontal" and x[1]==0 and x[2]==0)]
 assert len(touching)==3 and len(retained)==2
 assert {x[0] for x in retained}=={"horizontal","vertical"}
 rec=dict(M=m,base_faces=len(F),links=2*ne+nv,plaquettes=len(plaquettes),tree_edges=len(tree),target_chord=chord,incident=len(touching),retained=2)
 result.append(rec);print(rec)
with open("prism_plaquette_incidence.json","w") as f:json.dump(result,f,indent=2)
print("PASS all six candidate prism incidence checks")
