# PF-I16 branch preservation and provenance ledger

**Source branch:** `audit/pf-i16-local-interacting-vacuum-2026-11-08`  
**Integration destination:** `main`  
**Review date:** 2026-11-11

## Outcome

The source branch was compared against `main` before integration. The comparison reported 48 candidate paths on a divergent branch (53 commits ahead / 140 behind at the time of comparison). The branch was **not merged wholesale** because its history diverges substantially from the current mainline and includes historical claims superseded by later corrections.

Instead, all 48 candidate source paths were reconciled by exact file content:

- 46 files were copied to their original paths on `main`.
- Two theorem dossiers were already present on `main` with the same source blob identity.
- The older degree-four / (16^{k-1}) connected-support note was retained but explicitly qualified as finite-crop-only; the universal source bound is the later (d_e\le8), (D\le28), (784^{k-1}) correction.
- The original source branch remains intact as provenance. No branch was deleted and no unrelated history was merged.

This is a **content-preservation integration**, not a claim that every PF-I16 theorem is a final continuum result. Each file retains its own mathematical assumptions and status.

## Path and source-blob register

The SHA-1 column is the original Git blob SHA fetched from the source branch before copying. Status records whether the path was copied, already existed in main, or was copied with an explicit supersession qualification.

| Path | Source-branch blob SHA-1 | Main disposition |
|---|---|---|
| `research/geometry/PF_I16_AUTHENTICATED_THREE_FACE_MOTIF_AND_SHARP_INCIDENCE_2026_11_09.md` | `d231712ea437729379d4e1b2705dbd8a4f7eecac` | copied |
| `research/geometry/PF_I16_CENTER_SIGN_DUALITY_AND_FOURTH_ORDER_ENERGY_2026_11_09.md` | `e226b26d597d29c9eb26c06e10fd3f8e2d63a2e3` | copied |
| `research/geometry/PF_I16_CONDITIONAL_SCORE_INFORMATION_AND_MIXING_GATE_2026_11_08.md` | `ef7c91bc9cab65c6b1ba291ed82d89d3d7ac8872` | copied |
| `research/geometry/PF_I16_CONNECTED_CYCLE_LOCALITY_AND_CLUSTER_COUNT_2026_11_09.md` | `5a7c533c187c4cb31f3fd319bcccbe97dfbe381f` | copied |
| `research/geometry/PF_I16_D4_NONITERABILITY_ON_THREE_FACE_SOURCE_GRAPH_2026_11_09.md` | `9d31ecf6dbab69aafb7ccc927fd56a98a8f9b129` | copied |
| `research/geometry/PF_I16_EXACT_AUTHENTICATED_THREE_FACE_SIXTH_ORDER_ENERGY_2026_11_09.md` | `097cb3a02740a404a14a67b162917bf17e7c2886` | copied |
| `research/geometry/PF_I16_EXACT_EIGHTH_ORDER_TOPOLOGY_SPLITTING_2026_11_09.md` | `4d1a0c72dff172e0c539d3e99d011f1295a45cda` | copied |
| `research/geometry/PF_I16_EXACT_FOUR_VALENT_THREE_FACE_C222_AND_SIXTH_ORDER_COMPARISON_2026_11_09.md` | `4de533c46f3022bf5b772fb0f6c6a845ee3fc7e7` | copied |
| `research/geometry/PF_I16_EXACT_SEVEN_CLASS_FOUR_FACE_C2222_2026_11_09.md` | `aad1c5bdfb96608bd0dacdafb36facda23316262` | copied |
| `research/geometry/PF_I16_EXACT_SIXTH_ORDER_TWO_FACE_QUANTUM_LINKAGE_2026_11_09.md` | `48ae910d1a678c6cde6633e144a897f8ee047653` | copied |
| `research/geometry/PF_I16_EXACT_TWO_RHOMBUS_SHARED_EDGE_FUSION_2026_11_09.md` | `d2e2a8eed9990a93db83cb8886fe13396efc604b` | copied |
| `research/geometry/PF_I16_FOREST_HAAR_AND_CYCLE_CUT_INFORMATION_2026_11_09.md` | `fd061ecb932a7b8e81d33bce43c62e891c5fad99` | copied |
| `research/geometry/PF_I16_FOUR_FACE_C2222_REDUCED_50_SECTOR_CONTRACTION_2026_11_09.md` | `fa53185c475e40452fea2bf1f20f0a69022dd084` | copied |
| `research/geometry/PF_I16_FOUR_FACE_CONNECTED_SUPPORT_CENSUS_2026_11_09.md` | `9e08c4e2997938f77de10b6e12f913a6493af38a` | copied |
| `research/geometry/PF_I16_FOUR_FACE_EXACT_ISOMORPHISM_AND_CAUCHY_GATE_2026_11_09.md` | `dbafb6d63d8413772aee568843f0b9964acaacb3` | copied |
| `research/geometry/PF_I16_FOUR_FACE_SCHATTEN_THRESHOLD_AND_MOBIUS_C2222_GATE_2026_11_09.md` | `882d52321e0e5f644f1474b8596aaec6e0cc9d58` | copied |
| `research/geometry/PF_I16_GROUND_STATE_SPECTRAL_BRIDGE_2026_11_08.md` | `5cf99fe88ffda6bbc15f5003ad0b77ff6d0a0006` | copied |
| `research/geometry/PF_I16_HIGH_SPIN_RESOLVENT_AND_H1_OBSTRUCTION_2026_11_09.md` | `90fdd10f09e11dc7e8c7eae8ca0c9f9f48200067` | copied |
| `research/geometry/PF_I16_INFRARED_SPECTRAL_GATE_2026_11_08.md` | `a471ea0356d7400c753b6d23176390555375a3b5` | copied |
| `research/geometry/PF_I16_INTERACTING_SOURCE_RHOMBUS_SPECTRAL_SUM_RULE_2026_11_08.md` | `b957a78ea236e83af162fc78afe0474d07f692bb` | copied |
| `research/geometry/PF_I16_LOCAL_INTERACTING_VACUUM_AUDIT_2026_11_08.md` | `28e8901fb3de8d573d3f8b8f75ef7b2b2726d827` | copied |
| `research/geometry/PF_I16_LOCAL_LINK_ADJACENCY_UNIVERSAL_EIGHTH_ORDER_2026_11_09.md` | `6715d81d4cbe64aa48a652b9da70300a5c1bc467` | copied |
| `research/geometry/PF_I16_ONE_LOOP_BILINEAR_RESOLVENT_AND_MULTI_LOOP_THRESHOLD_2026_11_09.md` | `e5632b7b736f1d774e1f5ef639a438bd16d4e0fb` | copied |
| `research/geometry/PF_I16_THIRD_ORDER_LOW_SPIN_AND_COMPLETE_SECOND_ORDER_SCORE_2026_11_09.md` | `4cdb75257c94182d1e24cb4cdb01bf6514272ce1` | copied |
| `research/geometry/PF_I16_THREE_FACE_SCHATTEN_THRESHOLD_2026_11_09.md` | `b2a8b305cf97c3b95a8d65982d4334ad52e890aa` | copied |
| `research/geometry/PF_I16_TWO_RHOMBUS_THETA_RESOLVENT_2026_11_09.md` | `d366dd4fa544747b12e2a7cef75b107cb631ce8a` | copied |
| `research/scripts/verify_pf_i16_authentic_source_three_face.py` | `3561bd470f5aacab1296397ce350f03961d41e5d` | copied |
| `research/scripts/verify_pf_i16_conditional_information.py` | `4cd842e8293e1b8a6358aba92f931f61ec9d70fd` | copied |
| `research/scripts/verify_pf_i16_connected_cycles.py` | `c2b6def39338058fd97a2e793c7aa3a53f8f1768` | copied |
| `research/scripts/verify_pf_i16_d4_noniterability.py` | `780a6d4f13a8c33a13ba7974df3eeb91578ddf94` | copied |
| `research/scripts/verify_pf_i16_forest_cycle_information.py` | `18bc2a0292f17e312dcc8dbd51891e91e89687d7` | copied |
| `research/scripts/verify_pf_i16_four_face_c2222_reduced.py` | `3a06277805dd2345c845b9e619277c26da603506` | copied |
| `research/scripts/verify_pf_i16_fourth_order_center_duality.py` | `0754ada17d31837af433a6a3700974ea3b3cc494` | copied |
| `research/scripts/verify_pf_i16_high_spin_resolvent.py` | `4bd1b87b55196cde76faa28b7d5e7c27d7069ab6` | copied |
| `research/scripts/verify_pf_i16_infrared_spectral_gate.py` | `cd2b56b219a1053de6b06326b8a324ad21b52d12` | copied |
| `research/scripts/verify_pf_i16_one_loop_bilinear.py` | `621e199ac06c17d526cd9c27bfb532243e4ada5e` | copied |
| `research/scripts/verify_pf_i16_sixth_order_two_face.py` | `bff47eda17a191032fabf0ec32f1f502887e2193` | copied |
| `research/scripts/verify_pf_i16_source_rhombus_spectral.py` | `73e35d56bae280167b5190153b6c0cc2307b39df` | copied |
| `research/scripts/verify_pf_i16_theta_resolvent.py` | `111999141091b8edc9ba2bae3f50d023077bbd98` | copied |
| `research/scripts/verify_pf_i16_third_order_low_spin.py` | `e2b98636437b351df5f9f86cf6d6e4960fa45a8d` | copied |
| `research/scripts/verify_pf_i16_three_face_schatten.py` | `f929e7467903da4f78c61b76cdacdd7e3f36d880` | copied |
| `research/scripts/verify_pf_i16_two_rhombus_fusion.py` | `7b7ac17c35c20ba9fcfde73e0027aab4bba0d9c3` | copied |
| `research/theorems/PF_I16_CONNECTED_SUPPORT_INCIDENCE_CORRECTION_2026_11_10.md` | `8285ff968642992cf3e5ce8a59c6ae90b60da435` | already-in-main |
| `research/theorems/PF_I16_LOCAL_DRESSING_SHARED_LINK_RESIDUAL_2026_11_10.md` | `63350c256de4103da4ec7c90c53b9f7a2ba9f38d` | already-in-main |
| `research/theorems/PF_I16_UNIFORM_CONNECTED_CYCLE_MIXING_GATE_2026_11_10.md` | `8ed70bb629157d5b39547e8984959a72806d7a6c` | copied; incidence constants qualified |
| `research/verification/verify_pf_i16_connected_support_bound.py` | `537cc10412d3cfa217ff14008996ca72bf764a4c` | copied |
| `research/verification/verify_pf_i16_dressing_residual_constants.py` | `43142a9ea00a2c5236ca2f3d0f3568df9729e6c2` | copied |
| `research/verification/verify_pf_i16_incidence_count.py` | `b9da6e42a29309c74cc2bf03ac49f66099206aa8` | copied |

## Mathematical boundary

The PF-I16 contribution preserved here includes exact finite-source face and motif coefficients, center-sign duality, topology-sensitive higher-order terms, Haar/forest and cycle-cut information, high-spin resolvent obstructions, incidence counting, local dressing, and verifier scripts.

The remaining proof bottleneck is not a lack of finite motif calculations. It is a volume-uniform quantum activity estimate controlling repeated shared-link fusion and the infinite SU(2) Peter–Weyl tower, followed by the source-derived physical kinetic/time normalization and a uniform interacting-vacuum Poincaré inequality. No all-orders cluster convergence or physical continuum mass gap is claimed.

## Reproduction

Run the imported scripts from a complete checkout, using the dependencies and private source inputs stated in each script. A script that skips because a private input is unavailable is not a pass for that source-dependent claim. The public finite checks and private-source replays must be reported separately.
