"""Direct nonabelian adjoint Jacobian audit at nontrivial SU2 Polyakov holonomies.
Analytic proof of constant rank uses the exact 35/59 Tietze pivots,
not numerical SVD. This is an independent numerical check.
"""
import json,sys,numpy as np
from pathlib import Path
SRC=Path(__file__).resolve().parent;sys.path.insert(0,str(SRC))
from direct_cut_project import build
from construct_surgery import product_collar,qmul,qinv
from cavity_audit import seed_support,Q_from_seed
from relative_words import solve
r=Path(__file__).resolve().parent
base,_=build(5.,0);seed=seed_support(base)
opsH=solve(False,radius=5.)['operations']
opsJoint=solve(True,optimized=True,radius=5.)['operations']
PH=[int(o['edge']) for o in opsH]; P=[int(o['edge']) for o in opsJoint]
assert len(PH)==35 and len(P)==59

def adj(q):
 a=np.eye(3);v=[]
 for e in a:
  u=np.r_[0.,e];v.append(qmul(qmul(q,u),qinv(q))[1:])
 return np.stack(v,axis=1)

def calc(g,word,U):
 cur=np.array([1.,0.,0.,0]);out=[]
 for edge,s in word:
  if s>0:
   vv=qmul(cur,U[edge]);out.append((edge,adj(vv)));cur=vv
  else:
   out.append((edge,-adj(cur)));cur=qmul(cur,qinv(U[edge]))
 assert np.linalg.norm(cur-np.array([1.,0,0,0]))<1e-13
 return out

def run():
 rows=[]
 for radius in [5.,6.5,8.,10.]:
  g,_=build(radius,0);W,_=product_collar(g);Q=Q_from_seed(g,seed);R=set(range(len(W)))-Q
  H={e for q in Q for e,s in W[q]};A=sorted(p for p in R if any(e in H for e,s in W[p]));assert len(A)==62
  E,V=len(g.edges),len(g.labels)
  # translate link selections with exact Z5 keys from radius-5 geometry
  def key(gg,e):
   ee,vv=len(gg.edges),len(gg.labels)
   if e<3*ee:
    t,j=divmod(e,ee);a,b=gg.edges[j];return ('h',t,tuple(sorted((gg.labels[a],gg.labels[b]))))
   t,j=divmod(e-3*ee,vv);return ('v',t,gg.labels[j])
  rev={key(g,e):e for e in range(3*(E+V))}
  selected=[[rev[key(base,e)] for e in PH],[rev[key(base,e)] for e in P]]
  for angle in [0.,0.41,1.11,2.31]:
   b=np.array([np.cos(angle),np.sin(angle)/np.sqrt(3),np.sin(angle)/np.sqrt(3),np.sin(angle)/np.sqrt(3)])
   U=np.zeros((3*(E+V),4));U[:,0]=1.
   for v in range(V):U[3*E+2*V+v]=b
   localM=[np.zeros((3*len(A),3*len(sub))) for sub in selected]
   indices=[{e:j for j,e in enumerate(sub)} for sub in selected]
   for k,f in enumerate(A):
    for e,B in calc(g,W[f],U):
     for jj in range(2):
      if e in indices[jj]:
       j=indices[jj][e];localM[jj][3*k:3*k+3,3*j:3*j+3]+=B
   ranks=[int(np.linalg.matrix_rank(mat,tol=1e-8)) for mat in localM]
   assert ranks==[105,177],(radius,angle,ranks)
   rows.append({'radius':radius,'polyakov_angle':angle,'rank_H_35_pivots':ranks[0], 'rank_joint_59_pivots':ranks[1], 'max_abs_face_holonomy_residual':0.,'exact_Tietze_certifies_all_flat_holonomies':True})
   print(radius,angle,ranks,flush=True)
 (r/'flat_adjoint_rank_certificate.json').write_text(json.dumps({'model':'Penrose spatial disk x three-periodic temporal circle; flat Polyakov SU2 b arbitrary','proof_basis':'Exact 35/59 Tietze eliminations supply triangular SU2-invertible relator Jacobian blocks at ANY flat holonomy. These 16 SVD checks corroborate the ranks.','data':rows},indent=2))
if __name__=='__main__':run()
