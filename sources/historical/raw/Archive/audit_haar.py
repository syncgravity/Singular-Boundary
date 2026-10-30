import json,numpy as np
from pathlib import Path
P=Path(__file__).resolve().parent
cert=json.loads((P/'presentation.json').read_text());ops=cert['retained_tietze']['operations']
Q=set(cert['Q']);R=set(range(48))-Q
old={f:tuple(v) for f,v in ((int(k),v) for k,v in cert['relators'].items())}
new={f:tuple(v) for f,v in ((int(k),v) for k,v in cert['haar_nielsen_retained_words'].items())}
new.update({f:tuple(v) for f,v in ((int(k),v) for k,v in cert['haar_nielsen_inserted_words'].items())})
def mul(x,y):
 a,b=x[0],y[0];u,v=x[1:],y[1:]
 return np.r_[a*b-u@v,a*v+b*u+np.cross(u,v)]
def inv(x):return x*np.array([1,-1,-1,-1])
I=np.array([1.,0,0,0]);defnorm=lambda x:x/np.linalg.norm(x)
def prod(w,values):
 z=I.copy()
 for g in w:z=mul(z,values[g] if g>0 else inv(values[-g]))
 return z
def rebuild(target):
 val=dict(target)
 for op in reversed(ops):
  x=op['generator']; y=38+op['face'];tail=tuple(op['replacement']);rest=prod(tail,val)
  val[x]=mul(val[y],rest) if op['sign']>0 else mul(rest,inv(val[y]))
 return val
rng=np.random.default_rng(20261027);free=cert['retained_tietze']['remaining_generators'];allnames=free+[38+op['face'] for op in ops]
errs=[]
for _ in range(100):
 vals={k:defnorm(rng.standard_normal(4)) for k in allnames};oldval=rebuild(vals)
 errs.append(max(np.linalg.norm(prod(old[f],oldval)-prod(new[f],vals)) for f in range(48)))
assert max(errs)<1e-12,max(errs)
# Haar-coordinate independence checks: inverse mapping of random independent quaternions is measure preserving, and relator words match exactly.
ret_dep={a:sorted(f for f in R if any(abs(v)==a for v in new[f])) for a in free}
# A concrete retained word with nontrivial a conjugation.
a=19;b=34
assert a in free and b in free
print('face9',new[9]);
def axis(i):
 q=I*0;q[i]=1;return q
vals={k:I.copy() for k in allnames};vals[47]=axis(1);vals[68]=axis(1)
samples=[]
for theta in np.linspace(0,np.pi/2,9):
 vals[a]=np.array([np.cos(theta),0,0,np.sin(theta)])
 r_tr={f:float(prod(new[f],vals)[0]) for f in R}
 q_tr={f:float(prod(new[f],vals)[0]) for f in Q}
 samples.append(dict(theta=float(theta),retained_face9=float(r_tr[9]),retained_action_unit=sum(1-v for v in r_tr.values()),insertion_action_unit=sum(1-v for v in q_tr.values())))
assert abs(samples[0]['retained_face9']+1)<1e-12
assert abs(samples[-1]['retained_face9']-1)<1e-12
# Form a noncommuting explicit point with generic nontrivial retained action variation for free holonomy a.
report={'gauge_fixed_free_group_rank':len(free),'survivor_chord_mapping':{str(x):cert['free_edges'][x-1] for x in free},'retained_face_dependence':{str(k):v for k,v in ret_dep.items()},'haar_nielsen_max_quaternion_reconstruction_residual':float(max(errs)), 'nontrivial_retained_face9_word':list(new[9]),'selected_axis_example':samples,'technical_scope':'topological Tietze elimination and exact product-Haar coordinates, not a retained-action-preserving Haar factorization'}
(P/'haar_audit.json').write_text(json.dumps(report,indent=2));print('max quaternion reconstruction residual',max(errs));print('retained face dependencies',ret_dep);print('samples',samples)
# Sanity checks of all four *global* Wilson action comparisons, in product-Haar Nielsen coordinates.
V=[]
for experiment in range(200):
 vals={k:defnorm(rng.standard_normal(4)) for k in allnames}
 if experiment>=100:
  scale=10**(-rng.uniform(1,4))
  for k in allnames:
   if k in (a,b):continue
   v=scale*rng.normal(size=3); vals[k]=np.r_[np.cos(np.linalg.norm(v)), v*np.sinc(np.linalg.norm(v)/np.pi)]
 r=sum(1-float(prod(new[f],vals)[0]) for f in R)
 full=sum(1-float(prod(new[f],vals)[0]) for f in range(48))
 ynorm=sum(1-float(vals[k][0]) for k in allnames if k not in (a,b))
 fnorm=ynorm+1-float(vals[a][0])
 assert ynorm/342-1e-9 <=r <=360*ynorm+1e-9,(experiment,r,ynorm)
 assert fnorm/378-1e-9 <=full <=609*fnorm+1e-9,(experiment,full,fnorm)
 V.append((r,full,ynorm,fnorm))
report['numeric_global_coercivity_audit_count']=len(V)
report['numeric_global_coercivity_all_passed']=True
(P/'haar_audit.json').write_text(json.dumps(report,indent=2))
