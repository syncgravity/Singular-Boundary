# PF-I16 remaining graph-family full four-support diagrams

Date: 2026-11-24 UTC  
Branch: \`research/pf-i16-four-interval-diamond-2026-11-19\`  
Workflow: [45451670803](https://github.com/syncgravity/Singular-Boundary/actions/runs/45451670803), conclusion **SUCCESS**  
Workflow head: \`c2c3518c030f92f0c4c1bf005eb53785aa70b2b7\`  
Artifact: [14947622863](https://github.com/syncgravity/Singular-Boundary/actions/runs/45451670803/artifacts/14947622863)  
Artifact ZIP SHA-256: \`82a1362c153c754c7676e3cd68ee11d518f7ff39c70c5326c6711bdfe61d9560\`  
Decoded JSON SHA-256: \`f0c02e7d2f5a9bc850ed679e7162eca2059142d9cd4d0d946f6497aac5916be1\`

**Status:** 333 of 391 remaining graph-family candidates pass the full finite four-support diagram checks, including every source-eligible deletion restriction across every root-preserving source-to-support map. The other 58 candidates fail both full-union point-contractibility and source-eligible relative deletion. Every one of the eight graph families has at least one passing candidate.

## 1. Scope and pinned inputs

This audit covers graph families 4, 6, 7, 8, 9, 10, 11, and 13. Graph families 1, 2, and 3 were audited separately; graph families 5 and 12 have the 996-witness oriented-boundary and collapse-diamond audit.

Pinned inputs:
- Ngrid=12 support inventory SHA-256: \`5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f\`.
- All-graph parent-compatibility output SHA-256: \`4adf31790694d4080e51885e0d83fb9f90b690f0c5cb40818946a22bf693df88\`.

The parent-compatibility screen supplied 391 fourth-edge/support candidate witnesses across these eight graph families. This verifier independently reconstructs each four-support diagram and tests the full accepted-face geometry.

## 2. Candidate pass/failure census

| Graph | Candidate diagrams | Full diagram passes | Rejected |
|---:|---:|---:|---:|
| 4 | 97 | 97 | 0 |
| 6 | 32 | 18 | 14 |
| 7 | 65 | 65 | 0 |
| 8 | 105 | 105 | 0 |
| 9 | 32 | 19 | 13 |
| 10 | 19 | 10 | 9 |
| 11 | 23 | 1 | 22 |
| 13 | 18 | 18 | 0 |
| **Total** | **391** | **333** | **58** |

All 333 passing candidates have every source-eligible deletion valid under every root-preserving source-to-support map. All 58 rejected candidates have both failure conditions:
- the full four-support union is not point-contractible;
- at least one source-eligible relative-deletion restriction fails for at least one root-preserving map, leaving at least one source record without a valid map for that candidate.

No other failure reason occurs in this candidate family. In particular, the four matched-edge collapses, all 15 labelled intersection checks, pairwise overlap-graph equality, nonempty-intersection point-contractibility, anchored boundary cycles, and ordered footprint words pass for the candidate rows; the rejection is at the full-union and source-eligible restriction stage.

## 3. Source-map coverage

The number of source-map rows checked per candidate and the aggregate row counts are:

| Graph | Source-map rows per candidate | All candidate rows | Passing candidate rows |
|---:|---:|---:|---:|
| 4 | 2 | 194 | 194 |
| 6 | 36 | 1,152 | 648 |
| 7 | 12 | 780 | 780 |
| 8 | 12 | 1,260 | 1,260 |
| 9 | 36 | 1,152 | 684 |
| 10 | 96 | 1,824 | 960 |
| 11 | 96 | 2,208 | 96 |
| 13 | 2,304 | 41,472 | 41,472 |
| **Total** | — | **50,042** | **46,094** |

Every passing candidate has all its source-map rows valid. The graph-13 family is especially broad: all 18 candidates pass across 41,472 source-map rows.

## 4. Boundary and footprint census

Across all 391 candidates and their 1,564 support boundaries:

| Boundary length | Count |
|---:|---:|
| 4 | 300 |
| 6 | 379 |
| 8 | 885 |

Across the same 1,564 ordered footprint words:

| Number of footprints | Count |
|---:|---:|
| 1 | 428 |
| 2 | 746 |
| 3 | 390 |

These are observed finite distributions.

## 5. Relation to the other graph families

Combining the finite full-diagram candidate audits:

| Graph families | Candidate diagrams | Passing diagrams |
|---|---:|---:|
| 1, 2, 3 | 284 | 284 |
| 4, 6, 7, 8, 9, 10, 11, 13 | 391 | 333 |
| 5, 12 | 996 | 996 |
| **Total** | **1,671** | **1,613** |

Thus every one of the 13 order-eight overlap-graph families has at least one fully verified four-support candidate. The 58 rejected candidates are not accepted witnesses and must not be counted as such.

The current source-diamond path audits cover:
- graph families 1, 2, 3: 10 source critical pairs, 4,084 path instances;
- graph families 5, 12: 44 source critical pairs, 43,696 path instances.

The next verifier tests both collapse orders for all source critical pairs in the passing candidates of graph families 6, 7, 8, 9, 10, 11, and 13. Its expected finite scope is 436 distinct source critical pairs across 34,828 path instances. This path-level replay is separate from the present full-diagram pass/failure census.

## 6. Reproduction

Verifier:
\`research/scripts/verify_pf_i16_remaining_graph_full_diagram_candidates.py\`

Workflow:
\`.github/workflows/pf-i16-remaining-graph-full-diagram-candidates.yml\`

Successful clean replay: [45451670803](https://github.com/syncgravity/Singular-Boundary/actions/runs/45451670803), artifact [14947622863](https://github.com/syncgravity/Singular-Boundary/actions/runs/45451670803/artifacts/14947622863).

## 7. Nonclaims

This is a finite candidate-family verification. It does not establish:
- a two-order source deletion diamond or equality/naturality of collapse maps;
- a uniform all-orders accepted-face confluence theorem;
- geometric L8;
- the all-orders multivalued-\(\pi\) Hall inequality;
- split-demand capacity-preserving transport or the weighted one-link inequality.


## 8. Completed two-order path replay

The 333 passing candidate diagrams are now the input to the clean path replay:
[PF_I16_REMAINING_GRAPH_SOURCE_DIAMOND_PATH_NATURALITY_2026_11_24.md](PF_I16_REMAINING_GRAPH_SOURCE_DIAMOND_PATH_NATURALITY_2026_11_24.md).

All 436 source critical pairs in graph families 6, 7, 8, 9, 10, 11, and 13 pass 34,828 path instances. There are 34,804 same-pair-set cases, each normalized by valid adjacent swaps, and 24 graph-9 four-cell alternating-cycle cases, each with a three-pair dependency-closed suffix. This completes the finite n=8 source-diamond path comparison together with the graph-1/2/3 and graph-5/12 audits; it does not prove all-orders naturality or geometric L8.
