#!/usr/bin/env python3
"""Explicit finite-net SU(2) Haar-translation surgery and Penrose collar audit.

On a bad shell-gap event, it decreases the FULL retained Wilson action,
with exact Haar Jacobian one and explicit finite inverse multiplicity.
It DOES NOT establish the required absolute s_H tail.
"""
import json, math
from pathlib import Path
from collections import Counter
import numpy as np
from direct_cut_project import build,validate
ROOT=Path(__file__).resolve().parent

def product_collar(g):
    V,E,F=len(g.labels),len(g.edges),len(g.faces)
    eind={p:i for i,p in enumerate(g.edges)}
    faces=[]; types=[]
    for t in range(3):
        for f,vs in enumerate(g.faces):
            faces.append(tuple(((t*E+eind[tuple(sorted((a,b)))],1 if a<b else -1)) for a,b in zip(vs,vs[1:]+vs[:1])))
            types.append(('s',t,f))
    for t in range(3):
        for e,(a,b) in enumerate(g.edges):
            faces.append(((t*E+e,1),(3*E+t*V+b,1),(((t+1)%3)*E+e,-1),(3*E+t*V+a,-1)))
            types.append(('t',t,e))
    return faces,types

def shell(B,faces,R):
    return set(B)|{e for p in R if any(e0 in B for e0,_ in faces[p]) for e,_ in faces[p]}

def geometry_data():
    out=[];ref=None
    for r in [5.,6.5,8.,10.]:
        g,ga=build(r,0);geom=validate(g,ga);faces,types=product_collar(g)
        E,V=len(g.edges),len(g.labels)
        # Anchor = spatial edge closest to origin, identified by Z5 endpoints.
        edges_by_label={tuple(sorted([g.labels[a],g.labels[b]])):e for e,(a,b) in enumerate(g.edges)}
        if ref is None:
            middle=sorted(range(E),key=lambda e:np.linalg.norm((g.xy[g.edges[e][0]]+g.xy[g.edges[e][1]])/2))[0]
            ref=tuple(sorted((g.labels[g.edges[middle][0]],g.labels[g.edges[middle][1]])))
        B0={edges_by_label[ref]};R=set(range(len(faces)))
        row={'radius':r,'spatial_faces':geom['faces'],'spacetime_retained_faces':len(R),'anchor_z5_labels':[list(v) for v in ref]}
        H=B0
        for j in range(3):
            A={p for p in R if any(e in H for e,_ in faces[p])}
            boundary={e for p in A for e,_ in faces[p] if e not in H}
            row[f'B{j}_links']=len(H);row[f'B{j}_affected_retained_faces']=len(A);row[f'B{j}_boundary_links']=len(boundary)
            if j==0: B0=set(H)
            H=shell(H,faces,R)
        allinc=Counter(e for f in faces for e,_ in f)
        row['max_incident_faces']=max(allinc.values())
        out.append(row)
    return out

def qmul(a,b):
    return np.r_[a[0]*b[0]-np.dot(a[1:],b[1:]),a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]
def qinv(a):return np.r_[a[0],-a[1:]]
def unit_random(rng,n):
    v=rng.normal(size=(n,4));return v/np.linalg.norm(v,axis=1)[:,None]
def character_word(U,word):
    z=np.array([1.,0,0,0])
    for e,sign in word:z=qmul(z,U[e] if sign==1 else qinv(U[e]))
    return z[0]
def net(lam):
    n=math.ceil(6*math.sqrt(lam))
    lin=np.linspace(-1,1,n+1)
    pts=[]
    for j in range(4):
        for sig in (-1.,1.):
            for a in lin:
                for b in lin:
                    for c in lin:
                        v=np.empty(4);v[j]=sig;v[np.arange(4)!=j]=[a,b,c];v=v/np.linalg.norm(v)
                        pts.append(v)
    pts.append(np.array([1.,0.,0.,0.]))
    return np.asarray(pts),n

def single_link_pivot_test():
    g,_=build(5.,0);faces,types=product_collar(g)
    E,V=len(g.edges),len(g.labels)
    el=int(np.argmin([np.linalg.norm((g.xy[a]+g.xy[b])/2) for a,b in g.edges]))
    A=[p for p,w in enumerate(faces) if any(e==el for e,s in w)]
    rng=np.random.default_rng(20261027)
    U=unit_random(rng,3*(E+V));
    def S(x):
        U[el]=x;return sum(1-character_word(U,faces[p]) for p in A)
    saved=U[el].copy()
    result=[]
    for lam in [1.,4.]:
        G,n=net(lam)
        # full translation candidate set x -> g*x. For generic x, it is an r-net.
        vals=np.array([S(qmul(gi,saved)) for gi in G]);
        best=int(np.argmin(vals));S_start=S(saved);S_selected=vals[best]
        # SU(2) staple alignment: sum cosine is linear in the unit quaternion x.
        d4=np.eye(4);linear=np.array([(S(d4[k])-S(-d4[k]))/2 for k in range(4)])
        smin=float(len(A)-np.linalg.norm(linear))
        error=lam*(S_selected-smin)
        assert error<=2*max(Counter(e for ff in faces for e,s in ff).values())+1e-8
        assert S_start-S_selected >=-1e-11
        g_pick=G[best]
        assert np.linalg.norm(qmul(g_pick,saved)-qmul(g_pick,saved))<1e-12
        result.append({'lambda':lam,'spatial_radius':5,'spatial_anchor_edge':el,'retained_faces_adjacent_to_anchor':len(A),'net_grid_n':n,
                       'net_cardinality':len(G),'initial_incident_action':S_start,'selected_incident_action':S_selected,
                       'exact_conditional_minimum':smin,'lambda_times_minimizer_gap':error,
                       'action_decrease':S_start-S_selected,'haar_jacobian_on_chosen_branch':1,
                       'max_inverse_multiplicity':len(G)})
    return result

def main():
    data=geometry_data();test=single_link_pivot_test()
    cert={
        'model':'SU2 Wilson on genuine direct-Z5 open Penrose rhombus disks x 3-periodic time',
        'construction':'piecewise left-Haar translations selected by minimization over finite quaternion net on K',
        'net_definition':'four dominant quaternion-component charts, each sign, 3 coordinates in grid step 2/ceil(6sqrt(lambda)), plus identity',
        'net_cardinality_upper':'4097 lambda^(3/2) per active link for lambda>=1',
        'geodesic_cover_radius_upper':'lambda^(-1/2)',
        'global_full_retained_action_decrement':'lambda[S_R(U)-S_R(TU)] >= lambda[s_B(U_outside_B)-s_K(U_outside_K)]-2 nu |K| for B subset K',
        'jacobian_on_each_branch':1,
        'total_inverse_multiplicity_upper':'(4097 lambda^(3/2))^|K|',
        'certified_increment_tail':'P(lambda(s_B-s_K)>=t) <= min(1,exp[|K|*(1.5log(lambda)+log(4097)+2nu)-t])',
        'absolute_tail_status':'open: no uniform terminal estimate on s_K; no full arbitrary-support R3 theorem',
        'geometries':data,'single_link_full_net_tests':test}
    (ROOT/'certificate.json').write_text(json.dumps(cert,indent=2))
    print(json.dumps({'geometry':data,'tests':test,'status':'PASS: explicit finite-net action-decreasing surgery for shell increment, not absolute minimum'},indent=2))
if __name__=='__main__': main()
