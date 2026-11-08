#!/usr/bin/env python3
"""PF-I11 source-faithful finite SU(2) Wilson theory on Z5 accepted rhombi.

Mathematical scope: exact finite 2-cell construction, gauge covariance, positive
finite Haar integral, free-face collapses, and explicit flat non-Abelian holonomy.
This is NOT a proof of physical time, reflection positivity, continuum Yang-Mills,
or a uniform/nonzero physical mass gap. Cubic/triangular are not physical input.

For original source graph, pass the original unpublished source script via
--source-script; file must match SOURCE_SHA. No source files are embedded here.
"""
from __future__ import annotations
import argparse, collections, hashlib, importlib.util, json, math
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.special import iv
from scipy.integrate import quad

SOURCE_SHA="86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da"
THETA=2*math.pi*np.arange(5)/5
PAR=np.column_stack((np.cos(THETA),np.sin(THETA)))
PERP=np.column_stack((np.cos(2*THETA),np.sin(2*THETA)))
UNIT=np.eye(5,dtype=np.int64)
PHI=(1+math.sqrt(5))/2

# The two-face strata are triangles: in the 3 remaining cube coordinates,
# exactly h=1 or h=2 coordinates are 1 at each extremal vertex.
FACE_TRIANGLES={}
for j,k in combinations(range(5),2):
    free=[a for a in range(5) if a!=j and a!=k]
    for h in (1,2):
        vertices=np.array([PERP[list(c)].sum(axis=0) for c in combinations(free,h)])
        Q=np.column_stack((vertices[1]-vertices[0],vertices[2]-vertices[0]))
        assert abs(np.linalg.det(Q))>1e-8
        FACE_TRIANGLES[(j,k,h)]=(vertices[0],np.linalg.inv(Q))


def triangle_membership(lower, j, k, gamma, eps=1e-9):
    h=sum(lower)
    d=FACE_TRIANGLES.get((j,k,h))
    if d is None:return False
    y=(np.asarray(lower,dtype=float)+gamma)@PERP
    x=d[1]@(y-d[0]);a,b=float(x[0]),float(x[1])
    return min(a,b,1-a-b)>eps


def validate_source(src):
    path=Path(src)
    if hashlib.sha256(path.read_bytes()).hexdigest()!=SOURCE_SHA:
        raise ValueError('Original unpublished source hash mismatch: refusing to infer source identity')
    spec=importlib.util.spec_from_file_location('original_source_private',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    assert np.allclose(mod.GAMMA_GENERIC.sum(),0,atol=1e-12)
    return mod


def canonical_edge(a,b):return (a,b) if a<b else (b,a)


@dataclass
class Complex:
    labels:list
    edges:list
    faces:list
    face_edges:np.ndarray
    face_signs:np.ndarray
    face_families:list
    face_heights:list
    gamma:np.ndarray|None=None
    source_Ngrid:int|None=None
    def vertices_count(self):return len(self.labels)
    def edge_count(self):return len(self.edges)
    def face_count(self):return len(self.faces)


def assemble_complex(labels, gamma, source_Ngrid=None):
    """From exact accepted Z5 labels, add basis edges and actual triangle-tested rhombi.

    Source finite vertex *selection* is passed as data. No pentagrid line
    intersection is called in this function. Presence of four corners alone
    does not substitute for the face-window test.
    """
    gamma=np.asarray(gamma,dtype=float)
    if abs(float(gamma.sum()))>1e-10:raise ValueError('Expected source gamma of sum zero')
    labels=sorted(set(tuple(int(v) for v in m) for m in labels))
    if not labels:raise ValueError('Empty finite complex')
    selected=set(labels)
    edges=[]
    for a in labels:
        for j in range(5):
            b=tuple(a[k]+int(k==j) for k in range(5))
            if b in selected:edges.append((a,b))
    edges.sort()
    edge_index={e:i for i,e in enumerate(edges)}
    faces=[];face_edge=[];face_sign=[];fam=[];height=[]
    for a in labels:
        va=np.array(a,dtype=int)
        for j,k in combinations(range(5),2):
            b=tuple(va+UNIT[j]);c=tuple(va+UNIT[j]+UNIT[k]);d=tuple(va+UNIT[k]);
            if b not in selected or c not in selected or d not in selected:continue
            if not triangle_membership(a,j,k,gamma):continue
            f=(a,b,c,d)
            faces.append(f);fam.append((j,k));height.append(sum(a))
            eids=[];sign=[]
            for u,v in zip(f,f[1:]+f[:1]):
                canon=canonical_edge(u,v)
                eids.append(edge_index[canon]);sign.append(1 if canon==(u,v) else -1)
            face_edge.append(eids);face_sign.append(sign)
    return Complex(labels,edges,faces,np.array(face_edge,dtype=np.int32).reshape(-1,4),
                   np.array(face_sign,dtype=np.int8).reshape(-1,4),fam,height,gamma.copy(),source_Ngrid)


def source_complex(src, ngrid):
    mod=validate_source(src)
    tiling=mod.build_penrose_tiling(ngrid)
    selected=mod.select_interior_vertices(tiling,.35)
    labels=[tiling['multi_indices'][i] for i in selected]
    return assemble_complex(labels,mod.GAMMA_GENERIC,source_Ngrid=ngrid)


def sha_labels(labels):
    b='\n'.join(','.join(map(str,v)) for v in labels)+'\n'
    return hashlib.sha256(b.encode()).hexdigest()


def sha_face_labels(faces):
    b='\n'.join('|'.join(','.join(map(str,v)) for v in f) for f in faces)+'\n'
    return hashlib.sha256(b.encode()).hexdigest()


def connected_component_count(labels,edges,edge_ids=None):
    iv={v:i for i,v in enumerate(labels)};parent=list(range(len(labels)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    if edge_ids is None:edge_ids=range(len(edges))
    for e in edge_ids:
        a,b=edges[e];ra,rb=find(iv[a]),find(iv[b]);parent[ra]=rb
    roots={find(i) for i in range(len(labels))}
    return len(roots)


def collapse_complex(C):
    """Elementary 2-cell, free-1-cell collapses, yielding explicit graph.

    A face f with edge e incident to no other live face is deleted together
    with e. The remaining complex is a strong deformation retract. When all
    faces peel, fundamental group is a free group on E_remaining-V+C cycles.
    """
    E=C.edge_count();F=C.face_count();V=C.vertices_count()
    incidence=[[] for _ in range(E)]
    for fi in range(F):
        for edge in C.face_edges[fi]:incidence[int(edge)].append(fi)
    counts=[len(faces) for faces in incidence]
    face_alive=np.ones(F,dtype=bool)
    queue=collections.deque(i for i,c in enumerate(counts) if c==1)
    pairs=[]
    while queue:
        e=queue.popleft()
        if counts[e]!=1:continue
        active=next((fi for fi in incidence[e] if face_alive[fi]),None)
        if active is None:raise AssertionError('incidence accounting failed')
        face_alive[active]=False
        pairs.append((int(active),int(e)))
        for d in C.face_edges[active]:
            d=int(d);counts[d]-=1
            if counts[d]<0:raise AssertionError('negative edge incidence')
            if counts[d]==1:queue.append(d)
    paired={edge for _,edge in pairs}
    survivors=sorted(set(range(E))-paired)
    full_cc=connected_component_count(C.labels,C.edges)
    remain_cc=connected_component_count(C.labels,C.edges,survivors)
    assert remain_cc==full_cc
    VminusC=V-full_cc
    r=len(survivors)-VminusC
    return {'n_vertices':V,'n_edges':E,'n_faces':F,'full_components':full_cc,
            'face_pairs':pairs,'all_faces_collapse':len(pairs)==F,
            'unpeeled_face_count':F-len(pairs),'surviving_edges':survivors,
            'survivor_components':remain_cc,'free_group_rank_if_complete':r if len(pairs)==F else None,
            'zero_incidence_edges':sum(not x for x in incidence),
            'one_incidence_edges':sum(len(x)==1 for x in incidence),
            'two_incidence_edges':sum(len(x)==2 for x in incidence),
            'greater_than_two_incidence_edges':sum(len(x)>2 for x in incidence),
            'chi':V-E+F,
            'face_family_histogram':dict(sorted(collections.Counter(f'{a}-{b}' for a,b in C.face_families).items())),
            'face_height_histogram':dict(sorted(collections.Counter(map(str,C.face_heights)).items()))}


def tree_forest_and_chords(C, surviving_edges):
    """Build spanning forest of collapsed graph; chords generate free loops."""
    verts=C.labels;vmap={v:i for i,v in enumerate(verts)};parent=list(range(len(verts)))
    def find(x):
        while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    tree=[];chords=[]
    for idx in surviving_edges:
        a,b=C.edges[idx];ra=find(vmap[a]);rb=find(vmap[b])
        if ra==rb:chords.append(idx)
        else:parent[ra]=rb;tree.append(idx)
    return tree,chords


def qconj(q):
    q=np.asarray(q,dtype=float)
    return np.concatenate([q[...,:1],-q[...,1:]],axis=-1)


def qmul(x,y):
    """SU(2) in the real unit-quaternion representation; broadcasts batches."""
    a=np.asarray(x,dtype=float);b=np.asarray(y,dtype=float)
    scalar=(a[...,0]*b[...,0]-np.sum(a[...,1:]*b[...,1:],axis=-1))[...,None]
    vector=a[...,0:1]*b[...,1:]+b[...,0:1]*a[...,1:]+np.cross(a[...,1:],b[...,1:])
    return np.concatenate((scalar,vector),axis=-1)


def unit_quaternion(rng,shape):
    q=rng.standard_normal(tuple(shape)+(4,))
    return q/np.linalg.norm(q,axis=-1,keepdims=True)


def q_identity(n):
    z=np.zeros((n,4),dtype=float);z[:,0]=1.0;return z


def plaquette_holonomies(C,links):
    if C.face_count()==0:return np.empty((0,4))
    oriented=[]
    for i in range(4):
        x=links[C.face_edges[:,i]]
        oriented.append(np.where((C.face_signs[:,i]>0)[:,None],x,qconj(x)))
    h=oriented[0]
    for x in oriented[1:]:h=qmul(h,x)
    return h


def wilson_action(C,links,beta=0.7,mode='unit'):
    h=plaquette_holonomies(C,links)
    if mode=='unit':k=np.full(len(h),beta)
    elif mode=='projected-area':
        k=np.array([beta*abs(math.sin(2*math.pi*(b-a)/5)) for a,b in C.face_families])
    else:raise ValueError('Unknown optional face weight prescription')
    if np.min(k,initial=0)<0:raise ValueError('Need nonnegative coupling')
    return float(np.dot(k,1-h[:,0]))


def gauge_transform(C,links,gauge):
    vmap={v:i for i,v in enumerate(C.labels)}
    a=np.fromiter((vmap[u] for u,_ in C.edges),dtype=np.int32)
    b=np.fromiter((vmap[v] for _,v in C.edges),dtype=np.int32)
    return qmul(qmul(gauge[a],links),qconj(gauge[b]))


def oriented_link(C, links, edge_id, orientation):
    q=links[edge_id]
    return q if orientation==1 else qconj(q)


def flat_connection_witness(C,collapse,angle1=0.71,angle2=0.47):
    """Construct exact SU(2) plaquette-flat links with independent free-loop holonomies.

    Start with forest identity links and noncommuting chords on the collapsed
    graph, then restore free pairs in REVERSE face collapse order, solving
    each single unknown SU(2) edge to enforce U_face = 1.
    """
    if not collapse['all_faces_collapse']:raise ValueError('No complete free-face collapse')
    tree,chords=tree_forest_and_chords(C,collapse['surviving_edges'])
    # Chosen noncommuting loop generators must lie in the SAME connected
    # component, or their commutator is not gauge-invariant.
    parent={v:v for v in C.labels}
    def root(v):
        while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
        return v
    for edge_id in tree:
        a,b=C.edges[edge_id];parent[root(a)]=root(b)
    grouped=collections.defaultdict(list)
    for eid in chords:grouped[root(C.edges[eid][0])].append(eid)
    if len(chords)>1:
        two=next((ids[:2] for ids in grouped.values() if len(ids)>=2),None)
        if two is None:raise AssertionError('No two free loops in common connected component for commutator')
        chords=list(two)+[k for k in chords if k not in two]
    q=q_identity(C.edge_count())
    if chords:
        q[chords[0]]=[math.cos(angle1),0.,0.,math.sin(angle1)]
    if len(chords)>1:
        q[chords[1]]=[math.cos(angle2),math.sin(angle2),0.,0.]
    present=np.zeros(C.edge_count(),dtype=bool)
    present[collapse['surviving_edges']]=True
    for face,missing in reversed(collapse['face_pairs']):
        boundary=C.face_edges[face]
        j=list(boundary).index(missing)
        if not all(present[int(boundary[k])] for k in range(4) if k!=j):
            raise AssertionError('Invalid reversed elementary collapse')
        A=np.array([1.,0.,0.,0.]);B=A.copy()
        for k in range(j):A=qmul(A,oriented_link(C,q,int(boundary[k]),int(C.face_signs[face,k])))
        for k in range(j+1,4):B=qmul(B,oriented_link(C,q,int(boundary[k]),int(C.face_signs[face,k])))
        link=qmul(qconj(A),qconj(B))
        if C.face_signs[face,j]<0:link=qconj(link)
        q[missing]=link
        present[missing]=True
    assert present.all()
    plaquettes=plaquette_holonomies(C,q)
    defects=np.linalg.norm(plaquettes-np.array([1.,0,0,0]),axis=1) if len(plaquettes) else np.array([0.])
    # As all spanning-tree edge links are the identity, each non-tree chord
    # creates a fundamental loop with Wilson trace 2*q[chord,0].
    w=[float(q[c,0]) for c in chords[:2]]
    commutator=None
    if len(chords)>1:
        A=q[chords[0]];B=q[chords[1]]
        comm=qmul(qmul(qmul(A,B),qconj(A)),qconj(B))
        commutator=float(comm[0])
    return {'links':q,'survivor_spanning_tree_edges':tree,'survivor_chords':chords,
            'max_identity_holonomy_error':float(defects.max()),
            'first_two_fundamental_loop_halftraces':w,
            'nonabelian_commutator_halftrace':commutator,
            'flat_action_beta1':wilson_action(C,q,beta=1.)}


def exact_one_face(beta):
    if beta<0:raise ValueError('beta must be nonnegative')
    if beta==0:return {'beta':0.,'Z':1.,'mean_halftrace':0.}
    z=float(math.exp(-beta)*2*iv(1,beta)/beta)
    return {'beta':beta,'Z':z,'mean_halftrace':float(iv(2,beta)/iv(1,beta))}


def quadrature_one_face(beta):
    h=lambda t: (2/math.pi)*math.sin(t)**2
    Z=quad(lambda t:h(t)*math.exp(-beta*(1-math.cos(t))),0,math.pi,epsabs=2e-12)[0]
    W=quad(lambda t:h(t)*math.cos(t)*math.exp(-beta*(1-math.cos(t))),0,math.pi,epsabs=2e-12)[0]
    return {'Z':Z,'mean_halftrace':W/Z}


def case_summary(C,flat=False):
    T=collapse_complex(C)
    if not T['all_faces_collapse']:raise AssertionError('Noncollapsible finite complex')
    tree,chords=tree_forest_and_chords(C,T['surviving_edges'])
    assert len(chords)==T['free_group_rank_if_complete']
    row={k:v for k,v in T.items() if k not in ('face_pairs','surviving_edges')}
    row['Ngrid']=C.source_Ngrid
    row['source_vertices_sha256']=sha_labels(C.labels)
    row['direct_accepted_faces_sha256']=sha_face_labels(C.faces)
    row['collapse_pair_sha256']=hashlib.sha256(np.asarray(T['face_pairs'],dtype=np.int32).tobytes()).hexdigest()
    row['spanning_forest_edges']=len(tree)
    row['surviving_cycle_chords']=len(chords)
    row['H1_Z_rank']=len(chords)
    row['H2_Z_rank']=0
    row['pi1_free_rank']=len(chords)
    # The Hessian of the Wilson action at the identity is d1^T*kappa*d1
    # in each of the three su(2) directions. These are LINEARIZED classical
    # kernel dimensions, never an interacting quantum spectral-gap estimate.
    row['linearized_flat_tangent_dimensions_total']=3*(C.edge_count()-C.face_count())
    row['linearized_gauge_tangent_dimensions']=3*(C.vertices_count()-T['full_components'])
    row['linearized_extra_flat_moduli_dimensions']=3*len(chords)
    row['all_face_square_boundaries_have_d1_d0_zero']=True
    if flat:
        a=flat_connection_witness(C,T)
        row['flat_connection']={k:v for k,v in a.items() if k not in ('links','survivor_spanning_tree_edges','survivor_chords')}
    return row


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-script',type=Path,required=True)
    p.add_argument('--ngrids',nargs='+',type=int,default=[7,10,12,15,18,20,23,25])
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--private-snapshot',type=Path,default=None)
    args=p.parse_args();rows=[]
    source=validate_source(args.source_script)
    for n in args.ngrids:
        t=source.build_penrose_tiling(n)
        ids=source.select_interior_vertices(t,.35)
        C=assemble_complex([t['multi_indices'][i] for i in ids],source.GAMMA_GENERIC,n)
        row=case_summary(C,flat=n in [20,25])
        rows.append(row)
        print(json.dumps({k:row[k] for k in ['Ngrid','n_vertices','n_edges','n_faces','full_components','free_group_rank_if_complete','all_faces_collapse']}),flush=True)
        if args.private_snapshot is not None and n in [7,20,25]:
            snap=args.private_snapshot
            snap.mkdir(parents=True,exist_ok=True)
            collapse=collapse_complex(C)
            extra={}
            if n in [20,25]:
                flat=flat_connection_witness(C,collapse)
                extra['flat_SU2_links_quaternions']=flat['links']
                extra['flat_surviving_cycle_chords']=np.asarray(flat['survivor_chords'],dtype=np.int32)
            np.savez_compressed(snap/f'PF_I11_original_source_{n}.npz',
                vertex_labels=np.asarray(C.labels,dtype=np.int32),
                edge_vertex_labels=np.asarray(C.edges,dtype=np.int32),
                faces_vertex_labels=np.asarray(C.faces,dtype=np.int32),
                face_edges=C.face_edges,face_signs=C.face_signs,
                free_collapse_pairs=np.asarray(collapse['face_pairs'],dtype=np.int32),
                surviving_edges=np.asarray(collapse['surviving_edges'],dtype=np.int32),**extra)
    result={'checkpoint':'PF-I11','status':'finite intrinsic SU2 action/gauge covariance/flat-moduli topology only; no physical continuum mass gap',
            'source_original_sha256':SOURCE_SHA,'source_accepted_vertex_selection':'unmodified original 35% incident-tile rule',
            'rhombus_rule':'four source accepted basis-square corners PLUS direct internal triangle membership',
            'face_weight_rule':'arbitrary nonnegative kappa; projected-area mode optional, not source physical prescription',
            'results':rows,'continuum_Yang_Mills_gap_proved':False,'physical_time_emergence_proved':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')

if __name__=='__main__':main()
