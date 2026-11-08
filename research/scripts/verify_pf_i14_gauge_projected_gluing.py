#!/usr/bin/env python3
"""PF-I14: a CONDITIONAL finite source-link gauge-projected heat seam.

Proof object is P M_w (tensor_e H_te) M_w P on the actual source link
configuration space, where P is the local SU2 gauge projector. No claim
that its heat scale, duplicated phason fibers, or evolution is physical.
"""
from __future__ import annotations
import json, argparse
from pathlib import Path
import numpy as np
from verify_pf_i11_intrinsic_su2 import (
    qmul,qconj,unit_quaternion,q_identity,sha_labels,sha_face_labels)
from verify_pf_i12_two_sector_coupling import (
    transverse_pairs,holonomies_at_basepoint,pair_penalty,snapshot_complex)
from verify_pf_i12_conditional_heat_gluing import su2_heat_character_kernel


def heat_gram(U,t):
    """Exact central SU2 heat-link product Gram for finite sampled configurations.

    On L²(G^E), H=⊗_e e^{-t Δ_SU2}≥0 by Peter-Weyl; here finite Gram check.
    """
    n,e=U.shape[:2]
    out=np.ones((n,n))
    for k in range(e):
        a=U[:,None,k,:];b=U[None,:,k,:]
        rel=qmul(a,qconj(b))[...,0]
        out*=su2_heat_character_kernel(rel,t,nmax=38)
    assert np.allclose(out,out.T,atol=1e-8,rtol=1e-12)
    return out


def local_pair_link_model(C,seed=1415,beta=.3,lam=.4,t=.85,nconfigs=10,gauge_samples=9):
    pairs=transverse_pairs(C)
    assert len(pairs)>0
    first=pairs[0]
    p,q,a,b=map(int,first)
    assert len(set(C.face_families[p]+C.face_families[q]))==4
    assert C.faces[p][a]==C.faces[q][b]
    faceids=[p,q]
    edgeids=sorted(set(C.face_edges[[p,q],:].reshape(-1).tolist()))
    vertices=sorted(set(v for i in faceids for v in C.faces[i]))
    vids={v:i for i,v in enumerate(vertices)}
    tails=np.array([vids[C.edges[e][0]] for e in edgeids],dtype=int)
    heads=np.array([vids[C.edges[e][1]] for e in edgeids],dtype=int)
    rng=np.random.default_rng(seed)
    U=unit_quaternion(rng,(nconfigs,len(edgeids)))
    weights=np.zeros(nconfigs)
    # Compute source ACTUAL based face holonomies / nonabelian commutator.
    for i in range(nconfigs):
        full=q_identity(len(C.edges));full[edgeids]=U[i]
        h1=holonomies_at_basepoint(C,full,np.array([p]),np.array([a]))[0,0]
        h2=holonomies_at_basepoint(C,full,np.array([q]),np.array([b]))[0,0]
        penalty=float(pair_penalty(C,full,np.asarray([first],dtype=int))[0])
        S=beta*(2-h1-h2)+lam*penalty
        weights[i]=np.exp(-S)
    gram=heat_gram(U,t)
    weighted=weights[:,None]*gram*weights[None,:]
    eig=np.linalg.eigvalsh(weighted)
    assert eig.min()>-1e-9
    # Gauge-average a Gram over source-vertex group elements on BOTH sides.
    # Finite averaging produces PSD exactly (via mean feature embeddings).
    gauges=unit_quaternion(rng,(gauge_samples,len(vertices)))
    samples=np.empty((nconfigs*gauge_samples,len(edgeids),4))
    for i in range(nconfigs):
        for r in range(gauge_samples):
            samples[i*gauge_samples+r]=qmul(qmul(gauges[r,tails],U[i]),qconj(gauges[r,heads]))
    fullgram=heat_gram(samples,t)
    grp=fullgram.reshape(nconfigs,gauge_samples,nconfigs,gauge_samples).mean(axis=(1,3))
    grp=(weights[:,None]*grp)*weights[None,:]
    proj_eigs=np.linalg.eigvalsh(grp)
    assert proj_eigs.min()>-1e-9
    # A matched-seam link heat kernel is invariant under SAME vertex gauge
    # on both halves; it is not invariant under unrelated half transformations.
    identity=q_identity(len(edgeids))
    g=unit_quaternion(rng,(len(vertices),))
    transformed=qmul(g[tails],qconj(g[heads]))
    one=heat_gram(np.stack([identity,identity]),t)[0,1]
    mismatch=heat_gram(np.stack([identity,transformed]),t)[0,1]
    assert abs(one-mismatch)>1e-4
    # Exact full graph result uses projection P, not this finite random sample.
    return {'source_Ngrid':C.source_Ngrid,
       'source_vertex_sha256':sha_labels(C.labels),'source_face_sha256':sha_face_labels(C.faces),
       'local_pair_face_families':[list(C.face_families[p]),list(C.face_families[q])],
       'local_pair_source_face_indices':[p,q],
       'actual_source_link_variables':len(edgeids),'actual_source_vertices_in_local_patch':len(vertices),
       'sample_configs':nconfigs,'gauge_projector_Monte_Carlo_samples':gauge_samples,
       't_auxiliary':t,'beta_auxiliary':beta,'lambda_auxiliary':lam,
       'unprojected_weighted_link_heat_Gram_min_eigen':float(eig.min()),
       'two_sided_finite_gauge_averaged_heat_Gram_min_eigen':float(proj_eigs.min()),
       'unprojected_link_heat_seam_independent_gauge_change_detected':True,
       'difference_under_independent_half_gauge':float(abs(one-mismatch)),
       'global_analytic_gauge_projection':'T=P_G M_w (tensor_e H_t_e) M_w P_G is PSD, compact for finite E; P_G projects SU2^V local gauge invariants',
       'finite_auxiliary_simple_top_eigen_analytic_condition':'strictly positive heat kernel, w>0, compact operator => simple isolated Perron eigenvalue on gauge invariant sector; NOT uniform or physical mass gap',
       'global_original_source_OS_positive_proved':False,
       'source_physical_t_derived':False,
       'physical_continuum_gap_proved':False}


def main():
    p=argparse.ArgumentParser();p.add_argument('--snapshot',type=Path,default=None)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--num-configs',type=int,default=10)
    a=p.parse_args()
    if not a.snapshot:raise ValueError('Pass source snapshot for source-geometry test; use toy geometry through module API')
    C=snapshot_complex(a.snapshot)
    data=local_pair_link_model(C,nconfigs=a.num_configs)
    a.output.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(json.dumps(data,indent=2,sort_keys=True))
if __name__=='__main__':main()
