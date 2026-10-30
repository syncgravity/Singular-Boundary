import numpy as np, json, collections
from pathlib import Path
ROOT=Path(__file__).resolve().parent
z=np.load(ROOT/'prism_incidence.npz')
d1=z['d1'];d2=z['d2'];Q=set([13,18,22,25,26,29,32,37]);R=set(range(d2.shape[1]))-Q
nV,nE=d1.shape
ends={e:(int(np.flatnonzero(d1[:,e]<0)[0]),int(np.flatnonzero(d1[:,e]>0)[0])) for e in range(nE)}
# Selected tree: planar spanning tree at slice 0, all 18 lower vertical temporal links.
P=list(range(36,54));visited={0};sp=[]
for e in range(12):
 a,b=ends[e]
 if (a in visited)!=(b in visited): sp.append(e);visited.add(a if a not in visited else b)
assert len(sp)==8 and len(P)==18
T=set(sp+P);assert len(T)==26
# Validate connected tree
uf=list(range(nV))
def find(a):
 while uf[a]!=a:a=uf[a]
 return a
for e in T:
 a,b=ends[e];a=find(a);b=find(b);assert a!=b;uf[a]=b
assert len({find(x) for x in range(nV)})==1
chords=sorted(set(range(nE))-T);assert len(chords)==37
idx={e:i+1 for i,e in enumerate(chords)}
def reduce(w,cyclic=False):
 st=[]
 for a in w:
  if st and st[-1]==-a:st.pop()
  else:st.append(a)
 if cyclic:
  while len(st)>=2 and st[0]==-st[-1]:st=st[1:-1]
 return tuple(st)
def inverse(w):return tuple(-a for a in reversed(w))
def faceword(f):
 ee=list(map(int,np.flatnonzero(d2[:,f])))
 starts={e:ends[e][0] for e in ee};lasts={e:ends[e][1] for e in ee}
 pos=min(set(starts.values())|set(lasts.values()));w=[];used=set()
 for _ in ee:
  opts=[]
  for e in ee:
   if e in used:continue
   if starts[e]==pos and d2[e,f]==1:opts.append((e,1,lasts[e]))
   if lasts[e]==pos and d2[e,f]==-1:opts.append((e,-1,starts[e]))
  assert len(opts)==1,(f,pos,opts)
  e,sg,pos=opts[0];w.append(sg*idx[e] if e in idx else 0);used.add(e)
 return reduce([a for a in w if a],True)
words={f:faceword(f) for f in range(d2.shape[1])}
assert max(map(len,words.values()))<=4
# Single relator Tietze elimination, avoid exponential growth

def try_reduce(S):
 rel={f:words[f] for f in S};active=set(idx.values());operations=[]
 for it in range(80):
  freq=collections.Counter(abs(a) for w in rel.values() for a in w)
  options=[]
  for fid,w in rel.items():
   for j,a in enumerate(w):
    if sum(abs(v)==abs(a) for v in w)!=1:continue
    cost=(len(w)-1)*max(0,freq[abs(a)]-1)
    options.append((cost,len(w),-freq[abs(a)],fid,j))
  if not options:break
  *_,fid,j=min(options)
  w=rel.pop(fid);a=w[j]; tail=w[j+1:]+w[:j]
  # relator cyclically rotated as a tail =identity -> solve a for tail
  sub=inverse(tail) if a>0 else tail
  sub=reduce(sub)
  x=abs(a)
  if a<0: # a= x^-1 ; relator x^-1 tail=1 -> x=tail
   assert sub==tail
  replacements={x:sub,-x:inverse(sub)}
  for ff,ww in list(rel.items()):
   new=[]
   for v in ww:
    if abs(v)==x:new.extend(replacements[v])
    else:new.append(v)
   rel[ff]=reduce(new,True)
  active.remove(x)
  operations.append(dict(face=int(fid),generator=int(x),sign=int(np.sign(a)),replacement=list(sub),source_length=len(w),remaining=len(active),max_rel_length=max([len(w) for w in rel.values()]+[0])))
  if max([len(w) for w in rel.values()]+[0])>100000:break
 assert len(active)>=1
 return active,rel,operations
A,rel,ops=try_reduce(R)
print('spatial tree',sp,'chords',len(chords),'retained rels',len(R),'eliminations',len(ops),'remaining active',len(A))
print('remaining rels nontrivial',[(f,word) for f,word in rel.items() if word][:20]);print('maxword',max(map(len,rel.values())))
print('active generator physical edges',[(x,chords[x-1]) for x in sorted(A)])
print('word length retained',[(f,len(words[f])) for f in sorted(R) if len(words[f])>0][:20]);print('Q',[(f,words[f]) for f in sorted(Q)])
cert=dict(Q=sorted(Q),tree_edges=sorted(T),spatial_tree_edges=sp,free_edges=chords,relators={str(f):list(w) for f,w in words.items()},retained_tietze=dict(operations=ops,remaining_generators=sorted(A),remaining_relators={str(f):list(w) for f,w in rel.items()}))
(ROOT/'presentation.json').write_text(json.dumps(cert,indent=2))
# Trace inserted face words through the same Tietze transformations
qwords={f:words[f] for f in Q}
for op in ops:
 x=op['generator'];sub=tuple(op['replacement']); replacement={x:sub,-x:inverse(sub)}
 for f,w in list(qwords.items()):
  out=[]
  for a in w:out.extend(replacement[a] if abs(a)==x else [a])
  qwords[f]=reduce(out,True)
print('Q after retained elimination',[(f,qwords[f]) for f in sorted(Q)])
cert['Q_reduced_words']={str(f):list(qwords[f]) for f in sorted(Q)}
(ROOT/'presentation.json').write_text(json.dumps(cert,indent=2))
# Build product-Haar-preserving Nielsen coordinates (35 fresh relator coordinates + 2 free).
# At each step replace the eliminated generator by fresh face coordinate and remaining active words.
all_cur={f:words[f] for f in range(d2.shape[1])}
for op in ops:
 x=op['generator']; fid=op['face']; y=37+fid+1
 tail=tuple(op['replacement']) # actual x = tail in quotient
 if op['sign']>0: expr=(y,)+tail
 else: expr=tail+(-y,)
 rep={x:expr,-x:inverse(expr)}
 for f,w in list(all_cur.items()):
  o=[]
  for t in w:o.extend(rep[t] if abs(t)==x else [t])
  all_cur[f]=reduce(o)
count_h={h:sum(any(abs(t)==h for t in w) for f,w in all_cur.items() if f in R) for h in A}
count_h_q={h:sum(any(abs(t)==h for t in w) for f,w in all_cur.items() if f in Q) for h in A}
print('retained face dependence on free holonomies (word occurrences)',count_h)
print('inserted face dependence on free holonomies (word occurrences)',count_h_q)
print('max_retained_word',max(map(len,[w for f,w in all_cur.items() if f in R])),'max_Q_word',max(map(len,[w for f,w in all_cur.items() if f in Q])))
for f in sorted(R):
 if any(abs(t)==19 for t in all_cur[f]):print('free-19 occurs in retained face',f,all_cur[f][:60])
cert['haar_nielsen_word_lengths']={str(f):len(w) for f,w in all_cur.items()}
cert['haar_nielsen_free_appearance_retained']=count_h
cert['haar_nielsen_free_appearance_inserted']=count_h_q
cert['haar_nielsen_retained_words']={str(f):list(w) for f,w in all_cur.items() if f in R}
cert['haar_nielsen_inserted_words']={str(f):list(w) for f,w in all_cur.items() if f in Q}
(ROOT/'presentation.json').write_text(json.dumps(cert,indent=2))
