import numpy as np,json
from pathlib import Path
p=Path('/mnt/data/R3_nonabelian_relative_2026_10_27')
z=np.load(p/'prism_incidence.npz');D=z['d2'];Q=[13,18,22,25,26,29,32,37];R=[f for f in range(D.shape[1]) if f not in Q]
L=set(np.flatnonzero(np.any(D[:,Q]!=0,axis=1))); E=set(range(D.shape[0]))-L
rR=np.linalg.matrix_rank(D[:,R]);rF=np.linalg.matrix_rank(D)

def rankv(LL):
 B=np.array(sorted(LL));return [int(np.linalg.matrix_rank(D[B][:,fs])) for fs in [R,list(range(D.shape[1]))]]
base=rankv(L)
print('base local rank',base,'effective exterior ranks',[rR-base[0],rF-base[1]])
add=[]
for e in sorted(E):
 ra,rb=rankv(L|{e});d=(rF-rb)-(rR-ra)
 add.append(dict(edge=int(e),local_rank_retained=ra,local_rank_full=rb,exterior_rank_growth=d,retained_rank_increment=ra-base[0],full_rank_increment=rb-base[1]))
print('single edges preserving',[(x['edge'],x['retained_rank_increment'],x['full_rank_increment']) for x in add if x['exterior_rank_growth']==0]);print('45',add[sorted(E).index(45)],'53',add[sorted(E).index(53)])
# Full support is small; deterministic greedy add an edge reducing rank-growth.
LL=set(L); steps=[]
for i in range(10):
 cur=rankv(LL);g=(rF-cur[1])-(rR-cur[0]);
 if g==0:break
 cand=[]
 for e in E-LL:
  r1,r2=rankv(LL|{e});new=(rF-r2)-(rR-r1);cand.append((new,e,r1,r2))
 candidate=min(cand)
 if candidate[0]>=g:break
 new,e,r1,r2=candidate;LL.add(e);steps.append(dict(edge=e,exterior_rank_growth=new,retained_rank=r1,full_rank=r2))
print('greedy steps',steps)
cert={'Q':Q,'initial_local_edges':sorted(L),'initial_local_rank':base,'exterior_ranks_initial':[int(rR-base[0]),int(rF-base[1])],'candidate_extra_edges':add,'greedy_collar':steps,'resulting_local_edges':sorted(LL)}
(Path(__file__).parent/'collar_certificate.json').write_text(json.dumps(cert,indent=2,default=lambda x: int(x) if isinstance(x,np.integer) else x))
