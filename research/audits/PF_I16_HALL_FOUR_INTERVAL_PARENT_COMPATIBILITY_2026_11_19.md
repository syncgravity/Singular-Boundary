# PF-I16 four-interval parent-compatibility test

Date: 2026-11-19  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Pull request: #119 (draft)

## Result

The bounded parent-compatibility test finds **no common fourth matched edge** for the frozen demand-independent alternative triple.

The obstruction is witnessed by overlap graphs 5 and 12 in the canonical order-eight source census. Both have the same triangle on the first three intervals, but require incompatible attachment patterns for interval 4:

- Graph 5: edges `01, 02, 03, 12`; interval 4 overlaps interval 1 only. Its feasible fourth-edge set has 103 edges.
- Graph 12: edges `01, 02, 12, 13, 23`; interval 4 overlaps intervals 2 and 3, but not interval 1. Its feasible fourth-edge set has 21 edges.
- The intersection of these two candidate sets is empty.

The empty-set SHA-256 is `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` (SHA-256 of the canonical empty newline-terminated edge list).

This is a genuine finite obstruction to extending the **fixed three-edge motif** across all 13 order-eight overlap graph types under the enumerated support bounds. It is not a global obstruction to all possible first-three-edge motifs.

## Reproducibility

- Workflow run: `44571253464`
- Job: `135726593158`
- Parent-compatibility artifact ID: `14553892992`
- Artifact SHA-256: `975d02fc135d5784c37be836188d374262ba3b6a01bc3ed114c9323c33b64a30`
- Target face-key SHA-256: `f0f63287b3194a8625e4dd5c0a7369b04da315406fdc64a0d828627814ada7eb`
- Verifier: `research/scripts/verify_pf_i16_hall_four_interval_parent_compatibility.py`
- Inventory verifier: `research/scripts/verify_pf_i16_hall_four_interval_support_inventory.py`

The inventory and parent-compatibility calculations both completed and their artifacts uploaded. The workflow job was marked failed only because a later report-commit push raced with other branch updates; the compatibility test itself completed and uploaded its artifact before that push. The workflow was subsequently adjusted to remove the race-prone commit step and retain artifacts as the run outputs.

## Target and source sizes

| Quantity | Count |
|---|---:|
| Ngrid=12 completed-core vertices | 4,294 |
| Ngrid=12 completed-core edges | 8,382 |
| Ngrid=12 accepted rhombi | 4,089 |
| Eligible matched edges with exactly two accepted incident rhombi | 8,026 |
| Such edges vertex-disjoint from frozen triple | 8,004 |
| Locally relevant fourth edges after support-incidence prefilter | 249 |
| One-to-three-rhombus support options over all eligible matched edges | 214,108 |

The order-eight source reconstruction contains 608 sources, 1,050 eligible reverse-leaf projections, 13 distinct overlap graphs, and 490 unordered pairs of eligible deletions in the same source.

## Parent-compatible first-three support families

For the frozen three matched edges, exhaustive enumeration over their full one-to-three-rhombus support-option families yielded:

| First-three overlap graph | Parent-compatible support triples |
|---|---:|
| Star | 413 |
| Path | 397 |
| Triangle | 538 |

For each graph, the test requires:
- each support to collapse to its distinguished matched edge;
- exact pairwise intersection/nonintersection pattern;
- every nonempty pair intersection to collapse to a vertex;
- the triple union to collapse to a vertex;
- each eligible deletion in the corresponding parent pattern to admit a relative collapse to the retained union;
- retained pair intersections and unions to remain contractible; and
- every nonempty pair footprint to be a single boundary vertex or edge on the open complementary arc of the directed matched edge.

The tested mark sets are the union of possible non-root leaf marks over spanning trees of each three-interval overlap graph: star `[1,2]`, path `[2]`, triangle `[1,2]`. This makes the parent-support family graph-invariant and independent of a particular selected parent tree.

## Per-graph fourth-edge candidate counts

| Graph | Required adjacency of interval 4 to intervals 1,2,3 | Candidate edges |
|---:|:---:|---:|
| 1 | 100 | 99 |
| 2 | 001 | 110 |
| 3 | 010 | 75 |
| 4 | 001 | 97 |
| 5 | 100 | 103 |
| 6 | 101 | 32 |
| 7 | 010 | 65 |
| 8 | 001 | 105 |
| 9 | 011 | 32 |
| 10 | 110 | 19 |
| 11 | 101 | 23 |
| 12 | 011 | 21 |
| 13 | 111 | 18 |

No single edge realizes all 13 graphs; the best single edge realizes 10 graph types. The decisive pair is graphs 5 and 12, whose feasible candidate sets are disjoint.

## Exact scope of the obstruction

For each graph, the test existentially chooses a parent-compatible first-three support triple and a fourth support for the same candidate edge, then checks the exact fourth-interval adjacency vector and open-arc footprint conditions. It searches all 8,004 vertex-disjoint candidate edges and their enumerated support families, after a necessary support-incidence prefilter.

The obstruction is stronger than a failed greedy support choice: it compares complete feasible fourth-edge sets for the two decisive graph types, with existential freedom to choose different parent-compatible first-three support triples for each graph. If those sets are disjoint, no common fourth edge can satisfy both graph types under this frozen motif and support family.

## Limitations and nonclaims

1. The first-three matched-edge motif is fixed to the demand-independent alternative triple. A different three-edge motif has not been excluded.
2. Supports are bounded to at most three accepted rhombi. Larger connected supports are not included.
3. This is a parent-compatibility gate, not the complete four-support L6c/L7b diamond. It does not enumerate all four-support assignments, all nonempty triple/four-way intersections, or the full four-union relative-collapse certificates.
4. The test does not prove a four-interval lift, L8 construction independence, or the all-orders Hall inequality.
5. The target is the Ngrid=12 PF-I11 completed-window core, with strict acceptance checks. A result on this finite target is not a target-independent impossibility theorem.

## Next research step

Search for a different demand-independent first-three-edge motif in the same accepted target, or establish a principled target-independent obstruction to all motifs. The next search must preserve full support-option families and must not use Hall demands, loads, deficiencies, matchings, or flow outcomes to select target edges or supports.
