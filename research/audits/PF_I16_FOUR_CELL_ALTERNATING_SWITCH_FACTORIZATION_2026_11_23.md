# PF-I16 four-cell alternating-switch factorization audit

Date: 2026-11-23 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **finite four-cell switch factorization verified in all 64 certificate/map rows; the eight-row order-sensitive local template and restriction naturality remain open. Geometric L8 remains open.**

## 1. Objective

The preceding common-suffix test showed that the two complementary-arc edges could be factored into a common continuation. The stronger question is whether the *alternating-cycle pairings themselves* can be isolated as a local switch, leaving the same collapse prefix on both sides.

For each path, this verifier starts with that path's two elementary pairs in the symmetric difference of the alternating four-cycle. It closes the block under failed adjacent-swap tests, absorbing the exact interfering pair whenever a block operation cannot be commuted past it. Every accepted swap is checked by replaying both two-step orders from the same current cell inventory and requiring identical residual inventories.

## 2. Inputs and integrity

The verifier uses the same immutable artifacts as the 21 November rhombus-corner audits:

| Input | Artifact ID | Decoded payload SHA-256 |
|---|---:|---|
| Relative-collapse diamonds | `14680929981` | `d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141` |
| Independent four-support diagrams | `14681735833` | `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba` |
| Ngrid=12 accepted-face inventory | `14677507607` | `5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f` |

Scope is exactly 64 graph-5 minimal four-cell certificate/map rows: 32 geometric witnesses under both root-preserving graph maps, with source mark pair [1,2]. No support search or 5,012-case census is rerun.

## 3. Main result: a common prefix and a local switch suffix

**All 64/64 rows factor as follows:**

1. Each collapse path is reordered by certified adjacent commutations so that its two alternating-cycle pairs and all dependency-absorbed pairs form a terminal suffix.
2. The two prefixes have exactly the same elementary-pair set and reach exactly the same intermediate cell inventory.
3. The two prefixes can themselves be normalized to the same ordered sequence by valid adjacent swaps: 40 rows need no swaps, 8 need 16 swaps, and 16 need 24 swaps.
4. The two suffixes are valid collapse sequences from that common intermediate complex to the same grandparent.
5. The suffix pair sets differ **only** by the original two-versus-two alternating-cycle pairing. The additional dependency pairs form the same set on both sides in all 64 rows.

This is a stronger finite factorization than merely showing that both paths reach the same grandparent: it isolates the alternating-cycle comparison after a common prefix, up to exact elementary-collapse commutations.

## 4. Dependency-block census

| Suffix size (elementary pairs) | Common extra pairs | Rows |
|---:|---:|---:|
| 4 | 2 | 16 |
| 6 | 4 | 8 |
| 7 | 5 | 24 |
| 10 | 8 | 16 |
| **Total** | | **64** |

The common extra pair set is identical in the two paths in every row.

For 56 rows, the common extra pairs also occur in the same order. The remaining **8 rows** have a distinct order-sensitive six-pair switch template: the common extra sequence is `FE, EV, EV, EV` on one side and `EV, FE, EV, EV` on the other. Each orientation occurs four times. This is not a failed verifier or a counterexample; it identifies a genuinely larger local switch that cannot be reduced to the four-cell pairing change with the common operations held in the same order.

The intermediate inventory census is:

| Faces | Edges | Vertices | Rows |
|---:|---:|---:|---:|
| 7 | 24 | 18 | 16 |
| 8 | 26 | 19 | 8 |
| 8 | 27 | 20 | 24 |
| 9 | 30 | 22 | 16 |

## 5. What this establishes—and what it does not

**Established by the exact finite verifier:**
- common prefix pair sets in 64/64;
- common intermediate inventories in 64/64;
- prefix normalization by valid adjacent collapse commutations in 64/64;
- valid local suffixes to the common grandparent in 64/64;
- suffix matching differences exactly equal to the original alternating four-cycle pairings;
- identical dependency-pair sets in the two suffixes in 64/64.

**Still open:**
- an explicit homotopy/natural transformation between the two local suffix collapse maps;
- restriction compatibility when one or more supports are deleted, including compatibility of the dependency-closed block itself;
- a general four-cell switch lemma independent of the Ngrid=12 finite inventory;
- the eight order-sensitive six-pair cases as a reusable local template;
- six-, eight-, and larger alternating cycles;
- arbitrary connected-support L7b, geometric L8, and the all-orders Hall inequality.

The finite factorization is the correct interface for the next proof step: study the two local suffix maps on their common intermediate complex, beginning with the 56 order-aligned cases, then resolve the eight six-pair order-sensitive cases, and test the resulting switch under every further support restriction.

## 6. Reproduction

```bash
python research/scripts/verify_pf_i16_four_cell_switch_factorization.py \
  --collapse pf_i16_four_support_relative_collapse_diamonds.json.gz \
  --diagrams pf_i16_four_interval_independent_diagram_lifting.json \
  --inventory pf_i16_four_interval_support_inventory.json \
  --output pf_i16_four_cell_alternating_switch_factorization.json
```

The verifier pins the three payload hashes above and checks the complete 64-row factorization, both local collapse replays, the common prefix inventory, the prefix adjacent-swap normalization, and the exact suffix-pair symmetric difference.

Local decoded-output SHA-256: `a0b39fec71be366fe844fc3fab1b782c42cbcdeff3877bb767f2380fcc321128`.

**Research verdict:** the four-cell alternating-cycle discrepancy is now isolated to a local suffix after a common, commutation-normalized prefix in every tested certificate. This is finite geometric progress, not a global naturality theorem or geometric L8 closure.
