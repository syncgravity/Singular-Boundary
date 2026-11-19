# PF-I16 two-edge-anchored four-interval motif search

Date: 2026-11-19  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Pull request: #119 (draft)

## Result

A broader target-only search varied the third matched edge over the complete Ngrid=12 support inventory while keeping the first two matched edges of the demand-independent alternative triple fixed.

It found:

| Quantity | Count |
|---|---:|
| Eligible inventory matched edges | 8,007 |
| First-two support pairs passing the triangle-parent tests | 169 |
| First-three support assignments passing the tested triangle conditions | 8,957 |
| Distinct third matched edges with at least one such support assignment | 62 |
| Third edges with a common fourth edge for graph 5 and graph 12 | 0 |

For each of the 62 third edges, the verifier aggregates graph-5 fourth-edge candidates over **all** compatible first-three support assignments and separately aggregates graph-12 candidates over all compatible assignments. This allows graph 5 and graph 12 to use different first-three support assignments and different fourth support options. The two aggregated fourth-edge sets are disjoint for every third edge.

Graph-5 candidate-set sizes range from 44 to 103. Graph-12 candidate-set sizes range from 0 to 39. There are 41 third edges with at least one graph-12 candidate, but none has a candidate edge in common with its graph-5 set.

This rules out a four-interval extension that retains the first two matched edges of the original alternative triple, even after allowing every eligible third matched edge and every enumerated one-to-three-rhombus support assignment that passes the tested triangle-parent conditions.

## Method

The first two matched edges remain:
[
e_1=(-7,-4,5,7,0)	o(-6,-4,5,7,0),qquad
e_2=(-7,-3,5,7,-1)	o(-7,-3,6,7,-1).
]

For each support pair ((S_1,S_2)) on these edges, the verifier requires:
- each support collapses to its own distinguished matched edge;
- their intersection is nonempty and collapses to a vertex;
- each footprint is a single boundary cell on the open complementary arc of the other support.

It then enumerates every third matched edge in the inventory, excluding endpoint collisions, and every support (S_3) on that edge. It requires:
- (S_3) collapses to its own distinguished matched edge;
- all three pair intersections are nonempty and collapse to a vertex;
- all three pairwise footprints satisfy the two-sided open-complementary-arc condition;
- the three-support union collapses to a vertex; and
- relative deletion collapses hold for the two non-root leaves of the star parent tree (delete interval 1 or interval 2).

For each accepted first-three support assignment, the fourth-edge search forms two exact support-option masks:
- Graph 5: a fourth support intersects (S_1) and is vertex-disjoint from (S_2,S_3).
- Graph 12: a fourth support intersects both (S_2,S_3) and is vertex-disjoint from (S_1).

Both sides of every required open-arc footprint are checked. Candidate fourth edges must be vertex-disjoint from all three matched edges. Candidate fourth supports are not required to collapse to the fourth matched edge, and no four-support relative collapse or full L6c/L7b diagram test is imposed. This deliberately enlarges the candidate sets, making the empty-intersection result a necessary-condition obstruction.

## Reproducibility

- Workflow run: `44576452636`
- Job: `135745124704`
- Artifact ID: `14557741013`
- Artifact ZIP SHA-256: `937c47237c50593a751c89833f6b13e127e64257bf4af195ff58419b3d3b438f`
- Verifier: `research/scripts/verify_pf_i16_hall_four_interval_two_edge_anchored_search.py`
- Dependency geometry helpers: `research/scripts/verify_pf_i16_hall_four_interval_parent_compatibility.py`
- Target face-key SHA-256: `f0f63287b3194a8625e4dd5c0a7369b04da315406fdc64a0d828627814ada7eb`

## Scope and nonclaims

This is an exhaustive search over the third matched edge and support families **only with the first two matched edges fixed** as above. It does not search all possible first-two-edge pairs, all three-edge motifs, supports larger than three rhombi, or other target windows.

It is not a proof that no four-interval lift exists. It does not establish full L6c/L7b diamond confluence, L8 construction independence, or the all-orders Hall inequality.

## Next step

Vary the second matched edge while keeping the first edge anchored, or use the same support-incidence index to search all first-two-edge pairs. The graph-5/graph-12 common-fourth-edge test should remain the first pruning condition; full four-support L6c/L7b certificates should only be attempted after a common fourth edge survives.
