# PF-I16 rhombus-corner common-continuation audit

Date: 2026-11-21 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **new finite certificate-level continuation pattern verified in all 64 minimal four-cell cases; global homotopy naturality and geometric L8 remain open.**

## 1. Why this audit exists

The 20 November rhombus-corner correction established that the actual smallest alternating cycle is not the two-edge disk model. In each of the 64 graph-5 four-cell certificates, the two differing edges share one vertex but have distinct residual endpoints. The prior audit correctly left open whether the complementary arc (P) is retained in the common grandparent and whether a common continuation can be factored through it.

This audit answers the finite incidence question using the existing artifacts. It does **not** rerun the 5,012-diamond census.

## 2. Inputs and integrity

The verifier consumes three immutable artifacts from workflow [44833369833](https://github.com/syncgravity/Singular-Boundary/actions/runs/44833369833):

| Input | Artifact | ZIP SHA-256 |
|---|---:|---|
| Relative-collapse diamonds | 14680929981 | `a717a6ef2e1006225f31ef64b5a22033e2305b8bfe8fec53e3e3c2a885f6adbf` |
| Independent four-support diagrams | 14681735833 | `5761aef67b7ede6d8580eefff60a422307d2d69eefd3a18382c56b36e3372903` |
| Ngrid=12 accepted-face inventory | 14677507607 | `82a493237a7d20e74d17e1d4b563e0fde3143d33989b6515d426fb24237afc94` |

The corresponding decompressed/raw JSON SHA-256 values are recorded in the verifier output. Each ZIP contains exactly one expected JSON member (the collapse member is gzip-compressed inside the ZIP).

The verifier pins the payload hashes so the same check runs both on the downloaded ZIPs and directly on the generated CI files:
- Collapse JSON: `d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141`
- Independent diagrams JSON: `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba`
- Support inventory JSON: `5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f`

## 3. Finite construction

For each graph-5 certificate whose source critical mark pair is ([1,2]), and whose symmetric difference is the minimal typed cycle with one face (F), two edges (e_1,e_2), and one vertex (v), define (P) to be the two other boundary edges of the rhombus (F).

The common grandparent support is reconstructed from the two retained geometric supports, using the original accepted-face inventory. Its full face, edge and vertex sets are computed from the (mathbb Z^5) face keys, not inferred from the collapse booleans.

For each of the two ordered collapse paths, the verifier extracts, in order, every elementary pair that removes one of the two edges of (P). It retains the pair type and the paired cell (face or vertex), so this is stronger than checking only that the same two edges eventually disappear.

## 4. Result

**64 / 64 verified**

All 64 certificate/map rows (32 distinct geometric witnesses, each represented under both root-preserving graph maps) have the following exact pattern:

1. (P) has two edges.
2. (P) has **no edge** in common with the grandparent subcomplex (A).
3. (Pcap A) consists of exactly **one vertex**.
4. Both complete collapse paths remove the two (P)-edges exactly once.
5. The ordered restriction of each path to the (P)-edge removals is **identical**, including the elementary pair type and the other cell in each pair.

The common ordered pair-type census is:

| Pair types in the (P)-edge restriction | Cases |
|---|---:|
| edge–vertex, then edge–vertex | 16 |
| face–edge, then edge–vertex | 48 |
| **Total** | **64** |

Thus the 20 November hypothesis “(P) is retained as a two-edge subcomplex of (A)” is not what the actual certificates realize. Instead, the arc is reduced to its unique grandparent intersection vertex by the same ordered pair data in both paths. In 48 cases, the first (P)-edge is paired with an additional face, so the continuation is not a collapse of (P) in isolation; that adjacent face is part of the local continuation data.

## 5. What this does and does not establish

**Established for these 64 finite certificates:** exact reconstruction of (A); (Pcap A) is one vertex and no edges; and the two collapse paths have the same ordered elementary-pair restriction on the two (P)-edges.

**Not established:**

- that these two pair operations form a contiguous common suffix of each full collapse path;
- that all intervening elementary collapses can be commuted past this local continuation while preserving freeness;
- that the resulting local comparison homotopy extends over the full support union and is fixed on (A);
- compatibility with every further source/support restriction or third deletion;
- vertex-level source-prescribed oriented boundary-cycle comparison maps;
- the six-, eight- and twelve-cell alternating-cycle cases;
- arbitrary connected-support L7b, geometric L8, or the all-orders Hall inequality.

The exact next task is now narrower than the previous “check whether (P) is retained” question: build the dependency/interference graph of the two common (P)-edge pair operations against all other elementary pairs in each path. Determine whether each path can be reordered, by certified disjoint-pair commutations (or a stronger local move), so that the identical two-pair continuation is a genuine common suffix. Then test the same construction under every further support restriction.

## 6. Reproducibility

Run:

```bash
python research/scripts/verify_pf_i16_rhombus_corner_continuation.py \
  --collapse pf_i16_collapse_diamonds.zip \
  --diagrams pf_i16_independent_diagrams.zip \
  --inventory pf_i16_support_inventory.zip \
  --output pf_i16_rhombus_corner_continuation.json
```

The verifier pins all three ZIP SHA-256 values and checks the 64-case census, exact (P)-to-(A) intersection, full ordered pair identities, and distinct-witness count. Its output schema is `PF-I16-RHOMBUS-CORNER-COMMON-CONTINUATION-v1`.

**No theorem gate is promoted. Geometric L8 remains OPEN.**
