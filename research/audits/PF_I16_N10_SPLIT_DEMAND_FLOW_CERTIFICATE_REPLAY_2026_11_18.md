# PF-I16: exact n=10 split-demand flow certificate replay

Date: 2026-11-18

## Result

**The corrected n=10 split-demand quotient-flow workflow completed successfully.** The exact nonuniform flow was exported, independently replayed against the reconstructed finite relation, and uploaded as a 90-day artifact.

- Workflow: [44432123349](https://github.com/syncgravity/Singular-Boundary/actions/runs/44432123349)
- Job: `certificate`, job id `135251853928`
- Checked-out flow-builder commit: `75141c303dfad6191c5a797c262b704a6049fe5a`
- Research branch at the time of this audit: `research/pf-i16-direct-mixed-hall-2026-11-18`
- Artifact: [pf-i16-n10-split-demand-flow-certificate.zip](https://github.com/syncgravity/Singular-Boundary/actions/runs/44432123349/artifacts/14490510306)
- Artifact id: `14490510306`
- ZIP SHA-256: `d23af0dcf97433db01d209f220c0cafd6baef08109dea9f11ae78757e577d096`
- Uncompressed JSON: 8,204,258 bytes.

The first attempt [44426921009](https://github.com/syncgravity/Singular-Boundary/actions/runs/44426921009) had already computed and exported the flow but failed in a post-flow terminal diagnostic because `Counter` was not imported. The import correction was committed as `75141c3...`. The corrected run passed both the flow builder and replay; the earlier failure is a harness defect, not a mathematical counterexample.

## Exact n=10 flow

The builder enumerated the complete global fiber graph, not separate cut-block networks:

| Quantity | Exact result |
|---|---:|
| Child sources | 31,744 |
| Parent-source / deleted-interval fibers | 21,280 |
| Eligible target vertices in the full network | 95,864 |
| Exact total fiber demand | 31,744 |
| Denominator-clearing scale | 12 |
| Scaled demand | 380,928 |
| Maximum flow | 380,928 |
| Positive fiber-to-target arcs | 49,584 |
| Targets receiving positive flow | 32,414 |
| Maximum target load | 12 / 12 |

Thus the full split-demand quotient Hall condition holds at n=10: max-flow equals total demand. By the split-demand reduction, source-level Hall for the multivalued-π relation also holds at this finite order.

The exported certificate contains only the 32,414 targets carrying positive flow; the network itself had 95,864 eligible target vertices.

## Independent replay

The separate checker `verify_pf_i16_split_demand_flow_certificate.py` passed without rerunning max-flow. It reconstructed all sources and fibers and checked:
- each of the 21,280 fibers occurs exactly once;
- exact rational demand is reconstructed for every fiber;
- every positive assignment belongs to the actual retained parent-canonical row;
- every fiber receives exactly its scaled demand;
- no target exceeds capacity 12;
- total flow equals total demand.

Replay output:
```text
PASS: independent n=10 split-demand flow certificate replay
sources=31744 fibers=21280 targets=32414
positive_flow_arcs=49584
used_targets=32414
max_target_load=12 / capacity=12
total_scaled_flow=380928
```

**Independence boundary:** replay is independent of the max-flow algorithm and serialized residual-flow construction, but it shares the repository's canonical source enumeration, switch inversion, compression, and candidate-output primitives. It is therefore an independent certificate checker for the computed finite relation, not a separately implemented definition of that relation.

## Allocation support: exact census

The replayed certificate has the following positive-arc count per fiber:

| Positive targets assigned to a fiber | Fibers |
|---:|---:|
| 1 | 3,296 |
| 2 | 9,649 |
| 3 | 6,477 |
| 4 | 1,737 |
| 5 | 115 |
| 6 | 6 |
| **Total** | **21,280** |

The target-load histogram, in scale-12 units, is:

| Load | Targets |
|---:|---:|
| 1 | 41 |
| 2 | 142 |
| 3 | 60 |
| 4 | 201 |
| 5 | 47 |
| 6 | 324 |
| 7 | 63 |
| 8 | 222 |
| 9 | 42 |
| 10 | 187 |
| 11 | 45 |
| 12 | 31,040 |
| **Total used** | **32,414** |

So 31,040 used targets are saturated and 1,374 used targets are partially loaded. The total unused capacity among used targets is 8,040 scale units.

The 608 distinct eight-port parent sources each index exactly 35 deleted-interval fibers in this census. Parent demand varies substantially with the parent overlap-tree leaf count; the flow is not a uniform per-parent allocation.

## Interpretation: what the certificate does and does not reveal

This is a genuine exact finite Hall certificate, and it closes the previously missing replay/artifact step. It does **not** yet reveal an all-orders allocation rule.

The positive support is produced by the current Dinic implementation. The network is built by iterating fiber rows stored as `frozenset` objects, and the residual augmenting process is order-dependent. Consequently, the particular 49,584 positive arcs are not a canonical mathematical object. Their sparsity (at most six targets per fiber in this run) is an observation about this run, not a structural lemma. No proof should infer a universal priority rule from this support without first making the allocation canonical and proving its invariance.

The completed result strengthens finite evidence at n=10, but does not establish arbitrary-family Hall at all orders. The all-orders mixed Hall theorem, the unconditional weighted one-link inequality, and any mass-gap conclusion remain open.

## Next proof candidate: row-normalized target load

A different sufficient allocation, distinct from equal reciprocal reverse-degree splitting, is:
[
lambda(F,T)=rac{delta(F)}{|N(F)|},1_{{Tin N(F)}}.
]
It gives each fiber exactly its demand. It proves Hall if the target loads satisfy
[
oxed{
L(T):=sum_{F:Tin N(F)}rac{delta(F)}{|N(F)|}le 1
quad	ext{for every target }T.
}
	ag{RNL}
]
This criterion weights each reverse mark by the demand and row size of its fiber, rather than splitting target capacity equally among all incident fibers. It is only a candidate sufficient condition; no finite evaluation or all-orders bound is claimed in this audit.

The next discriminating test is exact rational evaluation of `L(T)` at n=8 and n=10, with all fibers in the full relation included. If it passes, seek an all-orders estimate using the exact demand formula
[
delta(p,J)=a(p,J)/d(p)+b(p,J)/(d(p)+1)
]
and a structural lower bound on `|N(F)|`. If it fails, retain the first overloaded target and its complete incident-fiber list as a concrete obstruction to this allocation only. Either outcome leaves the full mixed-Hall dual as the governing theorem.

No long workflow should be launched until the exact verifier for (RNL) is specified and its result is expected to change the proof strategy.
