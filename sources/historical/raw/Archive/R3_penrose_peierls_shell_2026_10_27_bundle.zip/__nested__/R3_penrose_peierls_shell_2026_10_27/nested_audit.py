#!/usr/bin/env python3
"""Nested genuine Z5 Penrose spatial rhombus disks x 3-step periodic time.
Sparse signed integer incidence and exact modular face-matroid ranks.
"""
from pathlib import Path
from collections import defaultdict, Counter
from itertools import combinations
import sys,json,time
import numpy as np
from direct_cut_project import build,validate,face_label_sets
ROOT=Path(__file__).resolve().parent
P=1000003

def rank_mod_columns(cols,allowed=None,mod=P):
    # Signed-sparse GF(p) column elimination. Allowed rows if specified.
    allowed=None if allowed is None else set(allowed)
    basis={}
    for col in cols:
        v={k:(int(x)%mod) for k,x in col.items() if x and (allowed is None or k in allowed)}
        while v:
            k=min(v)
            c=basis.get(k)
            if c is None:
                inv=pow(v[k],-1,mod)
                basis[k]={i:(a*inv)%mod for i,a in v.items()}
                break
            scale=v[k]
            for i,a in c.items():
                t=(v.get(i,0)-scale*a)%mod
                if t:v[i]=t
                else:v.pop(i,None)
    return len(basis)

def complex_3(g,nt=3):
    # Face orientation from CCW input face; edge orientation from smaller to larger vertex.
    V,E,F=len(g.labels),len(g.edges),len(g.faces)
    eind={pair:i for i,pair in enumerate(g.edges)}
    edge_spatial=[]
    for face in g.faces:
        items=[]
        for a,b in zip(face,face[1:]+face[:1]):
            idx=eind[tuple(sorted((a,b)))];sg=1 if a<b else -1
            items.append((idx,sg))
        edge_spatial.append(items)
    he=lambda t,e:t*E+e
    ve=lambda t,v:nt*E+t*V+v
    cols=[]; meta=[]
    # first spatial faces in every slice
    for t in range(nt):
        for f,w in enumerate(edge_spatial):
            col={he(t,e):sg for e,sg in w}
            cols.append(col);meta.append(('s',t,f))
    # then temporal faces in every time interval and spatial edge
    for t in range(nt):
        for e,(a,b) in enumerate(g.edges):
            # oriented rectangle + lower edge, + upper target vertical, - upper edge, - lower vertical
            nxt=(t+1)%nt
            col={he(t,e):1,ve(t,b):1,he(nxt,e):-1,ve(t,a):-1}
            cols.append(col);meta.append(('t',t,e))
    assert len(cols)==nt*(F+E)
    return cols,meta

def seed_support(g,mode='two-loop'):
    # fixed, nested label-based support. Faces nearest origin and two adjacent neighbors.
    centres=np.asarray([g.xy[list(f)].mean(axis=0) for f in g.faces]);root=int(np.argmin(np.linalg.norm(centres,axis=1)))
    f0=g.faces[root]; neibs=[]
    for i,f in enumerate(g.faces):
        if i==root:continue
        if len(set(f)&set(f0))==2:neibs.append((float(np.linalg.norm(centres[i])),i))
    ids=[root]+[f for _,f in sorted(neibs)[:2]]
    assert len(ids)==3
    edge_idx={pair:i for i,pair in enumerate(g.edges)}
    edgesets=[]
    for i in ids:
        face=g.faces[i];edgesets.append({edge_idx[tuple(sorted((a,b)))] for a,b in zip(face,face[1:]+face[:1])})
    # two temporal intervals with overlapping spatial edge selection
    temporal_support={(0,e) for e in edgesets[0]|edgesets[1]}
    temporal_support.update((1,e) for e in edgesets[0]|edgesets[2])
    # face-normalized anchored labels to match across radii
    base=set(g.labels[v] for i in ids for v in g.faces[i])
    canonical=[sorted(tuple(sorted((g.labels[u],g.labels[v]))) for e in sorted(s) for u,v in [g.edges[e]]) for s in edgesets]
    return {'face_indices':ids,'face_labels':[tuple(sorted(g.labels[v] for v in g.faces[i])) for i in ids], 'supports': temporal_support,'source_labels':base,'edgesets':edgesets,'canonical_edgesets':canonical}

def embed_support(seed,g):
    face_map={tuple(sorted(g.labels[v] for v in f)):i for i,f in enumerate(g.faces)}
    ids=[face_map[tuple(k)] for k in seed['face_labels']]
    eind={tuple(sorted((g.labels[u],g.labels[v]))):i for i,(u,v) in enumerate(g.edges)}
    edgesets=[{eind[p] for p in lst} for lst in seed['canonical_edgesets']]
    support={(0,e) for e in edgesets[0]|edgesets[1]}
    support|={(1,e) for e in edgesets[0]|edgesets[2]}
    return ids,support

def local_rank_audit(g,cols,meta,Q,nearby_extra=0,fullrank=False):
    nV,nE,nF=len(g.labels),len(g.edges),len(g.faces); Nedges=3*(nE+nV)
    Qset=set(Q);ret=[col for i,col in enumerate(cols) if i not in Qset]
    subset=[cols[i] for i in Q]
    local0=set(k for col in subset for k in col)
    L=set(local0)
    # added collar by minimum geometric midpoint distance (around affected volume)
    # adjacency metric on graph of 3D link variables: shortest cell-combinatorial radius
    # at each iteration add all links that share one retained/included face with current L
    Qr=[]
    for rad in range(nearby_extra+1):
        rRet=rank_mod_columns(ret,L);rFull=rank_mod_columns(cols,L)
        Qr.append((len(L),rRet,rFull))
        if rad<nearby_extra:
            L|=set(k for col in cols if any(e in L for e in col) for k in col)
    globalrankR=rank_mod_columns(ret) if fullrank else None
    globalrankF=3*nE
    # Full geometric rank identity for a disk x S1 = 3 E
    def extpair(tup):
        count,r0,r1=tup
        if globalrankR is None:return None
        return [globalrankR-r0,globalrankF-r1]
    return {'face_Q':Q,'local_link_count':len(local0),'collar_radii':[{'r':i,'links':int(n),'local_retained_rank':int(r0),'local_full_rank':int(r1),'exterior_ranks':extpair((n,r0,r1))} for i,(n,r0,r1) in enumerate(Qr)],'global_retained_rank':globalrankR,'global_full_rank':globalrankF}

if __name__=='__main__':
    radii=[5.,6.5,8.,10.]; seed=None;reports=[]
    for r in radii:
        t0=time.time();g,gamma=build(r,0);geo=validate(g,gamma)
        if seed is None:seed=seed_support(g)
        ids,support=embed_support(seed,g)
        cols,meta=complex_3(g);Q=sorted([i for i,m in enumerate(meta) if m[0]=='t' and (m[1],m[2]) in support]);assert len(Q)==len(support)
        aud=local_rank_audit(g,cols,meta,Q,nearby_extra=2,fullrank=(r<=6.5))
        rep={'radius':r,'geometry':geo,'prisms':3*geo['faces'],'three_dim_faces':len(cols),'links':3*(geo['vertices']+geo['edges']),'support_face_ids':Q,'support_keys':[meta[i] for i in Q],'anchor_face_ids':ids,'audit':aud,'seconds':time.time()-t0}
        reports.append(rep)
        print('radius',r,'geo',geo['vertices'],geo['edges'],geo['faces'],'support',len(Q),'ranks',[(x['links'],x['local_retained_rank'],x['local_full_rank']) for x in aud['collar_radii']],'global',aud['global_retained_rank'],'seconds',round(rep['seconds'],2),flush=True)
    (ROOT/'nested_certificate.json').write_text(json.dumps({'source':'direct_cut_project.py from uploaded Phase III certified Z5 window-first study','seed':{k:([[int(x) for x in lab] for lab in v] if k=='source_labels' else v) for k,v in seed.items() if k in ['face_labels']},'results':reports},default=lambda x:list(x) if isinstance(x,(tuple,set)) else int(x),indent=2))

def cell_boundaries(g,nt=3):
    V,E,F=len(g.labels),len(g.edges),len(g.faces)
    eind={pair:i for i,pair in enumerate(g.edges)};ncells=nt*F;nsf=nt*F
    cells=[]
    for t in range(nt):
        nxt=(t+1)%nt
        for f,vs in enumerate(g.faces):
            col={nxt*F+f:1,t*F+f:-1}
            for a,b in zip(vs,vs[1:]+vs[:1]):
                e=eind[tuple(sorted((a,b)))];sg=1 if a<b else -1
                col[nsf+t*E+e]=sg
            cells.append(col)
    return cells

def bianchi_peel(cols,cells,Q):
    # Formal group-level certificate under van Kampen prism Bianchi.
    # Each cell has six boundary faces, and we peel a q using a cell touching exactly one active q.
    remaining=set(Q); eliminated=[]; qexpr={}
    while True:
        opts=[]
        for ci,col in enumerate(cells):
            qs=[f for f in col if f in remaining]
            if len(qs)==1:
                q=qs[0];opts.append((sum(f in Q for f in col),ci,q))
        if not opts:break
        _,ci,q=min(opts);remaining.remove(q)
        c=cells[ci];rel={f:-sg*c[q] for f,sg in c.items() if f!=q}
        # q expressed as signed sum of other five face 2-chains
        # replace earlier Q symbols by their already-expanded retained chains
        # if q touches another original Q already eliminated, substitute known expression
        flat={}
        for f,coef in rel.items():
            if f in qexpr:
                for h,v in qexpr[f].items():flat[h]=flat.get(h,0)+coef*v
            else:flat[f]=flat.get(f,0)+coef
        qexpr[q]={f:v for f,v in flat.items() if v}
        eliminated.append({'face':q,'cell':ci,'relator_original_support':len(c),'expanded_L1':sum(map(abs,qexpr[q].values()))})
    return eliminated,remaining,qexpr

def sparse_boundary_projection_rank(cells,Q):
    return rank_mod_columns([{f:coef for f,coef in c.items() if f in set(Q)} for c in cells])
