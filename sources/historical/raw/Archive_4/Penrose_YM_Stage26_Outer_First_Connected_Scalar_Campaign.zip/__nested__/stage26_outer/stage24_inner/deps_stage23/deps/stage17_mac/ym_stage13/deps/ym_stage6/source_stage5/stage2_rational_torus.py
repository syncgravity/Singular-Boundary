"""Rational-plane Z5 periodic model-set torus adapter for corrected 2+1D Wilson geometry.

This *candidate* is checked from accepted lattice-window membership, not the
superseded de Bruijn graph generator. It is not a canonical Penrose inflation
supertile. All periodic edge displacement vectors are taken from the projected
parent basis, NOT differences of canonical wrapped coordinates.
"""
from __future__ import annotations
import hashlib,json
import numpy as np
from penrose_causal_study import Approximant,face_orientation_audit,pentagon_window_audit


def build_torus(M=8):
    approx=Approximant(M)
    if approx.stats()['euler_torus']!=0 or not np.all(approx.incidence==2):
        raise ValueError('not a valid torus cellulation')
    if not face_orientation_audit(approx)['all_opposite']:
        raise ValueError('opposite orientation per edge violated')
    if pentagon_window_audit(approx)!={1:5,2:5,3:5,4:5}:
        raise ValueError('wrong rational acceptance-window geometry')
    proj=approx.Qpar@np.eye(5)
    E=len(approx.edges)
    edges=np.empty((E,2),dtype=np.int64)
    vectors=np.empty((E,2),float)
    edgeids={}
    for i,(u,v,j) in enumerate(approx.edges):
        if u==v:raise ValueError('self-loop')
        x,y=sorted((int(u),int(v)))
        edgeids[(x,y)]=i
        edges[i]=(x,y)
        vectors[i]=(1 if u<v else -1)*proj[:,j]
    if len(edgeids)!=E:raise ValueError('multi-edges require distinct loop IDs and corrected path code')
    F=len(approx.faces)
    face_idx=np.empty((F,4),dtype=np.int64)
    face_sign=np.empty_like(face_idx)
    areas=np.empty(F,float)
    for i,(u,ua,uab,ub,a,b) in enumerate(approx.faces):
        cross=float(np.linalg.det(proj[:,[a,b]]))
        if abs(cross)<1e-10: raise ValueError('degenerate face')
        areas[i]=abs(cross)
        face=(u,ua,uab,ub) if cross>0 else (u,ub,uab,ua)
        for j in range(4):
            x,y=int(face[j]),int(face[(j+1)%4]);
            k=edgeids[tuple(sorted((x,y)))]
            face_idx[i,j]=k;face_sign[i,j]=1 if x<y else -1
    xy=np.asarray(approx.nodes,dtype=float)@approx.Qpar.T
    periods=np.column_stack([approx.Qpar@approx.t1,approx.Qpar@approx.t2])
    parea=abs(np.linalg.det(periods))
    if abs(sum(areas)-parea)/parea>1e-8:
        raise AssertionError('period area != sum of rhombic face areas')
    h=hashlib.sha256(json.dumps({'M':M,'t1':approx.t1.tolist(),
                                't2':approx.t2.tolist(),'nodes':approx.nodes},sort_keys=True).encode()).hexdigest()
    return {'V':len(approx.nodes),'E':E,'F':F,'xy':xy,'edges':edges,
            'face_idx':face_idx,'face_sign':face_sign,'face_areas':areas,
            'edge_vectors':vectors,'physical_area':parea,'periods':periods,
            'graph_hash':h,'stats':approx.stats(),'spatial_kind':'rational_modelset_torus',
            'approximation_scale':M}
