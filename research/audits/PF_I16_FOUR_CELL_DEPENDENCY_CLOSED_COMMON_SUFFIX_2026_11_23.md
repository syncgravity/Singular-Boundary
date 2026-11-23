# PF-I16 four-cell dependency-closed common-suffix audit

Date: 2026-11-23 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **finite certificate-level common-continuation factorization verified in all 64 minimal four-cell cases; prefix collapse-map comparison, restriction naturality, and geometric L8 remain open.**

## 1. Objective

The 21 November rhombus-corner audit established that the two complementary-arc (`P`) edge operations occur in the same order in both collapse paths. A naive attempt to move just those two operations to a common suffix succeeded in 16/64 cases. In the other 48 cases, the first failed adjacent swap involved the same exact interfering pair in both paths.

The present audit asks whether the obstruction disappears when the interfering operation is absorbed into a larger local block, and the block is then moved to the suffix by further certified adjacent swaps.

No new support enumeration or 5,012-diamond census is performed. The verifier consumes the same three immutable artifacts as the preceding rhombus-corner audits.

## 2. Inputs and integrity

| Input | Artifact ID | SHA-256 of decoded payload |
|---|---:|---|
| Relative-collapse diamonds | `14680929981` | `d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141` |
| Independent four-support diagrams | `14681735833` | `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba` |
| Ngrid=12 accepted-face inventory | `14677507607` | `5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f` |

The verifier reconstructs the accepted-face cell inventories and replays every elementary free face-edge and edge-vertex pair. It accepts an adjacent swap only when both orders are valid from the same intermediate inventory and yield exactly the same residual inventory.

## 3. Dependency-closure procedure

For each of the 64 graph-5 minimal four-cell certificate/map rows (32 geometric witnesses, each under both root-preserving maps):

1. Start with the two common (P)-edge collapse operations.
2. In the 48 rows with a first noncommuting neighbor, include that exact neighbor in the initial block. The first blocker is identical in both paths in every such row.
3. Move block operations to the right by stable adjacent swaps. A swap is accepted only after replaying both two-step orders and checking equality of the resulting cell inventories.
4. Whenever a block operation meets an outside operation that does not pass this exact swap test, absorb that outside operation into the block and continue.
5. Stop only when the block is a contiguous terminal suffix in each path.

The procedure is deterministic. It proves existence of the reported finite common suffixes under this specific dependency-closure rule; it does not assert that the resulting block is minimal or unique.

## 4. Results

**64/64 rows** produce the same ordered suffix in both collapse paths, and both prefixes terminate at the same intermediate cell inventory.

| Dependency-closed block size (elementary pairs) | Common suffix word | Rows |
|---:|---|---:|
| 2 | EV, EV | 16 |
| 4 | FE, EV, EV, EV | 8 |
| 5 | FE, EV, EV, EV, EV | 24 |
| 8 | FE, FE, EV, EV, EV, EV, EV, EV | 16 |
| **Total** | | **64** |

Here FE denotes a free face-edge pair and EV a free edge-vertex pair.

The first-blocker types in the 48 enlarged cases are:
- EV against EV: 8;
- FE against EV: 24;
- FE against FE: 16.

The two prefixes reach the same intermediate inventory in every row. Its cell-count census is:

| Faces | Edges | Vertices | Rows |
|---:|---:|---:|---:|
| 6 | 22 | 17 | 16 |
| 7 | 24 | 18 | 8 |
| 7 | 25 | 19 | 24 |
| 8 | 28 | 21 | 16 |

All swaps in the verifier are exact elementary-collapse commutations, not formal permutations. The two resulting suffix sequences agree pair-by-pair, including the paired cell identities.

## 5. Crucial limitation

The original four differing elementary pairs that form the alternating cycle remain in the two prefixes in **all 64 rows**. The prefix pair sets are still different, even though their terminal cell inventories agree.

Therefore this result factors off a common continuation but does **not** solve the alternating-cycle switch itself. It does not prove:
- homotopy or natural equivalence of the two prefix collapse maps;
- a vertex-level oriented boundary-cycle comparison map;
- compatibility under every further support restriction or third deletion;
- arbitrary connected-support L7b;
- geometric L8 or the all-orders Hall inequality.

This is not a Hall counterexample and not a proof of Hall. It is a finite reduction of the collapse-map comparison problem to the two prefixes ending at the same intermediate complex.

## 6. Reproduction

```bash
python research/scripts/verify_pf_i16_four_cell_dependency_closed_common_suffix.py \
  --collapse pf_i16_four_support_relative_collapse_diamonds.json.gz \
  --diagrams pf_i16_four_interval_independent_diagram_lifting.json \
  --inventory pf_i16_four_interval_support_inventory.json \
  --output pf_i16_four_cell_dependency_closed_common_suffix.json
```

The verifier pins all three input payload hashes above and asserts the 64-row census, exact swap validity, identical ordered suffixes, equal intermediate inventories, and persistence of the alternating-cycle pairings in the prefixes.

Local decoded-output SHA-256: `bfffb702a0d4cd679c27796fbe7c97524cb25a326c813d77e82aeaf043e8773a`.

**Research verdict:** a common dependency-closed continuation block exists in every tested minimal four-cell case. The unresolved alternating-cycle comparison has been pushed into the prefixes; no geometric L8 or all-orders Hall theorem is claimed.
