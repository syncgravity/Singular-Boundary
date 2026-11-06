#!/usr/bin/env python3
"""SU(2) full Wilson-exp shell + physical-time transfer: finite-grid scope only.

Analytical proof is in the paired markdown; numerical tests are independent
regressions of shell-incidence and harmonic-analysis identities, NOT proof of
continuum mass gap or a uniform renormalization limit.
"""
from __future__ import annotations
import argparse
import importlib.util
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.special import iv, eval_chebyu, roots_jacobi
from scipy.linalg import expm


def slab_geometry(prior: Path):
    spec=importlib.util.spec_from_file_location('prior_cubic_shell', str(prior))
    mod=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.slab()


def shell_incidence(g):
    eindex={v:i for i,v in enumerate(g['edges'])}
    shell=range(4,20)
    # Edges above z=0 cannot be covered by bottom xy plaquettes.
    shell_only_edges={i for i,e in enumerate(g['edges']) if e[0][2] or e[1][2]}
    counts={}
    good={}
    for k in range(1,9):
        surviving=[]
        for sub in itertools.combinations(shell,k):
            incidence=Counter(eindex[e] for fi in sub for e,sign in g['faces'][fi])
            if all(incidence[j]!=1 for j in shell_only_edges):
                surviving.append(sub)
        counts[k]=len(surviving);good[k]=surviving
    assert counts=={1:0,2:0,3:0,4:0,5:4,6:0,7:0,8:4},counts
    cap_signatures=[]
    for sub in good[5]:
        labels=tuple(g['labels'][fi] for fi in sub)
        # Exactly one top face and four walls above one bottom face.
        assert sum(z[0]=='xy' for z in labels)==1
        assert sum(z[0]!='xy' for z in labels)==4
        cap_signatures.append([list(x) for x in labels])
    return {'shell_faces':16,'nonbottom_integrated_edges':len(shell_only_edges),
            'surviving_shell_supports_by_cardinality':counts,
            'five_face_capping_disks':cap_signatures,
            'method':'independent all-subsets edge-exposure count: any edge with a unique nontrivial centered shell factor integrates to zero'}


def a(n,x):
    if x==0:return 1.0 if n==0 else 0.0
    return float(iv(n,2*x)-iv(n+2,2*x))


def a_analytic(n,x):
    # SU(2) dimensional recursion: (n+1) I_(n+1)(2x)/x
    if x==0:return 1.0 if n==0 else 0.0
    return float((n+1)*iv(n+1,2*x)/x)


def ap(n,x):
    return (a(n-1,x) if n>0 else 0.0)+a(n+1,x)


def bottom_series(x,beta,nmax=35):
    aa=np.array([a(n,beta) for n in range(nmax+1)])
    d=np.arange(1,nmax+2,dtype=float)
    u=np.array([eval_chebyu(n,x) for n in range(nmax+1)])
    p=np.sum((aa/aa[0])**4*u/(d**3))
    # exact fifth coefficient in gamma: (1/4 a0^4) sum a_n^3 a'_n / d_n^3 chi_n
    apn=np.array([ap(n,beta) for n in range(nmax+1)])
    c5=0.25*np.sum(aa**3*apn*u/(aa[0]**4*d**3))
    # derivative-based independent formula
    db=apn/aa[0]-(aa*apn[0]/aa[0]**2)
    derivative=np.sum(4*(aa/aa[0])**3*db*u/d**3)
    c5_2=(derivative+4*(apn[0]/aa[0])*p)/16
    return float(p),float(c5),float(c5_2)


def cap_kernel(cos_theta,gamma,nmax=35):
    a0=a(0,gamma)
    return sum((a(n,gamma)/a0)**5*eval_chebyu(n,cos_theta)/(n+1)**4 for n in range(1,nmax+1))


def residual_bound(beta,gamma):
    delta=2*math.expm1(2*abs(gamma))
    tail=sum(math.comb(16,k)*delta**k for k in range(8,17))
    return math.exp(8*abs(beta))*tail


def verify_characters():
    nodes,weights=roots_jacobi(160,.5,.5)
    values=[];mx=0
    for x in (-.7,-.2,.0,.2,.6,1.1):
        # beta may be negative: unnormalized exp remains positive.
        a0=a(0,x)
        haar=float((2/math.pi)*np.dot(weights,np.exp(2*x*nodes)))
        assert abs(a0-haar)<2e-13,(x,a0,haar)
        for n in range(13):
            an=a(n,x);other=a_analytic(n,x)
            haar_n=float((2/math.pi)*np.dot(weights,np.exp(2*x*nodes)*eval_chebyu(n,nodes)))
            er=max(abs(an-other),abs(an-haar_n));mx=max(mx,er)
            assert er<5e-12,(x,n,er)
        values.append({'beta':x,'a0':a0,'haar_total':haar})
    assert mx<5e-12
    checks=[]
    for beta in (0.,.12,.35,.9,1.5):
        for xx in (-.85,-.25,.2,.76):
            p,c5,c5b=bottom_series(xx,beta)
            assert abs(c5-c5b)<3e-12,(beta,xx,c5,c5b)
            # Differentiate normalized planar kernel numerically to cross-check.
            if beta>.001:
                eps=1e-5
                pp=bottom_series(xx,beta+eps)[0];pm=bottom_series(xx,beta-eps)[0]
                m=ap(0,beta)/a(0,beta)
                numerical=((pp-pm)/(2*eps)+4*m*p)/16
                assert abs(numerical-c5)<3e-9,(beta,xx,numerical,c5)
            checks.append({'beta':beta,'cos_theta':xx,'planar_kernel':p,
                           'exact_fifth_shell_taylor':c5})
    caps=[]
    for gamma in (.002,.01,.04,.12):
        for xx in (-.7,0.,.6):
            k=cap_kernel(xx,gamma)
            leading=gamma**5*eval_chebyu(1,xx)/16
            assert abs(k-leading) <= 8*(abs(gamma)**7), (gamma,xx,k,leading)
            caps.append({'gamma':gamma,'cos_theta':xx,'kernel':k,
                         'fundamental_gamma5_prediction':leading})
    bounds=[]
    for beta in (0.,.25,.65):
        for gamma in (.002,.008,.015,.04):
            b=residual_bound(beta,gamma)
            assert b>=0 and math.isfinite(b)
            bounds.append({'beta':beta,'gamma':gamma,'uniform_R8_bound':b})
    return {'harmonic_accuracy':mx,'haar_checks':values,'first_transverse_coefficient_checks':checks,
            'exact_five_face_cap_checks':caps,'controlled_shell_remainder_bounds':bounds}


def verify_physical_time():
    # One-face gauge-invariant Peter-Weyl reference exactly checks the
    # short-time variance formula, independent of the 3D incidence count.
    alpha=.8; beta=1.3; nmax=26
    C=np.array([n*(n+2)/4 for n in range(nmax+1)])
    H=np.diag(alpha*C+beta)
    K=np.diag(alpha*C)
    V=np.eye(nmax+1)*beta
    for n in range(nmax):H[n,n+1]=H[n+1,n]=-beta/2;V[n,n+1]=V[n+1,n]=-beta/2
    rows=[]
    for t in (.015,.025,.04,.07):
        amplitude=float(expm(-t*H)[0,0])
        naive=math.exp(-t*beta)
        diff=amplitude-naive
        # Finite symmetric heat-kernel transfer in the same character basis.
        half=expm(-t*V/2)
        transfer=half@np.diag(np.exp(-t*alpha*C))@half
        amplitude_t=float(transfer[0,0])
        two_step_memory=float(np.dot(transfer[1:,0],transfer[1:,0]))
        assert amplitude_t>naive and two_step_memory>0
        assert abs((amplitude_t-naive)/t**2-beta**2/8)<.028
        assert abs(two_step_memory/t**2-beta**2/4)<.09
        assert diff>0
        leading=beta**2/8
        rows.append({'time':t,'exact_one_plaquette_return':amplitude,'naive':naive,
                     'ratio_difference_over_t_squared':diff/t**2,'expected_as_t_to_zero':leading,
                     'trotter_one_step_return':amplitude_t,'trotter_vs_naive_over_t_squared':(amplitude_t-naive)/t**2,
                     'two_step_memory_over_t_squared':two_step_memory/t**2, 'expected_two_step_memory':beta**2/4})
        assert abs(diff/t**2-leading)<.028,(t,diff/t**2,leading)
    # For full 20-face slab, distinct elementary plaquettes are Haar-orthogonal.
    F=20;fourth=F*beta**2/4;coefficient=fourth/2
    assert abs(coefficient-4.225)<1e-12
    return {'finite_slab_faces':F,'physical_spatial_potential':'V=beta*sum_f(1-chi1(U_f)/2)',
            'Haar_mean_V':F*beta,'Haar_variance_V':fourth,
            'coarse_naive_time_semigroup_vs_fine_trotter_vacuum_t2_coefficient':coefficient,
            'two_step_markov_memory_t2_coefficient':fourth,
            'one_face_reference':rows,
            'analytic_all_time_inequality':'<1,T_eps 1> >= <1,exp(-eps V/2) 1>^2 > exp(-eps beta F) for all eps>0',
            'scope':'fixed spatial grid; asymptotic in temporal epsilon, no continuum uniformity'}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--prior-verifier',type=Path,default=Path(__file__).with_name('verify_cubic_transverse_shell_2026_11_06.py'))
    p.add_argument('--output',type=Path,default=Path(__file__).with_name('verification.json'))
    args=p.parse_args()
    geometry=slab_geometry(args.prior_verifier)
    nfaces=len(geometry['faces']);assert nfaces==20
    shell=shell_incidence(geometry)
    c=verify_characters()
    tm=verify_physical_time()
    data={'status':'PASS','scope':'finite 2x2x1 spatial Wilson-exponential slab and physical-time heat-kernel transfer, not 4D YM gap',
          'geometry':{'vertices':len(geometry['vertices']),'edges':len(geometry['edges']),
                      'faces':nfaces,'coarse_bottom_fixed_edges':len(geometry['fixed_boundary']),
                      'integrated_edges':len(geometry['edges'])-len(geometry['fixed_boundary'])},
          'shell_support':shell,'character_analysis':c,'physical_time_memory':tm,
          'invalid_inferences':['finite first-shell correction does not imply uniform interacting RG',
                                'positive transfer does not close continuum OS reconstruction',
                                'strict two-time coarse transfer memory prevents naive Markovian identification',
                                'no source-qualified 3D Penrose action equivalence']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS Wilson exponential; 4 five-face caps; exact SU2 Fourier identities; positive time-memory; source/continuum separation')
    print(json.dumps({'shell_supports':shell['surviving_shell_supports_by_cardinality'],
                      'max_character_numerical_residual':c['harmonic_accuracy'],
                      'temporal_memory_coefficient_beta_1p3':tm['two_step_markov_memory_t2_coefficient'],
                      'validation_summaries':len(c['first_transverse_coefficient_checks'])},indent=2))

if __name__=='__main__':main()
