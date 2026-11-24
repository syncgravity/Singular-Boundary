# PF-I16 four-cell switch: finite restriction-naturality audit

Date: 2026-11-24 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **the four-cell switch factorization survives the third-mark support restriction in all 64 tested certificate/map rows. This is a finite path-level restriction result; map-level naturality, the general restriction theorem, and geometric L8 remain open.**

## 1. Objective

The 23 November factorization isolated the four-cell alternating-cycle discrepancy after a common, commutation-normalized prefix in all 64 graph-5 rows. The next question was whether that factorization is compatible with a further source-prescribed support restriction.

The graph-5 source audit establishes that interval 0 is the root and is never a reverse mark, while interval 3 is eligible in all 12 graph-5 source records. The two root-preserving maps both fix labels 0 and 3 and may exchange labels 1 and 2. Thus, after the critical deletion pair [1,2], the remaining source-prescribed restriction is deletion of mark 3, corresponding to geometric support 3.

This audit tests that restriction directly on the stored elementary collapse sequences. It does not infer naturality from equality of the final support union alone.

## 2. Inputs and integrity

The verifier consumes the same immutable workflow artifacts as the 23 November four-cell factorization:

| Input | Artifact ID (prior immutable artifact) | Decoded payload SHA-256 |
|---|---:|---|
| Relative-collapse diamonds | `14680929981` | `d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141` |
| Independent four-support diagrams | `14681735833` | `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba` |
| Ngrid=12 accepted-face inventory | `14677507607` | `5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f` |

The current workflow regenerated the inventory with decoded payload hash `3e50240bf1b037f3de8dd4e4c4ab94d4523533c25ceeab4000410c641cf07b77`. Inspection shows the only JSON-value differences from the prior inventory are the two floating-point minimum-margin fields, each differing at the final decimal places. The accepted `face_key_table` is unchanged; the verifier therefore pins its canonical digest `c20b727809eeb173ec11f584c2d60fc7afa3283e39a2dc3ccde0187703ce9ec9` rather than treating harmless floating-point serialization as a change of geometric target.

## 3. Restriction construction

For each of the 64 original certificate/map rows:

1. Retain the graph-5 critical source mark pair [1,2].
2. Use the source-to-support map to identify the third eligible mark 3; both root-preserving maps fix support label 3.
3. Form the restricted three-support complex
   [
   X_{012}=K_0cup K_1cup K_2
   ]
   and the root target
   [
   K_0.
   ]
4. Restrict each stored full four-support collapse path by retaining an elementary pair exactly when both of its cells belong to (X_{012}). A pair with one cell inside and one outside would cross the restriction boundary and invalidate this induced sequence.
5. Replay both restricted sequences as elementary collapses from (X_{012}) to (K_0).

The stored single-deletion certificate for support 3 succeeds in all 64 rows. No elementary collapse pair in either path crosses the restriction boundary in any row.

## 4. Main result

**All 64/64 restricted path pairs replay successfully from (X_{012}) to (K_0).**

The restriction also preserves the alternating-switch factorization:

- The symmetric difference still consists of exactly two elementary pairs on each side (four pairs total).
- Its typed cell-incidence graph is one connected alternating cycle in all 64 rows.
- Dependency closure produces the same additional-pair set on both sides in all 64 rows.
- The two prefixes have the same elementary-pair set and reach the same intermediate cell inventory in all 64 rows.
- The prefixes normalize to the same ordered sequence by valid adjacent collapse commutations in all 64 rows.
- Both dependency-closed local suffixes replay from the common intermediate complex to (K_0).

The restricted prefix normalization counts are unchanged:

| Valid adjacent swaps | Rows |
|---:|---:|
| 0 | 40 |
| 16 | 8 |
| 24 | 16 |

The dependency-closed suffix census is also unchanged:

| Suffix size | Common extra pairs | Rows |
|---:|---:|---:|
| 4 | 2 | 16 |
| 6 | 4 | 8 |
| 7 | 5 | 24 |
| 10 | 8 | 16 |

The common extra-pair order agrees in 56 rows. The remaining eight preserve the same order-sensitive template seen before restriction: `FE, EV, EV, EV` on one side and `EV, FE, EV, EV` on the other, four rows in each orientation. These eight remain genuine order-sensitive local cases; they are not collapsed into a commuting four-pair switch.

The restricted intermediate inventory census is:

| Faces | Edges | Vertices | Rows |
|---:|---:|---:|---:|
| 4 | 14 | 11 | 16 |
| 5 | 16 | 12 | 8 |
| 5 | 17 | 13 | 24 |
| 6 | 20 | 15 | 16 |

## 5. What this establishes—and what it does not

**Established by the finite verifier:**

- the source-prescribed third-mark deletion is valid in all 64 rows;
- both original collapse paths restrict to the three-support complex without a crossing pair;
- both restricted paths replay to the root support;
- the four-pair alternating-cycle discrepancy survives the restriction;
- the common-prefix / dependency-closed-suffix factorization survives the restriction;
- the eight order-sensitive cases remain explicitly visible after restriction.

**Still open:**

- a map-level homotopy or natural transformation between the two local suffix collapse maps;
- compatibility for every other support restriction and every source critical pair, beyond this graph-5 [1,2] then 3 restriction;
- a general four-cell switch lemma independent of the Ngrid=12 inventory;
- a reusable resolution of the eight order-sensitive six-pair templates;
- six-, eight-, and larger alternating cycles;
- arbitrary connected-support L7b and geometric L8;
- the all-orders PF-I16 Hall inequality.

The result is stronger than a check of support-intersection tables: it is an explicit restriction test on the elementary collapse sequences themselves. It is still finite path-level evidence, not a proof of map-level naturality or all-orders confluence.

## 6. Reproduction

The verifier is:

`research/scripts/verify_pf_i16_four_cell_switch_restriction_naturality.py`

It uses the existing three artifact inputs and checks the complete 64-row restriction, every crossing-pair condition, both restricted replays, the alternating-cycle structure, dependency closure, common intermediate inventory, valid prefix commutations, and the separate 56/8 order census.

**Research verdict:** the four-cell local switch factorization is stable under the third source-mark restriction for the complete tested graph-5 family. This closes one finite restriction square, not the general restriction-naturality obligation and not geometric L8.
