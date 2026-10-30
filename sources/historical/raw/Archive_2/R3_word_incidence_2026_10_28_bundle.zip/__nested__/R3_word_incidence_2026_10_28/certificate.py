#!/usr/bin/env python3
"""Auditable Penrose prism face-word / link-star certificate.

The historical 14-face list is not mounted: an illustrative, precisely declared
14-face support is built and NEVER labelled as the historical original.
"""
from direct_cut_project import build,validate
from collections import Counter
from pathlib import Path
import json,hashlib,itertools,argparse,numpy as np
ROOT=Path(__file__).resolve().parent

def invert(w):return [[e,-s] for e,s in reversed(w)]
def reduce(w):
 out=[]
 for e,s in w:
  if out and out[-1]==[e,-s]:out.pop()
  else:out.append([e,s])
 return out

def build_spacetime(g):
 V,E,F=len(g.labels),len(g.edges),len(g.faces)
 edge_index={tuple(pair):i for i,pair in enumerate(g.edges)}
 def spatial(t,f):
  word=[]
  for a,b in zip(f,f[1:]+f[:1]):
   e=edge_index[tuple(sorted((a,b)))];word.append([t*E+e,1 if a<b else -1])
  return word
 def temporal(t,e):
  a,b=g.edges[e];s=t*E+e;sn=((t+1)%3)*E+e
  # loop a(t)->b(t)->b(t+1)->a(t+1)->a(t)
  return [[s,1],[3*E+t*V+b,1],[sn,-1],[3*E+t*V+a,-1]]
 words=[spatial(t,f) for t in range(3) for f in g.faces]+[temporal(t,e) for t in range(3) for e in range(E)]
 assert len(words)==3*(F+E)
 return words

def label_edge(g,e):
 V,E=len(g.labels),len(g.edges)
 if e<3*E:
  t,j=divmod(e,E);a,b=g.edges[j];return ['spatial',t,list(g.labels[a]),list(g.labels[b])]
 t,j=divmod(e-3*E,V);return ['temporal',t,list(g.labels[j])]

def label_face(g,f):
 F,E=len(g.faces),len(g.edges)
 if f<3*F:
  t,j=divmod(f,F);return ['spatial',t,[list(g.labels[v]) for v in g.faces[j]]]
 t,j=divmod(f-3*F,E);a,b=g.edges[j]
 return ['temporal',t,list(g.labels[a]),list(g.labels[b])]

def radius_seed(g):
 # A fully declared, reproducible example ONLY. No claim this is historical Q14.
 edge_dists=[(float(np.linalg.norm((g.xy[a]+g.xy[b])/2)),i) for i,(a,b) in enumerate(g.edges)]
 chosen=sorted(i for d,i in sorted(edge_dists)[:7])
 F,E=len(g.faces),len(g.edges)
 return sorted([3*F+i for i in chosen]+[3*F+E+i for i in chosen]), chosen

def cells(g):
 F,E=len(g.faces),len(g.edges)
 index={tuple(pair):i for i,pair in enumerate(g.edges)}
 out=[]
 for t in range(3):
  for f,vs in enumerate(g.faces):
   # closed oriented prism boundary: top - bottom +/- temporal sides
   c={((t+1)%3)*F+f:1,t*F+f:-1}
   for a,b in zip(vs,vs[1:]+vs[:1]):
    e=index[tuple(sorted((a,b)))];c[3*F+t*E+e]=1 if a<b else -1
   out.append(c)
 return out

def peel(g,Q):
 Q=set(Q);active=set(Q);c=cells(g);rec=[];dep={};
 while active:
  opts=[]
  for j,cell in enumerate(c):
   marked=active.intersection(cell)
   if len(marked)==1:
    q=next(iter(marked));opts.append((len(Q.intersection(cell)),j,q))
  if not opts:return dict(success=False,remaining=sorted(active),steps=rec)
  _,j,q=min(opts);active.remove(q)
  cnt=Counter()
  for f in c[j]:
   if f==q:continue
   cnt.update(dep.get(f,Counter({f:1})))
  assert not (Q&set(cnt))
  dep[q]=cnt
  rec.append(dict(face=q,cell=j,expanded_factors=sum(cnt.values())))
 count=Counter()
 for v in dep.values():count.update(v)
 return dict(success=True,steps=rec,fill_faces=sorted(count),max_factor=max(s['expanded_factors'] for s in rec),sum_support=len(count),max_energy_coeff=max(count.values()),multiplicity={str(k):int(v) for k,v in count.items()})

def word_stars(words,R):
 stars={}
 for f in R:
  for pos,(e,s) in enumerate(words[f]):
   word=words[f]
   # cyclic shift and reverse for negative orientation; oriented Wilson word = U_e^{s} * rest
   rest=word[pos+1:]+word[:pos]
   if s==1: staple=invert(rest) # energy 1-realtr(U_e rest)/2 -> quaternion dot with rest^{-1}
   else: staple=rest # 1-realtr(U_e^{-1} rest)/2 -> same quaternion dot with rest
   stars.setdefault(e,[]).append((f,staple))
 return stars

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--canonical-Q',default=None,help='JSON array of 14 canonical face labels, as in example_Q_labels.json')
 args=parser.parse_args()
 result={}
 g0,_=build(5,0);Q0,seed=radius_seed(g0)
 if args.canonical_Q:
  raw=json.loads(Path(args.canonical_Q).read_text())
  if isinstance(raw,dict):raw=raw['Q_canonical_labels']
  assert len(raw)==14 and len({json.dumps(v,sort_keys=True) for v in raw})==14
  key0={json.dumps(v,sort_keys=True) for v in raw}
 else:
  key0={json.dumps(label_face(g0,f),sort_keys=True) for f in Q0}
  (ROOT/'example_Q_labels.json').write_text(json.dumps([label_face(g0,f) for f in Q0],indent=2))
 for radius in [5,6.5,8,10]:
  g,gm=build(radius,0);v=validate(g,gm);words=build_spacetime(g)
  lab2id={json.dumps(label_face(g,f),sort_keys=True):f for f in range(len(words))}
  Q=sorted(lab2id[k] for k in key0)
  assert len(Q)==14
  R=set(range(len(words)))-set(Q)
  H=sorted({e for f in Q for e,s in words[f]})
  A=sorted(f for f in R if set(e for e,s in words[f])&set(H))
  peel_res=peel(g,Q)
  stars=word_stars(words,R)
  selected={str(e):[{'face':f,'staple_word':s} for f,s in stars.get(e,[])] for e in H}
  # All exact SU(2) staple pair *words* have no approximations.
  pairs={str(e):[{'faces':[f1,f2],'loop_word':reduce(w1+invert(w2))} for (f1,w1),(f2,w2) in itertools.combinations(stars.get(e,[]),2)] for e in H}
  # Pair-loop word value is equal to a_i a_j^{-1}; all identities symbolic.
  rec={'volume':radius,'geometry':v,'support_status':('user-supplied canonical 14-face support, indices verified against geometry' if args.canonical_Q else 'illustrative central-seven-edges in two temporal slabs; NOT the unavailable historical original'),
       'Q':Q,'Q_canonical_labels':[label_face(g,f) for f in Q],'H':H,'H_labels':[label_edge(g,e) for e in H],
       'H_size':len(H),'A_size':len(A),'A':A,'words_all':words,'Bianchi_peel':peel_res,
       'star_words':selected,'pair_staple_loop_words':pairs}
  output=ROOT/f'certificate_radius_{str(radius).replace(".","_")}.json';output.write_text(json.dumps(rec,separators=(',',':')))
  digest=hashlib.sha256(output.read_bytes()).hexdigest()
  result[str(radius)]={'H':len(H),'A':len(A),'Q':len(Q),'fill':peel_res.get('sum_support'),'peel_success':peel_res['success'],'max_energy_coeff':peel_res.get('max_energy_coeff'),'file':output.name,'sha256':digest}
  print(radius,result[str(radius)],flush=True)
 (ROOT/'manifest.json').write_text(json.dumps(result,indent=2))
if __name__=='__main__':main()
