"""A bounded-degree one-vertex, many-loop 2-complex showing why |Q|-sparse local repair does not follow from incidence bounds alone. This is NOT a prism complex."""
import numpy as np,json
from pathlib import Path
out={}
for n in [4,8,16,32]:
 # one-vertex loops x_i; retained words x_i x_(i+1)^-1; added word x0.
 D=np.zeros((n,n),dtype=int)
 for i in range(n-1):D[i,i]=1;D[i+1,i]=-1
 D[0,n-1]=1
 rank_R=n-1;rank_all=n
 rows=[]
 for m in [1,2,n//2,n-1,n]:
  if m<1 or m>n:continue
  local=np.arange(m)
  rr=np.linalg.matrix_rank(D[local,:n-1]); ra=np.linalg.matrix_rank(D[local,:]);h=ra-rr
  rows.append(dict(local_edges=m,local_rank_retained=int(rr),local_rank_full=int(ra),new_exterior_rank=1-int(h)))
 assert all(r['new_exterior_rank']==1 for r in rows if r['local_edges']<n)
 assert rows[-1]['new_exterior_rank']==0
 out[str(n)]=dict(vertices=1,edge_loops=n,retained_two_edge_faces=n-1,inserted_one_edge_faces=1,max_edge_incidence=2,max_face_length=2,computed=rows,group_presentation='retained: <x0,...,xN-1 | x_i x_(i+1)^-1> = Z; inserting x0 kills the generator')
(Path(__file__).parent/'chain_obstruction_certificate.json').write_text(json.dumps(out,indent=2))
print('verified bounded-incidence chain family, size 4,8,16,32; requires every link in repair collar to eliminate exterior-rank obstruction')
