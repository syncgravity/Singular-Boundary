#!/usr/bin/env python3
"""Exact relative exterior mode bases on nested direct-Z5 Penrose SU(2) prism cavities.
24 means real oriented incidence rank quotient for Q14's INITIAL 36-link H,
not the one-link B2 collar. (Tangent SU2 has 3 real dimensions per mode.)
"""
import json
from pathlib import Path
from collections import Counter,defaultdict
import numpy as np
from direct_cut_project import build
from construct_surgery import product_collar,shell
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent
PRIMES=(1000003,1000033)

def pivot_basis(cols,p=1000003):
    # faces are rows; cols contain signed coefficients across face index 0..n-1
    base={};accepted=[]
    for lab,init in cols:
        v={i:int(c)%p for i,c in init.items() if c%p}
        while v:
            k=min(v)
            if k not in base:
                factor=pow(v[k],-1,p)
                base[k]={i:(x*factor)%p for i,x in v.items()}
                accepted.append(lab);break
            fac=v[k]
            for i,x in base[k].items():
                nx=(v.get(i,0)-fac*x)%p
                if nx:v[i]=nx
                else:v.pop(i,None)
    return accepted

def link_key(g,e):
    E=len(g.edges);V=len(g.labels)
    if e<3*E:
        t,j=divmod(e,E);a,b=g.edges[j]
        return ['horizontal',t,[list(g.labels[a]),list(g.labels[b])]]
    t,v=divmod(e-3*E,V)
    return ['vertical',t,list(g.labels[v])]

def analyze(g):
    words,meta=product_collar(g);Q=Q_from_seed(g,seed_support(build(5.,0)[0]));R=set(range(len(words)))-Q
    H={e for q in Q for e,_ in words[q]};K=shell(H,words,R);KK=shell(K,words,R)
    reports=[]
    for j,B in enumerate((H,K,KK)):
        A=sorted(p for p in R if any(e in B for e,s in words[p]))
        active=sorted({e for p in A for e,s in words[p]});ext=sorted(set(active)-B)
        # Each column is the effect of a link rotation on 1 Lie-algebra component of the 62 face curvatures.
        inc={e: {i:s for i,p in enumerate(A) for ee,s in words[p] if ee==e} for e in active}
        inside=[(e,inc[e]) for e in sorted(B)]
        outside=[(e,inc[e]) for e in ext]
        basis_local=pivot_basis(inside);outside_new=pivot_basis(inside+outside)[len(basis_local):]
        for p in PRIMES:
            la=pivot_basis(inside,p);full=pivot_basis(inside+outside,p)
            assert len(la)==len(basis_local) and len(full)==len(basis_local)+len(outside_new)
        assert len(A)-len(basis_local)-len(outside_new)>=0
        if j==0:assert (len(H),len(A),len(basis_local),len(outside_new))==(36,62,35,24)
        # For each independent exterior pivot, record its bounded support and linking incidence.
        members=[]
        for e in outside_new:
            fs=[p for p in R if any(ee==e for ee,s in words[p])]
            members.append({'link_id':e,'key':link_key(g,e),'retained_faces_touching_pivot':len(fs),'retained_faces_in_original_A':sum(p in A for p in fs),
                            'face_ids':fs,'face_types':dict(Counter(meta[f][0] for f in fs))})
        # Conflict graph: two selected links interact if any retained plaquette contains both.
        shared=defaultdict(set)
        for i,e in enumerate(outside_new):
            for f in members[i]['face_ids']:shared[f].add(e)
        adj={e:set() for e in outside_new}
        for fs in shared.values():
            for e in fs:adj[e]|=set(fs)-{e}
        colors={}
        for e in sorted(outside_new,key=lambda x:(-len(adj[x]),x)):
            used={colors[v] for v in adj[e] if v in colors}
            colors[e]=min(c for c in range(100) if c not in used)
        # any selected exterior pivot touches <= ν total retained faces; reconstruct whole affected set for action audit
        action_faces=sorted(p for p in R if any(e in outside_new for e0,s in words[p] for e in [e0]))
        expected_colors=max(colors.values())+1
        groups=defaultdict(list)
        for e,c in colors.items():groups[c].append(e)
        for group in groups.values():
            for f in action_faces:assert sum(e==ee for e in group for ee,s in words[f])<=1
        reports.append({'shell':j,'adjustable_links':len(B),'A_faces':len(A),'exterior_halo_links':len(ext),
         'rank_local':len(basis_local),'rank_full':len(basis_local)+len(outside_new),
         'independent_exterior_modes':len(outside_new),'remaining_face_dependencies':len(A)-len(basis_local)-len(outside_new),
         'basis_exterior':members,'chosen_exterior_link_ids':outside_new,'colors':[groups[c] for c in sorted(groups)],
         'color_count':expected_colors,'conflict_max_degree':max(map(len,adj.values())),
         'retained_faces_touched_by_24_mode_links':len(action_faces),
         'link_types':dict(Counter(link_key(g,e)[0] for e in outside_new)),
         'temporal_layers':dict(Counter(str(link_key(g,e)[:2]) for e in outside_new)),
         'selected_basis_link_max_retained_face_incidence':max(sum(e==ee for f in R for ee,s in words[f]) for e in outside_new),
         'support_union_size':len(B|set(outside_new))})
    return reports

def main():
    results=[];canonical=None
    for radius in [5.,6.5,8.,10.]:
        g,_=build(radius,0);layers=analyze(g)
        print(radius,[(d['adjustable_links'],d['A_faces'],d['independent_exterior_modes'],d['color_count']) for d in layers],flush=True)
        if canonical is None:
            canonical=[[x['key'] for x in layer['basis_exterior']] for layer in layers]
        else:
            assert canonical==[[x['key'] for x in layer['basis_exterior']] for layer in layers]
        results.append({'radius':radius,'layers':layers})
    cert={'Q':'14 temporal faces near origin, anchored by exact Z5 labels',
          'definition':'linearized exterior directions = rank(D_A over all affected links) - rank(D_A restricted to adjustable H)',
          'warning':'24 modes refer to original H=36 inserted-face links, A=62; H=125 one-shell has 46 modes; H=258 two-shell has 63.',
          'tangent_dimensions':'24 SU2 tangent directions means 72 real infinitesimal components, not 24 disconnected gauge invariant Wilson loops',
          'verification':'exact finite field mod 1000003 and 1000033; canonical Z5 exterior pivot link selection agrees across four volumes',
          'results':results,'scope':'exterior link column quotient basis, not a nonabelian action-coercive repair'}
    (ROOT/'modes_certificate.json').write_text(json.dumps(cert,indent=2))
if __name__=='__main__':main()
