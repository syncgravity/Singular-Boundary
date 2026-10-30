import numpy as np, json
from collections import defaultdict
# Two edge-adjacent oriented quadrilaterals. This is a realizable local combinatorial
# rhombus patch, not an extraction of the uploaded Penrose tiling coordinates.
polygons=[(0,1,2,3),(2,1,4,5)]
vertices=[(v,t) for t in (0,1) for v in range(6)]
vid={x:i for i,x in enumerate(vertices)}
edges=[]; emap={}; faces=[]; fmap={}; cellcols=[]
def edge(u,v):
 key=tuple(sorted((u,v)))
 if key not in emap:
  emap[key]=len(edges);edges.append((u,v))
 idx=emap[key];return idx,1 if edges[idx]==(u,v) else -1
def face_cycle(p):
 col=defaultdict(int)
 for u,v in zip(p,p[1:]+p[:1]):
  i,s=edge(u,v);col[i]+=s
 return dict(col)
def add_face(p):
 key=tuple(sorted(p))
 col=face_cycle(p)
 if key not in fmap:
  fmap[key]=len(faces);faces.append((p,col))
 i=fmap[key]
 if col==faces[i][1]:s=1
 elif all(col.get(e,0)==-v for e,v in faces[i][1].items()) and len(col)==len(faces[i][1]):s=-1
 else:raise RuntimeError('inconsistent face')
 return i,s
for poly in polygons:
 col=defaultdict(int)
 bottom=[vid[v,0] for v in poly];top=[vid[v,1] for v in poly]
 for cycle,coeff in [(bottom,-1),(top,+1)]:
  i,s=add_face(cycle);col[i]+=coeff*s
 for a,b in zip(poly,poly[1:]+poly[:1]):
  side=[vid[a,0],vid[b,0],vid[b,1],vid[a,1]]
  i,s=add_face(side);col[i]+=s
 cellcols.append(dict(col))
B1=np.zeros((len(vertices),len(edges)),dtype=np.int64)
for i,(u,v) in enumerate(edges): B1[u,i]-=1;B1[v,i]+=1
B2=np.zeros((len(edges),len(faces)),dtype=np.int64)
for i,(_,col) in enumerate(faces):
 for e,s in col.items(): B2[e,i]=s
B3=np.zeros((len(faces),len(polygons)),dtype=np.int64)
for j,col in enumerate(cellcols):
 for i,s in col.items():B3[i,j]=s
assert np.all(B1@B2==0) and np.all(B2@B3==0)
assert len(faces)==11 and sum(np.count_nonzero(B3[i,:])==2 for i in range(len(faces)))==1
# Selected internal common temporal side face. Its six? total 11 faces, 1 internal.
internal=np.flatnonzero(np.count_nonzero(B3,axis=1)==2)
report={'source':'constructed two face-sharing quadrilateral prisms; NOT dataset-extracted Penrose tiling', 'vertices':len(vertices),'edges':len(edges),'faces':len(faces),'cells':len(polygons),'interior_faces':internal.tolist(),'rank_d1':int(np.linalg.matrix_rank(B1)),'rank_d2':int(np.linalg.matrix_rank(B2)),'rank_d3':int(np.linalg.matrix_rank(B3)),'chain_1_2_max':int(np.abs(B1@B2).max()),'chain_2_3_max':int(np.abs(B2@B3).max()),'max_faces_per_edge':int(np.max(np.sum(abs(B2),axis=1))),'shared_face_incidence':B3[internal[0]].tolist()}
np.savez('/mnt/data/R3_two_prism_certified_2026_10_27/incidence.npz',d1=B1,d2=B2,d3=B3,vertices=np.array(vertices),edges=np.array(edges),face_vertices=np.array([f[0] for f in faces],dtype=object))
with open('/mnt/data/R3_two_prism_certified_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
