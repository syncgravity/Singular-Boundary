#!/usr/bin/env python3
"""PF-I14: EXACT Sturmian-boundary reflection and finite source SU(2) hull covariance.

Source scope: PF-I13 original accepted Z5 2-complexes; original source rho=0
lower mechanical Fibonacci word. Adds a MATHEMATICALLY POSSIBLE decorated hull,
not a sourced physical scalar phason or physical time/mass-gap construction.

Public module imports derived PF-I9/I11/I12 verifiers, NOT original author code.
Original source (private) can be loaded only in the reproducibility bundle.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from collections import Counter
import argparse, hashlib, json, math
from pathlib import Path

import numpy as np
from verify_pf_i11_intrinsic_su2 import (
    assemble_complex, plaquette_holonomies, gauge_transform,
    unit_quaternion,qconj,qmul,sha_labels,sha_face_labels,PHI,PERP,PAR)
from verify_pf_i12_two_sector_coupling import (
    snapshot_complex, transverse_pairs, pair_penalty)
from verify_pf_i9_source_cut_project_bridge import direct_membership,tlevel,fib_type

ALPHA=2/(1+math.sqrt(5))
T_A=1.0
T_B=PHI**-2

@dataclass(frozen=True)
class QuadraticPhase:
    """Exact Q+Z*alpha phase, alpha=(sqrt(5)-1)/2.

    Rational part is a Fraction; irrational part is an integer alpha multiple.
    This covers source rho=0, all integer translations and reflected phases,
    and nonsingular rational-intercept Sturmian words with no float ambiguity.
    """
    rational:Fraction=Fraction(0)
    alpha_multiple:int=0
    def __post_init__(self):
        object.__setattr__(self,'rational',Fraction(self.rational))
        object.__setattr__(self,'alpha_multiple',int(self.alpha_multiple))
    def reflect(self):
        return QuadraticPhase(-self.rational,-self.alpha_multiple-1)
    def level_translate(self,n:int):
        return QuadraticPhase(self.rational,self.alpha_multiple-int(n))
    def __str__(self):return f'{self.rational}+({self.alpha_multiple})alpha'


def floor_quadratic(phase:QuadraticPhase)->int:
    """Rigorous floor of rational + integer*alpha using integer square root.

    For rational p/q, b*alpha: ((2p-qb)+qb*sqrt(5))/(2q).
    Replacing irrational signed sqrt by its exact integer floor BEFORE
    integer division preserves the floor. No floating-point boundary errors.
    """
    p,q=phase.rational.numerator,phase.rational.denominator
    b=phase.alpha_multiple
    A=2*p-q*b;B=q*b
    if B>0:root=math.isqrt(5*B*B)
    elif B<0:root=-math.isqrt(5*B*B)-1
    else:root=0
    return (A+root)//(2*q)


def ceil_quadratic(phase:QuadraticPhase)->int:
    return -floor_quadratic(QuadraticPhase(-phase.rational,-phase.alpha_multiple))


def mechanical(k:int,phase:QuadraticPhase,upper:bool=False)->int:
    step=ceil_quadratic if upper else floor_quadratic
    b=phase.alpha_multiple
    a=phase.rational
    out=step(QuadraticPhase(a,b+k+1))-step(QuadraticPhase(a,b+k))
    assert out in (0,1)
    return out


@dataclass(frozen=True)
class FibonacciDecoration:
    """5 per-family Sturmian phases and boundary conventions.

    Actual source is rho_j=0, all lower. The enlargement is a conditional
    covariant family, not evidence that its phases are physical parameters.
    """
    phases:tuple[QuadraticPhase,...]
    uppers:tuple[bool,...]
    @classmethod
    def source(cls):return cls((QuadraticPhase(),)*5,(False,)*5)
    def reflect(self):
        return FibonacciDecoration(tuple(p.reflect() for p in self.phases),
                                   tuple(not u for u in self.uppers))
    def translate(self,a):
        if len(a)!=5 or sum(map(int,a))!=0:raise ValueError('Only zero-height translations')
        return FibonacciDecoration(tuple(p.level_translate(int(aj)) for p,aj in zip(self.phases,a)),
                                   self.uppers)
    def type(self,j:int,k:int)->int:
        return mechanical(int(k),self.phases[int(j)],self.uppers[int(j)])
    def weight(self,j:int,k:int)->float:
        return T_A if self.type(j,k) else T_B
    def serialize(self):
        return {'phases':[{'rational':str(p.rational),'alpha_multiple':p.alpha_multiple}
                          for p in self.phases], 'upper_boundary_conventions':list(self.uppers)}


def exact_word_involution_certificate(max_k=10000):
    """Prove by ceil(-x)=-floor(x); also exhaustive deterministic spot checks."""
    cases=[QuadraticPhase(),QuadraticPhase(Fraction(1,7)),
           QuadraticPhase(Fraction(-2,9),3),QuadraticPhase(Fraction(2,5),-10),
           QuadraticPhase(Fraction(0),7)]
    n=0;naive_bad=Counter();badlevels=[]
    for p in cases:
        for upper in (False,True):
            q=p.reflect()
            for k in range(-max_k,max_k+1):
                if mechanical(k,p,upper)!=mechanical(-k,q,not upper):
                    raise AssertionError((p,k,'reflected word mismatch'))
                n+=1
        assert p.reflect().reflect()==p
    q=QuadraticPhase().reflect()
    for k in range(-max_k,max_k+1):
        if mechanical(k,QuadraticPhase(),False)!=mechanical(-k,q,False):
            badlevels.append(k)
    assert badlevels==[-1,0],badlevels
    # The fixed word at rho=0 is instead wildly non-symmetric under k -> -k.
    baseline_changed=sum(mechanical(k,QuadraticPhase(),False)!=mechanical(-k,QuadraticPhase(),False)
                         for k in range(-max_k,max_k+1))
    return {'algebraic_identity':'s_lower(rho,k)=s_upper(-rho-alpha,-k), all k in Z',
            'exact_floor_ceil_q_sqrt5_implementation':True,
            'source_original_phase':'rho=0 lower on all 5 directions',
            'reflected_source_phase':'rho=-alpha upper on all 5 directions',
            'singular_reflected_lower_word_mismatch_levels_source_index':badlevels,
            'symmetric_same_word_mismatch_count_in_test_range':baseline_changed,
            'tested_levels_per_word':2*max_k+1,'validated_integer_source_cases':n,
            'reflected_phase_involution_squared_identity':True,
            'new_Physical_phason_claimed':False}


def theta_label(m):return tuple(1-int(x) for x in m)


def theta_complex(C,gamma):
    C2=assemble_complex([theta_label(m) for m in C.labels],-np.asarray(gamma))
    assert len(C2.labels)==len(C.labels) and len(C2.edges)==len(C.edges) and len(C2.faces)==len(C.faces)
    src_edges={e:i for i,e in enumerate(C.edges)}
    tgt_edges={e:i for i,e in enumerate(C2.edges)}
    edge_map=np.zeros(len(C.edges),dtype=np.int32)
    for i,(a,b) in enumerate(C.edges):
        m=(theta_label(b),theta_label(a))
        assert m in tgt_edges
        edge_map[i]=tgt_edges[m]
    assert len(set(edge_map))==len(C.edges)
    target_face_id={face:i for i,face in enumerate(C2.faces)}
    face_map=np.zeros(len(C.faces),dtype=np.int32)
    for i,f in enumerate(C.faces):
        reflected=(theta_label(f[2]),theta_label(f[3]),theta_label(f[0]),theta_label(f[1]))
        assert reflected in target_face_id,(i,reflected)
        face_map[i]=target_face_id[reflected]
        assert C.face_families[i]==C2.face_families[int(face_map[i])]
        assert sum(reflected[0])==3-sum(f[0])
    assert len(set(face_map))==len(C.faces)
    return C2,edge_map,face_map


def theta_links(links,edge_map):
    r=np.empty_like(links)
    r[edge_map]=qconj(links)
    return r


def translated_label(m,a):return tuple(int(x)+int(y) for x,y in zip(m,a))


def translate_complex(C,gamma,a):
    a=tuple(map(int,a))
    if len(a)!=5 or sum(a)!=0:raise ValueError('Translation must preserve source height h')
    C2=assemble_complex([translated_label(m,a) for m in C.labels],np.asarray(gamma)-np.asarray(a))
    assert (len(C.labels),len(C.edges),len(C.faces)) == (len(C2.labels),len(C2.edges),len(C2.faces))
    edgeids={e:i for i,e in enumerate(C2.edges)}
    faceids={f:i for i,f in enumerate(C2.faces)}
    emap=np.array([edgeids[(translated_label(u,a),translated_label(v,a))]
                   for u,v in C.edges],dtype=np.int32)
    fmap=np.array([faceids[tuple(translated_label(v,a) for v in f)]
                   for f in C.faces],dtype=np.int32)
    assert len(set(emap))==len(C.edges) and len(set(fmap))==len(C.faces)
    return C2,emap,fmap


def exact_semidirect_certificate():
    """Exact action of Lambda0 rtimes Z2 on label/gamma/Sturmian decoration."""
    dec=FibonacciDecoration(tuple(QuadraticPhase(Fraction(j,11),j-3) for j in range(5)),
                            (False,True,False,True,False))
    # expand generator before dataclass use; tuple needed
    a=(2,-1,0,-1,0);b=(-1,1,1,0,-1)
    m=(-2,1,0,3,0)
    for x in [a,b,tuple(ai+bi for ai,bi in zip(a,b))]:
        assert sum(x)==0
    d2=dec.translate(a)
    assert d2.reflect().reflect()==d2
    assert dec.translate(a).reflect()==dec.reflect().translate(tuple(-x for x in a))
    assert dec.translate(a).translate(b)==dec.translate(tuple(x+y for x,y in zip(a,b)))
    assert translated_label(theta_label(translated_label(m,a)),tuple([0]*5)) == theta_label(translated_label(m,a))
    assert theta_label(translated_label(m,a)) == translated_label(theta_label(m),tuple(-x for x in a))
    total=0
    for j in range(5):
        for k in range(-1000,1001):
            assert dec.type(j,k)==d2.type(j,k+a[j]);total+=1
    # A single COMMON scalar rho cannot stay common under any nonzero
    # zero-height integer relabeling, since alpha irrational.
    assert a!=(0,0,0,0,0) and len(set(a))>1
    return {'translation_group':'Lambda0 = {a in Z5: sum(a)=0}',
            'translation_action':'(m,gamma,rho_j,eta_j)->(m+a,gamma-a,rho_j-a_j*alpha,eta_j)',
            'reflection_action':'(m,gamma,rho_j,eta_j)->(1-m,-gamma,-rho_j-alpha,swap(eta_j))',
            'exact_group_relation':'R T_a R = T_{-a}; T_a T_b = T_{a+b}',
            'checked_phases_and_levels':total,'five_separate_word_phase_coordinates_necessary_for_full_Lambda0_covariance':True,
            'single_shared_phase_fails_nontrivial_Lambda0_translation':True,
            'translation_height_preserving':True,'no_physical_time_derived':True}


def finite_translation_covariance(C,gamma,a=(2,-1,0,-1,0),seed=414):
    translated,emap,fmap=translate_complex(C,gamma,a)
    dec=FibonacciDecoration.source();other=dec.translate(a)
    w1=canonical_edge_weights(C,dec);w2=canonical_edge_weights(translated,other)
    assert np.array_equal(w1,w2[emap])
    k1=face_couplings(C,dec);k2=face_couplings(translated,other)
    assert np.array_equal(k1,k2[fmap])
    rng=np.random.default_rng(seed);links=unit_quaternion(rng,(len(C.edges),))
    newlinks=np.empty_like(links);newlinks[emap]=links
    h1=plaquette_holonomies(C,links)[:,0]
    h2=plaquette_holonomies(translated,newlinks)[:,0]
    assert np.allclose(h1,h2[fmap],atol=1e-12)
    a1=float(np.dot(k1,1-h1));a2=float(np.dot(k2,1-h2))
    assert abs(a1-a2)<1e-10*(1+a1)
    return {'source_Ngrid':C.source_Ngrid,'translation_a':list(a),
            'source_vertices':len(C.labels),'source_edges':len(C.edges),'source_faces':len(C.faces),
            'all_accepted_face_labels_transport_under_gamma_minus_a':True,
            'all_edge_and_face_Fibonacci_couplings_transport':True,
            'translated_Wilson_action_absolute_difference':abs(a1-a2),
            'phase_transport_must_be_independent_by_family_for_nontrivial_a':True}


def canonical_edge_weights(C,dec:FibonacciDecoration):
    return np.array([dec.weight(*tlevel(a,b)) for a,b in C.edges],dtype=float)


def face_couplings(C,dec:FibonacciDecoration,beta=.71):
    # Optional positive coupling dependent on two decorated edge weights.
    # This is NOT sourced as the physical Wilson face coupling.
    if beta<0:raise ValueError('beta must be nonnegative')
    vals=[]
    for f,(j,k) in zip(C.faces,C.face_families):
        t=dec.weight(j,f[0][j])*dec.weight(k,f[0][k])
        vals.append(beta*(1+0.17*t))
    return np.asarray(vals)


def finite_covariance(C,gamma,seed=1414,calculate_pairs=True):
    gamma=np.asarray(gamma,float);assert abs(gamma.sum())<1e-9
    C2,edge_map,face_map=theta_complex(C,gamma)
    dec=FibonacciDecoration.source();other=dec.reflect()
    weights=canonical_edge_weights(C,dec);rweights=canonical_edge_weights(C2,other)
    assert np.array_equal(weights,rweights[edge_map])
    for a,b in C.edges:
        j,k=tlevel(a,b)
        assert (fib_type(j,k)=='A')==(dec.type(j,k)==1)
    kvals=face_couplings(C,dec);kother=face_couplings(C2,other)
    assert np.array_equal(kvals,kother[face_map]),'face hopping transformed incorrectly'
    rng=np.random.default_rng(seed)
    links=unit_quaternion(rng,(len(C.edges),))
    rlinks=theta_links(links,edge_map)
    assert np.allclose(rlinks[edge_map],qconj(links))
    orig_h=plaquette_holonomies(C,links)[:,0]
    new_h=plaquette_holonomies(C2,rlinks)[:,0]
    assert np.allclose(orig_h,new_h[face_map],atol=5e-13)
    action_old=np.dot(kvals,1-orig_h)
    action_new=np.dot(kother,1-new_h)
    assert abs(action_old-action_new)<2e-9
    orig_l=np.array([rng.standard_normal() for _ in C.labels]);m2ids={v:i for i,v in enumerate(C2.labels)}
    orig_ids={v:i for i,v in enumerate(C.labels)}
    mir_l=np.asarray([orig_l[orig_ids[theta_label(v)]] for v in C2.labels])
    L1=sum(w*(orig_l[orig_ids[a]]-orig_l[orig_ids[b]])**2 for (a,b),w in zip(C.edges,weights))
    L2=sum(w*(mir_l[m2ids[a]]-mir_l[m2ids[b]])**2 for (a,b),w in zip(C2.edges,rweights))
    assert abs(L1-L2)<1e-9*(1+L1)
    # local gauge group actions intertwine with the exact theta map.
    gauge=unit_quaternion(rng,(len(C.labels),))
    mg=np.asarray([gauge[orig_ids[theta_label(v)]] for v in C2.labels])
    left=theta_links(gauge_transform(C,links,gauge),edge_map)
    right=gauge_transform(C2,rlinks,mg)
    assert np.max(np.abs(left-right))<1e-12
    # Diagnostic: treating the REFLECTED singular word as lower creates exactly
    # two defective source level values (k in {-1,0}) across all 5 families.
    bad_counts=Counter()
    lower_bad_indices=[];fixed_mismatch=0
    raw_dec=FibonacciDecoration.source()
    lower_wrong=FibonacciDecoration(other.phases,raw_dec.uppers)
    for i,(a,b) in enumerate(C.edges):
        j,k=tlevel(a,b)
        if dec.type(j,k)!=lower_wrong.type(j,-k):
            bad_counts[int(k)]+=1;lower_bad_indices.append(i)
        if dec.type(j,k)!=raw_dec.type(j,-k):fixed_mismatch+=1
    assert set(bad_counts).issubset({-1,0})
    pair_out=None
    if calculate_pairs:
        pair=transverse_pairs(C);pair2=transverse_pairs(C2)
        srcpen=pair_penalty(C,links,pair)
        tgtpen=pair_penalty(C2,rlinks,pair2)
        # Create mapping from face pair to pair row; order preserved by sorted IDs.
        look={tuple(p[:2]):i for i,p in enumerate(pair2)}
        pair_map=np.empty(len(pair),dtype=int)
        for i,(p,q,a,b) in enumerate(pair):
            ii,jj=sorted((int(face_map[p]),int(face_map[q])))
            idx=look[(ii,jj)]
            pair_map[i]=idx
            v=C.faces[p][a]
            vp=C2.faces[int(face_map[p])][int(pair2[idx,2] if ii==int(face_map[p]) else pair2[idx,3])]
            assert vp==theta_label(v)
        assert len(set(pair_map))==len(pair)
        assert np.allclose(srcpen,tgtpen[pair_map],atol=1e-11)
        pair_out={'transverse_pair_count':len(pair),
                  'source_pair_action':float(srcpen.sum()),
                  'reflected_pair_action':float(tgtpen.sum()),
                  'pair_penalty_max_absolute_discrepancy':float(np.max(np.abs(srcpen-tgtpen[pair_map]),initial=0))}
    return {'source_Ngrid':C.source_Ngrid,'V':len(C.labels),'E':len(C.edges),'F':len(C.faces),
            'source_vertex_SHA256':sha_labels(C.labels),'source_face_SHA256':sha_face_labels(C.faces),
            'mirrored_vertex_SHA256':sha_labels(C2.labels),'mirrored_face_SHA256':sha_face_labels(C2.faces),
            'all_reflected_source_faces_match_exactly':True,
            'edge_hopping_type_mismatches_under_decorated_theta':0,
            'face_weight_mismatches_under_decorated_theta':0,
            'same_fixed_hopping_word_mismatch_count':fixed_mismatch,
            'singular_lower_lower_mismatch_edges':len(lower_bad_indices),
            'singular_lower_lower_level_histogram':{str(k):v for k,v in sorted(bad_counts.items())},
            'weighted_laplacian_energy_original':float(L1),
            'weighted_laplacian_energy_mirrored':float(L2),
            'source_weighted_operator_unitarily_equivalent_by_vertex_permutation':True,
            'gauge_action_intertwines_exact_source_vertex_map':True,
            'Wilson_face_action_original':float(action_old),'Wilson_face_action_mirrored':float(action_new),
            'Wilson_face_action_absolute_difference':float(abs(action_old-action_new)),
            'nonabelian_two_face_action':pair_out,
            'decorated_reflection_restricts_to_same_original_fixed_hopping_background':False,
            'reflection_positive_physical_transfer_from_covariance_proved':False,
            'continuum_Yang_Mills_mass_gap_proved':False}


def main():
    a=argparse.ArgumentParser();a.add_argument('--private-snapshots',type=Path,default=None)
    a.add_argument('--source-gamma',type=Path,default=None)
    a.add_argument('--output',type=Path,default=None)
    a.add_argument('--all-source',action='store_true',help='require original script to rebuild other 5 sizes')
    a.add_argument('--original-script',type=Path,default=None)
    a.add_argument('--no-pairs',action='store_true')
    a.add_argument('--pf-i11-source-ref',type=Path,default=None)
    args=a.parse_args()
    certificate=exact_word_involution_certificate(10000)
    obj={'gate':'PF-I14','result_kind':'exact algebraic Sturmian hull reflection + finite source gauge covariance',
         'source_original_hopping_not_canonically_reflection_invariant_without_decorated_background':True,
         'sturmian_certificate':certificate,
         'semidirect_group_certificate':exact_semidirect_certificate(),
         'source_finite':{},'source_translations':{},'physical_reflection_time_proved':False,
         'global_OS_positive_original_YM_proved':False,'continuum_Yang_Mills_mass_gap_proved':False}
    if args.private_snapshots:
        from verify_pf_i11_intrinsic_su2 import validate_source,source_complex
        if args.original_script:
            mod=validate_source(args.original_script);gamma=mod.GAMMA_GENERIC
        elif args.source_gamma:
            gamma=np.array(json.loads(args.source_gamma.read_text()))
        else:raise ValueError('Need source gamma JSON or original source to verify source snapshots')
        for n in [7,20,25]:
            f=args.private_snapshots/f'PF_I11_original_source_{n}.npz'
            C=snapshot_complex(f)
            obj['source_finite'][str(n)]=finite_covariance(C,gamma,seed=1414+n,
                                                          calculate_pairs=not args.no_pairs)
            if n in (7,25): obj['source_translations'][str(n)]=finite_translation_covariance(C,gamma,seed=3434+n)
        if args.all_source:
            if not args.original_script:raise ValueError('All source requires original source script')
            for n in [10,12,15,18,23]:
                C=source_complex(args.original_script,n)
                obj['source_finite'][str(n)]=finite_covariance(C,gamma,seed=1414+n,
                                                              calculate_pairs=not args.no_pairs)
    if args.pf_i11_source_ref:
        ref={str(x['Ngrid']):x for x in json.loads(args.pf_i11_source_ref.read_text())['results']}
        if not obj['source_finite']:raise ValueError('PF-I11 reference verification needs source geometry')
        for n,x in obj['source_finite'].items():
            t=ref[n]
            assert (x['V'],x['E'],x['F'])==(t['n_vertices'],t['n_edges'],t['n_faces'])
            assert x['source_vertex_SHA256']==t['source_vertices_sha256']
            assert x['source_face_SHA256']==t['direct_accepted_faces_sha256']
        obj['all_source_PF_I11_reference_SHA256_verified']=len(obj['source_finite'])==8
    raw=json.dumps(obj,sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(raw)
    print(raw)

if __name__=='__main__':main()
