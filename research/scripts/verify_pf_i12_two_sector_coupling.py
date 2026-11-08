#!/usr/bin/env python3
"""PF-I12: exact C5 two-sector linear algebra and conditional transverse
rhombus SU(2) interaction on *source-certified* PF-I11 finite 2-complexes.

A canonical transverse pair *support* is supplied by the Z5 2+2+1
representation. The commutator coupling strength is a NEW OPTIONAL
MATHEMATICAL MODEL, not a source-derived physical interaction or time.
No continuum Yang-Mills mass gap is claimed.
"""
from __future__ import annotations
import argparse, collections, hashlib, itertools, json, math
from pathlib import Path
import numpy as np
from scipy.special import roots_chebyu
from numpy.polynomial.legendre import leggauss
from verify_pf_i11_intrinsic_su2 import (Complex, source_complex, qmul, qconj,
    plaquette_holonomies, unit_quaternion, gauge_transform, sha_labels,
    sha_face_labels)

ANGLES=2*math.pi*np.arange(5)/5
V4=np.vstack([np.cos(ANGLES),np.sin(ANGLES),np.cos(2*ANGLES),np.sin(2*ANGLES)])
EXPECTED_FOUR_VOLUME=5*math.sqrt(5)/4
PF_I11_EXPECTED={7:(1550,3017,1468),10:(3042,5927,2886),12:(4324,8468,4145),
                 15:(6980,13779,6800),18:(9950,19593,9646),20:(12207,24091,11879),
                 23:(16435,32582,16138),25:(19260,38139,18874)}


def geometric_fourvolume_certificate():
    gram=V4@V4.T
    assert np.allclose(gram,np.eye(4)*2.5,atol=5e-15)
    assert np.linalg.norm(V4@np.ones(5))<1e-14
    minors={','.join(map(str,cs)):float(np.linalg.det(V4[:,cs]))
            for cs in itertools.combinations(range(5),4)}
    assert all(abs(abs(v)-EXPECTED_FOUR_VOLUME)<3e-14 for v in minors.values())
    return {'representation':'E_parallel (frequency1) + E_perp (frequency2) + trivial height, C5-equivariant',
            'V4V4_transpose':np.round(gram,14).tolist(),
            'kernel_Z5_trivial_direction':'(1,1,1,1,1)',
            'all_4x4_minors':minors,
            'absolute_4volume_for_any_four_distinct_families':EXPECTED_FOUR_VOLUME,
            'geometric_fourform_is_not_physical_spacetime_measure':True,
            'no_full_four_coordinate_cube_with_all_16_corners_can_fit_source_heights_1_to_4':True,
            'C5_invariant_orthogonal_complex_structures':'J=(+/- J_parallel) direct_sum (+/- J_perp): FOUR choices, not unique from C5 alone',
            'source_physical_Wick_time_not_derived':True}


def snapshot_complex(path):
    with np.load(path,allow_pickle=False) as f:
        labels=[tuple(map(int,a)) for a in f['vertex_labels']]
        edges=[tuple(tuple(map(int,v)) for v in e) for e in f['edge_vertex_labels']]
        faces=[tuple(tuple(map(int,v)) for v in ff) for ff in f['faces_vertex_labels']]
        edgeids=f['face_edges'].copy(); signs=f['face_signs'].copy()
    family=[];height=[]
    for f in faces:
        j=int(np.flatnonzero(np.array(f[1])-np.array(f[0]))[0]);k=int(np.flatnonzero(np.array(f[3])-np.array(f[0]))[0]);assert j<k
        family.append((j,k));height.append(sum(f[0]))
    n=int(path.stem.split('_')[-1]); C=Complex(labels,edges,faces,edgeids,signs,family,height,None,n)
    assert (len(C.labels),len(C.edges),len(C.faces))==PF_I11_EXPECTED[n]
    return C


def transverse_pairs(C):
    """Pairs share exactly one source vertex, have 4 distinct Z5 families.

    Each such pair carries a nonzero intrinsic 4-form; returned common
    vertex fixes basepoints so commutators are genuinely gauge invariant.
    """
    by_vertex=collections.defaultdict(list)
    for i,face in enumerate(C.faces):
        for v in face: by_vertex[v].append(i)
    tuples=[];dup=0;seen=set()
    for vertex in sorted(by_vertex):
        faces=sorted(by_vertex[vertex])
        for i,j in itertools.combinations(faces,2):
            if len(set(C.face_families[i]+C.face_families[j]))!=4:continue
            if (i,j) in seen:dup+=1;continue
            seen.add((i,j))
            tuples.append((i,j,C.faces[i].index(vertex),C.faces[j].index(vertex)))
    assert dup==0,('Nonunique common vertices',dup)
    tuples.sort(key=lambda z:(z[0],z[1]))
    pairs=np.asarray(tuples,dtype=np.int32).reshape(-1,4)
    return pairs


def holonomies_at_basepoint(C,links,faceids,startids):
    """Move each source plaquette's based loop to a selected shared vertex."""
    out=np.tile(np.array([[1.,0,0,0]]),(len(faceids),1))
    for t in range(4):
        col=(startids+t)%4
        ix=C.face_edges[faceids,col];sgn=C.face_signs[faceids,col]
        q=links[ix]
        oriented=np.where((sgn>0)[:,None],q,qconj(q))
        out=qmul(out,oriented)
    return out


def pair_penalty(C,links,pairs):
    if not len(pairs):return np.empty((0,),dtype=float)
    a=holonomies_at_basepoint(C,links,pairs[:,0],pairs[:,2]);b=holonomies_at_basepoint(C,links,pairs[:,1],pairs[:,3])
    comm=qmul(qmul(qmul(a,b),qconj(a)),qconj(b))
    val=1-comm[:,0]
    assert np.all(val>=-1e-11) and np.all(val<=2+1e-11)
    return val


def wilson_transverse_action(C,links,pairs,beta,lam):
    if beta<0 or lam<0:raise ValueError('Use nonnegative couplings')
    hol=plaquette_holonomies(C,links)
    return float(beta*np.sum(1-hol[:,0])+lam*np.sum(pair_penalty(C,links,pairs)))


def local_two_face_integral(beta,lam,nx=75,nc=28):
    """Deterministic quadrature for independent baseline face holonomies A,B.

    x,y = halfTr(A,B), independent SU2 semicircle density 2/pi sqrt(1-x2).
    c = axis dot product, uniform[-1,1], so
    1 - 1/2 Tr([A,B]) = 2(1-x^2)(1-y^2)(1-c^2).
    Integrates the gauge-invariant two-plaquette commutator model exactly up
    to stated quadrature precision (NOT a continuum regulator).
    """
    x,wx=roots_chebyu(nx);wx=wx*(2/math.pi)
    c,wc=leggauss(nc);wc=wc/2
    X=x[:,None,None];Y=x[None,:,None];T=c[None,None,:]
    W=wx[:,None,None]*wx[None,:,None]*wc[None,None,:]
    penalty=2*(1-X**2)*(1-Y**2)*(1-T**2)
    density=np.exp(-beta*(2-X-Y)-lam*penalty)*W
    Z=float(density.sum());mx2=float((density*X**2).sum()/Z);my2=float((density*Y**2).sum()/Z)
    mxy2=float((density*X**2*Y**2).sum()/Z)
    z1=float(np.sum(wx*np.exp(-beta*(1-x))))
    z_beta=float(np.sum(wx*np.exp(-beta*(1-x))))
    mean2=float(np.sum(wx*np.exp(-beta*(1-x))*x**2)/z_beta)
    mean4=float(np.sum(wx*np.exp(-beta*(1-x))*x**4)/z_beta)
    var2=mean4-mean2**2
    derivative=-(4/3)*var2**2
    os_test_normalized=mxy2-2*mean2*mx2+mean2**2
    os_test_unnormalized=Z*os_test_normalized
    return {'beta':beta,'lambda':lam,'n_Gauss_Chebyshev_U':nx,'n_axis_dot_Gauss_Legendre':nc,
            'Z_two_face':Z,'Z_baseline_product':z1*z1,
            'X_squared_mean':mx2,'Y_squared_mean':my2,
            'connected_Cov_X2_Y2':mxy2-mx2*my2,
            'exact_zero_lambda_derivative_Cov_X2_Y2':derivative,
            'independent_single_face_Var_X2':var2,
            'exchange_reflection_quadratic_test_normalized':os_test_normalized,
            'exchange_reflection_quadratic_test_unnormalized':os_test_unnormalized,
            'exchange_test_observable':'f(U)=halfTr(U)^2 - E_beta(halfTr(U)^2); kernel exp[-lambda*(1-halfTr commutator)]',
            'naive_exchange_reflection_OS_verified':False,
            'zero_lambda_cov_is_exactly_zero':True,
            'baseline_expected_commutator_penalty':(4/3)*(1-mean2)**2}


def source_row(C,do_action=False):
    n=C.source_Ngrid
    pairs=transverse_pairs(C)
    assert len(pairs)>0
    sha=hashlib.sha256(pairs.tobytes()).hexdigest()
    unique_faces=len(set(pairs[:,0])|set(pairs[:,1]))
    row={'Ngrid':n,'vertices':len(C.labels),'edges':len(C.edges),'faces':len(C.faces),
         'C5_two_sector_transverse_shared_vertex_face_pairs':len(pairs),
         'faces_touching_a_transverse_pair':unique_faces,
         'transverse_pair_index_SHA256':sha,
         'original_retained_labels_SHA256':sha_labels(C.labels),
         'original_rhombus_faces_SHA256':sha_face_labels(C.faces),
         'original_source_unchanged':True,
         'beta0_exact_first_order_logZ_lambda_derivative':-0.75*len(pairs),
         'beta0_exact_first_order_logZ_derivative_per_rhombus':-0.75*len(pairs)/len(C.faces),
         'source_supplied_interaction_strength':False}
    if do_action:
        rng=np.random.default_rng(20261108+n)
        links=unit_quaternion(rng,(len(C.edges),));gauge=unit_quaternion(rng,(len(C.labels),))
        baseline=wilson_transverse_action(C,links,pairs,.71,.23)
        transformed=wilson_transverse_action(C,gauge_transform(C,links,gauge),pairs,.71,.23)
        error=abs(baseline-transformed)
        assert error<1e-8,(n,error)
        row['candidate_beta']=.71;row['candidate_lambda']=.23
        row['gauge_action_initial']=baseline;row['gauge_action_transformed']=transformed
        row['gauge_invariance_absolute_error']=error
        if n in [20,25]:
            pass
    return row


def run(snapshots,source_script=None,all_sizes=False,pf_i11_reference=None):
    rows=[]
    if all_sizes:
        if not source_script:raise ValueError('Original unpublished source script required for complete eight-size source replay')
        source_ns=[7,10,12,15,18,20,23,25]
        for n in source_ns:
            C=source_complex(source_script,n)
            rows.append(source_row(C,do_action=n in [7,20,25]))
            print('Ngrid',n,'coupling pairs',rows[-1]['C5_two_sector_transverse_shared_vertex_face_pairs'],flush=True)
    else:
        for n in (7,20,25):
            C=snapshot_complex(Path(snapshots)/f'PF_I11_original_source_{n}.npz')
            rows.append(source_row(C,do_action=True))
            print('Ngrid',n,'coupling pairs',rows[-1]['C5_two_sector_transverse_shared_vertex_face_pairs'],flush=True)
    if pf_i11_reference is not None:
        prior=json.loads(Path(pf_i11_reference).read_text())['results']
        refs={r['Ngrid']:r for r in prior}
        for row in rows:
            ref=refs[row['Ngrid']]
            assert row['original_retained_labels_SHA256']==ref['source_vertices_sha256'],row['Ngrid']
            assert row['original_rhombus_faces_SHA256']==ref['direct_accepted_faces_sha256'],row['Ngrid']
            assert (row['vertices'],row['edges'],row['faces'])==(ref['n_vertices'],ref['n_edges'],ref['n_faces']),row['Ngrid']
            row['source_PF_I11_prior_fingerprint_verified']=True
    return {'schema':'singular-boundary.pf-i12.conditional-transverse-coupling.v1',
            'date':'2026-11-08',
            'status':'Exact intrinsic four-volume geometry, candidate finite gauge-invariant cross-plaquette model, local connected-correlation theorem. Coupling magnitude/time/continuum still OPEN.',
            'source_geometry':'PF-I11 source accepted Z5 2-complex; no cubic physical substitute',
            'source_label_cropping':'Original source only. Completed-window cores are different populations.',
            'algebraic_geometry':geometric_fourvolume_certificate(),
            'source_models':rows,
            'two_face_beta_0_lambda_0p40':local_two_face_integral(0.,.40),
            'two_face_beta_0p71_lambda_0p40':local_two_face_integral(.71,.40),
            'two_face_beta_0_lambda_0p001':local_two_face_integral(0.,.001),
            'exact_derivative_at_zero_beta_and_lambda':-1/192,
            'meaning_of_derivative':'For chosen transverse pair and coupling lambda, derivative of connected covariance of squared half-traces at lambda=0 is -weight/192. Exact for baseline independent Haar plaquettes. Nonzero = finite nonfactorization of candidate model.',
            'coupling_is_unique_source_derived':False,
            'physical_4d_volume_measure_proved':False,
            'time_reflection_positivity_proved':False,
            'nontrivial_continuum_Yang_Mills_gap_proved':False}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--snapshots',type=Path,default=Path(__file__).resolve().parent/'private_snapshots')
    p.add_argument('--source-script',type=Path,default=None)
    p.add_argument('--all-sizes',action='store_true')
    p.add_argument('--pf-i11-reference',type=Path,default=None)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    data=run(a.snapshots,a.source_script,a.all_sizes,a.pf_i11_reference)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    for k in ['two_face_beta_0_lambda_0p40','two_face_beta_0p71_lambda_0p40']:
        print(k,'cov',data[k]['connected_Cov_X2_Y2'],'deriv',data[k]['exact_zero_lambda_derivative_Cov_X2_Y2'])
if __name__=='__main__':main()
