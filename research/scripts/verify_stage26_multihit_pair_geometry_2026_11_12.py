#!/usr/bin/env python3
"""Verify multihit source/target and minimum-image displacement against M55 torus."""
import argparse,hashlib,io,json,tempfile,zipfile,contextlib
from pathlib import Path
import numpy as np

GEOM_SHA="d7a3fa153e69dae0129a6f0771d8241b78a0145cbc4939ea16b0a02ea74e7d60"
GRAPH_HASH="f67fc4455b37bf18f16c0a5ae90c7c3c5ccd49ca8b739fa1f5e43562b4581c21"
ARRAY_HASH="fee7afad5b4b464537782b508402401502984947ac5caf5163a87dad8ae33e2e"

def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):h.update(b)
    return h.hexdigest()

def build(geometry_zip,td):
    with zipfile.ZipFile(geometry_zip) as z:
        source=z.read("rebuild_stage26_geometry.py").decode()
        inc=z.read("stage26_penrose_m55_reconstructed_incidence.npz")
    source=source.replace("/mnt/data/stage26_penrose_m55_reconstructed_incidence.npz",str(td/"rebuilt.npz"))
    source=source.replace("/mnt/data/stage26_penrose_m55_geometry_summary.json",str(td/"summary.json"))
    p=td/"rebuild.py";p.write_text(source);ns={"__file__":str(p)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(source,str(p),"exec"),ns)
    with np.load(io.BytesIO(inc),allow_pickle=False) as z:
        assert np.array_equal(z["nodes"],ns["nodes"])
        assert np.array_equal(z["spatial_edges"],ns["edges"])
    assert ns["h"]==GRAPH_HASH and ns["arrayhash"]==ARRAY_HASH
    return ns

def run(multihit_npz,geometry_zip,search_radius=2):
    gh=sha(geometry_zip)
    if gh!=GEOM_SHA:raise ValueError("M55 geometry archive hash mismatch")
    with tempfile.TemporaryDirectory(prefix="m55_paircheck_") as td:
        ns=build(geometry_zip,Path(td));Q=np.asarray(ns["Qpar"])
        nodes=np.asarray(ns["nodes"]);V=len(nodes);p=nodes@Q.T
        p1=Q@np.asarray(ns["t1"]);p2=Q@np.asarray(ns["t2"])
        with np.load(multihit_npz,allow_pickle=False) as z:
            src=z["source"].astype(int);tgt=z["target"].astype(int)
            dx=z["dx"].astype(float);r=z["r"].astype(float)
            cpi=z["candidate_path_indices"].astype(int)
            mpi=z["matched_pair_indices"].astype(int)
            seed=int(z["seed"]);geometry=str(z["geometry"]);sweep=int(z["sweep"])
        if np.any(src<0) or np.any(src>=V) or np.any(tgt<0) or np.any(tgt>=V):
            raise AssertionError("source/target outside M55 vertex index range")
        direct=p[tgt]-p[src];errors=[];shifts=[]
        for k,d in enumerate(direct):
            best=1e99;bestab=None
            for a in range(-search_radius,search_radius+1):
                for b in range(-search_radius,search_radius+1):
                    v=d-a*p1-b*p2;e=float(np.linalg.norm(v-dx[k]))
                    if e<best:best=e;bestab=(a,b)
            errors.append(best);shifts.append(bestab)
        errors=np.asarray(errors);rerr=np.abs(np.linalg.norm(dx,axis=1)-r)
        if errors.max()>1e-10:raise AssertionError(f"minimum-image displacement mismatch {errors.max()}")
        if rerr.max()>1e-12:raise AssertionError(f"r != norm(dx): {rerr.max()}")
        if len(np.unique(cpi))!=len(cpi):raise AssertionError("candidate path indices repeat in matched sample")
        if not np.array_equal(mpi,np.arange(len(mpi))):raise AssertionError("matched pair indices not canonical")
        from collections import Counter
        return {"status":"PASS_STAGE26_MULTIHIT_ENDPOINT_GEOMETRY",
            "multihit_npz_sha256":sha(multihit_npz),"geometry_zip_sha256":gh,
            "graph_hash":ns["h"],"source_array_sha256":ns["arrayhash"],
            "seed":seed,"geometry":geometry,"sweep":sweep,"vertex_count":V,"pair_count":len(src),
            "source_target_index_range":[int(min(src.min(),tgt.min())),int(max(src.max(),tgt.max()))],
            "minimum_image_period_search_radius":search_radius,
            "maximum_dx_reconstruction_error":float(errors.max()),
            "mean_dx_reconstruction_error":float(errors.mean()),
            "maximum_r_norm_error":float(rerr.max()),
            "minimum_image_shift_histogram":{str(k):int(v) for k,v in Counter(map(tuple,shifts)).items()},
            "candidate_path_indices":{"unique_count":int(len(np.unique(cpi))),"min":int(cpi.min()),"max":int(cpi.max())},
            "matched_pair_indices_canonical":True,
            "scope":"Endpoint coordinates and torus minimum-image displacement are verified against reconstructed M55 geometry. Candidate path IDs remain opaque until the complete measurement catalogue is inspected."}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("multihit_npz");ap.add_argument("geometry_zip")
    ap.add_argument("--search-radius",type=int,default=2);ap.add_argument("--output",type=Path)
    a=ap.parse_args();result=run(a.multihit_npz,a.geometry_zip,a.search_radius)
    s=json.dumps(result,indent=2,sort_keys=True)
    if a.output:a.output.write_text(s+"\n")
    print(s)
