"""Validated 2D Penrose P3 dual-pentagrid patch, audited against Z^5 window.

Conventions: grid family j has lines e_j dot x - gamma_j = integer;
labels of dual vertices are k in Z^5; positions r(k)=sum_j k_j e_j.
This module is explicitly TWO-dimensional, not a Z^6 3D tiling generator.
"""
import itertools
from collections import Counter,deque
import numpy as np
from scipy.spatial import ConvexHull
from legacy_phase2 import penrose as legacy_generator

THETA=2*np.pi*np.arange(5)/5
PAR=np.column_stack([np.cos(THETA),np.sin(THETA)])
PERP=np.column_stack([np.cos(2*THETA),np.sin(2*THETA)])
ORIGINAL_GAMMA=np.array([.07,.19,.31,.43,.61])
ALT_GAMMA=np.array([.073,.197,.313,.439,.613])
STEP=np.array([.119,.241,.347,.063,.173])
HULLS={h:ConvexHull(np.array([PERP[list(ind)].sum(axis=0) for ind in itertools.combinations(range(5),h)])) for h in range(1,5)}

def canonical_gamma(gamma, target_sum=1):
    """Minimal Euclidean projection of a shift vector onto sum gamma=target_sum.
    This changes the tiling. It is NOT a retrospective validation of legacy data.
    """
    g=np.array(gamma,dtype=float)
    if g.shape!=(5,): raise ValueError('Five offsets required')
    return g + (target_sum-np.sum(g))/5

def require_regular(gamma, radius, line_range, margin=1e-8):
    """Finite-patch test for triple or higher pentagrid crossings."""
    mindist=1.
    for i,j in itertools.combinations(range(5),2):
        inv=np.linalg.inv(PAR[[i,j]])
        for p in range(-line_range,line_range+1):
            for q in range(-line_range,line_range+1):
                x=inv@np.array([p+gamma[i],q+gamma[j]])
                if np.linalg.norm(x)>radius: continue
                for h in range(5):
                    if h==i or h==j: continue
                    z=PAR[h]@x-gamma[h]
                    mindist=min(mindist,abs(z-round(z)))
    if mindist<margin: raise ValueError(f'Singular or numerically unresolved pentagrid: {mindist}')
    return float(mindist)

def build(radius=7., offset=0, line_range=None):
    gamma=canonical_gamma((ORIGINAL_GAMMA+STEP*offset)%1)
    line_range=int(np.ceil(3*radius))+4 if line_range is None else int(line_range)
    if abs(sum(gamma)-1)>1e-10:raise AssertionError('sum gamma not 1')
    minsep=require_regular(gamma,radius,line_range)
    g=legacy_generator(radius=radius,line_range=line_range,gamma=gamma)
    return g,gamma,minsep

def window_membership(k,gamma,eps=1e-7):
    """Independent model-set acceptance from four hypersimplex slice windows.

    For f_j=n_j dot x-gamma_j-k_j in (0,1), sum f = -sum gamma -sum k.
    At integral sum gamma=1, only slices h=1,2,3,4 occur.
    Internal projection of f is -sum_j (k_j+gamma_j) exp(4pi i j/5).
    """
    k=np.asarray(k)
    h=int(np.rint(-np.sum(k)-np.sum(gamma)))
    if h<1 or h>4:return False
    y=-(k+gamma)@PERP
    hull=HULLS[h]
    return bool(np.max(hull.equations[:,:2]@y + hull.equations[:,2]) < eps)

def check(g,gamma,minsep=None,radius=None):
    labels={tuple(map(int,k)):i for i,k in enumerate(g.labels)}
    adj=[set() for _ in g.labels];edgefaces=Counter();types=Counter()
    for u,v in g.edges:adj[u].add(v);adj[v].add(u)
    for f in g.faces:
        assert len(f)==4 and len(set(f))==4
        diff=[np.array(g.labels[f[(i+1)%4]])-np.array(g.labels[f[i]]) for i in range(4)]
        ax=[int(np.argmax(np.abs(x))) for x in diff]
        t=(ax[1]-ax[0])%5
        types[min(t,5-t)]+=1
        for a,b in zip(f,f[1:]+f[:1]):edgefaces[tuple(sorted((a,b)))]+=1
    counts=Counter(edgefaces.values())
    assert set(counts).issubset({1,2})
    assert set(edgefaces)==set(g.edges)
    assert all(np.abs(np.array(g.labels[u])-np.array(g.labels[v])).sum()==1 for u,v in g.edges)
    assert all(window_membership(k,gamma) for k in g.labels)
    labelsums=Counter(sum(k) for k in g.labels)
    degrees=Counter(map(len,adj))
    edges={tuple(sorted(e)) for e in g.edges}
    missing=[];wrong=[];expected=0
    for k,v in labels.items():
        for axis in range(5):
            for jump in (-1,1):
                target=list(k);target[axis]+=jump;target=tuple(target)
                if not window_membership(target,gamma):continue
                if target in labels:
                    expected+=1
                    if tuple(sorted((v,labels[target]))) not in edges:wrong.append((k,target))
    assert not wrong
    # The old routine truncates in pentagrid intersection coordinates; its physical
    # bulk at |r(k)|<=cutoff must also be window-neighbor-complete.
    cutoff=min(11., 1.1*radius) if radius is not None else 0.
    bulk_missing=[]
    for k,v in labels.items():
        if np.linalg.norm(g.xy[v])>cutoff:continue
        for axis in range(5):
            for jump in (-1,1):
                target=list(k);target[axis]+=jump;target=tuple(target)
                if window_membership(target,gamma) and target not in labels:bulk_missing.append((k,target))
    assert not bulk_missing
    n=len(g.labels)
    assert n-len(g.edges)+len(g.faces)==1
    assert max(map(len,adj))<=7
    return dict(vertices=n,edges=len(g.edges),faces=len(g.faces),euler=n-len(g.edges)+len(g.faces),
       gamma_sum=float(np.sum(gamma)),min_third_line_distance=minsep,
       label_height_hist={str(k):v for k,v in sorted(labelsums.items())},
       degree_hist={str(k):v for k,v in sorted(degrees.items())},
       tile_class_hist={str(k):v for k,v in sorted(types.items())},
       edge_face_multiplicities={str(k):v for k,v in sorted(counts.items())},
       all_vertices_inside_discrete_window=True,all_observed_links_are_basis_steps=True,
       all_present_window_neighbors_connected=True,physical_bulk_window_neighbors_complete=True,
       face_ratio=float(types[1]/types[2]) if types[2] else None,
       permitted_height_classes=sorted(labelsums))
