#!/usr/bin/env python3
"""PF-I2: reproduce Paper 1 §§6.1,7.1 pentagrid P3 graph and Fibonacci edge rule.

This is not the unpublished coupled Paper 2 graph-zeta generator. All patches
and cutoffs are explicit, artificial finite tests; no continuum inference.
"""
import argparse
import collections
import itertools
import json
import math
from pathlib import Path

import numpy as np

PHI=(1+math.sqrt(5))/2
TA=1.0
TB=PHI**(-2)
J=np.arange(5,dtype=int)
D=np.stack((np.cos(2*math.pi*J/5),np.sin(2*math.pi*J/5)),axis=1)


def gamma_source():
    g=np.mod(J*math.sqrt(2)+J*J*math.sqrt(3),1.0)
    return g-g.mean()


def type_and_weight(j,k):
    # Paper 1 Eq. (14).  k can be negative.
    is_A=math.floor((k+1)/PHI)!=math.floor(k/PHI)
    return ('A' if is_A else 'B'), (TA if is_A else TB)


def generate(radius=6.5,nmax=11,tol=1e-9):
    """Enumerate de Bruijn grid-line intersections and all resulting rhombi.

    nmax bounds grid levels, radius bounds projected rhombus-centroid distance.
    Neither cutoff was specified as the original Paper 1 numerical experiment.
    """
    g=gamma_source(); faces={}; candidates=0; triples=0
    for j,k in itertools.combinations(range(5),2):
        inv=np.linalg.inv(np.stack([D[j],D[k]]))
        for n in range(-nmax,nmax+1):
            for m in range(-nmax,nmax+1):
                r=inv@np.array([n+g[j],m+g[k]])
                arr=r@D.T-g
                others=[h for h in range(5) if h not in (j,k)]
                if any(abs(arr[h]-round(arr[h]))<=tol for h in others):
                    triples+=1
                    continue
                base=np.array([math.ceil(x) for x in arr],dtype=int)
                base[j]=n;base[k]=m
                corners=[]
                for dj,dk in [(0,0),(1,0),(1,1),(0,1)]:
                    a=base.copy();a[j]+=dj;a[k]+=dk
                    corners.append(tuple(map(int,a)))
                pc=np.array(corners,dtype=int)@D
                centroid=pc.mean(axis=0)
                if np.linalg.norm(centroid)>radius:continue
                faces[tuple(corners)]=(j,k,n,m)
                candidates+=1
    edges={};vertices=set();conflicts=[]
    for corners,(j,k,n,m) in faces.items():
        vertices.update(corners)
        pairs=[(corners[0],corners[1],j),(corners[3],corners[2],j),
               (corners[0],corners[3],k),(corners[1],corners[2],k)]
        for a,b,h in pairs:
            direction=[int(b[t]-a[t]) for t in range(5)]
            assert direction==[int(t==h) for t in range(5)],(a,b,h,direction)
            typ,w=type_and_weight(h,a[h])
            key=(a,b)
            val=(h,a[h],typ,w)
            if key in edges and edges[key]!=val:
                conflicts.append((key,edges[key],val))
            edges[key]=val
    return dict(vertices=vertices,edges=edges,faces=faces,offsets=g,conflicts=conflicts,
                grid_intersections=candidates,triple_intersections=triples,
                radius=radius,nmax=nmax)


def quaternion_su2(vec):
    """Unit quaternion -> SU2 matrix (det=1, U*U=I)."""
    a,b,c,d=vec/np.linalg.norm(vec)
    return np.array([[a+1j*b,c+1j*d],[-c+1j*d,a-1j*b]],dtype=complex)


def test_wilson_gauge(q, rounds=3, max_faces=50):
    """Original-basis-edge SU2 Wilson gauge invariance on true P3 rhombi."""
    vs=sorted(q['vertices']); es=q['edges']; fs=list(q['faces']); rng=np.random.default_rng(20261107)
    checks=0; maxdiff=0.0
    fs=fs[::max(1,len(fs)//max_faces)][:max_faces]
    for _ in range(rounds):
        G={v:quaternion_su2(rng.normal(size=4)) for v in vs}
        U={e:quaternion_su2(rng.normal(size=4)) for e in es}
        Ug={(a,b):G[a]@u@G[b].conj().T for (a,b),u in U.items()}
        for corners in fs:
            directed=[(corners[0],corners[1]),(corners[1],corners[2]),
                      (corners[2],corners[3]),(corners[3],corners[0])]
            def holonomy(table):
                hol=np.eye(2,dtype=complex)
                for a,b in directed:
                    key=(a,b)
                    hol=hol@(table[key] if key in table else table[(b,a)].conj().T)
                return np.trace(hol)/2
            diff=abs(holonomy(U)-holonomy(Ug))
            maxdiff=max(maxdiff,float(diff))
            assert diff < 1e-12, diff
            checks+=1
    return checks,maxdiff


def verify(q, spectrum=True):
    verts=sorted(q['vertices']);ev=q['edges'];fc=q['faces']; idx={m:i for i,m in enumerate(verts)}
    assert not q['conflicts']
    n=len(verts); m=len(ev); f=len(fc)
    assertions=0
    # Index-sum theorem exact for all integer labels.
    sums=collections.Counter(sum(x) for x in verts)
    for x in verts:
        assert sum(x) in (1,2,3,4); assertions+=1
    # Isolated diagonal projections are excluded by layer span <=3.
    classes=set()
    for x in verts:
        v=tuple(x[j]-x[4] for j in range(4))
        assert v not in classes; classes.add(v);assertions+=1
    # Edges are original basis steps, supporting a sum-parity bipartition.
    adjacency=[set() for _ in verts]
    for (a,b),(h,k,typ,w) in ev.items():
        assert 0<=h<5 and k==a[h]
        assert sum(b)==sum(a)+1
        assert (sum(a)+sum(b))%2==1
        assert abs(w-(TA if typ=='A' else TB))<1e-13
        adjacency[idx[a]].add(idx[b]);adjacency[idx[b]].add(idx[a]);assertions+=4
    # Every enumerated rhombus has a closed Z5 boundary and exactly its 4 edges.
    incidences=collections.Counter()
    for corners,(j,k,n0,m0) in fc.items():
        assert len(set(corners))==4
        assert sum(corners[0]) in (1,2)
        assert sum(corners[2]) in (3,4)
        directed=[(corners[0],corners[1]),(corners[1],corners[2]),
                  (corners[2],corners[3]),(corners[3],corners[0])]
        for a,b in directed:
            assert (a,b) in ev or (b,a) in ev
            incidences[tuple(sorted([a,b]))]+=1
            assertions+=1
        assertions+=3
    assert all(v in (1,2) for v in incidences.values())
    assert len(incidences)==m
    assert n-m+f==1, (n,m,f,n-m+f)
    # Complete connected graph, finite 2-complex topologically a disk.
    seen={0};stack=[0]
    while stack:
        for k in adjacency[stack.pop()]:
            if k not in seen:seen.add(k);stack.append(k)
    assert len(seen)==n
    # Conditional source-equivalence audit: among the same selected P3 labels,
    # adding every allowed ±e_j nearest-basis pair makes NO extra bond.
    # This tests a literal Paper2 §8.2 reading against the genuine P3 graph,
    # not against a different acceptance-window or extra-vertex generator.
    all_basis={}
    selected=set(verts)
    for a in selected:
        for direction in range(5):
            b=list(a);b[direction]+=1;b=tuple(b)
            if b in selected:
                all_basis[(a,b)]=direction
                assertions+=1
    assert set(all_basis)==set(ev), (len(all_basis),len(ev),len(set(all_basis)-set(ev)))
    # Verify no edge crossings (except actual shared endpoints), if shapely exists.
    # This is an auxiliary finite geometric consistency test.
    coords=np.asarray(verts,dtype=float)@D
    edge_list=list(ev)
    try:
        from shapely.geometry import LineString
        from shapely.strtree import STRtree
        segments=[LineString([coords[idx[a]],coords[idx[b]]]) for a,b in edge_list]
        tree=STRtree(segments)
        cross=0
        for i,seg in enumerate(segments):
            for j in tree.query(seg):
                j=int(j)
                if j<=i or set(edge_list[i])&set(edge_list[j]):continue
                if seg.intersects(segments[j]):cross+=1
        assert cross==0,cross
        no_cross=True
    except ImportError:
        no_cross=None
    # Trace moments are exact polynomial checks on the finite weighted graph.
    degree=np.zeros(n);degree_count=np.zeros(n);squares=0.0
    edge_types=collections.Counter()
    rows=[];cols=[];data=[]
    for (a,b),(_,_,typ,w) in ev.items():
        i=idx[a];j=idx[b]
        edge_types[typ]+=1
        degree[i]+=w;degree[j]+=w;degree_count[i]+=1;degree_count[j]+=1
        squares+=2*w*w
        rows.extend([i,j]);cols.extend([j,i]);data.extend([-w,-w])
    import scipy.sparse as sp
    A=sp.coo_matrix((data,(rows,cols)),shape=(n,n)).tocsr()
    L=A+sp.diags(degree)
    assert abs(L.sum()) <1e-7
    moments={"trace_L":float(degree.sum()),"trace_L_squared":float(np.dot(degree,degree)+squares)}
    if spectrum:
        evals=np.linalg.eigvalsh(L.toarray())
        assert evals[0]>-1e-10
        assert abs(evals[0])<1e-9
        assert evals[1]>0
        assert abs(evals.sum()-moments['trace_L'])<1e-7
        assert abs(np.dot(evals,evals)-moments['trace_L_squared'])<1e-7
        # Trace e^{-tL}, scalar spectral diagnostic only (not physical YM).
        moments['spectral_gap_finite_scalar']=float(evals[1]);
        moments['heat_trace_per_site_t1']=float(np.exp(-evals).mean())
        # Paper1 says 'degree matrix' without disambiguating ordinary versus
        # weighted degree. Both interpretations must stay separately visible.
        count_evals=np.linalg.eigvalsh((A+sp.diags(degree_count)).toarray())
        assert count_evals[0]>0
        assert count_evals[0] > evals[0]+1e-5
        moments['count_degree_D_minus_weighted_W']={
            'minimum_eigenvalue':float(count_evals[0]),
            'trace_L':float(degree_count.sum()),
            'heat_trace_per_site_t1':float(np.exp(-count_evals).mean()),
            'zeta_minus_half_mass_squared_one':float(np.sqrt(count_evals+1).mean())}
        moments['weighted_degree_D_minus_W_zeta_minus_half_mass_squared_one']=float(np.sqrt(np.maximum(evals+1,0)).mean())
        assertions+=7
    wilson_checks,wilson_error=test_wilson_gauge(q)
    assertions+=wilson_checks
    assert abs(float(gamma_source().sum()))<1e-12
    assertions+=8
    return {
        "claimed_source":"Paper1 §§6.1,7.1 equations (12)-(14), plus Paper2 §8.2 cross-reference",
        "provenance_status":"published mathematical rules reconstructed; NOT original numerical generator",
        "radius_projected":q['radius'],"grid_level_limit":q['nmax'],"offsets":q['offsets'].tolist(),
        "vertex_count":n,"edge_count":m,"rhombus_count":f,"Euler_V_minus_E_plus_F":n-m+f,
        "sum_layers":{str(k):v for k,v in sorted(sums.items())},
        "edge_types":dict(edge_types),"observed_A_to_B_ratio":edge_types['A']/max(1,edge_types['B']),
        "mean_degree":2*m/n,"all_edges_original_basis_steps":True,
        "graph_bipartite_by_integer_sum":True,"pentagonal_cycles":0,
        "no_crossing_finite_patch":no_cross,
        "finite_weighted_Laplacian":moments,
        "su2_original_link_wilson_gauge_checks":wilson_checks,
        "su2_wilson_max_gauge_error":wilson_error,
        "D_definition_in_paper1":"D described as degree matrix, weighted vs ordinary degree not disambiguated in source",
        "no_triple_intersections_in_search":q['triple_intersections']==0,
        "assertions_passed":assertions,
        "original_paper2_coupled_generator_authenticated":False,
        "original_paper2_zeta_numbers_reproduced":False,
        "continuum_YM_gap_proved":False
    }


def main():
    p=argparse.ArgumentParser();p.add_argument('--radius',type=float,default=6.5)
    p.add_argument('--grid-levels',type=int,default=11)
    p.add_argument('--output',type=Path,default=None)
    p.add_argument('--no-spectrum',action='store_true',help='skip dense spectral diagonalisation')
    args=p.parse_args()
    obj=verify(generate(args.radius,args.grid_levels),spectrum=not args.no_spectrum)
    doc=json.dumps(obj,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(doc)
    print(doc)
if __name__=='__main__':main()
