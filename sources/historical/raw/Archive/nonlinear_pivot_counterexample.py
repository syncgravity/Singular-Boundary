#!/usr/bin/env python3
"""Nonlinear SU2 audit: optimized original pivot links may leave s_H>0.
This is a *numerical* realization; an exact rational tangent witness and
implicit-function argument supply the nearby analytic no-go.
"""
from pathlib import Path
import sys,json
import numpy as np
from scipy.optimize import minimize
from numba import njit
SRC=Path(__file__).resolve().parent;sys.path.insert(0,str(SRC))
from adaptive_surgery import input_data,surgery
from no_go_gaussian import full,Q,R,H,Aorig,Corig,total,U,P,Z,M,PP,ZZ,Acols,Ah,upos
ROOT=Path(__file__).resolve().parent
@njit
def qm(a,b):
 r=np.empty(4);r[0]=a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
 r[1]=a[0]*b[1]+b[0]*a[1]+a[2]*b[3]-a[3]*b[2]
 r[2]=a[0]*b[2]+b[0]*a[3]+a[1]*b[2]-a[3]*b[1]
 r[3]=a[0]*b[3]+b[0]*a[2]+a[3]*b[1]-a[1]*b[2]
 return r
@njit
def dag(a):
 r=a.copy();r[1:]*=-1;return r
@njit
def vg(U, E, S, active, variable):
 val=0.;gr=np.zeros_like(U)
 for f in range(len(E)):
  if not active[f]:continue
  pre=np.zeros((5,4));post=np.zeros((5,4));pre[0,0]=1.;post[4,0]=1.
  for i in range(4):
   edge=E[f,i];v=U[edge] if S[f,i]>0 else dag(U[edge]);pre[i+1]=qm(pre[i],v)
  for i in range(3,-1,-1):
   edge=E[f,i];v=U[edge] if S[f,i]>0 else dag(U[edge]);post[i]=qm(v,post[i+1])
  val+=1.-pre[4,0]
  for i in range(4):
   edge=E[f,i]
   if not variable[edge]:continue
   for k in range(4):
    v=np.zeros(4);v[k]=1 if k==0 or S[f,i]>0 else -1
    gr[edge,k]-=qm(qm(pre[i],v),post[i+1])[0]
 return val,gr

def optimize(U,E,S,active,links,maxiter=1500):
 ll=np.array(links,dtype=int);mask=np.zeros(len(U),dtype=np.bool_);mask[ll]=True
 def fg(z):
  V=U.copy();raw=z.reshape((-1,4));norm=np.linalg.norm(raw,axis=1);v=raw/norm[:,None];V[ll]=v
  score,gradient=vg(V,E,S,active,mask);grad=gradient[ll]
  grad=(grad-(grad*v).sum(axis=1)[:,None]*v)/norm[:,None]
  return score,grad.ravel().astype(float)
 res=minimize(fg,U[ll].ravel(),method='L-BFGS-B',jac=True,options={'maxiter':maxiter,'gtol':1e-12,'ftol':1e-15,'maxls':50})
 V=U.copy();zz=res.x.reshape((-1,4));V[ll]=zz/np.linalg.norm(zz,axis=1)[:,None]
 score,grad=vg(V,E,S,active,mask)
 rad=np.linalg.norm((grad[ll]-(grad[ll]*V[ll]).sum(axis=1)[:,None]*V[ll]),axis=1)
 return V,score,float(np.max(rad)),int(res.nit),bool(res.success)

def main():
 data=input_data();g,EA,SG,A,C,solved,ww,offs=data
 n=3*(len(g.labels)+len(g.edges));fullactive=np.zeros(len(EA),dtype=np.bool_);fullactive[A]=True;fullactive[C]=True
 aa=np.zeros(len(EA),dtype=np.bool_);aa[A]=True
 rows=[]
 for eps in [0.04,0.08,0.16]:
  config=np.zeros((n,4));config[:,0]=1.
  config[438,:]=[np.cos(eps),np.sin(eps),0,0]
  zz=np.zeros(len(Z));zz[Z.index(438)]=1
  xP=-np.linalg.lstsq(PP,ZZ@zz,rcond=None)[0]
  for e,x in zip(P,xP):config[e,:]=[np.cos(eps*x),np.sin(eps*x),0.,0.]
  fixed,_score,gradp,nit,success=optimize(config,EA,SG,fullactive,solved)
  hopt,sH,gradh,nitH,goodH=optimize(fixed,EA,SG,aa,H)
  tau,new,drop,_=surgery(fixed,data)
  rows.append({'epsilon':eps,'full_P_min_score':float(_score),'full_P_max_tangent_gradient':gradp,'optimizer_iterations_P':nit,'P_solver_success':success,'original_H_conditional_min':float(sH),'H_optimizer_gradient':gradh,'H_solver_iterations':nitH,'H_solver_success':goodH,'selected_adaptive_tau':tau,'adaptive_full_action_drop':float(drop),'sH_over_epsilon_squared':float(sH/eps**2),'local_full_action_over_epsilon_squared':float(_score/eps**2)})
  print(rows[-1],flush=True)
 ROOT.joinpath('nonlinear_no_go_probe.json').write_text(json.dumps({'scope':'numerical audit of exact rational tangent no-go. near-flat smooth implicit function theorem is analytic argument; numerical optimizer alone is not global minimum certificate','results':rows},indent=2))
if __name__=='__main__':main()
