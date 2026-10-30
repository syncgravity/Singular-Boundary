import sys,numpy as np,json
from pathlib import Path
src=Path(__file__).resolve().parent;sys.path.insert(0,str(src))
from adaptive_surgery import input_data
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
r=Path(__file__).resolve().parent
g,EA,SG,A,C,P,W,offs=input_data()
full,_=product_collar(g); Q=Q_from_seed(g,seed_support(g));R=sorted(set(range(len(full)))-Q)
H=sorted(set(e for f in Q for e,s in full[f]));Aorig=sorted(f for f in R if any(e in H for e,s in full[f]));Corig=sorted(f for f in R if f not in Aorig and any(e in set(P) for e,s in full[f]));total=sorted(set(Aorig)|set(Corig))
U=sorted(set(e for f in total for e,s in full[f]));P=list(map(int,P));Z=sorted(set(U)-set(P));M=np.zeros((len(total),len(U)));upos={e:i for i,e in enumerate(U)}
for j,f in enumerate(total):
 for e,s in full[f]: M[j,upos[e]]+=s
PP=M[:,[upos[e] for e in P]]; ZZ=M[:,[upos[e] for e in Z]];assert np.linalg.matrix_rank(PP)==len(P)
Acols=np.zeros((len(Aorig),len(U)));aface={f:i for i,f in enumerate(Aorig)}
for f in Aorig:
 for e,s in full[f]:Acols[aface[f],upos[e]]+=s
Ah=Acols[:,[upos[e] for e in H]];pr=np.eye(len(Aorig))-Ah@np.linalg.pinv(Ah)
S=(np.eye(len(U))-np.eye(len(U))[:,[upos[e] for e in P]]@np.linalg.pinv(PP)@M) # unsuitable formula? z basis later
out=[]
for e in Z:
 zz=np.zeros(len(Z));zz[Z.index(e)]=1
 xP=-np.linalg.lstsq(PP,ZZ@zz,rcond=None)[0]
 xx=np.zeros(len(U));xx[[upos[v] for v in P]]=xP;xx[[upos[v] for v in Z]]=zz
 resid=pr@Acols@xx
 fr=float(resid@resid/2)
 if fr>1e-10:out.append((fr,e,float(np.linalg.norm(M@xx)**2/2),float(np.linalg.norm(xP))))
print('P',len(P),'Z',len(Z),'H',len(H),'A',len(Aorig),'C',len(Corig),'rank Ah',np.linalg.matrix_rank(Ah),'nonzero frustration examples',len(out));print('top',sorted(out,reverse=True)[:8])
assert out
chosen=max(out)
json.dump({'pivot_count':len(P),'fixed_remaining_count':len(Z),'H_count':len(H),'A_count':len(Aorig),'C_count':len(Corig),'rank_P_all_faces':int(np.linalg.matrix_rank(PP)),'rank_A_H':int(np.linalg.matrix_rank(Ah)),'nonzero_relative_frustration_count':len(out),'best_one_link':chosen[1],'gaussian_sH_leading_coefficient_for_epsilon_squared':chosen[0],'gaussian_conditional_full_action_leading_coefficient_for_epsilon_squared':chosen[2], 'interpretation':'At fixed nonpivot z=epsilon e, choose the global minimized full retained Wilson action over P. No P-only action-decreasing surgery can reduce it, but the original H conditional frustration s_H is positive to order epsilon squared. Strong conditional coercivity for any P-only action-decreasing map is impossible.'},open(r/'gaussian_no_go_certificate.json','w'),indent=2)
