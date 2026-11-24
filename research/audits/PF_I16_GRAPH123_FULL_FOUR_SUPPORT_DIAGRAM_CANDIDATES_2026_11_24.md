# PF-I16 graph-1/2/3 full four-support diagram candidates

Date: 2026-11-24 UTC  
Branch: \`research/pf-i16-four-interval-diamond-2026-11-19\`  
Workflow: [45367265481](https://github.com/syncgravity/Singular-Boundary/actions/runs/45367265481), conclusion **SUCCESS**  
Workflow head: \`388ac8d74e8e1f391b305c1bf1b254b302cb79c1\`  
Artifact: [14908025381](https://github.com/syncgravity/Singular-Boundary/actions/runs/45367265481/artifacts/14908025381)  
Artifact ZIP SHA-256: \`807106ec6ae3a68c3cb6bcab9d5925c3f705297c5536ca1f157676f133667c84\`  
Decoded JSON SHA-256: \`29c2be19fefb2e80bd788ec086621d0df071c24da3db165cec060f2ea9688f66\`

**Status:** all 284 candidates in graph families 1, 2, and 3 pass the full finite four-support diagram checks and every source-eligible deletion restriction across all root-preserving source-to-support graph maps. This is a finite candidate-family result, not an all-orders naturality theorem.

## 1. Why this verifier was added

The parent-compatibility search produced fourth-edge candidate witnesses for graph families 1, 2, and 3. That screen checked the first-three parent restriction and fourth-support pairwise incidence/footprints. It did not by itself independently replay the full four-support diagrams.

This verifier therefore reconstructs each candidate from the accepted face inventory and checks the complete labelled four-support configuration, rather than treating parent compatibility as sufficient.

## 2. Exact candidate census

| Graph family | Candidate diagrams | Source-to-support map rows per candidate | Total map rows |
|---|---:|---:|---:|
| 1 | 99 | 12 | 1,188 |
| 2 | 110 | 2 | 220 |
| 3 | 75 | 4 | 300 |
| **Total** | **284** | — | **1,708** |

Every one of the 284 candidates passes. The first-failure traceback is absent because no candidate failed.

## 3. Checks performed on every candidate

For each candidate, the verifier independently:

1. Reconstructs all four accepted support complexes.
2. Checks the four matched-edge relative collapses.
3. Recomputes all 15 labelled intersections, including empty intersections, and checks the nonempty intersections for point-contractibility.
4. Recomputes the full pairwise overlap graph and verifies that it equals the specified graph family.
5. Checks that the full four-support union is point-contractible.
6. Reconstructs all four anchored boundary cycles from the accepted faces.
7. Reconstructs all four ordered multi-footprint words.
8. For every source record in the same graph family and every root-preserving source-to-support map, checks each source-eligible reverse mark against the corresponding relative-deletion collapse.

Aggregate results:

| Check | Result |
|---|---:|
| Four matched-edge relative collapses | 1,136 / 1,136 |
| Labelled intersections recomputed | 4,260 / 4,260 |
| Nonempty labelled intersections point-contractible | 1,988 / 1,988 |
| Full overlap graph matches | 284 / 284 |
| Four-support union point-contractible | 284 / 284 |
| Anchored boundary cycles reconstructed | 1,136 / 1,136 |
| Ordered footprint words reconstructed | 1,136 / 1,136 |
| Source-to-support map rows checked | 1,708 |
| Map rows with all source-eligible deletions passing | 1,708 / 1,708 |

Intersection census:
- 1-support intersections: 1,136 nonempty.
- 2-support intersections: 852 nonempty and 852 empty.
- 3-support intersections: 1,136 empty.
- 4-support intersections: 284 empty.

## 4. Important distinction: source-eligible deletion versus all four deletions

The verifier records all four relative-deletion outcomes, but does **not** require every support to admit a deletion. It requires exactly the deletions corresponding to eligible reverse marks in the source record, transported by the selected root-preserving graph map.

The observed valid relative-deletion index sets are:
- Graph 1: supports \`1,2,3\` (support \`0\` is not source-eligible).
- Graph 2: supports \`1,3\` (supports \`0,2\` are not source-eligible).
- Graph 3: supports \`0,2,3\` (support \`1\` is not source-eligible).

This distinction is essential. A statement that all four support deletions pass would be false for this candidate family. The verifier's passing claim is restricted to the source-eligible marks and is checked for every root-preserving map.

## 5. Boundary and footprint census

Across the 1,136 support boundaries:

| Boundary length | Count |
|---:|---:|
| 4 | 179 |
| 6 | 128 |
| 8 | 829 |

Across the 1,136 ordered footprint words:

| Number of footprints | Count |
|---:|---:|
| 1 | 742 |
| 2 | 220 |
| 3 | 174 |

These are measured finite distributions, not hypotheses imposed by the verifier.

## 6. Reproduction

Verifier:
\`research/scripts/verify_pf_i16_graph123_full_diagram_candidates.py\`

Workflow:
\`.github/workflows/pf-i16-graph123-full-diagram-candidates.yml\`

Pinned input digests:
- Ngrid=12 support inventory: \`5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f\`
- Parent-compatibility output: \`4adf31790694d4080e51885e0d83fb9f90b690f0c5cb40818946a22bf693df88\`

Successful replay: [45367265481](https://github.com/syncgravity/Singular-Boundary/actions/runs/45367265481).

## 7. Nonclaims and next obligation

This result does not establish:
- source-to-target port-map naturality;
- commutation of two source deletions as collapse maps;
- a common-prefix/local-switch factorization for these graph families;
- restriction naturality under arbitrary further support deletions;
- the all-orders L6c/L7b theorem;
- geometric L8;
- any all-orders Hall inequality, split-demand transport, or weighted one-link inequality.

The next finite proof obligation is to connect these graph-1/2/3 source-eligible restriction checks to the graph-5/graph-12 order-eight collapse-diamond audit, then test source deletion diamonds and path-level naturality for graph families 1, 2, and 3. The current result supplies the full support complexes and their eligible one-step restrictions; it does not yet supply the two-step diamond comparison.
