import numpy as np,json,collections
from pathlib import Path
z=np.load('/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz'); B1=z['d1'];B2=z['d2'];Q=list(map(int,z['seam_face_ids']))
E=sorted(set(map(int,np.flatnonzero(np.any(B2[:,Q]!=0,axis=1)))))
verts=sorted(set(map(int,np.flatnonzero(np.any(B1[:,E]!=0,axis=1)))))
endpoints={e:(int(np.flatnonzero(B1[:,e]==-1)[0]),int(np.flatnonzero(B1[:,e]==1)[0])) for e in E}
adj={v:[] for v in verts}
for e,(a,b) in endpoints.items():adj[a].append((b,e,1));adj[b].append((a,e,-1))
root=4; parent={root:None}; paths={root:[]}; tree=[];queue=collections.deque([root]);
while queue:
 v=queue.popleft()
 for w,e,s in sorted(adj[v],key=lambda t:t[1]):
  if w not in parent:parent[w]=v;paths[w]=paths[v]+[(e,s)];tree.append(e);queue.append(w)
assert len(verts)==10 and len(E)==13 and len(tree)==9
chords=sorted(set(E)-set(tree))
# signed based face word, as independently implemented in former contraction

def face_word(f):
 es=list(map(int,np.flatnonzero(B2[:,f])));st={e:int(np.flatnonzero(B1[:,e]==-1)[0]) for e in es};en={e:int(np.flatnonzero(B1[:,e]==1)[0]) for e in es};v=min(set(st.values())|set(en.values()));w=[]
 for _ in es:
  o=[(e,1,en[e]) for e in es if st[e]==v and B2[e,f]==1 and e not in [x[0] for x in w]]+[(e,-1,st[e]) for e in es if en[e]==v and B2[e,f]==-1 and e not in [x[0] for x in w]]
  assert len(o)==1,(f,v,o)
  e,s,v=o[0];w.append((e,s))
 return w
words={f:face_word(f) for f in Q}
reduced={f:[(e,s) for e,s in words[f] if e in chords] for f in Q}
# One chord per face validates genuine independent interface coordinates.
assert all(len(reduced[f])==1 for f in Q),(chords,reduced)
assert sorted([e for f in Q for e,s in reduced[f]])==chords
# Root path to face basepoint, to compare common-root holonomies: L_q=P_root->base W_q P_root->base^-1.
common_words={f:paths[min(set([endpoints[e][0] for e,s in words[f]]+[endpoints[e][1] for e,s in words[f]]))]+words[f]+[(e,-s) for e,s in reversed(paths[min(set([endpoints[e][0] for e,s in words[f]]+[endpoints[e][1] for e,s in words[f]]))]) ] for f in Q}
for f,word in common_words.items():
 pos=root
 for e,s in word:
  a,b=endpoints[e];assert pos==(a if s==1 else b),(f,e,s,pos)
  pos=b if s==1 else a
 assert pos==root
report={'interface_vertices':verts,'interface_edges':E,'tree_root':root,'tree_edges':tree,'chord_edges':chords,'face_words':{str(f):words[f] for f in Q},'root_paths':{str(k):v for k,v in paths.items()},'common_basepoint_words':{str(f):common_words[f] for f in Q},'gauge_fixed_face_chords':{str(f):reduced[f] for f in Q},'betti_1_interface':len(E)-len(verts)+1,'scope':'interface tree-coordinate identity, not completed exterior Fourier contraction'}
out=Path('/mnt/data/R3_four_prism_gaugefixed_2026_10_27');(out/'certificate.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:report[k] for k in ['tree_root','tree_edges','chord_edges','gauge_fixed_face_chords']},indent=2))
# extend interface tree to an all-vertex maximal tree
full_edges=list(range(B1.shape[1]));adjfull={v:[] for v in range(B1.shape[0])}
for e in full_edges:
 a=int(np.flatnonzero(B1[:,e]==-1)[0]);b=int(np.flatnonzero(B1[:,e]==1)[0]);adjfull[a].append((b,e));adjfull[b].append((a,e))
seen=set(verts);fulltree=list(tree)
while len(seen)<B1.shape[0]:
 eligible=sorted((e,a,b) for a in seen for b,e in adjfull[a] if b not in seen)
 assert eligible
 e,a,b=eligible[0];seen.add(b);fulltree.append(e)
assert len(fulltree)==17
free=sorted(set(full_edges)-set(fulltree));assert len(free)==16 and set(chords).issubset(free)
report['full_tree_edges']=fulltree;report['full_free_edges']=free;report['exterior_free_edges']=sorted(set(free)-set(chords));report['full_gaugefixed_dimension']=len(free)
(out/'certificate.json').write_text(json.dumps(report,indent=2));print('full gauge:',len(fulltree),'tree edges,',len(free),'free edges incl',len(chords),'ports +',len(free)-len(chords),'exterior')
