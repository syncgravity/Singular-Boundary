#!/usr/bin/env python3
"""Idempotent source-qualified PF-primary overlay after the historical cubic graph build.

This explicitly does NOT certify a 3D Penrose–Fibonacci SU(2) regulator or a mass gap.
Run by build_knowledge_graph.py before sync_theorem_catalog.py.
"""
import json
from pathlib import Path

def attach(root: Path):
    root=Path(root)
    source=root/"knowledge-graph.json"
    g=json.loads(source.read_text(encoding="utf-8"))
    overlay=json.loads((root/"pf-primary-overlay.json").read_text(encoding="utf-8"))
    assert overlay["schema"]=="singular-boundary.pf-primary-overlay.v1"
    assert g["canon_status"]=="OPEN" and g["indexed_theorem_paths"] in (740,754)
    nodes=g["nodes"];edges=g["edges"]
    by={n["id"]:n for n in nodes}
    if g.get("version")==overlay["version"]:
        assert len(nodes)==overlay['expected_final_nodes'] and len(edges)==overlay['expected_final_edges']
        assert all(x["id"] in by for x in overlay["nodes"])
        return g
    assert g["version"] in ("v2.40-draft","v2.41-draft"),g["version"]
    assert len(nodes)==overlay["expected_base_nodes"] and len(edges)==overlay["expected_base_edges"]
    old_source_files={n["id"]:(n.get("asset",{}).get("filename"),n.get("asset",{}).get("sha256")) for n in nodes if n["kind"]=="dataset"}
    for id,patch in overlay["patches"].items():
        n=by[id]
        for key in ("title","summary"):
            if key in patch:n[key]=patch[key]
        src=patch.get("source_to_append")
        if src and src not in n["sources"]:n["sources"].append(src)
    for n in overlay["nodes"]:
        assert n["id"] not in by,n["id"]
        nodes.append(n);by[n["id"]]=n
    present={(e["from_id"],e["to_id"],e["kind"]) for e in edges}
    for e in overlay["edges"]:
        assert e["from_id"] in by and e["to_id"] in by
        key=(e["from_id"],e["to_id"],e["kind"])
        assert key not in present,key
        present.add(key);edges.append(e)
    for key in ("version","build_date","scope","primary_hypothesis","pf_program"):
        g[key]=overlay[key]
    assert len(nodes)==overlay['expected_final_nodes'] and len(edges)==overlay['expected_final_edges']
    assert {n["id"]:(n.get("asset",{}).get("filename"),n.get("asset",{}).get("sha256")) for n in nodes if n["kind"]=="dataset"}==old_source_files
    assert all(n["status"]=="open" for n in nodes if n["kind"] in ("gate","goal"))
    source.write_text(json.dumps(g,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (root/"knowledge-graph-data.js").write_text("window.SB_KNOWLEDGE_GRAPH="+json.dumps(g,ensure_ascii=False,separators=(",",":"))+";\n",encoding="utf-8")
    return g

if __name__=="__main__":
    g=attach(Path(__file__).resolve().parents[1])
    print("PASS PF source-first graph overlay",len(g["nodes"]),"nodes",len(g["edges"]),"edges")
