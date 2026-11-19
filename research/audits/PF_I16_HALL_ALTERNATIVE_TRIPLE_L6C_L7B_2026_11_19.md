# PF-I16 — Alternative triple: full finite L6c and L7b verification

Date: 19 November 2026  
Branch: `research/pf-i16-z5-incidence-lift-2026-11-18`  
Verifier: `research/scripts/verify_pf_i16_hall_alternative_triple_l6c_l7b.py`

## 1. Frozen target-only candidate

This test continues the demand-independent search recorded in
`PF_I16_HALL_DEMAND_INDEPENDENT_ALTERNATIVE_TRIPLE_2026_11_19.md`.
The ordered matched edges and all three graph-pattern support assignments are
frozen; no Hall demand, load, deficiency, matching outcome, or flow result was
read to choose them.

```
e1: (-7,-4,5,7,0) -> (-6,-4,5,7,0)   +e0
e2: (-7,-3,5,7,-1) -> (-7,-3,6,7,-1) +e2
e3: (-6,-3,5,6,-1) -> (-6,-3,5,6,0)  +e4
```

The parent assignment is fixed once for the two-interval parent overlap graph:
the first two supports of the PATH pattern. It is not selected separately by
origin or by Hall outcome.

Notation `(m;j,k)` denotes the accepted rhombus with lower label `m` and
directions `j,k`.

### Star

- I1: `((-7,-4,5,7,0);0,1)`
- I2: `((-7,-3,5,7,-1);2,4)`
- I3: `((-6,-3,4,6,0);2,3)`, `((-6,-3,5,6,-1);3,4)`

### Path

- I1: `((-7,-4,5,7,0);0,1)`
- I2: `((-7,-3,5,7,-1);0,2)`, `((-7,-3,5,7,-1);0,4)`
- I3: `((-6,-3,5,6,-1);1,3)`, `((-6,-3,5,6,-1);1,4)`

### Triangle

- I1: `((-7,-4,5,7,0);0,1)`
- I2: `((-7,-3,5,7,-1);0,2)`, `((-7,-3,5,7,-1);0,4)`
- I3: `((-6,-3,4,6,0);2,3)`, `((-6,-3,5,6,-1);3,4)`

The two parent supports are the PATH I1 and I2 supports.

## 2. Finite domain and controls

- Hall indexing: all 22 order-six sources and all 30 eligible non-root-leaf
  marked projections to order-four parents.
- PF-I16 original-source replay: 1,550 vertices, 3,017 edges, 1,468 accepted
  rhombi.
- PF-I11 completed-window core: 1,432 vertices, 2,761 edges, 1,330 accepted
  rhombi; its accepted faces are contained in the PF-I16 replay.
- The three source graph patterns (star, path, triangle) and the two-interval
  parent graph are checked against the exact support intersections, including
  empty intersections for non-overlapping pairs.
- Each support is connected, has a single simple boundary cycle, and retains
  its distinguished matched edge on that boundary.
- Every required overlap footprint is a single connected boundary cell lying
  strictly in the open complementary arc on both participating supports.
  Non-overlapping support pairs are disjoint including vertices.
- Minimum strict acceptance margins across the selected supports:
  vertex-window margin `0.06831334502945263`; face-triangle margin
  `0.06831334502945297`.

Both target domains give identical incidence and boundary results.

## 3. L6c — parent naturality

For each of the 30 marked projections:

1. Restrict the frozen child support family by deleting the marked interval.
2. Check each retained support collapses to an edge.
3. Check the retained pair intersection is nonempty exactly when prescribed by
   the parent overlap graph, and collapses to a vertex.
4. Check the retained union collapses to a vertex.
5. Compare the complete two-support intersection-diagram signature with the
   fixed parent support diagram.
6. Collapse the full child union onto the retained child union using only
   relative free face-edge and edge-vertex pairs; no retained cell is removed.
7. Group projections by exact parent matching/tree and check coherence.

Results in each target domain:

| L6c test | Result |
|---|---:|
| Marked projections checked | 30 |
| Relative deletion collapses | 30/30 |
| Child-restriction / parent diagram comparisons | 30/30 |
| Parent coherence groups | 2/2 |
| Origins per parent coherence group | 15, 15 |
| Retained intersections: shared edge | 14 |
| Retained intersections: shared vertex | 16 |
| Relative collapse pairs: face-edge | 58 |
| Relative collapse pairs: edge-vertex | 110 |
| Total relative collapse pairs | 168 |
| Maximum pairs in one projection | 7 |

Per-projection collapse-length histogram:

| Elementary pairs | Projections |
|---:|---:|
| 4 | 2 |
| 5 | 12 |
| 6 | 12 |
| 7 | 4 |

All retained supports, their nonempty pair intersection, and their union have
the required contractible coarse type. The child and parent intersection
diagrams agree after forgetting shared-cell identity and dimension. Both
distinct parent structures receive the same coherent coarse diagram from all
15 incoming marked origins.

**Finite L6c verdict: PASS**, 30/30 projections in both target domains.

## 4. L7b — full retained cyclic-footprint placement

The L7b comparison is performed on each retained interval's support boundary,
oriented from its distinguished lower-port endpoint to its upper-port
endpoint. The directed matched edge is fixed; no target-wide total order,
port permutation, trace reversal, or observer phase is introduced.

For each marked projection and each of its two retained intervals, the
intersection with the other retained support is extracted as a complete
boundary subcomplex. The test verifies that it is exactly one connected
boundary cell (one vertex or one edge), then records its position relative to
the marked edge and ordered endpoints.

This matters because the L6c equivalence intentionally forgets shared-cell
identity and dimension. The L7b invariant retains the cyclic placement, not
the particular face/edge/vertex chosen to represent the overlap.

Results in each target domain:

| L7b test | Result |
|---|---:|
| Retained boundary-footprint comparisons | 60 |
| Cyclic-placement mismatches | 0 |
| Projections failing L7b | 0 |
| Parent boundary-word coherence groups | 2/2 |
| Origins in each parent group | 15 |

All 60 child footprints and all 60 parent footprints lie strictly in the open
complementary arc from the head endpoint back to the tail endpoint. None
contains the distinguished edge or touches either marked endpoint.

Footprint cell types:

| Child footprint | Parent footprint | Comparisons |
|---|---|---:|
| Vertex | Edge | 32 |
| Edge | Edge | 28 |

Thus the cell dimension can change in 32 comparisons, exactly as permitted by
the adopted L6c coarse equivalence. It does not change the relative cyclic
placement: every retained footprint is one connected cell in the same open
complementary arc. Since there is only one retained footprint on each
restricted boundary in a projection, there is no unresolved ordering among
multiple retained footprints. An orientation-preserving boundary
subdivision/collapse can carry the footprint along that same anchored arc
while fixing the directed matched edge and its ordered endpoints.

For each of the two exact parent structures, all 15 incoming restrictions
have one identical ordered two-interval word, equal to the parent word:
`(open_complementary_arc, open_complementary_arc)`.

**Finite L7b cyclic-placement verdict: PASS**, 60/60 comparisons and 30/30
projections in both target domains, under the stated dimension-forgetting
L6c convention.

A stricter requirement that preserve the dimension of the footprint cell
would reject the 32 vertex-to-edge comparisons. That is not the adopted
hierarchy: L6c explicitly forgets the shared-cell dimension, while L7b
preserves its anchored cyclic placement.

## 5. Independence and provenance

The support assignment is fixed solely from target geometry and the
demand-independent candidate search. The Hall source exporter is used only to
enumerate the 22 sources, eligible marks, and parent projections. No demand,
load, deficiency, matching output, or flow output enters support selection or
any L6c/L7b decision.

The finite calculations were executed in the analysis session against the
frozen PF-I16/PF-I11 target face populations and independently reconstructed
source records. The repository verifier has been committed and fetched back
for content verification; it has **not** been run from a clean cloned
repository checkout in this session. The script is the reproducibility
artifact; do not describe this as a clean-checkout execution.

## 6. Interpretation and limits

This removes the previous L7b obstruction for the old frozen motif: the
alternative triple satisfies L4-L5, finite L6c, and finite L7b simultaneously
for all order-six sources and eligible marks in the two Ngrid=7 target
domains.

It does **not** establish L8, a construction independent of the finite target
window, an all-orders incidence lift, or the arbitrary-family all-orders Hall
inequality. The direct mixed-fiber Hall inequality remains the main proof
route. The incidence lift remains a finite geometric diagnostic and possible
proof representation, not a replacement for the Hall argument.

Next: retain this triple and support assignment as the current finite
incidence-lift candidate; test larger target windows and higher parent orders
without changing the frozen n=6 result or using Hall demands/flows to select
supports.
