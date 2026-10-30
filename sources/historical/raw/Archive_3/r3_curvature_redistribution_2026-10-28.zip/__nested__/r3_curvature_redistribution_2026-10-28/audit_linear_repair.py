#!/usr/bin/env python3
"""Exact rational rank audit of tangent SU(2) plaquette curvature redistribution.
Usage: python audit_linear_repair.py incidence.json [--out report.json]
First order only; NOT a nonabelian nonlinear or Gibbs probability certificate.
"""
import argparse,collections,json,pathlib
from sympy import Matrix

def audit(o):
    F=o['faces']; C=o['cavity_faces']; Q=o['inserted_faces']; free=o['integrated_edges'];E=o['edges']
    loc={e:i for i,e in enumerate(free)}
    def mat(fs,edge_subset):
        inds={e:i for i,e in enumerate(edge_subset)}
        rows=[]
        for f in fs:
            rr=[0]*len(edge_subset)
            for e,s in F[f]:
                if e in inds:rr[inds[e]]+=s
            rows.append(rr)
        return Matrix(rows) if rows else Matrix.zeros(0,len(edge_subset))
    # Edges in seed, successive face-adjacent collars of cavity faces.
    face_edges={f:set(e for e,s in word) for f,word in F.items()}
    selected=set(Q);reports=[]
    for depth in range(5):
        edges=sorted(set().union(*(face_edges[f] for f in selected)) & set(free))
        # Include ALL cavity constraints affected by edge changes, not only those within the collar.
        touched=[f for f in C if face_edges[f]&set(edges)]
        Ac=mat(touched,edges);Aq=mat(Q,edges)
        r0=Ac.rank();r1=Ac.col_join(Aq).rank()
        reports.append({'depth':depth,'faces_in_collared_region':len(selected),'movable_edges':len(edges),
                        'affected_cavity_faces':len(touched),'rank_cavity':r0,
                        'rank_cavity_plus_insertions':r1,'accessible_inserted_rank':r1-r0,
                        'inserted_face_count':len(Q),'all_inserted_directions_accessible':r1-r0==len(Q)})
        all_edges=set().union(*(face_edges[f] for f in selected))
        selected|={f for f in F if face_edges[f]&all_edges}
    # Rank test for fixed exterior edge changes: this is a tangent linear test near all-identity.
    return {'schema':'r3-linearized-redistribution-v1','interpretation':'SU(2) Lie algebra first-order incidence rank only; three color coordinates share this rank; not a nonlinear gauge repair, finite-action estimate or Gibbs bound',
            'n_q':len(Q),'n_cavity':len(C),'n_integrated_edges':len(free),'collar_audit':reports,
            'limitation':'If all Q directions are accessible this is only infinitesimal controllability, not existence of a uniformly bounded nonlinear measure-preserving map.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('incidence');ap.add_argument('--out');args=ap.parse_args()
    data=json.loads(pathlib.Path(args.incidence).read_text());r=audit(data)
    if args.out:pathlib.Path(args.out).write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
if __name__=='__main__': main()
