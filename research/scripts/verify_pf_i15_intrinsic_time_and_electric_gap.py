#!/usr/bin/env python3
"""PF-I15 exact source graph electric spectrum, optional original source replay.

PUBLIC dependencies: Python stdlib, numpy, scipy (small local quadrature only).
PRIVATE replay: pass original author source and PF-I11 derived verifier references;
private script/snapshots are NOT embedded in this file or intended for Github.

This proves a volume-uniform PURE-ELECTRIC gap for finite source graphs,
NOT an interacting continuum Yang-Mills physical gap or a source-derived time.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.special import eval_chebyu

NGRID=[7,10,12,15,18,20,23,25]
PHI=(1+math.sqrt(5))/2
WEAK=PHI**-2
CASIMIR_FUND=3/4
SOURCE_CLOCK='source-bound h=sum_j m_j in {1,2,3,4}; C5 invariant homomorphism on Lambda0=0'


def C5_orbit(a):
    a=tuple(map(int,a))
    return [a[i:]+a[:i] for i in range(5)]


def clock_certificate():
    """Exact averaging argument: invariant character tau on Lambda0 vanishes.

    Invariant coefficients on R5 are all equal. Projection z2 imaginary is
    bounded on accepted window: it is not a globally monotone C5 clock.
    """
    vectors=[(1,-1,0,0,0),(2,0,-3,0,1),(-5,2,3,1,-1)]
    assert all(sum(a)==0 for a in vectors)
    assert all(tuple(sum(r[i] for r in C5_orbit(a)) for i in range(5))==(0,)*5
               for a in vectors)
    J=np.array([[0,-1],[1,0]])
    theta=.31
    R=np.cos(theta)*np.eye(2)+np.sin(theta)*J
    assert np.allclose(J@J,-np.eye(2))
    assert np.allclose(R.T@R,np.eye(2))
    assert not np.allclose(R,R.T)
    return {
      'invariant_scalar_linear_maps_on_R5':'tau(m)=c*sum_j m_j only',
      'Lambda0_invariant_additive_real_clock_is_zero':True,
      'proof':'5*tau(a)=tau(sum_{r=0}^4 sigma^r a)=tau(0)=0 for a in Lambda0',
      'source_accepted_heights':[1,2,3,4],
      'height_clock_bounded_on_accepted_source':True,
      'z2_perpendicular_accepted_window_bounded':True,
      'J_squared_negative_identity':True,
      'exponential_J_is_nontrivial_orthogonal_rotation_not_positive_selfadjoint_heat':True,
      'kinematic_helix_not_source_field_evolution':True,
      'source_draft_explicitly_says_no_field_dynamics':'Sharpe_Paper4_J_Operator_Hidden_Domain_Revised.tex, remark Algebraic versus dynamical content',
      'C5_clock_no_go_scope':'only invariant ADDITIVE real clocks on source Lambda0 and constant-height trival direction; nonlinear/dihedral/hull/lifted time not excluded',
      'physical_time_from_geometry_proved':False,
    }



def decorated_hull_measure_nonuniqueness():
    """Exact invariant-measure classification on the FIVE auxiliary word phases.

    This is the PF-I14 auxiliary T5 PHASE FIBER, not a physical Gibbs
    measure on original gauge fields, and not the full geometrical hull.
    T_a shifts rho -> rho-alpha*a for sum a=0, preserving s=sum rho mod1;
    R sends s -> -s-5alpha. Dense translations in each s-fiber force
    conditional Haar; R invariance only requires symmetric s marginal.
    Hence there are infinitely many invariant probabilities.
    """
    alpha=1/PHI
    s0=0.
    s1=(-s0-5*alpha)%1
    # Distinguish product Haar on T5 from invariant orbit-pair fiber Haar.
    Fourier_pair=(complex(1,0)+np.exp(2j*math.pi*s1))/2
    assert abs(Fourier_pair)>.1
    # Check the exact image of sums under R, and T_a leaves sums fixed.
    rng=np.random.default_rng(1515)
    for _ in range(30):
        rho=rng.random(5)
        a=np.array([2,-1,0,-1,0])
        shifted=(rho-alpha*a)%1
        assert abs(((float(shifted.sum())-float(rho.sum())+.5)%1)-.5)<1e-12
        reflected=(-rho-alpha)%1
        expected=(-float(rho.sum())-5*alpha)%1
        assert abs(((float(reflected.sum())-expected+.5)%1)-.5)<1e-12
    return {
      'phase_space':'T5 of five independent auxiliary Fibonacci word phases; not physical gauge configuration',
      'T_a_translation':'rho->rho-alpha a, sum(a)=0',
      'R_phase_involution':'rho->-rho-alpha 1_5',
      'conserved_translation_label':'s=sum_j rho_j (mod 1)',
      'R_action_on_label':'s->-s-5alpha (mod 1)',
      'dense_zero_sum_Kronecker_orbits_in_each_s_fiber':True,
      'invariant_measure_class':'choose any probability marginal on s symmetric under s->-s-5alpha, and use Haar conditional on each T4 sum fiber; global simultaneous lower/upper flip handled by independent symmetric flag measure',
      'example_A':'full Haar on T5 times uniform independent lower/upper flags',
      'example_A_fourier_E_exp_2pi_i_sum_rho':[0.,0.],
      'example_B':'half Haar on sum phase s=0 and half Haar on reflected sum phase s=-5alpha (mod1), with uniform independent flags',
      'example_B_fourier_E_exp_2pi_i_sum_rho':[float(Fourier_pair.real),float(Fourier_pair.imag)],
      'example_B_fourier_modulus':float(abs(Fourier_pair)),
      'two_symmetry_invariant_measures_distinct':True,
      'unique_physical_vacuum_selected':False,
      'physical_hull_invariant_probability_selected':False
    }

def spin_electric_gap(girth,epsilon=1):
    """Peter-Weyl spin-net lower bound saturated by shortest Wilson loop."""
    if epsilon<=0 or girth<3:raise ValueError('Positive scale and simple graph cycle length>=3 required')
    return CASIMIR_FUND*girth*epsilon


def weighted_gap_by_min_cycle_min_edge(weak_faces,strong_faces):
    """For source graph girth4, weak 4-face saturates lower bound 4*WEAK."""
    if weak_faces<=0 or strong_faces<=0:raise AssertionError('Need all-weak and all-strong 4-cycle witnesses')
    return {
       'uniform_epsilon_1_gap':3.0,
       'electric_epsilon_equals_source_scalar_Fibonacci_weights_gap':3*WEAK,
       'electric_epsilon_equals_inverse_scalar_Fibonacci_weights_gap':3.0,
       'source_scalar_weak_weight':WEAK,
       'source_weight_as_electric_coefficient_is_auxiliary':True,
       'exact_formula_general':'Delta_{sum_e epsilon_e C_e}=(3/4)*min_simple_cycle_sum_e epsilon_e for epsilon_e>0',
    }


def spin_network_proof():
    return {
      'Hilbert_space':'L2(SU2^E,product-Haar)^{SU2^V}',
      'operator':'H_el=sum_{e in E} epsilon_e*(-Delta_SU2)_e, epsilon_e>0',
      'edge_eigenvalues':'epsilon_e*j_e*(j_e+1), j_e in {0,1/2,1,...}',
      'gauge_constraint':'nontrivial spin at a degree-one occupied support vertex has no SU2 invariant intertwiner',
      'nontrivial_support_has_cycle':True,
      'lower_bound':'any nonzero spin network has supported simple cycle; all occupied nonzero links have Casimir >=3/4',
      'upper_witness':'fundamental j=1/2 Wilson character on minimum-weight simple cycle, all other edges j=0',
      'source_edges_connect_heights_plus_or_minus_1':True,
      'source_graph_bipartite_by_height_parity':True,
      'source_contains_verified_true_four_edge_rhombi':True,
      'source_graph_girth':4,
      'exact_uniform_pure_electric_gap':spin_electric_gap(4),
      'physical_mass_gap_proved':False,
    }


def jacobi(nchars=40,kappa=.71,epsilon=1):
    """Exact fundamental Wilson plaquette Hamiltonian in class-character basis.

    One genuine source rhombus, tree gauge fixed. Characters chi_{j=n/2}.
    4 epsilon j(j+1) electric Casimir; V=kappa(1-chi_{1/2}/2).
    SU2 fusion chi_{1/2} chi_j=chi_{j+1/2}+chi_{j-1/2}.
    """
    if nchars<3 or epsilon<=0 or kappa<0:raise ValueError('Invalid parameters')
    j=np.arange(nchars)/2
    M=np.diag(4*epsilon*j*(j+1)+kappa)
    M-=kappa/2*(np.diag(np.ones(nchars-1),1)+np.diag(np.ones(nchars-1),-1))
    return M


def independent_Haar_quadrature(nchars=6,kappa=.71,num_points=600):
    """Independent class-integral check of Jacobi potential coupling.

    Haar central measure = 2/pi sin^2(theta) dtheta, 0<=theta<=pi.
    Character chi_{n/2}(theta)=U_n(cos theta).
    """
    x,w=np.polynomial.legendre.leggauss(num_points)
    theta=(x+1)*math.pi/2
    weight=w*np.sin(theta)**2
    # 2/pi Haar factor * jacobian pi/2 -> one.
    chars=np.stack([eval_chebyu(n,np.cos(theta)) for n in range(nchars)],axis=0)
    G=(chars*weight)@chars.T
    pot=(chars*(weight*kappa*(1-np.cos(theta))))@chars.T
    expect=jacobi(nchars,kappa,1)-np.diag(np.diag(jacobi(nchars,0,1)))
    assert np.allclose(G,np.eye(nchars),atol=2e-12)
    assert np.allclose(pot,expect,atol=2e-12)
    return {'nchars':nchars,'quadrature_nodes':num_points,
            'Haar_orthogonality_max_error':float(np.max(np.abs(G-np.eye(nchars)))),
            'Wilson_potential_matrix_max_error':float(np.max(np.abs(pot-expect)))}


def interacting_one_face(kappa=.71,epsilon=1):
    lists={}
    for n in (8,12,20,40):
        vals=np.linalg.eigvalsh(jacobi(n,kappa,epsilon))
        lists[str(n)]={'vacuum_energy':float(vals[0]),'first_energy':float(vals[1]),
                       'gap':float(vals[1]-vals[0])}
    gap_lists=[x['gap'] for x in lists.values()]
    assert max(gap_lists)-min(gap_lists)<1e-9
    return {
       'model':'SU2 on one actual source rhombus: H=epsilon*sum_4 C_e + kappa*(1-halfTr U_f)',
       'character_basis_matrix':'diag(4 epsilon j(j+1)+kappa) - (kappa/2)*(nearest-character offdiagonals)',
       'kappa_auxiliary':kappa,'epsilon_auxiliary':epsilon,
       'truncation_checks':lists,
       'stable_gap_at_kappa':gap_lists[-1],
       'independent_class_Haar_integral':independent_Haar_quadrature(6,kappa),
       'continuum_YM_gap_proved':False,
    }


def mass_scale_certificate(vertices,faces,kappa=.001):
    if vertices<=0 or faces<=0:raise ValueError()
    dt=1/vertices
    # Pure-electric epsilon=1 transfer at auxiliary t=1/N.
    per_step_gap=-math.expm1(-3*dt)
    # By minmax E1>=3; Haar constant trial E0<=sum_f kappa=F*kappa.
    # This lower bound on INTERACTING gap is nonuniform and often vacuous.
    candidate=3-faces*kappa
    return {'N_vertices':vertices,'N_faces':faces,'auxiliary_heat_t_equals_1_over_N':dt,
            'pure_electric_lambda_1_equals_exp_negative_3t':math.exp(-3*dt),
            'pure_electric_per_step_transfer_gap_1_minus_lambda1':per_step_gap,
            'pure_electric_energy_gap_dividing_by_assumed_step':3.,
            'finite_interacting_minmax_lower_bound_3_minus_kappa_F':candidate,
            'nonnegative_interacting_gap_lower_bound_from_this_test':max(candidate,0.),
            'kappa_auxiliary_fixed_per_face':kappa,
            'bound_is_uniform_in_unbounded_F':False,
            'physical_energy_unit_derived':False}


def source_finite_replay(source_script,source_reference):
    # Imports are lazy so that public-only tests do not require unpublished code.
    from verify_pf_i11_intrinsic_su2 import source_complex,sha_labels,sha_face_labels
    from verify_pf_i14_decorated_hull import FibonacciDecoration
    evidence=json.loads(Path(source_reference).read_text())
    refs={r['Ngrid']:r for r in evidence['results']}
    dec=FibonacciDecoration.source()
    results=[]
    for n in NGRID:
        c=source_complex(source_script,n);ref=refs[n]
        assert sha_labels(c.labels)==ref['source_vertices_sha256']
        assert sha_face_labels(c.faces)==ref['direct_accepted_faces_sha256']
        assert (len(c.labels),len(c.edges),len(c.faces))==(ref['n_vertices'],ref['n_edges'],ref['n_faces'])
        assert all(sum(b)-sum(a)==1 for a,b in c.edges)
        assert all(1<=sum(v)<=4 for v in c.labels)
        # Source edges are unique, no loops or parallel pairs.
        assert len(c.edges)==len(set(c.edges)) and all(a!=b for a,b in c.edges)
        # Every source rhombus is a distinct four-cycle, the simplest cycle.
        assert len(c.faces)>0 and all(len(set(f))==4 for f in c.faces)
        weak=strong=0
        for i,(j,k) in enumerate(c.face_families):
            base=c.faces[i][0]
            bits=(dec.type(j,base[j]),dec.type(k,base[k]))
            weak += (bits==(0,0))
            strong += (bits==(1,1))
        assert weak>0 and strong>0
        from_weights=weighted_gap_by_min_cycle_min_edge(weak,strong)
        heights={str(h):n for h,n in sorted(Counter(map(sum,c.labels)).items())}
        item={'Ngrid':n,'source_vertices':len(c.labels),'source_edges':len(c.edges),
              'source_plaquettes':len(c.faces),'source_vertex_sha256':sha_labels(c.labels),
              'source_faces_sha256':sha_face_labels(c.faces),
              'height_histogram':heights,'bipartite_parity_rule_verified':True,
              'girth_exact':4,'all_weak_four_edge_rhombi':int(weak),
              'all_strong_four_edge_rhombi':int(strong),
              **from_weights,
              'extensive_interaction_bound_example':mass_scale_certificate(len(c.labels),len(c.faces))}
        results.append(item)
    assert len(results)==8
    return {'source_script_sha256':hashlib.sha256(Path(source_script).read_bytes()).hexdigest(),
            'verified_PF_I11_source_geometry':True,
            'source_data_kind':'original retained Z5 cut-project graph, no substituted cubic/periodic geometry',
            'results':results,'physical_mass_gap_proved':False}


def report(source_script=None,source_ref=None):
    out={'checkpoint':'PF-I15','status':'exact finite electric theorem + physical time nonselection and illustrative nonzero-plaquette quantum control; NOT continuum proof',
         'source_reference':'unpublished March 2026 dissertation and J paper: kinematic helix explicitly not a field equation',
         'C5_additive_clock':clock_certificate(),
         'auxiliary_decorated_hull_measure_nonuniqueness':decorated_hull_measure_nonuniqueness(),
         'exact_electric_spin_network_gap':spin_network_proof(),
         'finite_one_rhombus_interacting_quantum_control':interacting_one_face(),
         'no_physical_YM_gap_proved':True}
    if source_script or source_ref:
        if not source_script or not source_ref:raise ValueError('Both private source script and PF-I11 reference required')
        out['original_source_8size_replay']=source_finite_replay(source_script,source_ref)
    return out


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source-script',type=Path,default=None)
    p.add_argument('--source-ref',type=Path,default=None)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    payload=report(a.source_script,a.source_ref)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'output':str(a.output),'sizes':len(payload.get('original_source_8size_replay',{}).get('results',[])),
                      'electric_gap':payload['exact_electric_spin_network_gap']['exact_uniform_pure_electric_gap'],
                      'interacting_one_plaquette_gap':payload['finite_one_rhombus_interacting_quantum_control']['stable_gap_at_kappa']},indent=2))
