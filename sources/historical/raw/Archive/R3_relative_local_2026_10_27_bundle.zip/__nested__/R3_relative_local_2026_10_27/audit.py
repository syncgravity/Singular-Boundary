"""Independent exact modular rank and cross-certificate audit of the relative nonabelian collar."""
from pathlib import Path
import json,numpy as np
root=Path(__file__).resolve().parent
D=np.load('/mnt/data/R3_nonabelian_relative_2026_10_27/prism_incidence.npz')['d2'];r=json.loads((root/'collar_certificate.json').read_text());n=json.loads((root/'nonabelian_obstruction_certificate.json').read_text());g=json.loads((root/'flat_gluing_certificate.json').read_text());c=json.loads((root/'exterior_cycle_certificate.json').read_text())
Q=r['Q'];R=[f for f in range(D.shape[1]) if f not in Q]
def rank_mod(A,p=1000003):
 a=A.astype(np.int64)%p;t=0
 for j in range(a.shape[1]):
  if t>=a.shape[0]:break
  nz=np.flatnonzero(a[t:,j]);
  if not len(nz):continue
  k=t+int(nz[0]);a[[t,k]]=a[[k,t]];a[t]=(a[t]*pow(int(a[t,j]),-1,p))%p
  for i in range(t+1,a.shape[0]):
   if a[i,j]:a[i]=(a[i]-a[i,j]*a[t])%p
  t+=1
 return t
res={}
for tag,LL in [('original',r['initial_local_edges']),('collar45',g['new_local_edges'])]:
 rank0=rank_mod(D[np.ix_(LL,R)]);rank1=rank_mod(D[LL,:]);gr0=rank_mod(D[:,R]);gr1=rank_mod(D)
 res[tag]={'local_count':len(LL),'retained_local_rank':rank0,'full_local_rank':rank1,'exterior_retained_rank':gr0-rank0,'exterior_full_rank':gr1-rank1}
assert res['original']=={'local_count':26,'retained_local_rank':25,'full_local_rank':25,'exterior_retained_rank':10,'exterior_full_rank':11}
assert res['collar45']=={'local_count':27,'retained_local_rank':25,'full_local_rank':26,'exterior_retained_rank':10,'exterior_full_rank':10}
assert n['based_exterior_loop_45_times_inverse_53_word']==[c['a_generator']]
assert g['exterior_edge_constraints_exact'] and g['full_flat_face_relations_exact']
assert g['modified_local_edges']==[45,46,47,48,51]
cert={'status':'PASS','modular_ranks_prime':1000003,'relative_ranks':res,'nonabelian_exterior_cycle_word':'a','exterior_loop_lengths':[len(n['exterior_cycle1']),len(n['exterior_cycle2'])],'one_edge_collar_preserves_nonabelian_flat_exterior':True,'modified_edges_in_flat_gluing':g['modified_local_edges'],'max_gauge_word_length':g['max_symbolic_gauge_word_length'],'theorem_scope':'flat-stratum relative gluing on fixed combinatorial prism; no off-flat Gibbs-measure or arbitrary Penrose theorem'}
(root/'summary_certificate.json').write_text(json.dumps(cert,indent=2))
print(json.dumps(cert,indent=2))
