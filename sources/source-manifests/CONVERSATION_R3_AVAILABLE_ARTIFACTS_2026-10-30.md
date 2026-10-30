# Current R3 conversation source intake — 2026-10-30

**Scope and limitation.** This is an inventory of mounted original bytes and historical mentions, not a full verbatim source export. The current ChatGPT run recovered **46** top-level mounted files: **29** binary originals (80,085,244 bytes) and **17** other originals. Per-file size, hash, proposed Git destination and LFS classification are in the separately delivered checksum-verified local ZIP `singular_boundary_conversation_archival_2026-10-30.zip`, at `manifests/MOUNTED_ORIGINAL_BYTES_2026-10-30.csv`. **None of the data copied into that ZIP is claimed remotely uploaded.** Some binaries and text files overlap the existing 20-item [intake register](ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv); match SHA-256 before importing and avoid overwriting previously preserved bytes.

## Source-bearing R3 archives newly checkable locally

| Filename | Size (bytes) | SHA-256 | Interpretation |
| --- | ---: | --- | --- |
| `R3_uploaded_gaussian_audit_2026_10_27_bundle.zip` | 27913 | `a6396c61c060b356edf378e5eb2b81fa2aceb6e2e3a16270048951c7203e109e` | Includes original Q14 selection script `cavity_audit.py`, original `verify_bianchi.py`, `construct_surgery.py` and Gaussian analyses |
| `R3_word_incidence_2026_10_28_bundle.zip` | 83284 | `ecf9667c5de8bc9b0664aaa77a556b47afff08939a77cc86e376c180e8da37aa` | Initial illustrative support **not** original Q14; records a failed provenance reconstruction |
| `R3_staple_minima_block_2026_10_27_bundle.zip` | 44891 | `97bee4defdd102279b482db3638cdcd1bcf2a291854554fa60e9035cc2e8b793` | Derived 192-link correlated block, `block_certificate.json`, `block_audit.py`, formal note; independent proof audit pending |
| `R3_full_measure_cumulant_2026_10_26.zip` | 4297 | `a899fd063615cdb9b7bccdcf7084bf7b504d47087eaf4537e8096554dcd7de15` | Distinct **R3-IR** full-measure finite-regulator cumulant source; must not be merged into Q14 track |

The reported subsequent `R3_recovered_original_2026_10_27_bundle.zip`, `R3_historical_wordlevel_2026_10_27_bundle.zip`, `R3_Q14_full_cover_2026_10_27_bundle.zip` and `R3_joint_thermal_mgf_2026_10_27_bundle.zip` were mentioned in the visible conversation but are **not mounted as standalone original files in this session**. Do not invent their SHA-256 or equate their outputs with the four checkable originals.

## Other source families in the local package

The actual 46-file inventory contains the dissertation TAR.GZ, eight Stage26 ZIPs, eight sweep-10000 multihit NPZs, a full Penrose Stage26 archive, Stage23/24 comparison items, Stage32/33, Phase III geometry, 2+1D Wilson numerical/control materials, and methodological notes. Exact file names and byte hashes must be taken from the local CSV, not inferred from this human summary. Original Stage26 and dissertation items already appear in the 20-item register; their remote-byte readback remains OPEN until fresh-clone verification.

## Claim/reconciliation pointers

The historical order, corrections, failure modes, and evidence status appear in [R3 conversation chronology](../../docs/evidence/R3_PRISM_CONVERSATION_ARCHIVAL_RECONCILIATION_2026-10-30.md). Existing [R3-PRISM problem state](../../research/problems/R3-PRISM.md) and [claim ledger](../../research/claims/CLAIM_LEDGER.csv) retain the source-supported claims; no new claim IDs are allocated simply for repeated historical assertions. In particular a completed stationary all-integrated Q14 comparison and an unproved arbitrary nonstationary 12-prism/fixed-boundary comparison are different propositions.

## Integrity gate

To mark any binary original archived, first copy **the exact original bytes** to the proposed LFS destination in a fresh clone of the live main branch. Confirm LFS tracking, commit and push non-destructively, then retrieve from a **separate fresh clone**, run `git lfs pull`, `git lfs fsck`, and compare per-file byte size/SHA-256 with the source CSV. A local ZIP, Git LFS pointer or GitHub text manifest alone does **not** satisfy the gate.
