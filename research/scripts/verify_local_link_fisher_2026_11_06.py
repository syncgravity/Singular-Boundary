#!/usr/bin/env python3
"""Independent finite-geometry and 1-plaquette SU(2) checks for a local, gap-free ground-state Fisher bound.
The analytic theorem is in the matching research/theorems report; numerical checks are NOT its proof.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.integrate import quad


def exact_cubical_counts(n):
    assert n >= 1
    E = 3*n*(n+1)**2
    F = 3*n*n*(n+1)
    counts={2:12*n,3:12*n*(n-1),4:3*n*(n-1)**2}
    assert sum(counts.values()) == E
    assert sum(d*c for d,c in counts.items()) == 4*F
    # independently enumerate every oriented edge and its number of unit faces
    edges=[]
    for axis in range(3):
        other=[x for x in range(3) if x!=axis]
        for u in range(n):
            for v in range(n+1):
                for w in range(n+1):
                    coordinate=[None,None,None]
                    coordinate[axis]=u
                    coordinate[other[0]]=v
                    coordinate[other[1]]=w
                    degree=sum(int(0<coordinate[ax])+int(coordinate[ax]<n) for ax in other)
                    edges.append(degree)
    independent={d:edges.count(d) for d in [2,3,4]}
    assert independent==counts and len(edges)==E
    return {'n':n,'E':E,'F':F,'degree_counts':{str(k):v for k,v in counts.items()},'sum_degree':sum(edges),'max_degree':max(edges)}


def one_plaquette_rotor(alpha,beta,N=85):
    # Gauge-invariant 2D 1-face model: four link electric Laplacians reduce
    # to 4*alpha times the SU(2) Casimir on the plaquette holonomy.
    # Orthogonal Haar characters chi_n; chi_1*chi_n=chi_(n+1)+chi_(n-1).
    n=np.arange(N,dtype=float)
    diag=alpha*n*(n+2)+beta  # 4*alpha*C_n
    off=np.full(N-1,-beta/2,dtype=float)
    e, vectors=eigh_tridiagonal(diag,off,select='i',select_range=(0,0))
    a=vectors[:,0]
    if a[0]<0:a=-a
    assert abs(float(a@a)-1)<2e-13
    casimir=n*(n+2)/4
    J=float(np.dot(a*a,casimir))
    # Multiplication by character chi_1 is tridiagonal with coefficient 1.
    W_a=np.zeros(N+1)
    W_a[:N]+=np.r_[a[1:],0]
    W_a[1:N+1]+=a
    ew=float(a@W_a[:N]);ew2=float(W_a@W_a)
    variance=ew2-ew*ew
    assert variance>0
    # The normalized ground state is smooth and positive; check class-wavefunction
    # at 1001 angles away from endpoints using exact SU(2) characters.
    theta=np.linspace(0.001,math.pi-0.001,1001)
    chars=np.sin(np.outer(theta,n+1))/np.sin(theta[:,None])
    wave=chars@a
    assert wave.min()>-1e-12, wave.min()
    # Electric energy per original link is alpha*J. Model d_e=1 (only face).
    assert alpha*J<=beta+1e-10, (alpha,beta,alpha*J)
    assert alpha*J + beta*(1-ew/2) <= beta+1e-10, 'sharp local electric+magnetic excess inequality'
    # Even the stronger one-face trial E0<=beta is respected.
    assert float(e[0])<=beta+1e-10
    # Independent spectral measure: diagonalize the full finite-character rotor.
    # Its ground-state transformed normalized Wilson correlation must have
    # first moment equal to the Dirichlet/carre-du-champ expression.
    evals, evecs=eigh_tridiagonal(diag,off)
    wpsi=(W_a[:N]-ew*a)/math.sqrt(variance)
    weights=(evecs.T@wpsi)**2
    energies=evals-evals[0]
    assert abs(float(weights.sum())-1)<1e-10
    spectral_m1=float(weights@energies)
    dirichlet_m1=4*alpha*(1-ew2/4)/variance
    assert abs(spectral_m1-dirichlet_m1)<2e-9,(spectral_m1,dirichlet_m1)
    correlations=[]
    for t in [0,.01,.1,.5,1,2]:
        ct=float(weights@np.exp(-t*energies))
        assert ct>=1-t*spectral_m1-1e-9
        correlations.append({'t':t,'C_t':ct,'tangent_lower':1-t*spectral_m1})
    return {'alpha':alpha,'beta':beta,'beta_over_alpha':beta/alpha,
        'lowest_energy':float(e[0]),'one_link_kinetic':alpha*J,
        'local_grad_sqrt_rho_squared':J,'local_upper_bound':beta/alpha,
        'ratio_to_local_bound':alpha*J/beta,'joint_kinetic_plus_local_magnetic':alpha*J+beta*(1-ew/2),
        'wilson_mean':ew,'wilson_variance':variance,
        'minimum_approximate_positive_ground_wavefunction':float(wave.min()),
        'basis_size':N,'correlator_first_moment_exact':dirichlet_m1,'correlator_first_moment_spectral':spectral_m1,'time_correlations':correlations}


def haar_trace_band_probability(m,r):
    # Haar pushforward of SU2 fundamental trace W has p(w)=sqrt(4-w^2)/(2*pi).
    lo=max(-2,m-r);hi=min(2,m+r)
    if hi<=lo:return 0.0
    val,_=quad(lambda x: math.sqrt(max(0,4-x*x))/(2*math.pi),lo,hi,
               epsabs=1e-12,limit=100)
    assert val<=2*r/math.pi+1e-11
    return val


def run(out):
    cubes=[exact_cubical_counts(n) for n in [1,2,3,4,8,16,32]]
    # beta/alpha=4/g^4. SU2 local single-holonomy sqrt marginal energy <=4 beta/alpha
    bare=[{'g0':g,'beta_div_alpha':4/g**4,
           'max_grad_energy_single_loop':16/g**4,
           'max_Fisher_information':64/g**4} for g in [0.5,0.75,1.,1.5,2.,3.]]
    rotor=[one_plaquette_rotor(1.,b) for b in [0.05,.2,1.,4.,20.,60.]]
    for m in [-2,-1.9,-1,0,0.7,1.8,2]:
        for r in [.01,.1,.5,1.,2.]:haar_trace_band_probability(m,r)
    # The fixed Haar trace moments are 0,1 and 2 (fourth).
    mom=[quad(lambda x:x**k*math.sqrt(max(0,4-x*x))/(2*math.pi),-2,2,
              epsabs=1e-11)[0] for k in [0,1,2,4]]
    assert max(abs(mom[i]-v) for i,v in enumerate([1,0,1,2]))<1e-10
    report={
      'status':'PASS','theorem_scope':'Finite original-link SU2 Wilson vacuum; volume-independent local H1/Fisher estimate at fixed g0; NOT uniform as g0 tends to zero',
      'alpha':'g0^2/(2h)','beta':'2/(g0^2 h)',
      'exact_local_variational_inequality':'alpha <Omega,C_e Omega> <= beta degree(e) <= 4 beta',
      'marginal_single_holonomy':'int |grad sqrt(rho_U)|^2 <= degree(e) beta/alpha <=16/g0^4',
      'Fisher_information_bound':'int rho |grad log rho|^2 <= 4 degree(e) beta/alpha <=64/g0^4',
      'volume_independent_variance_bound':'Var_rho(trace_fundamental U)>=pi^2/[64 C_S^3 (1+16/g0^4)^3], with fixed SU2 Sobolev C_S >=1',
      'thermodynamic_conclusion':'At fixed h,g0, the local sqrt-marginals are precompact in L2 and normalized local Wilson spectral measures have subsequential weak limits with finite first moments. No uniqueness, uniform weak coupling, OS or mass gap.',
      'open_obligation':'Control the H1/marginal constants as g0(h)->0 and estimate the complete connected time-dependent Schur form',
      'cubical_geometry':cubes,'coupling_examples':bare,'independent_one_plaquette_character_regressions':rotor,
      'haar_fundamental_trace_moments':mom,
      'notes':['The 1-plaquette 2D rotor is an independent finite SU2 regression, not a 3D vacuum simulation.',
      'C_S is the fixed geometric SU(2) H1->L6 Sobolev constant. No numerical value or sharpness is asserted.',
      'No use is made of a finite-volume spectral-gap lower bound to establish the local energy estimate.']}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS 7 exact cubic edge-degree distributions, 6 SU2 one-plaquette character rotors, 35 Haar trace band checks')
    print('max single-link kinetic ratio:',max(z['ratio_to_local_bound'] for z in rotor))
    print('finite loop marginal Fisher bound independent of box E,F, but grows as g0^-4')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--out',type=Path,default=Path('docs/evidence/R3_LOCAL_WILSON_FISHER_2026-11-06.json'))
    run(p.parse_args().out)
