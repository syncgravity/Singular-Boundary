import numpy as np,json
from pathlib import Path
P=Path(__file__).resolve().parent;d=json.loads((P/'presentation.json').read_text())
ops=d['retained_tietze']['operations'];selected=[int(x['face']) for x in ops]
R=sorted(set(range(48))-set(d['Q']))
w={int(f):tuple(arr) for f,arr in d['haar_nielsen_retained_words'].items()}
w.update({int(f):tuple(arr) for f,arr in d['haar_nielsen_inserted_words'].items()})
y_names=sorted(38+x for x in selected)
a=19;b=34
assert len(y_names)==35 and len(set(y_names))==35
I=np.array([1.,0,0,0])
def mul(x,y):
 p=x[0];q=y[0];u=x[1:];v=y[1:]
 return np.r_[p*q-u@v,p*v+q*u+np.cross(u,v)]
def inv(x):return x*np.r_[1.,[-1.]*3]
def Ad(q):
 z=q[0];v=q[1:]
 skew=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
 return (z*z-v@v)*np.eye(3)+2*np.outer(v,v)+2*z*skew
def jacobian(faces,qs,names):
 pos={j:i for i,j in enumerate(names)}
 out=np.zeros((3*len(faces),3*len(names)))
 for k,f in enumerate(faces):
  prefix=I.copy()
  for t in w[f]:
   jj=abs(t); s=1 if t>0 else -1
   if jj in pos:out[3*k:3*k+3,3*pos[jj]:3*pos[jj]+3]+=s*Ad(prefix)
   v=qs[jj] if t>0 else inv(qs[jj]);prefix=mul(prefix,v)
  if np.linalg.norm(prefix-I)>1e-10:
   raise ValueError((f,prefix))
 return out
rng=np.random.default_rng(26027)
report=[]
for mode in ['identity','central','random_1','random_2','random_3','random_4','random_5']:
 qa=I.copy();qb=I.copy()
 if mode=='central': qa=-I;qb=-I
 if mode.startswith('random'):
  qa=rng.standard_normal(4);qa/=np.linalg.norm(qa)
  qb=rng.standard_normal(4);qb/=np.linalg.norm(qb)
 vals={j:I.copy() for j in y_names};vals[a]=qa;vals[b]=qb
 JR=jacobian(selected,vals,y_names)
 sign,ldet=np.linalg.slogdet(JR)
 smin=np.linalg.svd(JR,compute_uv=False)[-1]
 assert abs(ldet)<2e-9 and smin>1e-5,(mode,ldet,smin)
 # check all retained relators have derivative rank 105
 Jall=jacobian(R,vals,y_names)
 smin_all=np.linalg.svd(Jall,compute_uv=False)[-1]
 assert smin_all>1e-5
 # inserted full, a at I; b arbitrary
 vals[a]=I.copy()
 Jfull=jacobian(selected+[25],vals,y_names+[a])
 signF,ldF=np.linalg.slogdet(Jfull)
 sfull=np.linalg.svd(Jfull,compute_uv=False)[-1]
 assert abs(ldF)<2e-9 and sfull>1e-5
 report.append({'mode':mode,'selected_R_jacobian_log_abs_det':float(ldet),'selected_R_min_singular':float(smin),'all_R_min_singular':float(smin_all),'selected_full_log_abs_det':float(ldF),'selected_full_min_singular':float(sfull)})
print(json.dumps(report,indent=2))
(P/'clean_flat_certificate.json').write_text(json.dumps({'selected_retained_face_ids':selected,'normal_variables':y_names,'unconstrained_retained_holonomies':[a,b],'full_remaining_holonomy':b,'checks':report,'interpretation':'clean-flat and unit-Jacobian results near flat manifolds; uniform compactness follows because all flat moduli SU(2)^2 or SU(2) are compact. Not arbitrary ambient-uniform R3.'},indent=2))
