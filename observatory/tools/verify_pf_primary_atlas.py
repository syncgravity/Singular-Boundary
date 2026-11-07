#!/usr/bin/env python3
"""Validate PF-primary Observatory graph, UI links and preserved historical inventory.
Run from repository root: python observatory/tools/verify_pf_primary_atlas.py
No network or external Python dependencies. This is metadata governance, not proof review.
"""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[2]
obs=root/"observatory"
prefix="window.SB_KNOWLEDGE_GRAPH="
raw=(obs/"knowledge-graph-data.js").read_text(encoding="utf-8").strip()
assert raw.startswith(prefix) and raw.endswith(";")
graph=json.loads(raw[len(prefix):-1])
nodes=graph["nodes"];edges=graph["edges"];ids=[n["id"] for n in nodes]
assert len(nodes)==156,(len(nodes),156)
assert len(edges)==362,(len(edges),362)
assert len(ids)==len(set(ids))
S=set(ids)
assert all(e["from_id"] in S and e["to_id"] in S for e in edges)
assert all(n["status"]=="open" for n in nodes if n["id"] in ("P0","P1","P2","P3","P4","P5"))
assert graph["canon_status"]=="OPEN"
assert graph["indexed_theorem_paths"]==754
assert graph["historical_indexed_theorem_paths"]==740
assert graph["primary_hypothesis"].lower().find("coupled")>=0
assert graph["pf_program"]["approved_deployment"] is False
assert graph["pf_program"]["stages"]==[f"PF-G{i}" for i in range(6)]
assert graph["pf_program"]["control_model"]=="M-CUBIC"\nassert graph["pf_program"]["helical_observer"]["stages"]==[f"PF-H{i}" for i in range(7)]\nassert all(next(n for n in nodes if n["id"]==f"PF-H{i}")["status"] in ("open","conditional") for i in range(7))
assert sum(n["kind"]=="dataset" for n in nodes)>=26
assert all(next(n for n in nodes if n["id"]==f"PF-G{i}")["status"]=="open" for i in range(6))
for a,b in zip(graph["pf_program"]["stages"],graph["pf_program"]["stages"][1:]):
    assert any(e["from_id"]==a and e["to_id"]==b for e in edges)
for t in ["penrose-program.html","data-view=\"pf\"","data-view=\"bridge\""]:
    assert t in (obs/"graph.html").read_text(encoding="utf-8") if t!="penrose-program.html" else (obs/"penrose-program.html").is_file()
app=(obs/"graph-app.js").read_text(encoding="utf-8")
assert "let view='pf'" in app
assert "selectNode('PF-G0')" in app
assert "PF-G0" in app and "PF-G5" in app
for path in ["index.html","README.md","MATHEMATICAL_PHYSICS_GUIDE.md","integration.html"]:
    s=(obs/path).read_text(encoding="utf-8")
    assert "penrose-program.html" in s,path
    assert "PF-G0" in s,path
assert "754" in (obs/"index.html").read_text()
assert (root/"docs/research/THEOREM_INDEX_CURRENT.md").is_file()
print("PASS PF primary Atlas: 156 nodes, 362 edges, 754 indexed paths; 6 canonical YM gates OPEN; PF-G0..G5 routed")
