#!/usr/bin/env python3
"""PF-I9: source-faithful Z5 direct cut-and-project finite operator bridge.

The new graph generator enumerates Z5 lattice labels using four hypersimplex
internal windows and basis-neighbour BFS. It does NOT call source grid lines.
The author's generator is independently invoked only for verification/crop
parameters. Its finite tile selection and Fibonacci hopping are then compared
at the exact original label/face/edge-set level, for every Ngrid.

This does NOT prove a physical spacetime, continuum Yang-Mills or mass gap.
"""
from __future__ import annotations
import argparse
from collections import Counter,deque,defaultdict
from hashlib import sha256
from itertools import combinations,product
import importlib.util, json, math, pathlib, time

import numpy as np
from scipy.spatial import ConvexHull

THETA=2*np.pi*np.arange(5)/5
PAR=np.column_stack([np.cos(THETA),np.sin(THETA)])
PERP=np.column_stack([np.cos(2*THETA),np.sin(2*THETA)])
WINDOW_EQ={h:ConvexHull(np.array([PERP[list(combo)].sum(axis=0)
     for combo in combinations(range(5),h)])).equations
     for h in range(1,5)}
BASIS=np.eye(5,dtype=int)
# A finite cell 4-cycle is a face only if its *lower* cube square
# intersects the 2D cut plane. Vertex-window membership alone is not enough.
# For fixed families j,k and sum(m)=1 or2, the three unfixed cube coordinates
# must lie in (0,1) and sum to sum(m). Their perpendicular images are one of
# two triangles, NOT the four-slice vertex window.
FACE_EQ={}
for j,k in combinations(range(5),2):
    free=[f for f in range(5) if f not in (j,k)]
    for h in (1,2):
        pts=np.array([PERP[list(c)].sum(axis=0)
                      for c in combinations(free,h)])
        FACE_EQ[(j,k,h)]=ConvexHull(pts).equations


def direct_face_membership(m,j,k,gamma,eps=1e-9):
    h=sum(m)
    eq=FACE_EQ.get((j,k,h))
    if eq is None:return False
    y=(np.asarray(m,dtype=float)+gamma)@PERP
    return float(np.max(y@eq[:,:2].T+eq[:,2]))<-eps



def direct_membership(m: tuple[int,...],gamma:np.ndarray,epsilon=1e-9)->tuple[bool,float]:
    """Only perpendicular-window constraints and integer sum: no pentagrid."""
    height=sum(m)
    if height not in WINDOW_EQ:return False,float('inf')
    y=(np.asarray(m,dtype=float)+gamma)@PERP
    eq=WINDOW_EQ[height]
    violation=float(np.max(y@eq[:,:2].T+eq[:,2]))
    return violation < -epsilon,violation


def build_direct(radius:float,gamma:np.ndarray)->dict:
    """BFS over accepted Z5 nodes with physical radius cutoff; no grid lines.

    Seed enumeration is bounded and independently window-tested. A safety
    collar radius is caller-chosen to contain complete local stars.
    """
    def physical(m):return np.asarray(m,dtype=float)@PAR
    seeds={m for m in product(range(-2,3),repeat=5)
        if np.linalg.norm(physical(m))<1.4 and direct_membership(m,gamma)[0]}
    if not seeds:raise AssertionError('no regular window seed')
    explored=set(seeds);checked=set(seeds);q=deque(sorted(seeds));margin=1.0e-7
    while q:
        k=q.popleft()
        for fam in range(5):
            for dd in (-1,1):
                m=list(k);m[fam]+=dd;m=tuple(m)
                if m in checked:continue
                checked.add(m)
                if np.linalg.norm(physical(m))>radius+margin:continue
                if direct_membership(m,gamma)[0]:
                    explored.add(m);q.append(m)
    xy={m:physical(m) for m in explored}
    faces=set()
    for k in explored:
        for j,h in combinations(range(5),2):
            p=tuple(np.array(k)+BASIS[j]);q=tuple(np.array(p)+BASIS[h]);r=tuple(np.array(k)+BASIS[h])
            face=frozenset((k,p,q,r))
            if p in explored and q in explored and r in explored and direct_face_membership(k,j,h,gamma):
                faces.add(face)
    return {'labels':explored,'xy':xy,'faces':faces,'tested':len(checked),'seeds':len(seeds),'collar_radius':radius}


def face_center(f,xy):return np.mean(np.array([xy[k] for k in f]),axis=0)


def source_import(filepath):
    spec=importlib.util.spec_from_file_location('source_tiler',filepath)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


def tlevel(m,n):
    d=[j for j in range(5) if m[j]!=n[j]]
    if len(d)!=1 or abs(m[d[0]]-n[d[0]])!=1:
        raise AssertionError((m,n))
    j=d[0];k=min(m[j],n[j]);return j,k


def fib_type(j,k):
    phi=(1+math.sqrt(5))/2
    return 'A' if math.floor((k+1)/phi)!=math.floor(k/phi) else 'B'


def edge_key(a,b):return tuple(sorted((a,b)))


def edges_from_faces(faces):
    # A rhombus has four original-basis edges among its four vertices.
    edges=set()
    for face in faces:
        for a,b in combinations(face,2):
            d=[abs(a[j]-b[j]) for j in range(5)]
            if sum(d)==1:
                edges.add(edge_key(a,b))
    return edges


def edges_from_basis(verts):
    edges=set()
    for a in verts:
        for j in range(5):
            b=tuple(a[h]+int(h==j) for h in range(5))
            if b in verts:edges.add((a,b))
    return edges


def source_tile_edges(tiling,selected):
    mids=tiling['multi_indices'];retained=set(selected)
    return {edge_key(mids[i],mids[j]) for i in selected
        for j in tiling['adjacency'].get(i,set()) if j in retained}


def sha_vertex_labels(xs):
    return sha256(('\n'.join(' '.join(map(str,x)) for x in sorted(xs))+'\n').encode()).hexdigest()


def sha_edges(xs):
    return sha256(('\n'.join(' '.join(map(str,a))+'|'+ ' '.join(map(str,b))+'|'
         +str(tlevel(a,b)[0])+'|'+str(tlevel(a,b)[1])+'|'+fib_type(*tlevel(a,b))
         for a,b in sorted(xs))+'\n').encode()).hexdigest()


def topological_moments(edges,vertices):
    phi=(1+math.sqrt(5))/2;wB=phi**-2
    strengths=defaultdict(float);counts=Counter();hist=Counter();fam=Counter();wt=Counter();sum_w2=0.;sum_w=0.
    for a,b in sorted(edges):
        j,k=tlevel(a,b);t=fib_type(j,k);w=1. if t=='A' else wB
        strengths[a]+=w;strengths[b]+=w
        counts[a]+=1;counts[b]+=1;hist[t]+=1;fam[j]+=1;wt[t]+=w
        sum_w+=w;sum_w2+=w*w
    verts=set(vertices);assert verts
    cc=0;sizes=[];unseen=set(verts);adj=defaultdict(set)
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    while unseen:
        cc+=1;v=unseen.pop();q=[v];sz=1
        while q:
            for u in adj[q.pop()]&unseen:
                unseen.remove(u);q.append(u);sz+=1
        sizes.append(sz)
    n=len(verts)
    return {'count':len(edges),'type_counts':dict(hist),'per_family_count':dict(sorted(fam.items())),
     'mean_degree':2*len(edges)/n,'mean_weighted_strength':2*sum_w/n,
     'traceL_div_N':2*sum_w/n,'traceL2_div_N':(sum(v*v for v in strengths.values())+2*sum_w2)/n,
     'connected_components':cc,'component_sizes':sorted(sizes,reverse=True),'weighted_laplacian_nullity':cc,
     'zero_modes_if_connected':cc==1,'max_degree':max(counts.values())}


def face_family_levels(f):
    verts=np.asarray(list(f),dtype=int)
    lower=np.min(verts,axis=0)
    high=np.max(verts,axis=0)
    jks=np.flatnonzero(high-lower==1)
    assert len(jks)==2 and np.all((high-lower)[[k for k in range(5) if k not in jks]]==0)
    return (int(jks[0]),int(jks[1])),(int(lower[jks[0]]),int(lower[jks[1]]))


def one_case(source,n_grid:int,epsilon=1e-9,collar=4):
    t0=time.time()
    til=source.build_penrose_tiling(n_grid)
    gamma=source.GAMMA_GENERIC.copy()
    source_labels=til['multi_indices'];source_set=set(source_labels)
    center=np.asarray(til['vertices']).mean(axis=0)
    source_all_faces={frozenset(x['mi_vertices']) for x in til['tiles']}
    assert len(source_all_faces)==len(til['tiles']), 'duplicate source tiles'
    centers=np.asarray([np.mean(tt['positions'],axis=0) for tt in til['tiles']])
    cutoff=.35*float(np.max(np.linalg.norm(centers-center,axis=1)))
    direct=build_direct(cutoff+collar,gamma)
    # Source is used ONLY here, after independently generating the window set.
    source_inner=source.select_interior_vertices(til,.35)
    source_in_labels={source_labels[i] for i in source_inner}
    assert source_in_labels<=direct['labels'],('missing interior',len(source_in_labels-direct['labels']))
    # Source labels and direct point sets coincide in a smaller common disk.
    core_r=cutoff-2
    source_core_ball={k for k in source_set if np.linalg.norm(np.asarray(k)@PAR-center)<core_r}
    direct_core_ball={k for k,x in direct['xy'].items() if np.linalg.norm(x-center)<core_r}
    assert source_core_ball<=direct_core_ball, ('source point outside direct window',n_grid)
    # Face completion: direct method may produce GENUINE tiles not enumerated
    # by the source because its line levels were capped by Ngrid.
    src_selected_faces={frozenset(x['mi_vertices']) for x,c in zip(til['tiles'],centers) if np.linalg.norm(c-center)<cutoff}
    cut_faces={f for f in direct['faces'] if np.linalg.norm(face_center(f,direct['xy'])-center)<cutoff}
    assert src_selected_faces<=cut_faces,('source faces not in direct',n_grid)
    extra_selected=cut_faces-src_selected_faces
    invalid_level=[];margin_out=Counter();family_level=Counter()
    for f in extra_selected:
        (j,k),(nj,nk)=face_family_levels(f)
        overshoot=max(abs(nj),abs(nk))-n_grid
        if overshoot<=0:invalid_level.append((j,k,nj,nk))
        margin_out[overshoot]+=1
        if abs(nj)>n_grid:family_level[(j,nj)]+=1
        if abs(nk)>n_grid:family_level[(k,nk)]+=1
    assert not invalid_level,('extra selected face in original enumerated levels',invalid_level[:2])
    # Corrected 35%-tile-centre one-pass interior uses the entire incident
    # face star in the direct-window collar. This intentionally can differ.
    incident=defaultdict(list)
    for f in direct['faces']:
        ok=f in cut_faces
        for k in f:incident[k].append(ok)
    direct_interior={k for k,states in incident.items() if states and all(states)}
    # Recompute the author's TWO finite weighted edge dictionaries ON SOURCE
    # retained labels, then independently complete tile faces using C&P.
    source_tile=source_tile_edges(til,source_inner)
    basis_s=edges_from_basis(source_in_labels)
    full_direct_edges=edges_from_faces(direct['faces'])
    full_tile_on_source={e for e in full_direct_edges if e[0] in source_in_labels and e[1] in source_in_labels}
    assert source_tile<=full_tile_on_source,('missing source tile',n_grid)
    assert full_tile_on_source==basis_s,('basis neighbour not true tile',n_grid)
    coupled_extra=basis_s-source_tile
    completed_tile_edges=full_tile_on_source-source_tile
    assert coupled_extra==completed_tile_edges
    # Every source basis-only edge has an explicitly named missing rhombus
    # witness in the finite source line-range enumeration.
    missing_faces=direct['faces']-source_all_faces
    missing_edge_witness=set()
    missing_outside_level_count=0
    for f in missing_faces:
        (j,k),(nj,nk)=face_family_levels(f)
        if max(abs(nj),abs(nk))>n_grid:missing_outside_level_count+=1
        for e in edges_from_faces((f,)):
            if e[0] in source_in_labels and e[1] in source_in_labels:
                missing_edge_witness.add(e)
    assert coupled_extra<=missing_edge_witness,('coupled extras without omitted tile witness',n_grid)
    true_tile_edges={e for e in full_direct_edges if e[0] in direct_interior and e[1] in direct_interior}
    true_basis_edges=edges_from_basis(direct_interior)
    assert true_tile_edges==true_basis_edges,('completed window graph mismatch',n_grid)
    selected_clearance=min(-direct_membership(k,gamma)[1] for k in source_in_labels)
    assert selected_clearance>1e-8
    extra_family=Counter(tlevel(a,b)[0] for a,b in coupled_extra)
    source_counts=Counter(sum(k) for k in source_in_labels)
    true_counts=Counter(sum(k) for k in direct_interior)
    return {
      'Ngrid':n_grid,'source_all_vertices':len(source_set),'source_all_faces':len(source_all_faces),
      'cutoff_radius':cutoff,'source_center':center.tolist(),
      'direct_collar_radius':direct['collar_radius'],'direct_seed_count':direct['seeds'],
      'direct_window_BFS_vertices':len(direct['labels']),'direct_window_BFS_faces':len(direct['faces']),
      'direct_tested_integer_labels':direct['tested'],
      'source_retained_vertices':len(source_in_labels),'direct_recovered_source_retained':len(source_in_labels),
      'source_retained_set_sha256':sha_vertex_labels(source_in_labels),
      'direct_recovered_source_set_sha256':sha_vertex_labels(source_in_labels),
      'source_retained_heights':{str(int(k)):int(v) for k,v in sorted(source_counts.items())},
      'small_common_disk_radius':core_r,'small_common_disk_accepted_vertex_count':len(source_core_ball),
      'small_common_disk_accepted_vertex_sets_equal':direct_core_ball==source_core_ball,
      'small_common_disk_source_missing_vertices':len(direct_core_ball-source_core_ball),
      'small_common_disk_direct_missing_vertices':len(source_core_ball-direct_core_ball),
      'source_selected_tile_faces':len(src_selected_faces),
      'direct_window_selected_tile_faces':len(cut_faces),
      'missing_source_tile_faces_in_selected_disk':len(extra_selected),
      'missing_face_crossing_levels_outside_enumeration':len(extra_selected),
      'source_unenumerated_face_overshoot_levels':dict(sorted(margin_out.items())),
      'source_missing_face_level_family_count':{str(k):v for k,v in sorted(family_level.items())},
      'source_35pct_interior_count':len(source_in_labels),
      'direct_35pct_full_star_interior_count':len(direct_interior),
      'direct_complete_interior_height_counts':{str(int(k)):int(v) for k,v in sorted(true_counts.items())},
      'source_interior_false_positive_count_vs_complete_window':len(source_in_labels-direct_interior),
      'source_interior_false_negative_count_vs_complete_window':len(direct_interior-source_in_labels),
      'minimum_source_selected_vertex_window_clearance':selected_clearance,
      'source_tile_edge_count':len(source_tile),'source_coupled_basis_edge_count':len(basis_s),
      'source_coupled_extra_over_truncated_tiles':len(coupled_extra),
      'all_extra_basis_bonds_have_omitted_rhombus_witness':True,
      'completed_window_tile_edges_on_original_source_vertices':len(full_tile_on_source),
      'completed_window_tile_equals_all_basis_on_original_source_vertices':True,
      'source_extra_basis_family_histogram':dict(sorted(extra_family.items())),
      'corrected_direct_interior_tile_and_basis_edges':len(true_tile_edges),
      'source_original_vertex_SHA256':sha_vertex_labels(source_in_labels),
      'source_original_tile_edge_SHA256':sha_edges(source_tile),
      'source_original_coupled_edge_SHA256':sha_edges(basis_s),
      'direct_complete_tile_edge_SHA256_on_source_vertices':sha_edges(full_tile_on_source),
      'corrected_direct_vertex_SHA256':sha_vertex_labels(direct_interior),
      'corrected_direct_all_edges_SHA256':sha_edges(true_basis_edges),
      'source_tile_scalar_weighted_moments':topological_moments(source_tile,source_in_labels),
      'source_coupled_scalar_weighted_moments':topological_moments(basis_s,source_in_labels),
      'direct_complete_star_scalar_weighted_moments':topological_moments(true_basis_edges,direct_interior),
      'source_code_output_not_overwritten':True
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-script',type=pathlib.Path,required=True)
    ap.add_argument('--Ngrid',nargs='+',type=int,default=[7,10,12,15,18,20,23,25])
    ap.add_argument('--output',type=pathlib.Path,required=True)
    args=ap.parse_args()
    source=source_import(args.source_script)
    rows=[]
    for n in args.Ngrid:
        row=one_case(source,n)
        print(json.dumps({k:row[k] for k in ['Ngrid','source_retained_vertices','direct_35pct_full_star_interior_count','source_selected_tile_faces','missing_source_tile_faces_in_selected_disk','source_coupled_extra_over_truncated_tiles']},sort_keys=True),flush=True)
        rows.append(row)
    out={
       'scope':'FINITE original-integer cut-project source comparison identifies missing genuine rhombi caused by finite grid-level cap; all source coupled basis-extra edges become true completed tiling edges; corrected one-pass core differs from truncated source',
       'original_script_reference':args.source_script.name,'source_script_sha256':sha256(args.source_script.read_bytes()).hexdigest(),
       'generator_independence':'direct source generates accepted Z5 points with perpendicular hypersimplex window; source pentagrid only called for independent comparison and crop parameters',
       'gamma_sum_zero':float(source.GAMMA_GENERIC.sum()),
       'source_gamma':source.GAMMA_GENERIC.tolist(),
       'size_rows':rows,'mass_gap_proved':False,'original_interacting_four_dimensional_continuum_constructed':False,
       'spectral_eigensolver_executed':False,'periodic_control_needed_for_geometry_equivalence':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
if __name__=='__main__':main()
