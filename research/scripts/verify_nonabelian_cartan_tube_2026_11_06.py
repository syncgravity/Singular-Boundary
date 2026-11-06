#!/usr/bin/env python3
"""Independently test finite 3D SU(2) noncommuting neighborhoods of Cartan flow.

Checks are finite numerical regressions. The mathematical statement uses the
compact product-group Hessian estimate from PR #70, not numerical extrapolation.
Not a sampling of the true interacting Wilson quantum vacuum.
"""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from verify_nonlinear_energy_flow import (
    cubical, qexp, qmul, qinv, action_gradient, ode_rhs,
    quats_and_parts, unit
)
from verify_cartan_physical_flow import planar, smooth_angles


def qdistance(q, p):
    """Product SU(2) bi-invariant geodesic distance; generator T=i sigma/2 is unit."""
    prod = qmul(qinv(q),p)
    phi = np.arctan2(np.linalg.norm(prod[...,1:],axis=-1), prod[...,0])
    # Near the positive group ball (no quotient by center), d=2*phi
    return 2*phi


def make_cartan_reference(geom):
    n=geom['n'];B,L,edges=planar(n)
    angles=smooth_angles(n,edges)
    by_edge=dict(zip(edges,angles))
    a=np.array([by_edge.get(((i,j),d),0.) if d<2 else 0.
                for (i,j,k),d in geom['edges']])
    return qexp(np.column_stack((np.zeros(len(a)),np.zeros(len(a)),a)))


def flow(q,geom,tau):
    s=tau/geom['h']**2
    r=solve_ivp(lambda t,y:ode_rhs(t,y,geom),(0,s),q.ravel(),
                method='DOP853',rtol=1e-10,atol=2e-12,
                max_step=min(0.05,max(s/5,0.001)))
    assert r.success,r.message
    p=unit(r.y[:,-1].reshape(-1,4))
    return p,r.nfev


def curvature_vec(q,geom):
    hol=quats_and_parts(q,geom)[1][-1]
    return 2*np.asarray(hol[:,1:])/geom['h']**2


def haar_ball(r):
    """P(d_SU2(I,U)<r) for radius-2 S3 metric, 0<=r<=2pi."""
    r=min(max(float(r),0.),2*math.pi)
    # stable small radius, no cancellation
    if r<0.01:return r**3/(12*math.pi)*(1-r*r/20+r**4/840)
    return (r-math.sin(r))/(2*math.pi)


def experiment(n,tau,amplitude,seed):
    g=cubical(n);h=g['h'];E=len(g['edges'])
    ref=make_cartan_reference(g)
    rng=np.random.default_rng(seed)
    # Genuine 3-axis noncommuting perturbation at every original link.
    X=rng.normal(size=(E,3));X=X/np.linalg.norm(X,axis=1)[:,None]
    perp=(X[:,:2]**2).sum(axis=1)
    assert np.count_nonzero(perp>0.1) > E/2
    pert=qmul(qexp(amplitude*X),ref)
    initial_d=np.linalg.norm(qdistance(ref,pert))
    # A strictly open geodesic product ball around ref is a positive-Haar event.
    # We test smaller perturbations numerically than the bound requires; even when
    # the theoretical estimate is huge it remains valid.
    a,eval_ref=flow(ref,g,tau);b,eval_pert=flow(pert,g,tau)
    evolved_d=np.linalg.norm(qdistance(a,b))
    bound_d=math.exp(4*tau/h**2)*initial_d
    ca=curvature_vec(a,g);cb=curvature_vec(b,g)
    maxdiff=float(np.linalg.norm(ca-cb,axis=1).max())
    bound_curv=8*bound_d/h**2
    groupdiff=quats_and_parts(a,g)[1][-1]-quats_and_parts(b,g)[1][-1]
    maxgroup=float(np.linalg.norm(groupdiff,axis=1).max())
    # exact physical-radius tube ensuring at most unit perturbation of curvature
    radius_flow=h*h*math.exp(-4*tau/h**2)/8
    radius_energy=h/(32*len(g['ids']))
    radius=min(radius_flow,radius_energy)
    r_per_edge=radius/math.sqrt(E)
    p=haar_ball(r_per_edge)
    # log probability, not exp to avoid underflow. Positive for every finite mesh.
    log_haar_lower=E*math.log(p)
    # Faces zero and one start at (0,0,0), so their plaquette commutator is gauge covariant.
    firsttwo=quats_and_parts(pert,g)[1][-1][:2]
    based_plaquette_commutator=float(np.linalg.norm(np.cross(firsttwo[0,1:],firsttwo[1,1:])))
    noncommuting = based_plaquette_commutator>1e-14
    assert noncommuting,(n,tau,based_plaquette_commutator)
    assert evolved_d <= bound_d*(1+1e-7)+1e-8,(n,tau,evolved_d,bound_d)
    assert maxdiff <= bound_curv*(1+1e-6)+1e-8,(n,tau,maxdiff,bound_curv)
    assert maxgroup <= 4*bound_d+1e-8
    assert log_haar_lower<0 and p>0
    return dict(n=n,h=h,E=E,F=len(g['ids']),tau=tau,amplitude=amplitude,
        initial_product_distance=float(initial_d),evolved_product_distance=float(evolved_d),
        rigorous_evolved_distance_upper=float(bound_d),
        actual_max_physical_curvature_vector_difference=maxdiff,
        rigorous_physical_curvature_difference_upper=float(bound_curv),
        exact_tube_radius=float(radius),tube_radius_flow=float(radius_flow),
        tube_radius_energy=float(radius_energy),per_edge_subbox_radius=float(r_per_edge),
        one_edge_Haar_ball_probability=float(p),
        log_Haar_lower_bound=float(log_haar_lower),
        max_holonomy_quaternion_difference=maxgroup,
        based_plaquette_noncommutativity=based_plaquette_commutator,
        numerically_noncommuting=bool(noncommuting),nfev_ref=eval_ref,nfev_nonabelian=eval_pert)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    tests=[experiment(n,tau,amplitude,seed) for n,tau,amplitude,seed in [
        (2,0.006,0.002,2401),(2,0.025,0.001,2402),
        (3,0.012,0.0008,2403),(3,0.035,0.0005,2404),
        (4,0.008,0.0004,2405)]]
    # analytic cap volume: Haar uniform on S3 of radius 2
    ball_tests=[]
    for r in (0.001,0.02,0.2,0.6,1.5,3.0,2*math.pi):
        exact=haar_ball(r)
        assert 0<exact<=1
        ball_tests.append({'r':r,'Haar_ball_probability':exact})
    # Uniform Liouville measure of fixed maximal torus is 0. Every finite ball is positive.
    out={'status':'PASS',
         'scope':'Finite noncommuting full 3D SU2 classical flow in exponentially thin positive-Haar tubes near an exactly invariant Cartan-planar reference; no uniform vacuum probability, quantum Schur or continuum theorem',
         'reference':'PR73 full 3D original-link Cartan-planar SU2 reference',
         'hessian_bound':4.,
         'guaranteed_radius':'delta_h(tau)=min(h^2 exp(-4tau/h^2)/8, h/(32F)) in product SU2 geodesic norm',
         'probability_lower':'nu_h(B_delta(U0)) >= min(Omega_h^2) [p(delta/sqrt(E))]^E > 0, p(r)=(r-sin r)/(2pi)',
         'curvature_difference_bound':'max_p |2Im U_p(s)/h^2 - 2Im U0_p(s)/h^2| <= 8 exp(4s)d_2(U,U0)/h^2',
         'tests':tests,'Haar_ball_volume_tests':ball_tests,
         'open':['No h/R uniform lower probability for the tube; tube is super-small as h decreases',
                 'No generic non-Abelian positive-radius regularity for typical Wilson vacuum configurations',
                 'No weak-coupling quantum expectation bound, renormalized covariance or complete Schur form',
                 'No 4D OS quantum Yang-Mills mass gap, Penrose transfer or gravity UV theorem']}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','tested_cubic_meshes':sorted(set(x['n'] for x in tests)),
                      'max_actual_evolved_over_bound':max(x['evolved_product_distance']/x['rigorous_evolved_distance_upper'] for x in tests),
                      'max_actual_curvature_over_bound':max(x['actual_max_physical_curvature_vector_difference']/x['rigorous_physical_curvature_difference_upper'] for x in tests),
                      'minimum_log_haar_tube_probability':min(x['log_Haar_lower_bound'] for x in tests),
                      'all_noncommuting':all(x['numerically_noncommuting'] for x in tests)},indent=2))


if __name__=='__main__':main()
