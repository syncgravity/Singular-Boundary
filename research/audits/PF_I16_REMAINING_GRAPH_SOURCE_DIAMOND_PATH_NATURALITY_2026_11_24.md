# PF-I16 remaining graph-family source deletion-diamond path naturality

Date: 2026-11-24 UTC  
Branch: \`research/pf-i16-four-interval-diamond-2026-11-19\`  
Workflow: [45453607246](https://github.com/syncgravity/Singular-Boundary/actions/runs/45453607246), conclusion **SUCCESS**  
Workflow head: \`08a0d7275f2aa25e13df49381f454eee21dc0248\`  
Artifact: [14949866004](https://github.com/syncgravity/Singular-Boundary/actions/runs/45453607246/artifacts/14949866004)  
Artifact ZIP SHA-256: \`300a43473e1015e9e18b594241cebed2bd34dcf442c51b4ddb842ec2003e1e52\`  
Decoded JSON SHA-256: \`597b6a0fd4e77a8ac1ef15a0d3d2397eaceb338ae39a3895e134a983a1ed62a2\`

**Status:** all 436 distinct source critical pairs in graph families 6, 7, 8, 9, 10, 11, and 13 pass both-order geometric collapse-path comparison over the 333 passing full-diagram candidates. All 34,828 path instances replay. Of these, 34,804 have identical elementary-pair sets; the remaining 24 are graph-9 four-cell alternating-cycle cases with a dependency-closed local suffix.

## 1. Pinned inputs and candidate scope

Inputs:
- Support inventory SHA-256: \`5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f\`.
- Parent-compatibility output SHA-256: \`4adf31790694d4080e51885e0d83fb9f90b690f0c5cb40818946a22bf693df88\`.
- Remaining graph full-diagram output SHA-256: \`f0c02e7d2f5a9bc850ed679e7162eca2059142d9cd4d0d946f6497aac5916be1\`.

The preceding full-diagram verifier selected 333 passing candidate diagrams from 391 candidates in graph families 4, 6, 7, 8, 9, 10, 11, and 13. The 58 rejected candidates were excluded because their full four-support union was not point-contractible and source-eligible relative deletion failed. The path verifier uses only the 333 passing candidates.

## 2. Source-map and path-instance census

| Graph | Passing candidate diagrams | Source-map rows per candidate | Aggregate source-map rows | Distinct source critical pairs | Path instances |
|---:|---:|---:|---:|---:|---:|
| 4 | 97 | 2 | 194 | 0 | 0 |
| 6 | 18 | 36 | 648 | 30 | 1,080 |
| 7 | 65 | 12 | 780 | 8 | 520 |
| 8 | 105 | 12 | 1,260 | 8 | 840 |
| 9 | 19 | 36 | 684 | 6 | 228 |
| 10 | 10 | 96 | 960 | 48 | 960 |
| 11 | 1 | 96 | 96 | 48 | 96 |
| 13 | 18 | 2,304 | 41,472 | 288 | 31,104 |
| **Total** | **333** | — | **46,094** | **436** | **34,828** |

Graph 4 has no source critical pairs; its 97 passing candidate diagrams contribute no path instances.

## 3. Checks for every path instance

For every passing candidate, every root-preserving source-to-support map, and every pair of eligible source marks, the verifier:

1. Checks source endpoint compression in both deletion orders, including the final parent intervals, parent tree, and original-to-final port map.
2. Maps the source marks through the exact source-to-support map.
3. Checks that the two retained supports have a nonempty point-contractible intersection.
4. Checks the retained pair's common footprint from both oriented boundary words, including cell type and exact cell vertices.
5. Constructs both two-step relative-collapse paths from the four-support union to the retained two-support complex.
6. Replays every FE/EV collapse and checks that both paths reach the same target.
7. Compares the elementary pair sets. Equal sets are normalized by valid adjacent commutations; different sets are classified by alternating cycle and dependency-closed factorization.

| Check | Result |
|---|---:|
| Source endpoint-compression diamonds | 34,828 / 34,828 |
| Retained-pair common footprints | 34,828 / 34,828 |
| Both two-order geometric paths replay | 34,828 / 34,828 |
| Source-map rows checked | 46,094 |

## 4. Collapse-path comparison

| Comparison | Instances |
|---|---:|
| Same elementary-pair set | 34,804 |
| Same pair set, normalized by valid adjacent swaps | 34,804 |
| Different elementary-pair sets | 24 |
| Different sets forming one connected alternating cycle | 24 |

All 24 differing-pair cases occur in graph 9:
- alternating-cycle size: 4 cells;
- dependency-closed suffix size: 3 elementary pairs;
- common additional pair: 1 EV pair;
- common additional-pair order agrees on both paths;
- common prefixes normalize by 30 valid adjacent swaps.

No graph-6, graph-7, graph-8, graph-10, graph-11, or graph-13 path instance has a different elementary-pair set.

## 5. Combined finite order-eight source-diamond path result

The graph-1/2/3 and graph-5/12 path audits are recorded separately. Combining all three clean replays:

| Graph families | Distinct source critical pairs | Path instances | Same pair set | Different pair sets |
|---|---:|---:|---:|---:|
| 1, 2, 3 | 10 | 4,084 | 4,084 | 0 |
| 5, 12 | 44 | 43,696 | 25,472 | 18,224 |
| 4, 6, 7, 8, 9, 10, 11, 13 | 436 | 34,828 | 34,804 | 24 |
| **Total** | **490** | **82,608** | **64,360** | **18,248** |

All 64,360 same-set cases normalize by valid adjacent collapse commutations. All 18,248 different-set cases are single connected alternating cycles and pass dependency-closed common-prefix/local-suffix factorization:
- 4-cell cycles: 280;
- 6-cell cycles: 7,488;
- 8-cell cycles: 9,120;
- 12-cell cycles: 1,360.

The graph-5/graph-12 cases account for all 5,424 order-sensitive common-extra-pair sequences; the 24 graph-9 cases are order-aligned.

Thus every one of the 490 order-eight source critical pairs has at least one verified finite geometric path comparison within the accepted candidate families. This is a finite \(n=8\) result, not an all-orders theorem.

## 6. Reproduction

Verifier:
\`research/scripts/verify_pf_i16_remaining_graph_source_diamond_path_naturality.py\`

Workflow:
\`.github/workflows/pf-i16-remaining-graph-source-diamond-path-naturality.yml\`

Successful clean replay: [45453607246](https://github.com/syncgravity/Singular-Boundary/actions/runs/45453607246), artifact [14949866004](https://github.com/syncgravity/Singular-Boundary/actions/runs/45453607246/artifacts/14949866004).

## 7. Nonclaims and next theorem obligation

The finite result does not prove:
- equality of collapse maps or a natural homotopy under arbitrary further support restrictions;
- a uniform all-orders local switch or accepted-face confluence theorem;
- a source-prescribed unique \(\mathbb Z^5\) displacement/oriented boundary word;
- geometric L8 at all orders;
- the all-orders multivalued-\(\pi\) Hall inequality;
- split-demand capacity-preserving transport or the weighted one-link inequality.

The next proof obligation is to extract a uniform structural lemma from the finite path classifications: same-pair commutation versus a single alternating-cycle dependency-closed switch. That lemma must be independent of the finite candidate census and stable under further support restrictions. The Hall workstream remains separate: continue reverse-mark-sensitive, nonuniform global transport across parent fibers using \((J,P_J(T))\) and parent-overlap data; do not return to fixed-selector, equal-share row normalization, or single-parent-neighborhood repair.
