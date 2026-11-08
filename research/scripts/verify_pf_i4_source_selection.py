#!/usr/bin/env python3
"""PF-I4: source-consistency constraints for the published Paper1/2/4 graph operators.

This is a finite-model and exact combinatorial audit, NOT a reconstruction of the
unpublished Paper2/Paper4 spectral generator or a YM/grav proof.
Dependence: verify_pf_i2_pentagrid.py, the independently reconstructed Paper1 P3 model.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import tarfile

import numpy as np
from verify_pf_i2_pentagrid import generate, D, TA, TB

PAPER2_FULL=[1550,3042,4324,6980,9950,12207,16435,19260]
PAPER4_PRIME=[1550,3042,4324,6979,9947,12206,16434,19255]
NGRID=[7,10,12,15,18,20,23,25]


def paper4_degree_arithmetic():
    # Paper4 Sec6.1: p_3=28.6%, p_4=65.9%, p_5=5.0%; Sec6.2: rest 0.5% has degree >=6.
    p3,p4,p5=map(Fraction,['0.286','0.659','0.050'])
    rest=1-p3-p4-p5
    assert rest == Fraction(5,1000)
    lower=3*p3+4*p4+5*p5+6*rest
    report=Fraction('3.748')
    # Rounding to one decimal percent: each stated share +/- 0.0005.
    delta=Fraction(5,10000)
    # Equivalent min mean 6 - 3p3 -2p4-p5, monotone decreasing in stated shares.
    round_min=6-3*(p3+delta)-2*(p4+delta)-(p5+delta)
    # The extra mass from remaining vertices >= 6 cannot reduce the mean.
    assert lower == Fraction(3774,1000)
    assert round_min == Fraction(3771,1000)
    assert round_min > report
    # Reported D = .786 vs explicitly sqrt(<d>/6) in Paper4 Sec6.2.
    dsource=Fraction('0.786')
    inferred_mean=6*dsource*dsource
    return {
        'paper4_section':'6.1-6.2','fractions':{'deg3':str(p3),'deg4':str(p4),'deg5':str(p5),'remaining_ge6':str(rest)},
        'claimed_mean_degree':str(report),'exact_lower_bound_mean_degree':str(lower),
        'minimum_allowing_each_percent_rounded_to_0p1pct':str(round_min),
        'mean_degree_gap_at_least':str(round_min-report),
        'reported_degree_factor_D':str(dsource),'mean_degree_implied_by_6D_squared':str(inferred_mean),
        'same_population_same_unweighted_degree_interpretation_compatible':False,
        'note':'The percentages and degree >=6 remainder cannot produce <d>=3.748 on one unweighted vertex population; different populations/weighting remain possible.'
    }


def components(vertices,adj):
    unseen=set(vertices);sizes=[]
    while unseen:
        start=unseen.pop();q=[start];num=1
        while q:
            for w in adj[q.pop()] & unseen:
                unseen.remove(w);q.append(w);num+=1
        sizes.append(num)
    return sorted(sizes,reverse=True)


def patch_report(radius,nmax):
    g=generate(radius=radius,nmax=nmax)
    labels=sorted(g['vertices']);ids={a:i for i,a in enumerate(labels)}
    adj=[set() for _ in labels]
    weights=[]
    for (a,b),(_,_,t,w) in g['edges'].items():
        i,j=ids[a],ids[b];adj[i].add(j);adj[j].add(i)
        weights.append(float(w))
    assert len(components(range(len(labels)),adj))==1
    pt=np.asarray(labels,dtype=float)@D
    root=int(np.argmin(np.sum(pt**2,axis=1)))
    dist=[-1]*len(labels);dist[root]=0;q=deque([root])
    while q:
        i=q.popleft()
        for j in adj[i]:
            if dist[j]<0:dist[j]=dist[i]+1;q.append(j)
    assert all(d>=0 for d in dist)
    maxdist=max(dist)
    cutoff=int(np.floor(0.35*maxdist))
    cand={i for i,d in enumerate(dist) if d<=cutoff}
    core={i for i in cand if adj[i].issubset(cand)}
    assert core and len(core)<len(labels)
    # One pass may be sensible, but is *not* a fixed point of the criterion.
    leak=sum(bool(adj[i]-core) for i in core)
    assert leak > 0
    count=Counter(len(neigh) for neigh in adj)
    core_components=components(core,adj)
    assert core_components==[len(core)]
    # Weighted connected graph Laplacian has exactly one zero mode, by
    # x^T L x = sum_e w_e (x_u-x_v)^2; no matrix eigensolver necessary.
    assert all(0<w<=1 for w in weights) and any(w<1 for w in weights)
    zero_count=1
    # If D is UNWEIGHTED degree instead of weighted strength,
    # x^T(D#-W)x = sum_e w_e(x_u-x_v)^2 + sum_e(1-w_e)(x_u^2+x_v^2).
    # This is positive definite on a connected graph with some weak edge.
    count_diagonal_zero_count=0
    return {
      'cutoff_radius_physical':radius, 'grid_level_limit':nmax,
      'independent_P3_source_equation_reconstruction':True,
      'source_original_Ngrid_selection_authenticated':False,
      'full_vertices':len(labels),'full_edges':len(g['edges']),
      'full_components':1,'full_zero_modes_weighted_L':1,
      'full_zero_modes_count_degree_minus_weighted_W':count_diagonal_zero_count,
      'full_degree_distribution':{str(k):v for k,v in sorted(count.items())},
      'full_mean_unweighted_degree':2*len(g['edges'])/len(labels),
      'root_index':root,'maximum_graph_distance_from_root':maxdist,
      'illustrative_35pct_integer_BFS_cutoff':cutoff,
      'candidate_35pct_vertices':len(cand),
      'one_pass_all_original_neighbors_in_candidate_vertices':len(core),
      'one_pass_core_components':len(core_components),
      'one_pass_core_zero_modes_weighted_L':zero_count,
      'one_pass_core_has_neighbors_outside_itself':True,
      'count_core_vertices_with_neighbors_outside_core':leak,
      'note':'BFS tile distance rooted near origin is an explicitly illustrative interpretation, NOT the source implementation or source Ngrid patch.'
    }


def zero_mode_hypothesis():
    gaps=[a-b for a,b in zip(PAPER2_FULL,PAPER4_PRIME)]
    assert gaps==[0,0,0,1,3,1,1,5]
    # Every nonempty finite standard positive-weight graph Laplacian has
    # >=1 zero mode, and if connected exactly one.
    cannot_all_zero=[i for i,d in enumerate(gaps) if d<1]
    cannot_connected=[i for i,d in enumerate(gaps) if d!=1]
    return {
      'paper2_full_Nint':PAPER2_FULL,
      'paper4_section3_prime_N':PAPER4_PRIME,
      'Ngrid':NGRID,
      'published_count_differences':gaps,
      'not_possible_as_all_zero_modes_of_same_nonempty_weighted_graph_indices':cannot_all_zero,
      'not_possible_as_one_zero_mode_from_same_connected_weighted_graph_indices':cannot_connected,
      'same_graph_and_zero_mode_removal_alone_can_reconcile_all_eight':False,
      'under_hypotheses':'Same Nint full graph, positive weighted-degree Laplacian, Nprime = Nint minus exactly its zero eigenspace dimension, with no different graph/vertex selection/threshold.',
      'necessary_alternatives':'Source N denotes different selection or normalization; graph/weight conventions differ; zero filtering is not applied consistently; or tables have source errors. None selected here.'
    }


# Original archive-native PDF SHA256 values verified from the supplied tar bytes.
ORIGINAL_PDF_HASHES={
 'paper1':'2b11426161c32c41a36fd816e3fcd668c7f1b44ee9cf73be1a62638fe6d46be5',
 'paper2':'2bfc52c29140149d483b8e1b980143b05a43d21fe0e2098516efb1615b7e50e7',
 'paper4':'871bf58f9d5adf66b2ad7d115f8031dd0c36efc18b147ae91caa48e6865d54ab'
}
PROCESSED_COPY_HASHES={
 'paper1':'42da2082f86858f75771a06ef7767bbea59bf53bd2d27e20357b7a3d62cedf4e',
 'paper2':'5f010279d4cea5ea5db4abac3834759c2cf15e2cb084d56b7beefa0b1d98263f',
 'paper4':'741660e2654a6891c95b25ef689faa16915c32356f537c14d0402fc32ee1ede5'
}
PDF_PATHS={
 'paper1':'delivery/papers/Paper_1/Sharpe_Paper1_Spectral_Dimension_Flow.pdf',
 'paper2':'delivery/papers/Paper_2/Sharpe_Paper2_Z5_Minkowski_Lapidus.pdf',
 'paper4':'delivery/papers/Paper_4/Sharpe_Paper4_Conformal_Boundary_CC.pdf'
}


def source_sha_archive(tar_path):
    output={}
    with tarfile.open(tar_path,'r:gz') as archive:
        for name,path in PDF_PATHS.items():
            item=archive.extractfile(path)
            assert item is not None, path
            sha=hashlib.sha256(item.read()).hexdigest()
            assert sha==ORIGINAL_PDF_HASHES[name],(path,sha)
            output[name]={'archive_member':path,'source_native_sha256':sha,'matches_pinned_sha256':True}
    return output


def produce(source_tar=None):
    originals={name:{'archive_member':PDF_PATHS[name],
                     'source_native_sha256':sha,
                     'previous_processed_copy_sha256':PROCESSED_COPY_HASHES[name]}
               for name,sha in ORIGINAL_PDF_HASHES.items()}
    if source_tar is not None:
        verify=source_sha_archive(source_tar)
        for name in originals:
            originals[name]['archive_bytes_independently_checked']=verify[name]['matches_pinned_sha256']
    else:
        for name in originals:
            originals[name]['archive_bytes_independently_checked']=False
    return {
      'status':'exact conditional exclusion + independent finite P3 controls, NOT source Paper2/Paper4 reproduction',
      'paper_source_sha256':originals,
      'source_provenance_correction':'Processed PDF copies from the earlier PF-I2/I3 workspace have different SHA256 from original tar members. All rendered pages at 1.2x and all extracted text were verified identical in this audit; do not mislabel processed copy hashes as original archive bytes.',
      'paper1_interior_selection_printed':'Sec7.2: tile distance within 35% maximum, then all neighbors of each interior vertex also interior. No one-pass / iterative implementation stated.',
      'interior_closure_theorem':'In a connected finite graph, a nonempty neighbor-closed vertex subset equals the whole graph; otherwise boundary removal can only be one-pass or use a different ambient adjacency.',
      'paper4_degree_consistency':paper4_degree_arithmetic(),
      'paper4_mode_count_consistency':zero_mode_hypothesis(),
      'paper4_two_graphs_printed':'Sec7.1 distinguishes 2D Penrose tile-based adjacency vs coupled Z5 all-five-basis-direction adjacency; numerical operator equality NOT established.',
      'finite_reconstructed_P3':{'radius6p5':patch_report(6.5,11),'radius12':patch_report(12.0,19)},
      'continuum_Yang_Mills_mass_gap_proved':False,
      'source_Paper2_exact_generator_authenticated':False,
      'source_Paper4_zero_mode_filter_authenticated':False
    }

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=None)
    p.add_argument('--source-tar',type=Path,default=None,help='Optional original dissertation tar for exact source SHA256 check')
    args=p.parse_args();out=json.dumps(produce(args.source_tar),sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(out)
    print(out)
