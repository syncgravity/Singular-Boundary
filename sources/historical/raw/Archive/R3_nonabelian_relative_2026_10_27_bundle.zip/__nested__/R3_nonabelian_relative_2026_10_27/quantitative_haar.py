import json, math, numpy as np
from pathlib import Path
P=Path(__file__).resolve().parent
D=json.loads((P/'presentation.json').read_text());ops=D['retained_tietze']['operations']
W={int(i):tuple(q) for i,q in D['haar_nielsen_retained_words'].items()};W.update({int(i):tuple(q) for i,q in D['haar_nielsen_inserted_words'].items()})
R=sorted(set(range(48))-set(D['Q']));F=list(range(48));ys=[38+op['face'] for op in ops];a=19;b=34

def red(w):
 z=[]
 for x in w:
  if z and z[-1]==-x:z.pop()
  else:z.append(x)
 while len(z)>=2 and z[0]==-z[-1]:z=z[1:-1]
 return z
# Exact nonnegative recurrence: theta(normal_j) <= theta(selected_face_j) + sum_{i<j} L[j,i] theta(normal_i)
def triangular_certificate(face_order,normal_order):
 n=len(face_order);L=[[0]*n for _ in range(n)]
 for j,(f,y) in enumerate(zip(face_order,normal_order)):
  early=set(normal_order[:j]); rest=red([x for x in W[f] if abs(x) not in early]);assert rest in ([y],[-y]),(j,f,rest)
  for i in range(j):L[j][i]=sum(abs(x)==normal_order[i] for x in W[f])
 # M=(I-L)^-1 explicit nonnegative integer array, computed recursively
 M=[[0]*n for _ in range(n)]
 for j in range(n):
  M[j][j]=1
  for i in range(j):
   M[j][i]=sum(L[j][k]*M[k][i] for k in range(i,j))
 one=max(sum(M[j][i] for j in range(n)) for i in range(n))
 inf=max(sum(row) for row in M)
 norm_bound_sq=one*inf
 return {'face_order':face_order,'normal_generators':normal_order,'ell_one':one,'ell_infty':inf,'spectral_norm_sq_bound':norm_bound_sq,'chordal_coercivity_constant':float(1/norm_bound_sq),'max_recurrence_coefficient':max(max(row) for row in L),'max_transport_coefficient':max(max(row) for row in M)}

def action_upper(faces,normals):
 active=set(normals)
 count=[sum(abs(x) in active for x in W[f]) for f in faces]
 # deleting all active letters must evaluate to identity as a reduced word on leftover generators
 assert all(red([x for x in W[f] if abs(x) not in active])==[] for f in faces)
 return {'sum_active_word_occurrence_squares':sum(k*k for k in count),'max_active_occurrences':max(count),'max_total_face_word_length':max(len(W[f]) for f in faces),'chordal_upper_constant':float(sum(k*k for k in count))}
CRlower=triangular_certificate([op['face'] for op in ops],ys)
CFullower=triangular_certificate([op['face'] for op in ops]+[25],ys+[a])
CRupper=action_upper(R,ys);CFulupper=action_upper(F,ys+[a])
cert={'retained_action_lower':CRlower,'retained_action_upper':CRupper,'inserted_action_lower':CFullower,'inserted_action_upper':CFulupper,'exact_sandwich':'q(C_all_upper lambda)^36 / q(c_R_lower lambda)^35 <= Z_all/Z_R <= q(c_all_lower lambda)^36 / q(C_R_upper lambda)^35','q_formula':'q(t)=2 exp(-t) I_1(t)/t; q(0)=1','derived_power':'two-sided Theta(lambda^-3/2) for this fixed 3-step 8-face cavity; constants depend on this complex','scope':'exact nonlinear SU(2) product-Haar comparison, no added Gaussian regularizer, not uniform over arbitrary prism complexes'}
(P/'quantitative_certificate.json').write_text(json.dumps(cert,indent=2))
print(json.dumps({k:{z:v for z,v in x.items() if z not in ('face_order','normal_generators')} for k,x in cert.items() if isinstance(x,dict)},indent=2))
