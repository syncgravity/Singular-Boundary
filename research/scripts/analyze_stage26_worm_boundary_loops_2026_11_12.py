#!/usr/bin/env python3
"""Extract M55 worm-strip boundary loops and evaluate them on Stage26 restart links."""
import argparse, hashlib, io, json, math, tempfile, zipfile
from pathlib import Path
import numpy as np

STAGE26_SHA="6cfa12935428533cfeaff40a467705d632b19ede07b7f30e0bb9fb7a0cc68657"
GEOM_SHA="d7a3fa153e69dae0129a6f0771d8241b78a0145cbc4939ea16b0a02ea74e7d60"
GRAPH_HASH="f67fc4455b37bf18f16c0a5ae90c7c3c5ccd49ca8b739fa1f5e43562b4581c21"
ARRAY_HASH="fee7afad5b4b464537782b508402401502984947ac5caf5163a87dad8ae33e2e"
RESTART_SOURCE_SHA="275243c7da74941db5bdd882dbb7f44ce02c915503033f040841b75f80409638"

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def cross2(a,b):
    return float(a[0]*b[1]-a[1]*b[0])

def qmul(a,b):
    a0=a[0]; av=a[1:]; b0=b[0]; bv=b[1:]
    return np.r_[a0*b0-np.dot(av,bv),a0*bv+b0*av+np.cross(av,bv)]

def qconj(a):
    return np.r_[a[0],-a[1:]]

def qmul_batch(a,b):
    a0=a[:,0]; av=a[:,1:]; b0=b[:,0]; bv=b[:,1:]
    return np.column_stack((a0*b0-np.sum(av*bv,axis=1),
                            a0[:,None]*bv+b0[:,None]*av+np.cross(av,bv)))

def qconj_batch(a):
    out=a.copy(); out[:,1:]*=-1
    return out

def build_source(geometry_zip,td):
    with zipfile.ZipFile(geometry_zip) as z:
        source=z.read("rebuild_stage26_geometry.py").decode()
        inc_bytes=z.read("stage26_penrose_m55_reconstructed_incidence.npz")
    source=source.replace("/mnt/data/stage26_penrose_m55_reconstructed_incidence.npz",str(td/"rebuilt.npz"))
    source=source.replace("/mnt/data/stage26_penrose_m55_geometry_summary.json",str(td/"summary.json"))
    p=td/"rebuild.py"; p.write_text(source)
    ns={"__file__":str(p)}; exec(compile(source,str(p),"exec"),ns)
    with np.load(io.BytesIO(inc_bytes),allow_pickle=False) as inc:
        assert np.array_equal(inc["fi"],ns["fi"])
        assert np.array_equal(inc["sg"],ns["sg"])
        assert np.array_equal(inc["spatial_face_idx"],ns["fidx"])
        assert np.array_equal(inc["spatial_edges"],ns["edges"])
    assert ns["h"]==GRAPH_HASH and ns["arrayhash"]==ARRAY_HASH
    return ns

def extract_segments(ns,radius=40.0,min_faces=10):
    nodes=np.asarray(ns["nodes"]); faces=ns["faces"]; edges=np.asarray(ns["edges"])
    edgeid=ns["edgeid"]; fidx=np.asarray(ns["fidx"]); fsg=np.asarray(ns["fsg"])
    E=len(edges); F=len(faces); Qpar=np.asarray(ns["Qpar"])
    t1=np.asarray(ns["t1"]); t2=np.asarray(ns["t2"])
    center=.5*(Qpar@t1+Qpar@t2)
    edge_family=np.full(E,-1,dtype=np.int8)
    face_family=np.empty((F,2),dtype=np.int8)
    face_type=np.empty(F,dtype="U5")
    face_centers=np.empty((F,2))
    for k,(u,ua,uab,ub,a,b) in enumerate(faces):
        face_family[k]=[a,b]
        face_type[k]="thick" if min((b-a)%5,(a-b)%5)==1 else "thin"
        face_centers[k]=Qpar@(nodes[u].astype(float)+.5*(np.eye(5)[a]+np.eye(5)[b]))-center
        for e,j in [(edgeid[tuple(sorted((u,ua)))],a),
                    (edgeid[tuple(sorted((ub,uab)))],a),
                    (edgeid[tuple(sorted((u,ub)))],b),
                    (edgeid[tuple(sorted((ua,uab)))],b)]:
            if edge_family[e] not in (-1,j): raise AssertionError("edge direction label conflict")
            edge_family[e]=j
    if np.any(edge_family<0): raise AssertionError("unlabelled spatial edge")
    edge_faces=[[] for _ in range(E)]
    for fi,row in enumerate(fidx):
        for e in row: edge_faces[int(e)].append(fi)
    if not all(len(x)==2 for x in edge_faces): raise AssertionError("edge not incident to two faces")
    mask=np.linalg.norm(face_centers,axis=1)<=radius
    segments=[]
    for family in range(5):
        active=np.flatnonzero(mask & np.any(face_family==family,axis=1))
        adj={int(f):set() for f in active}
        for e,fs in enumerate(edge_faces):
            if edge_family[e]!=family: continue
            a,b=fs
            if mask[a] and mask[b]: adj[a].add(b); adj[b].add(a)
        if any(len(v)>2 for v in adj.values()): raise AssertionError("worm adjacency branches")
        seen=set()
        for root in active:
            root=int(root)
            if root in seen: continue
            comp=[]; stack=[root]; seen.add(root)
            while stack:
                v=stack.pop(); comp.append(v)
                for w in adj[v]:
                    if w not in seen: seen.add(w); stack.append(w)
            ends=[v for v in comp if len(adj[v])<=1]
            start=min(ends) if ends else min(comp)
            order=[start]; prev=None; cur=start
            while True:
                nxt=sorted(x for x in adj[cur] if x!=prev and x not in order)
                if not nxt: break
                prev,cur=cur,nxt[0]; order.append(cur)
            if len(order)!=len(comp): raise AssertionError("worm traversal incomplete")
            if len(order)<min_faces: continue
            types=[str(face_type[f]) for f in order]
            segments.append({"family":family,"faces":order,"tile_types":types,
                             "tile_count":len(order),"L_count":types.count("thick"),
                             "S_count":types.count("thin")})
    return segments,edges,fidx,fsg,face_centers,mask

def boundary_loop(segment,edges,fidx,fsg):
    coeff={}
    for f in segment["faces"]:
        for e,s in zip(fidx[f],fsg[f]):
            e=int(e); coeff[e]=coeff.get(e,0)+int(s)
    if any(abs(v)>1 for v in coeff.values()): raise AssertionError("boundary multiplicity >1")
    bnd={e:int(np.sign(v)) for e,v in coeff.items() if v}
    if len(bnd)!=2*segment["tile_count"]+2:
        raise AssertionError("strip boundary length is not 2L+2")
    outgoing={}; incoming={}
    for e,s in bnd.items():
        u,v=map(int,edges[e]); a,b=(u,v) if s>0 else (v,u)
        if a in outgoing or b in incoming: raise AssertionError("boundary is not a simple cycle")
        outgoing[a]=(b,e,s); incoming[b]=(a,e,s)
    vertices=set(outgoing)|set(incoming)
    if any(v not in outgoing or v not in incoming for v in vertices):
        raise AssertionError("boundary has an open endpoint")
    start=min(vertices); cur=start; ordered=[]; visited=set()
    while True:
        nxt,e,s=outgoing[cur]
        if e in visited: break
        ordered.append((e,s)); visited.add(e); cur=nxt
        if cur==start: break
    if cur!=start or len(visited)!=len(bnd): raise AssertionError("boundary did not close exactly once")
    return ordered

def evaluate_loops(spatial_links,loops):
    nt=spatial_links.shape[0]; nloops=len(loops); maxlen=max(map(len,loops))
    eids=np.zeros((nloops,maxlen),dtype=np.int64)
    signs=np.zeros((nloops,maxlen),dtype=np.int8)
    for k,loop in enumerate(loops):
        eids[k,:len(loop)]=[e for e,s in loop]
        signs[k,:len(loop)]=[s for e,s in loop]
    U=spatial_links[:,eids,:].copy()
    neg=np.broadcast_to(signs[None,:,:]<0,U.shape[:3])
    if np.any(neg):
        flat=U[neg].reshape(-1,4); U[neg]=qconj_batch(flat)
    for k,loop in enumerate(loops):
        if len(loop)<maxlen: U[:,k,len(loop):,:]=np.array([1.,0.,0.,0.])
    q=np.zeros((nt*nloops,4)); q[:,0]=1
    U=U.reshape(nt*nloops,maxlen,4)
    for k in range(maxlen): q=qmul_batch(q,U[:,k,:])
    return (1-q[:,0]).reshape(nt,nloops)

def evaluate_spatial_faces(spatial_links,fidx,fsg):
    nt=spatial_links.shape[0]; F=len(fidx); E=spatial_links.shape[1]
    q=np.zeros((nt*F,4)); q[:,0]=1
    flat_links=spatial_links.reshape(nt*E,4)
    for k in range(4):
        ids=np.tile(fidx[:,k],nt)
        u=flat_links[np.repeat(np.arange(nt),F)*E+ids]
        signs=np.tile(fsg[:,k],nt); neg=signs<0
        if np.any(neg): u[neg]=qconj_batch(u[neg])
        q=qmul_batch(q,u)
    return q[:,0].reshape(nt,F)

def run(stage26_zip,geometry_zip,radius=40.0,min_faces=10,phase_max=1000,check_gauge=True):
    if sha256(stage26_zip)!=STAGE26_SHA: raise ValueError("Stage26 archive hash mismatch")
    if sha256(geometry_zip)!=GEOM_SHA: raise ValueError("M55 geometry archive hash mismatch")
    with tempfile.TemporaryDirectory(prefix="stage26_worms_") as td:
        ns=build_source(geometry_zip,Path(td))
        segments,edges,fidx,fsg,face_centers,mask=extract_segments(ns,radius,min_faces)
        E=len(edges); F=len(ns["faces"]); V=len(ns["nodes"]); nt=int(ns["nt"])
        with zipfile.ZipFile(stage26_zip) as z:
            restart_name=next(x for x in z.namelist() if x.endswith("/restart.npz"))
            with np.load(io.BytesIO(z.read(restart_name)),allow_pickle=False) as a:
                links=a["links"].copy(); stored=a["plaquette_trace"].copy()
                restart_sha=str(a["source_sha256"])
                restart_sweeps=np.asarray(a["sweeps"]).tolist() if "sweeps" in a.files else None
        if restart_sha!=RESTART_SOURCE_SHA: raise ValueError("Restart source hash mismatch")
        assert links.shape==(nt*(E+V),4) and stored.shape==(nt*(F+E),)
        # Reconstruct every stored normalized plaquette trace from the source fi/sg incidence.
        fi_all=np.asarray(ns["fi"]); sg_all=np.asarray(ns["sg"])
        q_all=np.zeros((len(fi_all),4)); q_all[:,0]=1
        for k in range(4):
            uu=links[fi_all[:,k]].copy()
            neg=sg_all[:,k]<0
            if np.any(neg): uu[neg]=qconj_batch(uu[neg])
            q_all=qmul_batch(q_all,uu)
        incidence_error=np.abs(q_all[:,0]-stored)
        max_incidence_error=float(incidence_error.max())
        if max_incidence_error>1e-12:
            raise AssertionError("full spacetime link/face reconstruction mismatch")
        loops=[]
        for sid,seg in enumerate(segments):
            loop=boundary_loop(seg,edges,fidx,fsg); loops.append(loop)
            seg["segment_id"]=sid; seg["loop_length"]=len(loop)
            seg["loop_edges"]=[[int(e),int(s)] for e,s in loop]
            seg["L_over_S"]=seg["L_count"]/max(seg["S_count"],1)
        spatial_links=links[:nt*E].reshape(nt,E,4)
        defects=evaluate_loops(spatial_links,loops)
        family_ids=np.asarray([s["family"] for s in segments])
        F_j=np.stack([defects[:,family_ids==j].mean(axis=1) for j in range(5)],axis=1)
        phi=(1+math.sqrt(5))/2; rho=phi**-2
        n=np.arange(phase_max+1); theta=2*math.pi*rho*n
        u=np.sqrt(2/5)*np.cos(4*math.pi*np.arange(5)[None,:]/5-theta[:,None])
        O=F_j@u.T; O_full=F_j.mean(axis=1)
        A=F_j@(np.exp(2j*math.pi/5)**(2*np.arange(5)))
        amp=np.sqrt(2/5)*np.abs(A)
        gauge_error=None; worm_gauge_error=None
        if check_gauge:
            rng=np.random.default_rng(419)
            g=rng.normal(size=(nt,V,4)); g/=np.linalg.norm(g,axis=2,keepdims=True)
            gu=g[:,edges[:,0],:]; gv=g[:,edges[:,1],:]
            tmp=qmul_batch(gu.reshape(-1,4),spatial_links.reshape(-1,4))
            transformed=qmul_batch(tmp,qconj_batch(gv.reshape(-1,4))).reshape(nt,E,4)
            pred_sp=evaluate_spatial_faces(transformed,fidx,fsg)
            original_sp=stored.reshape(nt,F+E)[:,:F]
            gauge_error=float(np.max(np.abs(pred_sp-original_sp)))
            if gauge_error>1e-11: raise AssertionError("gauge transformed plaquettes changed")
            transformed_defects=evaluate_loops(transformed,loops)
            worm_gauge_error=float(np.max(np.abs(transformed_defects-defects)))
            if worm_gauge_error>1e-11: raise AssertionError("worm loops not gauge invariant")
        family_summary=[]
        for j in range(5):
            js=[s for s in segments if s["family"]==j]
            family_summary.append({"family":j,"segments":len(js),
                "mean_tile_count":float(np.mean([s["tile_count"] for s in js])),
                "mean_L_over_S":float(np.mean([s["L_over_S"] for s in js])),
                "within_15_percent_phi":int(sum(abs(s["L_over_S"]-phi)/phi<.15 for s in js)),
                "mean_loop_length":float(np.mean([s["loop_length"] for s in js])),
                "family_worm_defect_mean_over_slices":float(F_j[:,j].mean()),
                "family_worm_defect_std_over_slices":float(F_j[:,j].std())})
        catalogue_payload=json.dumps(segments,sort_keys=True,separators=(",",":")).encode()
        catalogue_hash=hashlib.sha256(catalogue_payload).hexdigest()
        phase_angles=np.angle(A)
        phase_mean=float(np.angle(np.mean(np.exp(1j*phase_angles))))
        phase_spread=float(np.sqrt(-2*np.log(abs(np.mean(np.exp(1j*phase_angles))))))
        inradius=min(abs(cross2(ns["Qpar"]@ns["t1"],ns["Qpar"]@ns["t2"]))/np.linalg.norm(ns["Qpar"]@ns["t1"]),
                     abs(cross2(ns["Qpar"]@ns["t1"],ns["Qpar"]@ns["t2"]))/np.linalg.norm(ns["Qpar"]@ns["t2"]))/2
        if radius>=inradius:
            raise ValueError("disk crop must remain inside the M55 fundamental-cell inradius")
        result={
            "status":"PASS_M55_WORM_BOUNDARY_LOOP_EXTRACTION_AND_STAGE26_EVALUATION",
            "stage26_archive_sha256":STAGE26_SHA,"geometry_archive_sha256":GEOM_SHA,
            "graph_hash":ns["h"],"source_array_sha256":ns["arrayhash"],
            "restart_source_sha256":restart_sha,"restart_sweeps":restart_sweeps,
            "exact_incidence_validation":{"reconstructed_spacetime_faces":int(len(fi_all)),
                "max_abs_normalized_trace_error":max_incidence_error,
                "count_error_over_1e_12":int(np.count_nonzero(incidence_error>1e-12))},
            "crop":{"radius":radius,"fundamental_cell_inradius":float(inradius),
                    "min_faces":min_faces,"active_faces":int(mask.sum())},
            "worm_segments":{"total":len(segments),"family_summary":family_summary,
                "path_catalogue_sha256":catalogue_hash,
                "all_boundary_loops_closed":True,"all_boundary_loop_lengths_equal_2L_plus_2":True,
                "loop_length_min":int(min(map(len,loops))),"loop_length_max":int(max(map(len,loops)))},
            "stage26_worm_boundary_wilson_diagnostic":{"timeslices":nt,
                "family_defect_mean_over_slices":[float(x) for x in F_j.mean(axis=0)],
                "family_defect_std_over_slices":[float(x) for x in F_j.std(axis=0)],
                "full_family_control_mean":float(O_full.mean()),"full_family_control_std":float(O_full.std()),
                "second_harmonic_amplitude_mean":float(amp.mean()),"second_harmonic_amplitude_std":float(amp.std()),
                "second_harmonic_amplitude_min":float(amp.min()),"second_harmonic_amplitude_max":float(amp.max()),
                "second_harmonic_phase_circular_mean_rad":phase_mean,
                "second_harmonic_phase_circular_spread_rad":phase_spread,
                "relative_amplitude_to_full_control":float(amp.mean()/O_full.mean()),
                "O_n_global_min":float(O.min()),"O_n_global_max":float(O.max()),
                "O_n_first_13_slice_means":[float(O[:,k].mean()) for k in range(min(13,phase_max+1))],
                "family_defect_by_timeslice":[[float(x) for x in row] for row in F_j],
                "O_n_by_timeslice_first_13_phases":[[float(x) for x in row] for row in O[:,:min(13,phase_max+1)]]},
            "gauge_covariance_check":{"performed":bool(check_gauge),
                "max_spatial_plaquette_trace_change":gauge_error,
                "max_worm_loop_defect_change":worm_gauge_error},
            "scope":"Reconstructed M55 source geometry, radius-40 disk crop inside the periodic cell, and one Stage26 seed-101 restart configuration across 20 slices. Worm-strip boundaries are closed spatial Wilson loops. This is not an ensemble correlator or mass-gap estimate; byte identity with the separate complete measurement catalogue remains unverified."
        }
        return result,segments

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("stage26_zip"); ap.add_argument("geometry_zip")
    ap.add_argument("--radius",type=float,default=40.0); ap.add_argument("--min-faces",type=int,default=10)
    ap.add_argument("--phase-max",type=int,default=1000); ap.add_argument("--no-gauge-check",action="store_true")
    ap.add_argument("--output",type=Path); ap.add_argument("--catalogue-output",type=Path)
    args=ap.parse_args()
    result,catalogue=run(args.stage26_zip,args.geometry_zip,args.radius,args.min_faces,args.phase_max,not args.no_gauge_check)
    rendered=json.dumps(result,indent=2,sort_keys=True)
    if args.output: args.output.write_text(rendered+"\n",encoding="utf-8")
    if args.catalogue_output: args.catalogue_output.write_text(json.dumps(catalogue,indent=2)+"\n",encoding="utf-8")
    print(rendered)
