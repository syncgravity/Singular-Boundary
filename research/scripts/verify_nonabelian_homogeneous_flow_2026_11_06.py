#!/usr/bin/env python3
"""Periodic cubic SU(2) noncommuting homogeneous spatial Wilson flow.
Independent exact quaternion force/geometry check against a scalar ODE.
No interacting-vacuum uniformity or Yang--Mills quantum gap asserted.
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

# Independent existing original-link quaternion evaluator, source PR #72.
SRC = Path(__file__).resolve().parent / "verify_nonlinear_energy_flow.py"
if not SRC.exists():
    SRC = Path('/mnt/data/sb_nonlinear_energy_2026_11_06/research/scripts/verify_nonlinear_energy_flow.py')
import importlib.util
spec=importlib.util.spec_from_file_location('original_su2',SRC)
orig=importlib.util.module_from_spec(spec);spec.loader.exec_module(orig)


def periodic(n):
    assert n>=2
    verts=[(i,j,k) for i in range(n) for j in range(n) for k in range(n)]
    edges=[(v,d) for v in verts for d in range(3)]
    idx={key:i for i,key in enumerate(edges)}
    def shift(x,d):
        xx=list(x);xx[d]=(xx[d]+1)%n;return tuple(xx)
    faces=[]
    for x in verts:
        for a,b in [(0,1),(0,2),(1,2)]:
            faces.append([(idx[x,a],1),(idx[shift(x,a),b],1),
                          (idx[shift(x,b),a],-1),(idx[x,b],-1)])
    ids=np.array([[e for e,s in f] for f in faces],int)
    signs=np.array([[s for e,s in f] for f in faces],int)
    deg=np.bincount(ids.ravel(),minlength=len(edges))
    assert len(faces)==3*n**3 and len(edges)==3*n**3
    assert np.all(deg==4)
    assert all(len(set(row))==4 for row in ids)
    return dict(n=n,h=1/n,verts=verts,edges=edges,ids=ids,signs=signs,degree=deg)


def homogeneous(geom,theta):
    links=np.tile([1.,0,0,0],(len(geom['edges']),1))
    qx=orig.qexp(np.array([theta,0,0.])); qy=orig.qexp(np.array([0.,theta,0]))
    for i,(_,d) in enumerate(geom['edges']):
        links[i]=qx if d==0 else (qy if d==1 else [1,0,0,0])
    return links


def grad_check(n,theta):
    geom=periodic(n);q=homogeneous(geom,theta)
    S,grad,defects=orig.action_gradient(q,geom)
    u=math.sin(theta/2);v=math.cos(theta/2)
    targetS=2*n**3*u**4
    targetg=2*u**3*v
    target=np.array([[targetg if d==0 else 0.,targetg if d==1 else 0.,0.] for _,d in geom['edges']])
    # Truly non-Abelian: plaquette C=Ux Uy Ux^-1 Uy^-1 !=I
    qx=orig.qexp([theta,0.,0.]);qy=orig.qexp([0.,theta,0.])
    comm=orig.qmul(orig.qmul(orig.qmul(qx,qy),orig.qinv(qx)),orig.qinv(qy))
    expectedreal=1-2*u**4
    return dict(n=n,theta=theta,links=len(q),faces=len(defects),
       action_error=abs(S-targetS),gradient_max_error=float(np.abs(grad-target).max()),
       commutator_real_error=abs(comm[0]-expectedreal),commutator_nontrivial=bool(np.linalg.norm(comm[1:])>1.e-8),
       transverse_max_defect=float(np.max(defects[[i for i in range(len(defects)) if i%3!=0]])))


def scalar(theta0,n,tau):
    h=1/n
    def rhs(t,y):
        th=y[0];return [-2/h**2*math.sin(th/2)**3*math.cos(th/2)]
    ans=solve_ivp(rhs,[0,tau],[theta0],rtol=1.e-12,atol=1.e-13,method='DOP853')
    assert ans.success
    th=float(ans.y[0,-1]); z=math.sin(th/2)**2
    initial_a=theta0/h
    continuum_a=initial_a/math.sqrt(1+initial_a**2*tau/2)
    physical_F=4*math.asin(z)/h**2
    return dict(n=n,h=h,physical_tau=tau,initial_a=initial_a,final_theta=th,
                final_a=th/h,continuum_a=continuum_a,continuum_a_error=abs(th/h-continuum_a),
                rigorous_a_error=tau*h*h*abs(initial_a)**5/16,
                curvature=physical_F,universal_bound=2*math.pi/tau,
                curvature_bound_ratio=physical_F/(2*math.pi/tau),
                continuum_F=continuum_a**2)


def perturbation(n,theta,delta,tau):
    geom=periodic(n);base=homogeneous(geom,theta);other=base.copy()
    # perturb a single z-link in an independent Lie direction (breaks homogeneous symmetry)
    other[0]=orig.qmul(orig.qexp(np.array([0.,0.,delta])),other[0]);
    dist=delta;h=1/n;end=tau/h**2
    def phi(y0):
      r=solve_ivp(lambda s,y: orig.ode_rhs(s,y,geom),[0,end],y0.ravel(),
        method='DOP853',rtol=1.e-10,atol=1.e-12,max_step=min(0.08,end/5))
      assert r.success
      return orig.unit(r.y[:,-1].reshape(-1,4))
    a=phi(base);b=phi(other)
    # angular distance in metric T=i sigma/2: d=2 arccos |quaternion real relative|
    rel=orig.qmul(orig.qinv(a),b);ang=2*np.arctan2(np.linalg.norm(rel[:,1:],axis=1),rel[:,0]);
    df=float(np.linalg.norm(ang))
    lip=math.exp(4*end)*dist
    _,_,pa=orig.action_gradient(a,geom)
    _,_,pb=orig.action_gradient(b,geom)
    # angular plaquette curvature: phi=2 acos Re(C), S_face=1-Re(C)
    # robust arccos near 1; difference physically compared to the predicted Lipschitz bound.
    phi_a=2*np.arcsin(np.sqrt(np.clip(pa/2,0,1))) * 2 # wait: 1-Re=2 sin²(phi/4), so phi=4 asin sqrt(defect/2)
    phi_b=2*np.arcsin(np.sqrt(np.clip(pb/2,0,1))) * 2
    curv_err=float(np.max(np.abs(phi_a-phi_b))*2/h**2)
    bound=4*math.exp(4*end)*dist/h**2
    return dict(n=n,theta=theta,delta=delta,tau=tau,flow_geodesic_distance=df,
      flow_distance_bound=lip,curvature_difference=curv_err,curvature_difference_bound=bound,
      dist_ratio=df/lip,curv_ratio=curv_err/bound)


def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 cases=[grad_check(n,theta) for n in (2,3,4) for theta in (.16,.6,1.1)]
 assert max(x['gradient_max_error'] for x in cases)<5e-13
 assert max(x['action_error'] for x in cases)<1e-10
 assert max(x['commutator_real_error'] for x in cases)<1e-12
 assert all(x['commutator_nontrivial'] for x in cases)
 numerical=[scalar(1.2/n,n,t) for n in (4,8,16,32,64) for t in (.025,.12,.3)]
 for x in numerical:
   assert x['continuum_a_error']<=x['rigorous_a_error']+2e-11,x
   assert x['curvature_bound_ratio']<1,x
 perturb=[perturbation(2,.4,.0004,.025),perturbation(3,.3,.0002,.035)]
 for x in perturb:
   assert x['dist_ratio']<1+1e-7,x
   assert x['curv_ratio']<1+1e-7,x
 out={"status":"PASS","model":"periodic cubic SU2 original links, exact noncommuting homogeneous Wilson spatial flow", "scope":"finite nonlinear classical invariant non-Abelian sector; small open tubes have positive finite Wilson vacuum probability, no uniform h,R lower bound or quantum time claims", "force_tests":cases,"physical_flow":numerical,"nonhomogeneous_perturbation":perturb,
    "theorem":{"theta_flow":"dtheta/ds = -2 sin(theta/2)^3 cos(theta/2)","physical_a_flow":"da/dtau = -(2/h^3) sin(ha/2)^3 cos(ha/2)","continuum":"da/dtau=-a^3/4", "curvature_bound":"2d(Uxy,I)/h^2 <=2pi/tau for 0<theta(0)<=pi/2", "continuum_error":"abs(a_h-a)<= tau*h^2*a_0^5/16", "tube":"radius eta*h^2 exp(-4tau/h^2)/4 implies curvature <= 2pi/tau+eta"},
    "gates":{k:"OPEN" for k in ['P0','P1','P2','P3','P4','P5','T0','T1','T2','T3','T4','T5','YM_gap','gravity_UV']}}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({"status":"PASS","cases_force":len(cases),"cases_flow":len(numerical),"perturb":len(perturb),"max_grad":max(x['gradient_max_error'] for x in cases),"max_cont_error":max(x['continuum_a_error'] for x in numerical),"max_rel_curv":max(x['curv_ratio'] for x in perturb)},indent=2))
if __name__=='__main__':main()
