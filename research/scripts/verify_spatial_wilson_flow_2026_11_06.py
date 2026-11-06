#!/usr/bin/env python3
"""Finite SU(2) spatial Wilson flow / Fisher-vs-gap countermodel verification.

Verifies standard character integrals, an exact smooth-density low-gap countermodel,
Haar first-moment covariance/Dirichlet forms, and quaternion geometry/flow checks.
No continuum Yang--Mills gap or quantum gravity theorem is implied.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import roots_chebyu, eval_chebyu
from scipy.integrate import quad


def points(n=280):
    xs, raw = roots_chebyu(n)
    return xs, raw / (math.pi / 2)


def quat_mul(a,b):
    return np.array([a[0]*b[0] - np.dot(a[1:],b[1:]), *(a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:]))])


def quat_inv(a):
    return np.r_[a[0],-a[1:]]


def quat_normal(a):
    return a/np.linalg.norm(a)


def exp_lie(v):
    t=float(np.linalg.norm(v))
    if t<1e-14:return np.r_[1.,v*0.5]
    return np.r_[np.cos(t/2),np.sin(t/2)*v/t]


def random_haar(rng,n):
    a=rng.normal(size=(n,4))
    return a/np.linalg.norm(a,axis=1,keepdims=True)


def geometry(ns=(2,2,1)):
    nx,ny,nz=ns
    bounds=tuple(int(n) for n in ns)
    verts=[(i,j,k) for i in range(nx+1) for j in range(ny+1) for k in range(nz+1)]
    edges=[]
    for v in verts:
        for d in range(3):
            if v[d]<bounds[d]:edges.append((v,d))
    indices={x:i for i,x in enumerate(edges)}
    faces=[]
    for v in verts:
        for d1,d2 in ((0,1),(0,2),(1,2)):
            if v[d1]>=bounds[d1] or v[d2]>=bounds[d2]:continue
            a=list(v);a[d1]+=1
            b=list(v);b[d2]+=1
            faces.append([(indices[v,d1],1),(indices[tuple(a),d2],1),
                          (indices[tuple(b),d1],-1),(indices[v,d2],-1)])
    deg=np.zeros(len(edges),dtype=int)
    for f in faces:
        for i,_ in f:deg[i]+=1
    assert deg.max()<=4
    return {'verts':verts,'edges':edges,'faces':faces,'degree':deg.tolist(),'ns':list(ns)}


def face_prod(q,face):
    a=np.array([1.,0.,0.,0.])
    for eid,sgn in face:
        a=quat_mul(a,q[eid] if sgn==1 else quat_inv(q[eid]))
    return a


def wilson_action(q,geom):
    return sum(1-face_prod(q,f)[0] for f in geom['faces'])


def mutate_left(q,edge,vec):
    x=q.copy(); x[edge]=quat_mul(exp_lie(vec),x[edge]);return x


def left_gradient(q,geom,step=1e-5):
    grad=np.empty((len(q),3))
    for e in range(len(q)):
        for k in range(3):
            v=np.zeros(3);v[k]=step
            grad[e,k]=(wilson_action(mutate_left(q,e,v),geom)-wilson_action(mutate_left(q,e,-v),geom))/(2*step)
    return grad


def one_square_flow_test(rng):
    geom=geometry((1,1,1));face=geom['faces'][0]
    q=random_haar(rng,len(geom['edges']))
    # This particular face can be used even while the rest of the cube is present,
    # but for an *isolated* face the action includes only this face.
    g={'faces':[face]}
    x0=face_prod(q,face)[0]
    q0=q.copy()
    dt=0.001;steps=200
    for k in range(steps):
        grad=left_gradient(q,g,step=1e-5)
        for e in range(len(q)):
            q[e]=quat_mul(exp_lie(-dt*grad[e]),q[e])
    x_end=face_prod(q,face)[0]
    t=math.tanh(steps*dt)
    expected=(x0+t)/(1+x0*t)
    err=abs(x_end-expected)
    assert err<0.002,(err,x0,x_end,expected)
    # A gauge-transformed configuration has the identical Wilson action.
    ve=geom['verts'];at={v:i for i,v in enumerate(ve)}
    gauge=random_haar(rng,len(ve))
    qt=np.empty_like(q0)
    for eid,(v,d) in enumerate(geom['edges']):
        z=list(v);z[d]+=1
        qt[eid]=quat_mul(quat_mul(gauge[at[v]],q0[eid]),quat_inv(gauge[at[tuple(z)]]))
    action_error=abs(wilson_action(q0,g)-wilson_action(qt,g))
    assert action_error<1e-12
    grad0=left_gradient(q0,g);gradt=left_gradient(qt,g)
    gauge_error=0.0
    for eid,(v,d) in enumerate(geom['edges']):
        gv=gauge[at[v]]
        expvec=quat_mul(quat_mul(gv,np.r_[0.,grad0[eid]]),quat_inv(gv))[1:]
        gauge_error=max(gauge_error,np.linalg.norm(gradt[eid]-expvec))
    assert gauge_error<3e-8, gauge_error
    return {'initial_trace_over_two':float(x0),'flow_time':steps*dt,
            'final_trace_over_two':float(x_end),'exact_formula':float(expected),
            'euler_error':float(err),'gauge_action_error':float(action_error),'gauge_force_error':float(gauge_error)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,default=Path('docs/evidence/R3_SPATIAL_WILSON_FLOW_2026-11-06.json'))
    args=ap.parse_args()
    rng=np.random.default_rng(20261106)
    x,w=points(320)
    assert abs(w.sum()-1)<1e-13
    assert abs(np.dot(w,x*x)-.25)<1e-13
    assert abs(np.dot(w,x**4)-.125)<1e-13
    # Smooth strictly positive SU2 class densities, uniform Fisher, gap -> 0.
    cases=[]
    for eps in (0.5,0.2,0.05,0.01,0.002):
        z=0.25+eps**2
        rho=(x*x+eps**2)/z
        u=np.sqrt(rho)
        grad_u_sq=(x*x/(z*(x*x+eps**2)))*(1-x*x)/4
        # Adaptive integrals resolve epsilon-width barrier layers even at 0.002.
        haarp=lambda y:2/math.pi*math.sqrt(max(0.,1-y*y))
        H=quad(lambda y:haarp(y)*(y*y/(z*(y*y+eps*eps)))*(1-y*y)/4,
               -1,1,epsabs=5e-13,epsrel=5e-13,limit=900,points=[0])[0]
        f=x/np.sqrt(x*x+eps**2)
        variance=0.25/z # E_rho(f^2)= E_Haar(x²)/Z; mean zero by symmetry
        D=quad(lambda y:haarp(y)*(eps**4/(4*z))*(1-y*y)/(y*y+eps*eps)**2,
               -1,1,epsabs=5e-13,epsrel=5e-13,limit=900,points=[0])[0]
        quotient=D/variance
        var_trace=4*(.125+.25*eps*eps)/z # E_Haar x^4=1/8
        # The positive class rotor -Delta + V_epsilon has ground state sqrt(rho).
        # Check the explicit radial Laplace--Beltrami identity at sample points.
        sample_x=np.array([-.93,-.4,0.,.25,.71])
        potential=eps*eps*(1-sample_x**2)/(4*(sample_x**2+eps*eps)**2)-3*sample_x**2/(4*(sample_x**2+eps*eps))
        root=np.sqrt(sample_x**2+eps*eps)
        deriv=sample_x/root;second=eps*eps/(sample_x**2+eps*eps)**1.5
        lap=(1-sample_x**2)*second/4 -3*sample_x*deriv/4
        assert np.max(np.abs(-lap+potential*root))<1e-10
        assert H<=.75+1e-12, H
        assert variance>0 and quotient<=eps+2e-7,(eps,quotient)
        assert var_trace>=1-1e-10
        cases.append({'epsilon':eps,'H1_sqrt_density':H,'Fisher':4*H,
            'gap_upper_rayleigh':quotient,'exact_bound':eps,
            'variance_of_test':variance,'variance_fund_trace':var_trace,
            'class_rotor_potential_barrier':1/(4*eps*eps),
            'density_min':eps*eps/z,'density_max':(1+eps*eps)/z})
    # Central heat convolution on SU2 class densities and fundamental character.
    heat=[]
    for s in (.1,.3,1.2):
        spec=sum((n+1)*math.exp(-n*(n+2)*s/4)*eval_chebyu(n,x) for n in range(58))
        normalized=float(np.dot(w,spec))
        # Peter--Weyl convolution coefficient is E_Haar[k_s * chi1] / dim(chi1).
        eig=float(np.dot(w,spec*eval_chebyu(1,x))/2)
        target=math.exp(-3*s/4)
        assert abs(normalized-1)<2e-12
        assert abs(eig-target)<2e-12,(s,eig,target)
        eps=0.002;a=1/(1+4*eps*eps)
        rhobar=1+a*math.exp(-2*s)*eval_chebyu(2,x)
        assert min(rhobar)>=1-math.exp(-2*s)-1e-10
        # Centered normalized physical character: scalar group-heat multiplier cancels.
        # A distinct strictly positive reference density gives a nonzero mean.
        test_rho=1+0.2*(2*x)
        u=2*x
        mean=float(np.dot(w,test_rho*u))
        var=float(np.dot(w,test_rho*(u-mean)**2))
        old_center=(u-mean)/math.sqrt(var)
        flowed_center=(target*u-target*mean)/(target*math.sqrt(var))
        normalized_character_error=float(np.max(np.abs(old_center-flowed_center)))
        assert normalized_character_error<1e-13
        heat.append({'group_heat_time':s,'fundamental_multiplier':eig,
                     'expected_multiplier':target,'adjoint_density_multiplier':math.exp(-2*s),
                     'smoothed_density_min':float(rhobar.min()),'uniform_min_certificate':1-math.exp(-2*s),
                     'normalized_deterministic_wilson_error':normalized_character_error})
    # Haar covariance and Dirichlet matrix for chi1 and chi2 of the SAME L-edge loop.
    S=np.array([[np.dot(w,(2*x)**2),np.dot(w,(2*x)*eval_chebyu(2,x))],
                [np.dot(w,(2*x)*eval_chebyu(2,x)),np.dot(w,eval_chebyu(2,x)**2)]])
    Dx=(1-x*x)/4
    der=np.stack((2*np.ones_like(x),8*x))
    gram=np.array([[np.dot(w,Dx*der[i]*der[j]) for j in range(2)] for i in range(2)])
    assert np.allclose(S,np.eye(2),atol=2e-13)
    assert np.allclose(gram,np.diag([.75,2]),atol=2e-13)
    G4=4*gram
    eigvals=np.linalg.eigvalsh(np.linalg.solve(S,G4))
    assert np.allclose(eigvals,[3,8],atol=2e-12)
    # Full finite gauge-covariant spatial flow with a volume-independent Hessian bound.
    geom=geometry((2,2,1))
    assert len(geom['verts'])==18 and len(geom['edges'])==33 and len(geom['faces'])==20
    q=random_haar(rng,len(geom['edges']))
    directional=[]
    for _ in range(24):
        v=rng.normal(size=(len(q),3));v/=np.linalg.norm(v)
        step=0.0003
        qp=np.array([quat_mul(exp_lie(step*v[e]),q[e]) for e in range(len(q))])
        qm=np.array([quat_mul(exp_lie(-step*v[e]),q[e]) for e in range(len(q))])
        hess=(wilson_action(qp,geom)+wilson_action(qm,geom)-2*wilson_action(q,geom))/(step*step)
        assert abs(hess)<=4+0.001,hess
        directional.append(float(hess))
    flow=one_square_flow_test(rng)
    # Exact one-plaquette spatial Wilson flow in an independent quadrature.
    flowed=[]
    for s in (0,.1,.3,.8,1.5):
        t=math.tanh(s)
        y=2*(x+t)/(1+x*t)
        dy=(1-t*t)/(1+x*t)**2 # dW_s/dW
        mean=float(np.dot(w,y)); var=float(np.dot(w,(y-mean)**2))
        D=float(4*np.dot(w,dy*dy*(1-x*x)))
        assert var>0 and D/var>=3-1e-10
        flowed.append({'lattice_flow_time':s,'mean':mean,'variance':var,
                       'dirichlet_4link':D,'normalized_first_moment_alpha1':D/var})
    # Uniform-volume exterior influence upper bound from 4-Hessian row sums.
    tails=[]
    for s in (.1,.5,1.0):
        for r in (8,16,32):
            term=1.
            vals=[]
            for k in range(0,200):
                if k>0:term*=4*s/k
                if k>=r:vals.append(term)
            tail=float(sum(vals))
            tails.append({'lattice_flow_time':s,'distance_in_plaquette_adjacency':r,
                          'sensitivity_row_tail_upper_bound':tail})
    output={
       'status':'PASS','scope':'FINITE 3D spatial SU2 and independent exact SU2 class density; no continuum Yang--Mills theorem',
       'countermodel':cases,'heat_character_tests':heat,
       'Haar_loop_gram':{'S':S.tolist(),'G_one_edge':gram.tolist(),'G_four_link':G4.tolist(),'generalized_eigenvalues_L4':eigvals.tolist()},
       'cubic_geometry':{'vertices':18,'edges':33,'faces':20,'max_edge_face_degree':max(geom['degree'])},
       'Hessian_random_checks':{'count':len(directional),'max_abs_directional_Hessian':max(map(abs,directional)),
                                'analytic_uniform_bound':4},
       'exact_single_face_flow':flow,'flowed_single_face_haar':flowed,'quasilocal_Poisson_tail':tails,
       'open_obligations':['No g0(h)-uniform interacting covariance/Dirichlet quotient',
                           'No physical radius t=h²s uniform spatial flowed observable',
                           'No full energy-dependent Schur/physical-time infrared comparison',
                           'No four-dimensional OS continuum or Yang--Mills mass gap',
                           'No source-certified 3D Penrose transfer or gravitational UV theorem'],
       'test_only':['One-face flow and Haar class functions are exact finite controls, NOT interacting 3D vacuum data',
                    'Random Hessian/gauge covariance checks are consistency checks; analytic proofs are separate']}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'result':'PASS','H1_countermodel_max':max(c['H1_sqrt_density'] for c in cases),
                      'Rayleigh_min':min(c['gap_upper_rayleigh'] for c in cases),
                      'Hessian_max_check':max(map(abs,directional)),
                      'flow_exact_error':flow['euler_error'],'geometry':[18,33,20],
                      'gates':'OPEN'}))

if __name__=='__main__':main()
