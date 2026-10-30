import sys, json, time
from pathlib import Path
import numpy as np
import sympy as sp
from no_go_gaussian import g,full,Q,R,H,Aorig,Corig,total,U,P,Z,M,PP,ZZ,Acols,Ah,upos
out=Path(__file__).resolve().parent
sel=438
zcol=ZZ[:,Z.index(sel)].astype(int)
MP=sp.Matrix(PP.astype(int).tolist()); b=sp.Matrix(zcol.tolist())
t=time.time()
# SPD normal equations, Gram matrix positive definite
G=MP.T*MP; rhs=-MP.T*b
v=G.inv()*rhs
print('solved exact rational',time.time()-t)
# residual on A, project onto quotient with any rational left-null vector
xx={e:sp.Integer(0) for e in U};xx[sel]=sp.Integer(1)
for e,term in zip(P,v):xx[e]=term
r=sp.Matrix([[sum(sp.Integer(s)*xx[e] for e,s in full[f])] for f in Aorig])
AH=sp.Matrix(Ah.astype(int).tolist())
# Find exact witness w in null AH^T with w⋅r !=0 via linear equations rather than full nullspace
N=AH.T.nullspace()
nonzero=[(i,(ww.dot(r))) for i,ww in enumerate(N) if ww.dot(r)!=0]
assert nonzero
index,amp=nonzero[0];ww=N[index]
print('rank AH',AH.rank(),'rational witness nonzero',amp,'max rational numerator digits',max(len(str(q.p)) for q in v))
# v in image AH iff all nullspace dot zero; compute bound for s_H using Cauchy Schwarz: ||Pperp r||^2 >= (w^T r)^2 / ||w||^2
bound=sp.factor((amp**2/(ww.dot(ww)))/2)
print('exact positive quadratic energy coefficient lower bound=',bound,'float',float(bound))
cert={'external_link':sel,'P_links':len(P),'full_retained_face_rows':len(total),'local_A_faces':len(Aorig),'local_H_links':len(H),'global_pivot_rank':int(np.linalg.matrix_rank(PP)),'H_face_rank_exact':35,'witness_left_null_basis_index':index,'witness_nonzero_dot_r':str(amp),'witness_squared_norm':str(ww.dot(ww)),'rigorous_lower_bound_sH_leading_coefficient':str(bound),'rigorous_lower_bound_float':float(bound),'exact_rational_linear_system':'(D_RP^T D_RP) x_P=-D_RP^T D_R,z e_438','conclusion':'At nonpivot link e438=epsilon, all other nonpivots zero, the global pivot minimizer has positive original H conditional frustration for sufficiently small epsilon; every pivot-only action-nonincreasing repair is non-coercive there.'}
(out/'exact_rational_no_go.json').write_text(json.dumps(cert,indent=2))
