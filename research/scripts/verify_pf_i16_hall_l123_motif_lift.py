#!/usr/bin/env python3
"""Finite L1-L3 check for PF-I16 Hall sources in the two Ngrid=7 PF targets.

This is deliberately only a port/matching-edge realization. It does not claim
L4-L8, interval supports, overlap witnesses, parent naturality, or Hall.
The target-side three-face motif and edge matching are frozen independently
of Hall loads, deficiencies, flows, and observer phases.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import defaultdict
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import verify_pf_i9_source_cut_project_bridge as cp
import export_pf_i16_hall_source_records as hall

NGRID=7
GAMMA=np.array([(j*np.sqrt(2)+j*j*np.sqrt(3))%1 for j in range(5)])
GAMMA-=GAMMA.mean()
GAMMA[4]=-GAMMA[:4].sum()
EXPECTED_CORE_LABEL_SHA="bb9aa7fca99bea4e32e2014190588e43d1913a179ecd1c2cccb25854d6cc4114"
EXPECTED_CORE_FACE_SHA="005605e2253ce7e04fe5ed6f5d512b1c19f54ca3d6ecacaca12c6dc5a86467b4"

# Three accepted PF-I16 source rhombi: (lower Z5 label, direction pair).
MOTIF=((0,1,0,0,0,2,3),
       (0,1,0,0,0,3,4),
       (0,1,0,0,1,0,3))
# Three pairwise vertex-disjoint links in that authenticated motif.
# The direction index is zero-based; each edge is oriented +e_j.
MOTIF_EDGES=(
 ((0,1,0,0,0),(0,1,0,0,1),4),
 ((0,1,0,1,0),(0,1,0,1,1),4),
 ((0,1,1,0,0),(0,1,1,1,0),3),
)

def sha_labels(labels):
    b="\n".join(",".join(map(str,v)) for v in sorted(labels))+"\n"
    return hashlib.sha256(b.encode()).hexdigest()

def sha_faces(faces):
    b="\n".join("|".join(",".join(map(str,v)) for v in f) for f in faces)+"\n"
    return hashlib.sha256(b.encode()).hexdigest()

def face_tuple(m,j,k):
    a=np.asarray(m,dtype=int)
    return (tuple(a),tuple(a+cp.BASIS[j]),
            tuple(a+cp.BASIS[j]+cp.BASIS[k]),tuple(a+cp.BASIS[k]))

def basis_edges(labels):
    S=set(labels); out=set()
    for a in S:
        for j in range(5):
            b=tuple(a[t]+int(t==j) for t in range(5))
            if b in S: out.add((a,b))
    return out

def accepted_faces(labels,gamma):
    S=set(labels); out=[]
    for a in sorted(S):
        for j,k in itertools.combinations(range(5),2):
            f=face_tuple(a,j,k)
            if all(v in S for v in f[1:]) and cp.direct_face_membership(a,j,k,gamma):
                out.append(f)
    return out

def original_source_complex(ngrid):
    """Independent indexed-pentagrid replay used by the PF-I16 audit."""
    vd={}; tiles=[]
    for j,k in itertools.combinations(range(5),2):
        a,b=cp.PAR[j],cp.PAR[k]
        det=a[0]*b[1]-a[1]*b[0]
        for nj in range(-ngrid,ngrid+1):
            for nk in range(-ngrid,ngrid+1):
                bj=nj+GAMMA[j]; bk=nk+GAMMA[k]
                point=np.array([(bj*b[1]-bk*a[1])/det,
                                (a[0]*bk-bj*a[0])/det])
                base=[0]*5
                for f in range(5):
                    if f not in (j,k):
                        base[f]=int(np.ceil(point@cp.PAR[f]-GAMMA[f]-1e-9))
                corners=[]
                for dj in (0,1):
                    for dk in (0,1):
                        m=base.copy();m[j]=nj+dj;m[k]=nk+dk
                        corners.append(tuple(m))
                if any(not 1<=sum(m)<=4 for m in corners): continue
                for m in corners: vd.setdefault(m,np.asarray(m)@cp.PAR)
                tiles.append((corners[0],corners[2],corners[3],corners[1]))
    center=np.mean(list(vd.values()),axis=0)
    centers=np.asarray([np.mean([vd[m] for m in t],axis=0) for t in tiles])
    dist=np.linalg.norm(centers-center,axis=1)
    inside=set(np.flatnonzero(dist<.35*float(dist.max())))
    vtiles=defaultdict(list)
    for ix,t in enumerate(tiles):
        for v in t: vtiles[v].append(ix)
    labels={v for v,ix in vtiles.items() if all(i in inside for i in ix)}
    edges=basis_edges(labels)
    faces=accepted_faces(labels,GAMMA)
    return labels,edges,faces,center,.35*float(dist.max())

def completed_window_core(ngrid,center,cutoff):
    direct=cp.build_direct(cutoff+4,GAMMA)
    incident=defaultdict(list)
    for f in direct["faces"]:
        fc=np.mean([direct["xy"][v] for v in f],axis=0)
        ok=np.linalg.norm(fc-center)<cutoff
        for v in f: incident[v].append(ok)
    labels={v for v,states in incident.items() if states and all(states)}
    edges=basis_edges(labels)
    faces=accepted_faces(labels,GAMMA)
    return labels,edges,faces

def window_margin(m):
    ok,violation=cp.direct_membership(tuple(m),GAMMA)
    if not ok: return -float(violation)
    return -float(violation)

def face_margin(m,j,k):
    h=sum(m); eq=cp.FACE_EQ[(j,k,h)]
    y=(np.asarray(m,dtype=float)+GAMMA)@cp.PERP
    return -float(np.max(y@eq[:,:2].T+eq[:,2]))

def check_target(name,labels,edges,faces,records):
    # The target-side motif is fixed before the Hall source records are read.
    motif_faces=[face_tuple(m,j,k) for *mjk,j,k in []]  # overwritten below
    motif_faces=[face_tuple(tuple(row[:5]),row[5],row[6]) for row in MOTIF]
    face_set=set(faces)
    if not all(f in face_set for f in motif_faces):
        raise AssertionError(f"{name}: authenticated three-face motif absent")
    edge_set=set(edges)
    for a,b,j in MOTIF_EDGES:
        if (a,b) not in edge_set: raise AssertionError(f"{name}: motif edge missing {(a,b)}")
        d=np.asarray(b)-np.asarray(a)
        if tuple(d)!=tuple(int(t==j) for t in range(5)):
            raise AssertionError("signed basis-edge label mismatch")
    endpoints=[v for a,b,j in MOTIF_EDGES for v in (a,b)]
    if len(set(endpoints))!=len(endpoints): raise AssertionError("motif edges are not vertex-disjoint")
    margins=[window_margin(v) for v in endpoints]
    if min(margins)<=1e-9: raise AssertionError(f"{name}: non-strict vertex acceptance")
    f_margins=[face_margin(tuple(row[:5]),row[5],row[6]) for row in MOTIF]
    if min(f_margins)<=1e-9: raise AssertionError(f"{name}: non-strict face acceptance")

    source_checks=0
    examples={}
    for rec in records:
        intervals=[tuple(x) for x in rec["intervals"]]
        port_map={}
        for i,(p,q) in enumerate(intervals):
            a,b,j=MOTIF_EDGES[i]
            port_map[p]=a; port_map[q]=b
        if set(port_map)!=set(range(1,2*len(intervals)+1)):
            raise AssertionError("port map incomplete")
        if len(set(port_map.values()))!=2*len(intervals):
            raise AssertionError("L1 port collision")
        for p,q in intervals:
            a,b=port_map[p],port_map[q]
            if (a,b) not in edge_set: raise AssertionError("L2 edge not in target")
            delta=np.asarray(b)-np.asarray(a)
            if np.count_nonzero(delta)!=1 or np.max(np.abs(delta))!=1:
                raise AssertionError("L2 not a signed basis edge")
            if window_margin(a)<=1e-9 or window_margin(b)<=1e-9:
                raise AssertionError("L3 vertex acceptance failure")
        source_checks+=1
        if not examples: examples={"intervals":[list(x) for x in intervals],
                                   "port_to_Z5":{str(p):list(k) for p,k in sorted(port_map.items())}}
    return {
      "target":name,"vertices":len(labels),"edges":len(edges),"faces":len(faces),
      "vertex_label_sha256":sha_labels(labels),"accepted_face_sha256":sha_faces(faces),
      "hall_sources_checked":source_checks,"L1_source_checks_passed":source_checks,
      "L2_source_checks_passed":source_checks,"L3_source_checks_passed":source_checks,
      "motif_faces_present":len(motif_faces),"motif_edges_present":len(MOTIF_EDGES),
      "pairwise_disjoint_motif_edges":True,
      "minimum_assigned_vertex_window_margin":min(margins),
      "motif_face_triangle_margins":f_margins,
      "example_assignment":examples
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=None)
    args=ap.parse_args()
    original=original_source_complex(NGRID)
    labels_o,edges_o,faces_o,center,cutoff=original
    if (len(labels_o),len(edges_o),len(faces_o))!=(1550,3017,1468):
        raise AssertionError(("PF-I16 original-source counts",len(labels_o),len(edges_o),len(faces_o)))
    core=completed_window_core(NGRID,center,cutoff)
    labels_c,edges_c,faces_c=core
    if (len(labels_c),len(edges_c),len(faces_c))!=(1432,2761,1330):
        raise AssertionError(("PF-I11 completed-core counts",len(labels_c),len(edges_c),len(faces_c)))
    if sha_labels(labels_c)!=EXPECTED_CORE_LABEL_SHA or sha_faces(faces_c)!=EXPECTED_CORE_FACE_SHA:
        raise AssertionError("completed-core Ngrid=7 labels/faces do not match frozen PF-I11 evidence")
    rows={}
    for n in (4,6):
        records=hall.source_records(n)
        expected=2 if n==4 else 22
        if len(records)!=expected: raise AssertionError(("Hall source count",n,len(records)))
        rows[str(n)]={"source_count":len(records),
          "eligible_mark_count":sum(len(r["eligible_reverse_marks"]) for r in records),
          "PF_I16_original_source":check_target("PF-I16 original-source replay",labels_o,edges_o,faces_o,records),
          "PF_I11_completed_window_core":check_target("PF-I11 completed-window core",labels_c,edges_c,faces_c,records)}
    result={
      "schema":"PF-I16-HALL-L123-MOTIF-LIFT-v1",
      "scope":"bounded Ngrid=7 finite target check; L1-L3 only",
      "gamma_convention":"PF-I16 generic gamma: ((j*sqrt(2)+j^2*sqrt(3)) mod 1), mean-centered, gamma[4] reset to minus first-four sum",
      "hall_enumeration":"independent ordered perfect matchings, strict-interior overlap graph, all spanning trees, all non-root leaves",
      "frozen_target_motif":[{"lower":list(r[:5]),"directions":[r[5],r[6]]} for r in MOTIF],
      "frozen_disjoint_edges":[{"lower":list(a),"upper":list(b),"direction":j} for a,b,j in MOTIF_EDGES],
      "target_center":center.tolist(),"target_cutoff":cutoff,
      "PF_I16_original_source_counts":{"V":len(labels_o),"E":len(edges_o),"F":len(faces_o)},
      "PF_I11_completed_core_counts":{"V":len(labels_c),"E":len(edges_c),"F":len(faces_c)},
      "orders":rows,
      "not_claimed":["L4 interval support","L5 overlap witnesses","L6 parent naturality",
                     "L7 global port-order compatibility","L8 beyond the frozen construction",
                     "helical phases","Hall theorem"]
    }
    payload=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(payload)
    print(payload,end="")

if __name__=="__main__": main()
