#!/usr/bin/env python3
"""Finite SU(2) vacuum-weighted blocking: exact identities and independent rotor tests.

The two-link rotor is a mathematical test of projection/memory only, NOT a
3+1D Yang--Mills or a local-gauge-invariant Wilson lattice simulation.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import iv


def weighted_grad_norm(kappa: float) -> float:
    # Haar class density (2/pi) sin^2(theta) dtheta, character=2cos(theta).
    # Ground-state density exp(kappa*character), normalized by a0.
    z=2*kappa
    return float((3*iv(0,z)-4*iv(2,z)+iv(4,z))/(4*(iv(0,z)-iv(2,z))))


def weighted_grad_quad(kappa: float) -> tuple[float,float,float]:
    z=2*kappa
    norm=quad(lambda th:(2/math.pi)*math.sin(th)**2*math.exp(z*math.cos(th)),0,math.pi,epsabs=1e-13,epsrel=1e-13)[0]
    num=quad(lambda th:(2/math.pi)*math.sin(th)**4*math.exp(z*math.cos(th)),0,math.pi,epsabs=1e-13,epsrel=1e-13)[0]
    return num/norm,norm,num


def rotor_memory_double_quadrature(alpha:float,kappa:float,N:int=96)->float:
    # Independent theta_A x theta_X quadrature, with isotropic orientation moment
    # E[(n_A dot n_X)^2]=1/3 (also exactly checked by 6-axis octahedral rule).
    pts,weights=np.polynomial.legendre.leggauss(N)
    theta=math.pi/2*(pts+1)
    wt=math.pi/2*weights
    sn2=np.sin(theta)**2
    a0=iv(0,2*kappa)-iv(2,2*kappa)
    prob_A=(2/math.pi)*sn2*np.exp(2*kappa*np.cos(theta))/a0
    prob_X=(2/math.pi)*sn2
    A=float(np.dot(wt,prob_A*sn2));X=float(np.dot(wt,prob_X*sn2))
    axes=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=float)
    angular=float(np.mean((axes@axes.T)**2))
    return float(alpha**2*kappa**2*A*X*angular)


def quaternion_character_derivative_check(seed:int=341)->dict:
    rng=np.random.default_rng(seed)
    q=rng.standard_normal((100,4));q=q/np.linalg.norm(q,axis=1,keepdims=True)
    delta=1e-4
    # Left unit quaternion exp(delta*T_i), T_i represented by quaternion (0,e_i/2).
    # tr_fund(exp(delta T_i)U) = 2 cos(delta/2) q0 - 2 sin(delta/2) qi.
    deriv=(2*np.cos(delta/2)*q[:,0,None]-2*np.sin(delta/2)*q[:,1:]
          -(2*np.cos(delta/2)*q[:,0,None]+2*np.sin(delta/2)*q[:,1:]))/(2*delta)
    err_grad=float(np.max(np.abs(deriv+q[:,1:])))
    pos=2*np.cos(delta/2)*q[:,0,None]-2*np.sin(delta/2)*q[:,1:]
    neg=2*np.cos(delta/2)*q[:,0,None]+2*np.sin(delta/2)*q[:,1:]
    center=2*q[:,0,None]
    lap=((pos-2*center+neg)/delta**2).sum(axis=1)
    err_lap=float(np.max(np.abs(lap+0.75*(2*q[:,0]))))
    assert err_grad<1e-9,(err_grad,"quaternion gradient")
    assert err_lap<3e-7,(err_lap,"quaternion Casimir")
    return {"sample_quaternions":len(q),"finite_difference_gradient_max_abs_error":err_grad,
            "finite_difference_laplacian_max_abs_error":err_lap}


def toy_cases() -> list[dict]:
    alpha_f=0.5;alpha_c=1.0
    cases=[]
    for k in (0.0,0.2,0.7,1.0,1.5,2.5):
        G=weighted_grad_norm(k)
        Gquad,a0,_=weighted_grad_quad(k)
        Bpred=alpha_f**2*k**2*G/4
        Bnumeric=rotor_memory_double_quadrature(alpha_f,k)
        assert abs(G-Gquad)<4e-12,(k,G,Gquad)
        assert abs(Bpred-Bnumeric)<3e-12,(k,Bpred,Bnumeric)
        # The 8-edge boundary formula is 8*a*E(1-W^2/4).
        # Here the toy is one coarse product (two fine SU2 links):
        # projected electric coefficient a_f=2*alpha_f, a_c=alpha_c.
        assert alpha_c==2*alpha_f
        slope_coarse=3*alpha_c/4
        slope_fine=3*2*alpha_f/4
        assert slope_coarse==slope_fine
        delta_second=Bpred
        cases.append({"kappa":k,"weighted_grad_squared_bessel":G,
          "weighted_grad_squared_quadrature":Gquad,"a0_bessel":float(iv(0,2*k)-iv(2,2*k)),"a0_quadrature":a0,
          "vacuum_weighted_coarse_density":"Haar (exact, independent of kappa)",
          "coarse_compressed_electric_coefficient":alpha_c,
          "fine_compressed_electric_coefficient":2*alpha_f,
          "first_positive_time_moment":slope_coarse,
          "two_link_influence_norm_squared_predicted":Bpred,
          "two_link_influence_norm_squared_integrated":Bnumeric,
          "fine_minus_coarse_second_derivative":delta_second,
          "fine_minus_coarse_small_t_coefficient":delta_second/2,
          "strict_positive_time_difference":bool(k!=0)})
    return cases


def su2_haar_quaternion_monte_carlo(kappa:float=1.0,alpha:float=0.5,n:int=150000,seed:int=206):
    """Independent Monte Carlo check, not used to prove analytic SU(2) identity."""
    rng=np.random.default_rng(seed)
    accepted=[];total=0
    while sum(x.shape[0] for x in accepted)<n:
        count=350000
        raw=rng.standard_normal((count,4));raw/=np.linalg.norm(raw,axis=1)[:,None]
        take=rng.random(count)<np.exp(kappa*(2*raw[:,0]-2))
        accepted.append(raw[take]);total+=count
        if total>8_000_000:raise RuntimeError("insufficient rejection samples")
    A=np.concatenate(accepted,axis=0)[:n]
    B=rng.standard_normal((n,4));B/=np.linalg.norm(B,axis=1)[:,None]
    X0=A[:,0]*B[:,0]-np.sum(A[:,1:]*B[:,1:],axis=1)
    Xv=A[:,0,None]*B[:,1:]+B[:,0,None]*A[:,1:]+np.cross(A[:,1:],B[:,1:])
    chi=2*X0
    bval=(-alpha*kappa*np.sum(A[:,1:]*Xv,axis=1))
    measured=float(np.mean(bval**2))
    expected=alpha**2*kappa**2*weighted_grad_norm(kappa)/4
    assert abs(measured-expected)<0.001,(measured,expected)
    assert abs(float(np.mean(chi)))<0.02
    assert abs(float(np.mean(chi**2))-1)<0.02
    return {"sample_size":n,"candidate_quaternions":total,"kappa":kappa,"alpha":alpha,
     "observed_chi_mean":float(np.mean(chi)),"observed_chi_second_moment":float(np.mean(chi**2)),
     "observed_influence_norm_squared":measured,"exact_influence_norm_squared":expected,
     "abs_error":abs(measured-expected),"warning":"Monte Carlo regression ONLY; analytic theorem uses SU2 Haar/Bessel identities."}


def finite_matrix_shorting_regression(seed:int=147)->list[dict]:
    """Independent bounded finite-matrix Feshbach/shorted-form regression.
    In the theorem, the actual QLP may be unbounded; variational form is essential.
    """
    rng=np.random.default_rng(seed)
    q,_=np.linalg.qr(rng.standard_normal((3,3)))
    rot=np.eye(4);rot[1:,1:]=q
    L=rot@np.diag([0.0,0.4,1.5,3.1])@rot.T
    assert np.max(np.abs(L[:,0]))<1e-13
    out=[]
    for z in (0.05,0.5,2.0):
        inverse=np.linalg.inv(L+z*np.eye(4))[:2,:2]
        S=np.linalg.inv(inverse)
        A=L[:2,:2];B=L[2:,:2];D=L[2:,2:]
        short=A+z*np.eye(2)-B.T@np.linalg.solve(D+z*np.eye(2),B)
        err=float(np.linalg.norm(S-short,ord=2))
        eig=np.linalg.eigvalsh(short-z*np.eye(2))
        assert err<2e-12,(z,err)
        assert np.min(eig)>-1e-12,(z,eig)
        assert abs(short[0,0]-z)<2e-12 and abs(short[0,1])<2e-12
        assert np.min(np.linalg.eigvalsh(A+z*np.eye(2)-short))>-1e-12
        out.append({"z":z,"resolvent_vs_variational_schur_abs_error":err,
          "minimum_schur_minus_z_eigenvalue":float(np.min(eig)),
          "vacuum_schur_value":float(short[0,0])})
    return out


def two_scale_kinematics() -> dict:
    # This checks exact fixed-physical-support coefficients, not an interacting vacuum.
    rows=[]
    for g_f in (1.0,0.98,0.8,0.5,0.25):
        h=0.5;g_c=1.0
        a_c=g_c**2/(2*h)
        a_f=2*g_f**2/(2*(h/2))
        expected=4*(g_f/g_c)**2
        assert abs(a_f/a_c-expected)<1e-13
        rows.append({"g_c":g_c,"g_f":g_f,"coarse_alpha":a_c,
                     "refined_subdivided_alpha":a_f,"ratio":a_f/a_c,
                     "asymptotic_free_weak_coupling_not_certified":True})
    return {"geometry":"eight fixed physical coarse boundary holonomies, two fine links per product",
            "coarse_link_count":8,"fine_boundary_link_count":16,
            "exact_kinetic_ratio":"4*(g0(h/2)/g0(h))**2", "samples":rows}


def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path('verification.json'));args=ap.parse_args()
    q=quaternion_character_derivative_check()
    cases=toy_cases()
    kin=two_scale_kinematics()
    form=finite_matrix_shorting_regression()
    mc=su2_haar_quaternion_monte_carlo()
    out={"status":"PASS", "scope":"finite SU(2) conditional-vacuum blocking and analytic SU(2) two-link rotor counterexample; NOT a Wilson mass-gap theorem",
         "source_normalization":{"H":"alpha sum_e (-Delta_e) + V", "casimir_fundamental":0.75,
           "fundamental_gradient_squared":"1-chi_1(U)**2/4", "weighted_ground_state":"Omega>0, L=Omega**(-1)*(H-E0)*Omega"},
         "quaternion_identity_checks":q,"rotor_cases":cases,"two_scale_boundary_diffusion":kin,"finite_matrix_variational_Schur":form,"independent_haar_quaternion_MC":mc,
         "theorem_status":{"finite_true_vacuum_projection":"exact conditional theorem",
           "coarse_marginal_equals_full_time_dynamics":"FALSE, exact SU(2) rotor counterexample",
           "uniform_long_time_interacting_comparison":"OPEN",
           "genuine_three_dimensional_Penrose_refinement":"OPEN",
           "four_dimensional_Yang_Mills_mass_gap":"OPEN",
           "quantum_gravity_finiteness":"OPEN"}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print("PASS: exact SU(2) character gradient; weighted vacuum/rotor integrals; source-normalized kinetic ratio")
    for row in cases:
        print("kappa",row['kappa'],"G",format(row['weighted_grad_squared_bessel'],'.10f'),
              "B^2",format(row['two_link_influence_norm_squared_predicted'],'.10f'),
              "quadrature_err",format(abs(row['two_link_influence_norm_squared_predicted']-row['two_link_influence_norm_squared_integrated']),'.3g'))
    print("Finite-matrix Schur-form max error", max(r["resolvent_vs_variational_schur_abs_error"] for r in form))
    print("Independent Haar-quaternion Monte Carlo n",mc["sample_size"],"influence error",format(mc["abs_error"],".6g"))
    print("Physical continuum, Penrose and gravity gates: OPEN")

if __name__=='__main__':main()
