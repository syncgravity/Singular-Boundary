# PF-I16 graph-1/2/3 source deletion-diamond path naturality

Date: 2026-11-24 UTC  
Branch: \`research/pf-i16-four-interval-diamond-2026-11-19\`  
Workflow: [45450043737](https://github.com/syncgravity/Singular-Boundary/actions/runs/45450043737), conclusion **SUCCESS**  
Workflow head: \`dda13d4300c9659ef45dc9ab7dbc684ec5213c91\`  
Artifact: [14948566421](https://github.com/syncgravity/Singular-Boundary/actions/runs/45450043737/artifacts/14948566421)  
Artifact ZIP SHA-256: \`4505c7c45ca21dd3b0821d6381c31bbd16c68aacf4ef4c168c1b018cb01978a1\`  
Decoded JSON SHA-256: \`7fce5ff57a7fc263e45589a98c951c0f21da53d1b2821b0aaeae1a906110cfd4\`

**Status:** all 4,084 finite source-diamond path instances in graph families 1, 2, and 3 pass both-order replay, source endpoint-compression comparison, retained-pair footprint comparison, and valid adjacent-swap normalization. All 4,084 comparisons have the same elementary collapse-pair set; there are no alternating-cycle discrepancies in these three graph families.

## 1. Inputs and scope

This verifier combines:
- the Ngrid=12 accepted-face support inventory;
- the graph-1/2/3 parent-compatibility graph catalogue;
- the independently replayed 284-candidate full-diagram audit;
- the canonical order-eight source exporter.

Pinned input SHA-256 values:

| Input | SHA-256 |
|---|---|
| Support inventory | \`5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f\` |
| Parent compatibility | \`4adf31790694d4080e51885e0d83fb9f90b690f0c5cb40818946a22bf693df88\` |
| Graph-1/2/3 full diagrams | \`29c2be19fefb2e80bd788ec086621d0df071c24da3db165cec060f2ea9688f66\` |

The finite candidate family comprises 99 graph-1 diagrams, 110 graph-2 diagrams, and 75 graph-3 diagrams. The source records have respectively 6, 2, and 2 distinct eligible-mark critical pairs.

## 2. Exact source-pair and path-instance census

| Graph | Candidate diagrams | Source-map rows per candidate | Source-map rows | Distinct source critical pairs | Path instances |
|---:|---:|---:|---:|---:|---:|
| 1 | 99 | 12 | 1,188 | 6 | 3,564 |
| 2 | 110 | 2 | 220 | 2 | 220 |
| 3 | 75 | 4 | 300 | 2 | 300 |
| **Total** | **284** | — | **1,708** | **10** | **4,084** |

The ten distinct source critical pairs are:

| Graph | Source record index | Eligible mark pair |
|---:|---:|---|
| 1 | 326 | (1,2) |
| 1 | 326 | (1,3) |
| 1 | 326 | (2,3) |
| 1 | 467 | (1,2) |
| 1 | 467 | (1,3) |
| 1 | 467 | (2,3) |
| 2 | 82 | (1,3) |
| 2 | 83 | (1,3) |
| 3 | 8 | (2,3) |
| 3 | 15 | (2,3) |

The path-instance multiplicity is the product of candidate diagrams, root-preserving source-to-support maps, and eligible mark pairs. Every instance retains the source record index and exact source-to-support map.

## 3. Checks performed for every path instance

For each source-map row and each eligible source-mark pair \((m,n)\), the verifier:

1. Composes source interval compression and source-tree deletion in both orders and checks equality of the final parent intervals, parent tree, and original-to-final port map.
2. Maps the two deleted source marks through the exact root-preserving source-to-support map.
3. Checks that the two retained supports have a nonempty point-contractible intersection.
4. Reconstructs the retained pair's footprint from both oriented boundary words and checks that the two footprint descriptions have the same cell type and exact cell vertices.
5. Constructs both geometric paths
   \[
   U_4\searrow U_3^{(-m)}\searrow U_2^{(-m,-n)},\qquad
   U_4\searrow U_3^{(-n)}\searrow U_2^{(-n,-m)}.
   \]
6. Replays every FE and EV elementary collapse at the moment it is applied, and checks that both paths terminate at the same retained two-support complex.
7. Compares the elementary pair sets. When the sets agree, it normalizes one path to the other by valid adjacent collapse commutations, checking that both two-step orders at every swap reach the same intermediate cell inventory.

Aggregate checks:

| Check | Result |
|---|---:|
| Source endpoint-compression diamonds | 4,084 / 4,084 |
| Retained-pair common footprints | 4,084 / 4,084 |
| Both two-order geometric paths replay | 4,084 / 4,084 |
| Same elementary-pair set | 4,084 / 4,084 |
| Valid adjacent-swap normalizations | 4,084 / 4,084 |
| Different elementary-pair sets | 0 |
| Alternating-cycle discrepancies | 0 |

## 4. Adjacent-swap normalization census

The number of valid adjacent commutations needed to normalize the two deterministic collapse sequences is:

| Valid adjacent swaps | Path instances |
|---:|---:|
| 28 | 12 |
| 30 | 2 |
| 36 | 36 |
| 40 | 254 |
| 54 | 4 |
| 60 | 34 |
| 63 | 52 |
| 70 | 414 |
| 81 | 16 |
| 90 | 536 |
| 100 | 2,724 |
| **Total** | **4,084** |

The maximum observed normalization length is 100 valid adjacent swaps. This is a property of the deterministic finite path pairs in this candidate family, not a uniform all-orders bound.

## 5. Relation to the graph-5/graph-12 collapse-diamond result

The separate order-eight replay covers 44 graph-5/graph-12 source critical pairs across 43,696 lifted instances:
- 25,472 have the same elementary-pair set and normalize by valid adjacent swaps;
- 18,224 have different pair sets, each a single connected alternating cycle, and factor through a common normalized prefix plus dependency-closed local suffixes.

Combining the two independently replayed candidate families gives:

| Quantity | Graphs 1/2/3 | Graphs 5/12 | Combined |
|---|---:|---:|---:|
| Distinct source critical pairs | 10 | 44 | 54 |
| Lifted path instances | 4,084 | 43,696 | 47,780 |
| Same elementary-pair set | 4,084 | 25,472 | 29,556 |
| Different elementary-pair sets | 0 | 18,224 | 18,224 |
| Valid same-set / prefix normalizations | 4,084 | 25,472 + 18,224 | 47,780 |

For graph families 1, 2, 3, 5, and 12, every represented path instance therefore has a finite certified comparison: either same-pair adjacent commutation or the graph-5/graph-12 alternating-cycle factorization.

## 6. Interpretation and remaining obligation

This closes the two-order finite path comparison for the ten graph-1/2/3 source critical pairs over the 284 full candidate diagrams. In these families the two collapse paths use exactly the same elementary FE/EV pair set; their discrepancy is ordering only, and the deterministic paths are connected by valid adjacent commutations.

Together with the graph-5/graph-12 result, the finite geometric path audit now covers 54 of the 490 order-eight source critical pairs, across 1,280 full four-support candidate diagrams in graph families 1, 2, 3, 5, and 12.

The remaining 436 source critical pairs lie in graph families 6, 7, 8, 9, 10, 11, and 13. Their full four-support diagrams and path comparisons remain open. Graph 4 has no source critical pairs.

This finite result does **not** prove equality of collapse maps or a natural homotopy under arbitrary restriction. It does not supply a uniform all-orders local switch lemma, all-orders accepted-face confluence, geometric L8, split-demand Hall, or the all-orders weighted one-link inequality.

## 7. Reproduction

Verifier: \`research/scripts/verify_pf_i16_graph123_source_diamond_path_naturality.py\`  
Workflow: \`.github/workflows/pf-i16-graph123-source-diamond-path-naturality.yml\`  
Successful replay: [45450043737](https://github.com/syncgravity/Singular-Boundary/actions/runs/45450043737)  
Artifact: [14948566421](https://github.com/syncgravity/Singular-Boundary/actions/runs/45450043737/artifacts/14948566421)
