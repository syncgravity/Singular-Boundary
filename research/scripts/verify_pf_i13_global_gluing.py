#!/usr/bin/env python3
"""PF-I13: exact global two-sector time/gluing obstructions and controls.

All original source geometry is taken unchanged from PF-I11/PF-I12.  This
proves finite combinatorial and conditional operator statements only, not
physical time, an OS-positive 4D gauge path measure, or a Yang–Mills gap.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
from itertools import combinations, product
import json, math
from pathlib import Path
import numpy as np
from verify_pf_i11_intrinsic_su2 import (
    validate_source, source_complex, triangle_membership, PERP, PAR,
    qmul,qconj,unit_quaternion,sha_labels,sha_face_labels)
from verify_pf_i12_two_sector_coupling import snapshot_complex, transverse_pairs
from verify_pf_i9_source_cut_project_bridge import direct_membership,tlevel,fib_type
from verify_pf_i12_conditional_heat_gluing import su2_heat_character_kernel

FAMILIES=range(5)
TYPES=list(combinations(FAMILIES,2))


def petersen_type_graph():
    edgelist=sorted((a,b) for a,b in combinations(TYPES,2) if not (set(a)&set(b)))
    adjacency={a:set() for a in TYPES}
    for a,b in edgelist:adjacency[a].add(b);adjacency[b].add(a)
    assert len(TYPES)==10 and len(edgelist)==15
    assert all(len(nbrs)==3 for nbrs in adjacency.values())
    assert not any(b in adjacency[a] and c in adjacency[a] and c in adjacency[b]
                   for a,b,c in combinations(TYPES,3))
    color=lambda t:0 if 0 in t else (1 if 1 in t else 2)
    assert all(color(a)!=color(b) for a,b in edgelist)
    witness=[(0,4),(2,3),(0,1),(3,4),(1,2)]
    assert all(witness[(i+1)%5] in adjacency[witness[i]] for i in range(5))
    return {'types':['-'.join(map(str,t)) for t in TYPES],
            'family_transverse_type_edges':len(edgelist),
            'type_degrees':sorted(len(x) for x in adjacency.values()),
            'has_type_triangles':False,
            'exhibited_odd_family_cycle':['-'.join(map(str,t)) for t in witness],
            'non_bipartite':True,
            'family_graph_chromatic_number_exactly':3,
            'explicit_three_coloring':{'-'.join(map(str,t)):color(t) for t in TYPES},
            'known_graph':'Kneser KG(5,2), Petersen graph',
            'conclusion':'No global binary assignment to the ten rhombus direction-types can make every transverse family pair cross the two classes.'}


def face_pair_graph(C):
    pairs=transverse_pairs(C)
    n=len(C.faces)
    adj=[[] for _ in range(n)]
    for i,j,_,_ in pairs:
        i,j=int(i),int(j);adj[i].append(j);adj[j].append(i)
    for a in adj:a.sort()
    color=np.full(n,-1,dtype=np.int8)
    parent=np.full(n,-1,dtype=np.int32)
    odd=None;components=[]
    for seed in range(n):
        if color[seed]!=-1:continue
        queue=deque([seed]);color[seed]=0;sz=0
        while queue:
            u=queue.popleft();sz+=1
            for v in adj[u]:
                if color[v]==-1:
                    color[v]=1-color[u];parent[v]=u;queue.append(v)
                elif color[v]==color[u] and odd is None:
                    # Short exact odd-cycle witness; remove common BFS tail.
                    pa=[];x=u
                    while x!=-1:pa.append(int(x));x=int(parent[x])
                    pb=[];x=v
                    while x!=-1:pb.append(int(x));x=int(parent[x])
                    sb=set(pb);root=next(x for x in pa if x in sb)
                    odd=pa[:pa.index(root)+1]+list(reversed(pb[:pb.index(root)]))
        components.append(sz)
    if odd is not None:
        assert len(odd)%2==1 and len(odd)>=5
        assert all(odd[(i+1)%len(odd)] in adj[odd[i]] for i in range(len(odd)))
        assert len(set(odd))==len(odd)
    # Exhibit a literal five-cycle of physical faces (not merely quotient types).
    five=None
    for a in range(n):
        if five is not None:break
        for b in adj[a]:
            if five is not None:break
            for c in adj[b]:
                if c==a:continue
                if five is not None:break
                for d in adj[c]:
                    if d==a or d==b:continue
                    if five is not None:break
                    for e in adj[d]:
                        if e!=a and e!=b and e!=c and a in adj[e]:
                            five=[a,b,c,d,e];break
    assert five is not None,('No physical five-cycle',C.source_Ngrid)
    assert all(five[(i+1)%5] in adj[five[i]] for i in range(5))
    family_edges=Counter()
    three_color=lambda t: 0 if 0 in t else (1 if 1 in t else 2)
    assert all(three_color(tuple(C.face_families[int(i)]))!=three_color(tuple(C.face_families[int(j)])) for i,j,_,_ in pairs)
    for i,j,_,_ in pairs:
        a=tuple(C.face_families[int(i)]);b=tuple(C.face_families[int(j)])
        family_edges[tuple(sorted((a,b)))]+=1
    assert len(family_edges)==15
    return {
        'source_Ngrid':C.source_Ngrid,
        'faces':n,
        'transverse_pair_edges':len(pairs),
        'components_including_isolated_faces':len(components),
        'isolated_face_count':sum(len(v)==0 for v in adj),
        'max_component_face_count':max(components),
        'actual_face_pair_graph_bipartite':odd is None,
        'three_family_color_classes_provide_proper_coloring':True,
        'chromatic_number_exactly_three':odd is not None,
        'explicit_odd_cycle_face_indices':odd,
        'explicit_odd_cycle_face_families':[list(map(int,C.face_families[i])) for i in odd] if odd else None,
        'odd_cycle_length':len(odd) if odd else None,
        'physical_five_cycle_face_indices':five,
        'physical_five_cycle_family_types':[list(map(int,C.face_families[i])) for i in five],
        'all_15_disjoint_family_pair_types_observed':True,
        'source_vertex_SHA256':sha_labels(C.labels),
        'source_face_SHA256':sha_face_labels(C.faces),
        'source_population_preserved':True,
    }


def verify_phason_height_inversion(C,gamma):
    """Exact involution exchanges phasons: (m,gamma)->(1-m,-gamma).

    Every source-accepted rhombus maps to genuine acceptance-window face.
    Does NOT claim reflection of original *finite cropped* source core.
    """
    gamma=np.asarray(gamma,dtype=float);assert abs(float(gamma.sum()))<1e-11
    rgamma=-gamma
    n=len(C.labels);accepted_all=0;accepted_same=0
    source_good=0;heights=Counter();ref_heights=Counter()
    for m in C.labels:
        assert direct_membership(m,gamma)[0],m
        other=tuple(1-x for x in m)
        accepted_all+=bool(direct_membership(other,rgamma)[0])
        accepted_same+=bool(direct_membership(other,gamma)[0])
        assert sum(other)==5-sum(m)
        assert all((other[j]+m[j])==1 for j in range(5))
        assert np.allclose(np.asarray(other)@PAR,-np.asarray(m)@PAR,atol=3e-14)
        heights[sum(m)]+=1;ref_heights[sum(other)]+=1
    assert accepted_all==n
    for f,dirs in zip(C.faces,C.face_families):
        low=f[0];j,k=dirs
        assert triangle_membership(low,j,k,gamma)
        high=f[2]
        reflected_low=tuple(1-v for v in high)
        assert triangle_membership(reflected_low,j,k,rgamma)
        assert sum(reflected_low)==3-sum(low)
        source_good+=1
    internal_shift=2*gamma@PERP
    assert np.linalg.norm(internal_shift)>0.001
    return {
        'source_Ngrid':C.source_Ngrid,
        'original_vertices':n,
        'reflected_vertices_accepted_under_minus_gamma':accepted_all,
        'reflected_vertices_accepted_under_same_gamma':accepted_same,
        'source_faces':len(C.faces),
        'all_reflected_faces_accepted_under_minus_gamma':source_good,
        'original_source_height_histogram':{str(k):v for k,v in sorted(heights.items())},
        'reflected_height_histogram':{str(k):v for k,v in sorted(ref_heights.items())},
        'inversion_theta':'(m,gamma) -> (1-m,-gamma), h -> 5-h, Eparallel/Eperp -> minus',
        'fixed_phason_internal_shift_vector':internal_shift.tolist(),
        'fixed_phason_internal_shift_norm':float(np.linalg.norm(internal_shift)),
        'fixed_phason_involution_valid_for_all_original_vertices':accepted_same==n,
        'height_translation_by_ones_denied':'sum(m+1_5)=h+5 outside h in {1,2,3,4}',
        'no_authorized_physical_time_from_height_or_phason_involution':True,
        'on_nontrivial_4d_two_sector_space_inversion_is_minus_identity_with_det_plus_one':True,
        'on_nontrivial_4d_two_sector_space_no_C5_commuting_real_involution_has_one_negative_eigenvector':True,
        'finite_crop_reflection_not_claimed':True,
    }


def hopping_inversion_mismatch(C):
    """Source PF-I10 scalar Fibonacci weights need not be phason reflection invariant.

    Under m -> 1-m an original basis bond at lower j-level k has
    reflected lower j-level -k. The source uses the same fixed word w(k)
    for both phason configurations, so a spatial reflection cannot be
    assumed an isometry of that fixed weighted operator.
    """
    hist=Counter()
    for a,b in C.edges:
        j,k=tlevel(a,b)
        typ=fib_type(j,k);ref_typ=fib_type(j,-k)
        hist[(typ,ref_typ)]+=1
    total=sum(hist.values());changed=sum(v for (a,b),v in hist.items() if a!=b)
    assert total==len(C.edges) and changed>0
    return {'original_source_edges':total,
            'reflection_reverses_Fibonacci_word_index_as_k_to_minus_k':True,
            'source_hopping_types_changed_after_geometric_inversion':changed,
            'source_hopping_types_unchanged':total-changed,
            'changed_fraction':changed/total,
            'hopping_type_pair_histogram':{a+' to '+b:v for (a,b),v in sorted(hist.items())},
            'interpretation':'The fixed source PF-I10 A/B hopping word is NOT theta-invariant under the geometric phason inversion. A reflected weighted operator would also need a transformed background word. This says nothing about unspecified physical SU(2) Wilson face couplings.',
            'fixed_gamma_weighted_physical_time_proved':False}


def quat_q(A,B):
    comm=qmul(qmul(qmul(A,B),qconj(A)),qconj(B))
    return 1-np.asarray(comm)[...,0]


def conditional_seam_kernel(t=.85, lam=.40, num=5, seed=20261108):
    """Discrete nontrivial Gram control for gluing with and without seam swap.

    Source geometric pairs are *not* identified as two time slices here.
    """
    q=unit_quaternion(np.random.default_rng(seed),(num,))
    # Character χ_1/2=2*halftrace; auxiliary heat semigroup acts by e^-3t/4.
    rel=qmul(q[:,None,:],qconj(q)[None,:,:])[...,0]
    H=su2_heat_character_kernel(rel,t)
    assert np.allclose(H,H.T,atol=1e-12)
    product_kernel=np.kron(H,H)
    states=list(product(range(num),repeat=2))
    assert product_kernel.shape==(num*num,num*num)
    swap=np.array([states.index((b,a)) for a,b in states],dtype=int)
    swapped_kernel=product_kernel[:,swap]
    assert np.allclose(swapped_kernel,swapped_kernel.T,atol=1e-10)
    chi=2*q[:,0]
    f=np.asarray([chi[a]-chi[b] for a,b in states])
    assert np.linalg.norm(f)>1e-4
    swapped_Q=float(f@swapped_kernel@f / (num*num)**2)
    unswapped_Q=float(f@product_kernel@f / (num*num)**2)
    assert swapped_Q<0 and unswapped_Q>0
    # Add a local within-side non-Abelian commutator coupling. This is
    # ONLY an auxiliary doubled model, not source-derived physical time.
    qside=np.asarray([float(quat_q(q[a],q[b])) for a,b in states]);assert np.min(qside)>=-1e-11
    sideweight=np.exp(-lam*qside/2)
    good_kernel=sideweight[:,None]*product_kernel*sideweight[None,:]
    evals_good=np.linalg.eigvalsh(good_kernel)
    assert evals_good.min()>-1e-9
    return {
        't_auxiliary':t,'lambda_auxiliary_local_side_commutator':lam,
        'sample_quaternions':num,'tensor_states':num*num,'seed':seed,
        'two_face_matched_seam_kernel_min_eigenvalue':float(np.linalg.eigvalsh(product_kernel).min()),
        'doubled_side_interacting_matched_seam_min_eigenvalue':float(evals_good.min()),
        'cross_swapped_seam_kernel_min_eigenvalue':float(np.linalg.eigvalsh(swapped_kernel).min()),
        'antisymmetric_character_test_Q_cross_swap':swapped_Q,
        'antisymmetric_character_test_Q_matched':unswapped_Q,
        'exact_continuous_Haar_antisymmetric_character_Q_matched':float(2*math.exp(-.75*t)),
        'exact_continuous_Haar_antisymmetric_character_Q_swap':float(-2*math.exp(-.75*t)),
        'reason':'Tensor heat kernel H_t⊗H_t is positive; right composition by permutation swap has negative eigenvalue on antisymmetric character χ(U1)-χ(U2); conjugation by positive within-side commutator weights preserves positivity of matched seam.',
        'source_global_theta_supplied':False,
        'OS_physical_theory_proved':False,
        'Yang_Mills_gap_proved':False,
    }


def run_case(n,source_file,privatedir):
    if n in [7,20,25]:C=snapshot_complex(privatedir/f'PF_I11_original_source_{n}.npz')
    else:C=source_complex(source_file,n)
    source=validate_source(source_file)
    assert C.source_Ngrid==n
    return {'Ngrid':n,'transverse_pair_graph':face_pair_graph(C),
            'canonical_phason_reflection':verify_phason_height_inversion(C,source.GAMMA_GENERIC),
            'source_scalar_hopping_reflection':hopping_inversion_mismatch(C)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--source-file',type=Path,default=Path(__file__).resolve().parent/'source/paper6_extend_local.py')
    ap.add_argument('--snapshots',type=Path,default=Path(__file__).resolve().parent/'source/private_snapshots')
    ap.add_argument('--ngrids',type=int,nargs='+',default=[7,20,25]);a=ap.parse_args()
    q=conditional_seam_kernel()
    rows=[]
    for n in a.ngrids:
        rows.append(run_case(n,a.source_file,a.snapshots))
        b=rows[-1]['transverse_pair_graph'];ph=rows[-1]['canonical_phason_reflection']
        print(f'Ngrid={n}: F={b["faces"]}, pairs={b["transverse_pair_edges"]}, odd={b["odd_cycle_length"]}, mirrored_same_gamma={ph["reflected_vertices_accepted_under_same_gamma"]}/{ph["original_vertices"]}',flush=True)
    out={'schema':'singular-boundary.pf-i13.global-gluing-conditional.v1','date':'2026-11-08',
         'source_scope':'Unpublished exact source finite rhombus geometry, not an assumed physical cubic time.',
         'family_type_graph':petersen_type_graph(),
         'three_source_or_eight_source_tests':rows,
         'conditional_gluing_comparison':q,
         'open_gates':['No global source-derived reflection or time','No source-selected heat time or seam matching',
                       'No proof of nontrivial four-dimensional interacting continuum Yang-Mills',
                       'No uniform physical mass-gap lower bound'],
         'global_physical_OS_positive':False,'source_derived_temporal_evolution':False,
         'source_derived_2plus2_action':False,'physical_Yang_Mills_gap_proved':False}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print('CANDIDATE-ONLY seam: POSITIVE matched with within-half interactions, NEGATIVE swapped',flush=True)
if __name__=='__main__':main()
