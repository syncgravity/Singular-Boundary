import json,numpy as np
from pathlib import Path
P=Path(__file__).resolve().parent;d=json.loads((P/'presentation.json').read_text())
ops=d['retained_tietze']['operations'];y_names=sorted(38+x['face'] for x in ops)
a=19;b=34
R=sorted(set(range(48))-set(d['Q']))
ws={int(f):tuple(u) for f,u in d['haar_nielsen_retained_words'].items()}
ws.update({int(f):tuple(u) for f,u in d['haar_nielsen_inserted_words'].items()})
I=np.array([1.,0,0,0])
def mul(x,y):
 p=x[0];q=y[0];u=x[1:];v=y[1:]
 return np.r_[p*q-u@v,p*v+q*u+np.cross(u,v)]
def inv(x):return x*np.array([1.,-1.,-1.,-1.])
def Ad(q):
 z=q[0];v=q[1:];s=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
 return (z*z-v@v)*np.eye(3)+2*np.outer(v,v)+2*z*s

def J(faces,qs,names):
 loc={j:i for i,j in enumerate(names)};out=np.zeros((3*len(faces),3*len(names)))
 for k,f in enumerate(faces):
  q=I.copy()
  for x in ws[f]:
   l=abs(x)
   if l in loc:out[3*k:3*k+3,3*loc[l]:3*loc[l]+3]+=np.sign(x)*Ad(q)
   q=mul(q,qs[l] if x>0 else inv(qs[l]))
  assert np.max(abs(q-I))<1e-10
 return out

def amplitude(F,qs,names):
 M=J(F,qs,names)
 _,rr=np.linalg.qr(M,mode='reduced')
 return float(np.exp(-np.log(np.abs(np.diag(rr))).sum()))
rng=np.random.default_rng(20261027)
N=256; amp0=[];amp1=[]; allnames=y_names+[a]
for i in range(N):
 qa=rng.standard_normal(4);qa/=np.linalg.norm(qa)
 qb=rng.standard_normal(4);qb/=np.linalg.norm(qb)
 vals={j:I.copy() for j in y_names};vals[a]=qa;vals[b]=qb
 amp0.append(amplitude(R,vals,y_names))
 vals[a]=I
 amp1.append(amplitude(list(range(48)),vals,allnames))
amp0=np.array(amp0);amp1=np.array(amp1)
# correlated draws not necessary; uncertainty descriptive MC only
c=np.sqrt(2/np.pi)*amp1.mean()/amp0.mean()
report={'n_haar_moduli_samples':N,'denominator_mean_normal_Hessian_inverse_sqrt':float(amp0.mean()),'numerator_mean_normal_Hessian_inverse_sqrt':float(amp1.mean()),'predicted_limit_lambda_to_infinity_of_lambda_3over2_times_Zall_over_ZR':float(c),'denominator_amp_range':[float(amp0.min()),float(amp0.max())],'numerator_amp_range':[float(amp1.min()),float(amp1.max())],'status':'Numerical integral of analytically defined clean-Laplace prefactors. Exponent 3/2 rigorous for fixed complex; coefficient MC estimate not rigorous.'}
(P/'laplace_prefactor_certificate.json').write_text(json.dumps(report,indent=2))
np.savez_compressed(P/'laplace_prefactor_samples.npz',amp_retained=amp0,amp_inserted=amp1)
print(json.dumps(report,indent=2))
