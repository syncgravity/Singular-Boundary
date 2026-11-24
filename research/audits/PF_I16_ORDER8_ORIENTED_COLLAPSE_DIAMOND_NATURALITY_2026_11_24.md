# PF-I16 order-eight oriented boundaries and collapse-diamond naturality

Date: 2026-11-24 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **clean GitHub Actions replay succeeded** for the graph-5/graph-12 collapse-diamond audit (run [45449218223](https://github.com/syncgravity/Singular-Boundary/actions/runs/45449218223)). Separate full-diagram replay also succeeded for 284 graph-1/2/3 candidates (run [45449218309](https://github.com/syncgravity/Singular-Boundary/actions/runs/45449218309)). The finite support-diagram and two-order path frontier now covers graph families 1, 2, 3, 5, and 12. The 10 graph-1/2/3 source critical pairs pass 4,084 two-order path instances with same-pair-set adjacent commutation; the 44 graph-5/12 pairs pass 43,696 instances, including the alternating-cycle cases.

## 1. Purpose

The previous source-labelled audit retained all 15 labelled intersections for each four-support witness, relative-deletion booleans, anchored footprint words, and the source parent deletion diamonds. The present audit strengthens that record in two ways:

1. Reconstruct each oriented boundary cycle directly from the accepted rhombus faces, anchored at the directed matched edge, rather than trusting the stored boundary-cycle field.
2. Construct explicit elementary relative-collapse sequences along both orders of each source critical pair, compare their pair sets, and factor every differing-pair case into a common prefix and dependency-closed local suffixes.

The source-side deletion theorem and the target-side geometric comparison remain distinct. In particular, the order-eight source exporter provides interval endpoints and overlap trees, but no source-prescribed ℤ^5 displacement or oriented boundary word.

## 2. Pinned inputs

- Independent four-support diagram JSON SHA-256: `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba`.
- Accepted-face inventory face-key-table SHA-256: `c20b727809eeb173ec11f584c2d60fc7afa3283e39a2dc3ccde0187703ce9ec9`.
- Source audit schema: `PF-I16-SOURCE-LABELLED-FOUR-SUPPORT-RESTRICTION-AUDIT-v2`.
- Source order: (n=8), with 608 canonical source records.

The verifier imports the repository's canonical order-eight source exporter and geometric cell/collapse primitives. It independently reconstructs the boundary cycles, intersection contents, and elementary collapse paths.

## 3. Exact oriented-boundary reconstruction

For each of the 996 retained four-support witnesses, the verifier:

- Builds the support complex from its accepted rhombus face indices.
- Counts face incidences of each edge and extracts the one-face boundary.
- Checks that the boundary is a single 2-regular cycle.
- Starts the cycle at the directed matched edge, lower endpoint to upper endpoint.
- Compares the complete vertex sequence and open complementary arc with the stored certificate.
- Independently reconstructs each neighboring support's boundary footprint and its position in the oriented open arc.
- Rechecks every footprint-meeting relation.

Results:

| Check | Count |
|---|---:|
| Four-support witnesses | 996 |
| Independently reconstructed anchored oriented cycles | 3,984 / 3,984 |
| Open complementary arcs | 3,984 / 3,984 |
| Ordered multi-footprint words | 3,984 / 3,984 |
| Labelled intersection entries recomputed, including empty entries | 14,940 / 14,940 |
| Relative single-support deletion-collapse checks | 3,984 / 3,984 |

The boundary-footprint word census over the 3,984 support boundaries is:

| Number of footprints | Support boundaries |
|---:|---:|
| 1 | 514 |
| 2 | 1,478 |
| 3 | 1,992 |

Thus the finite order-eight candidate family has genuine multi-footprint data, not just one distinguished footprint per boundary.

### Eligible source marks by graph family

The pinned source-labelled audit has this exact mark census across all witness rows and both root-preserving maps:

| Source graph | Source records | Eligible marks per source record | Mark-set distribution in map rows | Source critical pairs |
|---|---:|---|---|---:|
| Graph 5 | 12 | 2 or 3 | \`(1,2,3)\`: 4 records; \`(2,3)\`: 4; \`(1,3)\`: 4 | 20 |
| Graph 12 | 48 | 1 or 2 | \`(2,3)\`: 12 records; \`(1,3)\`: 12; \`(3)\`: 12; \`(2)\`: 6; \`(1)\`: 6 | 24 |

For graph 12, no source record has three eligible marks. Thus there is no additional third-mark restriction beyond its two-mark source diamonds. The order-eight collapse audit instead checks both elementary collapse orders for all 24 graph-12 critical pairs across all 482 graph-12 witnesses and both root-preserving graph maps (23,136 lifted instances). Graph 5 contributes 20 source critical pairs across 514 witnesses and both maps (20,560 instances). Together these give the 43,696 lifted path comparisons below.

## 4. Source-side order-eight deletion diamonds

The canonical source exporter generates 608 order-eight records and 490 pairs of simultaneous eligible non-root leaf deletions. The verifier independently composes endpoint compression in both orders and compares the final parent intervals, parent tree, and original-to-final port map.

All 490 / 490 source-side diamonds commute.

The current geometric four-support inventory represents only two overlap-graph families:

- Graph 5: 12 source records and 20 source critical pairs.
- Graph 12: 48 source records and 24 source critical pairs.

Therefore 44 of the 490 source diamonds are represented by the present four-support geometry; the other 446 belong to other order-eight overlap-graph families and remain without a geometric lift in this audit.

Across the 996 witnesses, the 60 represented source records, and both root-preserving graph maps, the verifier checks:

| Check | Count |
|---|---:|
| Source/witness/map rows | 58,608 |
| Parent port-order restriction checks | 98,192 |
| Source-diamond geometric lift instances | 43,696 |
| Distinct source critical pairs represented geometrically | 44 |

Both root-preserving graph maps remain admissible. A direct label-swap diagnostic confirms that the ambiguity matters at the finer geometric level:

- Swapping support labels 1 and 2 preserves the coarse 15-entry intersection signature in 288 of 996 witnesses (178 graph-5 and 110 graph-12), but changes it in the other 708.
- The same swap preserves the ordered multi-footprint word data in 0 of 996 witnesses; all 996 ordered word systems distinguish the two labelings.

This is not a proof that no more general geometric diagram isomorphism exists. It does show that the source's overlap graph alone supplies no criterion for selecting the boundary-word orientation required by the finer L7b comparison.

## 5. Elementary relative-collapse paths

For each represented source critical pair, the verifier constructs both paths:
[
U_4 searrow U_3^{(-m)} searrow U_2^{(-m,-n)},qquad
U_4 searrow U_3^{(-n)} searrow U_2^{(-m,-n)}.
]

Each elementary pair is checked at the moment it is applied:
- an FE pair removes a free edge and its unique incident face, neither in the retained target;
- an EV pair removes a free vertex and its unique incident edge, with no remaining incident face.

Both paths replay to the same retained two-support complex in all 43,696 source-map diamond instances.

The collapse-path comparison gives:

| Comparison | Instances |
|---|---:|
| Same elementary-pair set | 25,472 |
| Same pair set, normalized by valid adjacent collapse commutations | 25,472 |
| Different elementary-pair sets | 18,224 |
| Different pair sets forming one connected alternating cycle | 18,224 |

The alternating-cycle sizes are:

| Alternating-cycle cells | Instances |
|---:|---:|
| 4 | 256 |
| 6 | 7,488 |
| 8 | 9,120 |
| 12 | 1,360 |

The source-graph split is informative:

| Source graph family | Same pair set | Different pair set | Alternating-cycle types |
|---|---:|---:|---|
| Graph 5 | 18,944 | 1,616 | 256 four-cell; 1,360 twelve-cell |
| Graph 12 | 6,528 | 16,608 | 7,488 six-cell; 9,120 eight-cell |

No differing-pair case in this finite family decomposes into multiple alternating components.

## 6. Dependency-closed local switch factorization

For each of the 18,224 differing-pair instances, the verifier starts with the alternating-difference pairs and closes the local block under failed adjacent commutations. It then checks:

- The two paths have the same prefix pair set.
- The prefixes reach the same intermediate cell inventory.
- The common prefixes normalize to the same ordered sequence by valid adjacent collapse commutations.
- The two dependency-closed suffixes have the same additional-pair set.
- Both suffixes replay from the common intermediate complex to the same retained two-support target.

All 18,224 instances pass these checks.

Dependency-closed suffix sizes:

| Suffix pairs | Instances |
|---:|---:|
| 4 | 1,696 |
| 5 | 8,064 |
| 6 | 32 |
| 7 | 1,680 |
| 8 | 3,824 |
| 10 | 1,360 |
| 11 | 1,568 |

Common additional-pair counts:

| Additional pairs | Instances |
|---:|---:|
| 0 | 1,632 |
| 1 | 2,160 |
| 2 | 6,912 |
| 4 | 4,496 |
| 5 | 512 |
| 6 | 1,296 |
| 7 | 1,152 |
| 8 | 64 |

The order of common additional pairs agrees in 12,800 instances and is order-sensitive in 5,424. The latter are not failed replays: both local suffixes remain valid and have the same additional-pair set. They identify larger local switch templates that cannot be reduced to adjacent swaps alone.

## 7. Updated coverage frontier across all order-eight source diamonds

The source inventory has 490 critical pairs across 608 source records and 13 overlap-graph families. The geometric and path-level coverage is now:

| Graph | Source records | Source diamonds | Root-preserving maps | Candidate fourth edges | Full four-support verification | Two-order collapse-path diamond |
|---:|---:|---:|---:|---:|---|---|
| 1 | 2 | 6 | 6 | 99 | 99 / 99 candidates pass | 3,564 instances pass; same pair set |
| 2 | 2 | 2 | 1 | 110 | 110 / 110 candidates pass | 220 instances pass; same pair set |
| 3 | 2 | 2 | 2 | 75 | 75 / 75 candidates pass | 300 instances pass; same pair set |
| 4 | 2 | 0 | 1 | 97 | Candidate frontier only | No source diamond |
| 5 | 12 | 20 | 2 | 103 | 514 witness rows pass | 20 source pairs; 20,560 lifted instances pass |
| 6 | 18 | 30 | 2 | 32 | Candidate frontier only | Not yet checked |
| 7 | 12 | 8 | 1 | 65 | Candidate frontier only | Not yet checked |
| 8 | 12 | 8 | 1 | 105 | Candidate frontier only | Not yet checked |
| 9 | 18 | 6 | 2 | 32 | Candidate frontier only | Not yet checked |
| 10 | 48 | 48 | 2 | 19 | Candidate frontier only | Not yet checked |
| 11 | 48 | 48 | 2 | 23 | Candidate frontier only | Not yet checked |
| 12 | 48 | 24 | 2 | 21 | 482 witness rows pass | 24 source pairs; 23,136 lifted instances pass |
| 13 | 384 | 288 | 6 | 18 | Candidate frontier only | Not yet checked |
| **Total** | **608** | **490** | — | — | **1,280 verified candidate diagrams in families 1,2,3,5,12** | **54 / 490 source pairs; 47,780 lifted instances** |

The graph-1/2/3 full-diagram verifier checks 284 candidate diagrams (99, 110, and 75 respectively) against the accepted face inventory. It recomputes all 15 labelled intersections, the full overlap graph, point-contractibility of nonempty intersections and the full union, four matched-edge collapses, four anchored boundary cycles, four ordered footprint words, and all source-eligible single-deletion restrictions for every root-preserving source-to-support map. All 1,708 source-map rows pass. See [the separate graph-1/2/3 full-diagram audit](PF_I16_GRAPH123_FULL_FOUR_SUPPORT_DIAGRAM_CANDIDATES_2026_11_24.md).

The subsequent graph-1/2/3 source-diamond verifier checks both orders for all ten distinct source critical pairs across the candidate diagrams and root-preserving maps. All 4,084 path instances replay to the same retained two-support complex. In all 4,084, the elementary FE/EV pair sets are identical and one path normalizes to the other by valid adjacent commutations. See [the graph-1/2/3 path-naturality audit](PF_I16_GRAPH123_SOURCE_DIAMOND_PATH_NATURALITY_2026_11_24.md).

For graph 5 and 12, the two-order paths are checked in 43,696 lifted instances. Of these, 25,472 have the same pair set and normalize by adjacent commutations; the other 18,224 have different pair sets, each a single alternating cycle, and factor through a common normalized prefix plus dependency-closed local suffixes.

The remaining 436 source diamonds lie in graph families 6, 7, 8, 9, 10, 11, and 13, and remain without full four-support diagrams in this audit. Graph 4 has no source critical pairs. Thus the 490 source diamonds divide exactly into:
- 54 graph-1/2/3/5/12 pairs with complete finite two-order path comparisons;
- 436 pairs in the remaining graph families without full four-support geometric lifts.

## 8. Interpretation

This advances the finite geometric confluence audit in four concrete ways:

1. It independently authenticates the complete oriented boundary cycles and multi-footprint words for the 996 graph-5/graph-12 four-support witnesses.
2. It verifies 284 additional full four-support diagrams in graph families 1, 2, and 3, including all source-eligible one-step restrictions across 1,708 source-map rows.
3. It upgrades the ten graph-1/2/3 source critical pairs to 4,084 two-order path comparisons; all have identical elementary-pair sets and valid adjacent-swap normalizations.
4. It verifies 43,696 graph-5/graph-12 two-order path instances; differing-pair cases are single alternating cycles and factor through a common normalized prefix plus dependency-closed local suffixes.

It does **not** close geometric L8. In particular:

- 436 of the 490 order-eight source diamonds in graph families 6, 7, 8, 9, 10, 11, and 13 remain without full four-support geometric lifts.
- Both root-preserving graph maps remain possible.
- The source does not prescribe a unique ℤ^5 edge displacement or oriented boundary word.
- A finite factorization of collapse sequences is not yet a natural homotopy or equality of collapse maps.
- No all-orders local switch lemma, all-orders accepted-face confluence theorem, or all-orders PF-I16 Hall inequality follows.

## 9. Graph-1/2/3 full-diagram replay

Verifier: `research/scripts/verify_pf_i16_graph123_full_diagram_candidates.py`  
Audit: [PF_I16_GRAPH123_FULL_FOUR_SUPPORT_DIAGRAM_CANDIDATES_2026_11_24.md](PF_I16_GRAPH123_FULL_FOUR_SUPPORT_DIAGRAM_CANDIDATES_2026_11_24.md)  
Workflow: [45449218309](https://github.com/syncgravity/Singular-Boundary/actions/runs/45449218309), conclusion SUCCESS  
Artifact: [14947201304](https://github.com/syncgravity/Singular-Boundary/actions/runs/45449218309/artifacts/14947201304)  
Decoded JSON SHA-256: `29c2be19fefb2e80bd788ec086621d0df071c24da3db165cec060f2ea9688f66`.

The 284 candidate diagrams pass all full-diagram checks and 1,708 source-map rows. The verifier intentionally checks only source-eligible deletion indices; it does not claim that all four support deletions pass. The exact eligible support-index sets are graph 1 `{1,2,3}`, graph 2 `{1,3}`, and graph 3 `{0,2,3}`.

## 10. Reproduction

Verifier:

`research/scripts/verify_pf_i16_order8_oriented_collapse_diamond_naturality.py`

The CI step consumes the generated order-eight diagram JSON, accepted-face inventory, and source-labelled restriction audit. It emits row-level witness/pair path digests and the complete finite census above. The clean-checkout reproducibility gate passed in workflow [45449218223](https://github.com/syncgravity/Singular-Boundary/actions/runs/45449218223), artifact [14947481287](https://github.com/syncgravity/Singular-Boundary/actions/runs/45449218223/artifacts/14947481287). Decoded JSON SHA-256: `15b3b16d1d3f7ae2e7d49847f8df7fa15f9708b0c6376f5f1d8d4fcc03d8c00a`.
