# PF-I16 four-interval parent-compatibility obstruction

Date: 2026-11-19  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Pull request: #119 (draft)

## Result

The frozen demand-independent three-edge motif does not admit one common fourth matched edge across all 13 order-eight interval-overlap graphs, within the following bounded target family:

- Ngrid=12 PF-I11 completed-window core (4,294 vertices, 8,382 edges, 4,089 accepted rhombi).
- First three matched edges fixed to the previously authenticated alternative triple.
- Fourth matched edge vertex-disjoint from the first six endpoints and incident to exactly two accepted rhombi.
- Every interval support is a connected, simple-boundary union of one to three accepted rhombi.
- Every pairwise overlap footprint is a single boundary vertex or edge, strictly on the open complementary arc of both directed matched edges.

The parent-triple inventory is exhaustive within this support family. It contains 413 star-compatible triples, 397 path-compatible triples, and 538 triangle-compatible triples. A triple is parent-compatible here when its exact pair-intersection graph is correct, its supports and union/intersections pass the tested collapsibility conditions, all required three-to-two relative deletion collapses succeed, and every retained overlap footprint is a single open-arc boundary cell.

For each of the 13 order-eight graphs, the verifier tests every locally relevant fourth edge and every one-to-three-rhombus support option against at least one parent-compatible first-three support family. The resulting feasible fourth-edge counts, in canonical graph order, are:

`99, 110, 75, 97, 103, 32, 65, 105, 32, 19, 23, 21, 18`.

No edge realizes all 13 graph types. The best single edge realizes 10 of 13.

## Explicit disjointness certificate

Two graph types suffice to certify the obstruction.

Graph 5 has edges
[
{01,02,03,12}
]
and requires interval 3 to overlap interval 0 only among the first three intervals. It has 103 feasible fourth edges; sorted-edge-set SHA-256:
`5faf6c6642d3730f051a4851a3700f0439958155058aa5079b3f63cfce66ec25`.

Graph 12 has edges
[
{01,02,12,13,23}
]
and requires interval 3 to overlap intervals 1 and 2, but not interval 0. It has 21 feasible fourth edges; sorted-edge-set SHA-256:
`c6c1c9f9a4c43fbf60b152915069a7a8f76043c3305b23d584553b81665a013c`.

Both have the same triangle parent graph on intervals 0,1,2, so the comparison is not caused by switching between star/path/triangle parent families. Their feasible fourth-edge sets have empty intersection. The empty-set SHA-256 is
`01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b`.

## Reproducibility

Verifier:
`research/scripts/verify_pf_i16_hall_four_interval_parent_compatibility.py`

Input inventory:
`research/scripts/verify_pf_i16_hall_four_interval_support_inventory.py`

GitHub Actions run: `44571253464`  
Run head: `1132ae482fb263039cfcac1b32f935607efaa85d`  
Parent-compatibility artifact ID: `14553892992`  
Artifact ZIP SHA-256: `975d02fc135d5784c37be836188d374262ba3b6a01bc3ed114c9323c33b64a30`

The inventory and parent-compatibility verifier steps both completed successfully and uploaded artifacts. The final job failed only at an auxiliary attempt to commit generated JSON into the branch because the branch had advanced during overlapping workflow runs. That commit/publish step has been removed; the machine-readable results remain available as workflow artifacts, and this audit plus the verifier are committed in the research branch.

## Interpretation and limits

This is a bounded obstruction for the frozen first-three matched edges and the stated Ngrid=12/support/footprint family. It is not a counterexample to the Hall theorem and does not prove that no four-interval diamond exists in another target motif or under a broader support definition.

The fourth-edge test is a necessary parent-compatibility gate, not a complete four-support proof. It does not test all three other deletion restrictions for each four-support assignment, the full four-support L6c intersection diagram, four-union relative-collapse certificates, or the complete L7b multi-footprint boundary word. It does not search supports larger than three rhombi, matched edges with a different incident-face multiplicity, or a different first-three edge motif. It establishes neither L8 nor an all-orders Hall theorem.

## Next research move

Do not spend effort on the 490 source diamonds for this frozen motif: the common fourth edge already fails a necessary graph-type compatibility condition. Preserve the finite obstruction and restart the target-only motif search with the fourth-edge attachment patterns included from the outset. The next candidate triple must admit both graph-5 and graph-12 attachment patterns on a common fourth edge before any full four-way L6c/L7b diamond certificates are attempted.
