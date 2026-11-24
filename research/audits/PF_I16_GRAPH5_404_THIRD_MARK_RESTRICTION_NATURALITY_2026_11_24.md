# PF-I16 graph-5 third-mark restriction naturality: all 404 differing-pair diamonds

Date: 2026-11-24 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **the original dependency-closed collapse factorization restricts exactly to the factorization on the three-support subcomplex in all 404 graph-5 source-mark-[1,2] certificate/map rows.** This closes the tested finite graph-5 restriction family, not all-orders geometric L8.

## 1. Question

The preceding 64-row audit treated the minimal four-cell alternating-cycle diamonds. The graph-5 collapse inventory contains a further 340 differing-pair-set rows with twelve-cell alternating cycles. All graph-5 source records admit the third reverse mark 3, while interval 0 is the fixed root.

This audit asks whether deleting source mark 3 is compatible with the complete dependency-closed factorization—not merely whether the original collapse paths can be replayed after restriction.

## 2. Inputs and integrity

The verifier consumes the immutable artifacts:

| Input | Artifact ID (prior immutable artifact) | Decoded payload SHA-256 |
|---|---:|---|
| Relative-collapse diamonds | `14680929981` | `d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141` |
| Independent four-support diagrams | `14681735833` | `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba` |
| Ngrid=12 accepted-face inventory | `14677507607` | `5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f` |

The current workflow regenerates the inventory with payload SHA-256 `3e50240bf1b037f3de8dd4e4c4ab94d4523533c25ceeab4000410c641cf07b77`; only the two floating-point minimum-margin values differ at the last decimal places. The accepted `face_key_table` is identical and is pinned separately by canonical digest `c20b727809eeb173ec11f584c2d60fc7afa3283e39a2dc3ccde0187703ce9ec9`.

## 3. Scope and restriction

The scope is every graph-5 certificate with:

- source critical mark pair [1,2];
- differing elementary-pair sets;
- both root-preserving source-to-support maps.

This gives **404 certificate/map rows from 202 distinct geometric witnesses**. The source-to-support maps fix labels 0 and 3 and may exchange labels 1 and 2.

For each row, the restriction deletes support 3:
[
X_{012}=K_0cup K_1cup K_2,qquad K_0subset X_{012}.
]

The verifier performs two factorizations independently:

1. Factor the original four-support collapse paths (X_{0123}searrow K_0cup K_3) into a common prefix and dependency-closed local suffixes.
2. Restrict the original paths to (X_{012}), factor the restricted paths (X_{012}searrow K_0), and compare the resulting prefix and suffix sequences with the restrictions of the original factorization components.

A pair is retained only if both cells lie in the restricted subcomplex. A pair with one cell inside and one outside is a crossing pair and would invalidate the induced restriction.

## 4. Main result

**All 404/404 rows pass exact restriction naturality.**

| Check | Rows |
|---|---:|
| Third-mark single-deletion certificate succeeds | 404/404 |
| No elementary pair crosses the restriction boundary | 404/404 |
| Both restricted paths replay to the root support | 404/404 |
| Restricted alternating difference remains one connected alternating cycle | 404/404 |
| Original four-support dependency-closed factorization is valid | 404/404 |
| Restricted dependency-closed factorization is valid | 404/404 |
| Restricted original prefixes equal independently factored restricted prefixes, sequence-for-sequence | 404/404 |
| Restricted original suffixes equal independently factored restricted suffixes, sequence-for-sequence | 404/404 |
| Both restricted suffixes replay to the root support | 404/404 |

In particular, the restriction preserves the actual dependency-closed block and its order, not just its pair set. The original common prefix restricts to the restricted common prefix, and each original local suffix restricts to the corresponding restricted local suffix exactly.

## 5. Alternating-cycle and dependency-block census

The 404 rows split into two cycle types:

| Original and restricted alternating-cycle signature | Rows |
|---|---:|
| 1 face, 2 edges, 1 vertex; 4 cells total | 64 |
| 2 faces, 6 edges, 4 vertices; 12 cells total | 340 |

The 340 larger cycles produce two dependency-closed block sizes:

| Cycle type | Dependency-closed suffix pairs | Common extra pairs | Rows |
|---|---:|---:|---:|
| 12-cell | 8 | 2 | 236 |
| 12-cell | 11 | 5 | 104 |

All 340 larger-cycle rows are order-sensitive in the common extra pairs. The two observed order templates occur in both orientations:

| Dependency block | Left extra-pair word | Right extra-pair word | Rows per orientation |
|---:|---|---|---:|
| 8 pairs | `FE, EV` | `EV, FE` | 118 |
| 11 pairs | `FE, FE, EV, EV, EV` | `FE, EV, EV, EV, FE` | 52 |

The 64 minimal four-cell rows retain their earlier census: dependency blocks of 4, 6, 7, and 10 pairs in 16, 8, 24, and 16 rows respectively. Their common-extra order agrees in 56 rows and differs in the eight hinged two-square cases.

## 6. Restricted intermediate inventories and prefix normalization

The restricted intermediate inventory counts are:

| Cycle type | Faces | Edges | Vertices | Rows |
|---|---:|---:|---:|---:|
| 4-cell | 4 | 14 | 11 | 16 |
| 4-cell | 5 | 16 | 12 | 8 |
| 4-cell | 5 | 17 | 13 | 24 |
| 4-cell | 6 | 20 | 15 | 16 |
| 12-cell | 6 | 18 | 13 | 236 |
| 12-cell | 7 | 21 | 15 | 104 |

Every restricted pair of common prefixes normalizes by valid adjacent collapse commutations. The swap counts are:

| Cycle type | Valid swaps | Rows |
|---|---:|---:|
| 4-cell | 0 | 40 |
| 4-cell | 16 | 8 |
| 4-cell | 24 | 16 |
| 12-cell | 0 | 140 |
| 12-cell | 6 | 28 |
| 12-cell | 9 | 64 |
| 12-cell | 18 | 108 |

## 7. Interpretation and limits

This is a stronger finite result than the earlier 64-row minimal-cycle audit. It establishes that, for the complete graph-5 [1,2] family, deleting the third source mark 3 commutes exactly with the dependency-closed collapse factorization. The result includes the 340 twelve-cell alternating cycles and their two order-sensitive dependency templates.

It does **not** establish:

- restriction naturality for graph-12 source families or other source-mark configurations;
- a uniform all-orders description of the 8-pair and 11-pair templates;
- decomposition of arbitrary larger alternating cycles into a finite list of local switches;
- arbitrary connected-support L7b or geometric L8;
- the all-orders PF-I16 Hall inequality.

The result closes one complete finite graph-5 restriction family. It is not an all-orders confluence theorem.

## 8. Reproduction

Verifier:

`research/scripts/verify_pf_i16_graph5_404_third_mark_restriction_naturality.py`

The verifier replays both original and restricted collapse paths, independently computes both dependency-closed factorizations, compares the restricted prefix and suffix sequences exactly, and emits a row-level JSON certificate for all 404 cases.
