import json,numpy as np
from pathlib import Path
P=Path('/mnt/data/R3_nonabelian_relative_2026_10_27');R=Path(__file__).resolve().parent
j=json.loads((R/'exterior_cycle_certificate.json').read_text());p=json.loads((P/'presentation.json').read_text());z=np.load(P/'prism_incidence.npz');d1=z['d1'];d2=z['d2'];a=j['a_generator'];b=j['b_generator'];tree=set(p['tree_edges']);ch=p['free_edges'];wm={int(k):v for k,v in j['group_word_map'].items()}
def inv(w):return [-x for x in reversed(w)]
def red(w):
 s=[]
 for t in w:
  if s and s[-1]==-t:s.pop()
  else:s.append(t)
 return s
ends={e:(int(np.flatnonzero(d1[:,e]<0)[0]),int(np.flatnonzero(d1[:,e]>0)[0])) for e in range(d1.shape[1])}
ew={e:([] if e in tree else wm[ch.index(e)+1]) for e in range(d1.shape[1])}
def face(f):
 es=list(map(int,np.flatnonzero(d2[:,f])));pos=min(x for e in es for x in ends[e]);ww=[];used=set()
 for _ in es:
  o=[]
  for e in es:
   if e in used:continue
   u,v=ends[e]
   if pos==u and d2[e,f]==1:o.append((e,1,v))
   if pos==v and d2[e,f]==-1:o.append((e,-1,u))
  assert len(o)==1
  e,s,pos=o[0];used.add(e);ww.extend(ew[e] if s>0 else inv(ew[e]))
 return red(ww)
q=set(j['Q']);rfaces={f:face(f) for f in range(d2.shape[1]) if f not in q};assert all(not w for w in rfaces.values())
qwords={f:face(f) for f in sorted(q)}
print('exact inserted group words',qwords)
# The based exterior circuit corresponding to cycle edges 45 and 53 is precisely a.
cy={c['edge']:c for c in j['cycles']};relation=red(cy[45]['word']+inv(cy[53]['word']))
assert relation==[a],relation
assert all(not w or set(map(abs,w))=={a} for w in qwords.values())
print('EXTERIOR-ONLY obstruction loop = generator a, length paths',len(cy[45]['walk'])+len(cy[53]['walk']))
cert={'Q_words_exact':{str(k):v for k,v in qwords.items()},'retained_all_flat':True,'based_exterior_loop_45_times_inverse_53_word':relation,'nontrivial_for_a_minus_identity':True,'nonabelian_relative_generator':a,'exterior_cycle1':cy[45]['walk'],'exterior_cycle2':cy[53]['walk'],'conditional_frustration_proof':'Freeze exterior edges at retained flat assignment with a=-I,b=I. The based exterior-only loop has holonomy -I. All fully flat connections have a=I and hence this loop I, impossible for any change to links on inserted faces. Compactness yields strictly positive full conditional minimal action, hence conditional insertion ratio decays exponentially up to a polynomial factor in lambda.'}
(R/'nonabelian_obstruction_certificate.json').write_text(json.dumps(cert,indent=2))
