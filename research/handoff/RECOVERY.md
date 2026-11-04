# Singular Boundary — Durable Research Handoff and Recovery Contract

Updated 2026-10-30 (research checkpoints through R3-IR-537; an additional local R3-IR-539 handoff note is bundled, not independently verified as a committed claim).

## Problem diagnosis

GitHub on branch `audit/2026-10-28-independent-reconstruction` is persistent, but a ChatGPT execution container's `/mnt/data` is not a persistent GitHub working tree. It can retain uploaded attachments during a session yet be empty or different in a later conversation. Creating a GitHub report does NOT persist an NPZ, ZIP, source module, local test, or a Python environment. A reported checkout is not adequate unless the files are committed and retrievable. A new conversation must fetch verified bytes, never assume prior absolute paths work.

## Source of truth, with distinct layers

- **Tracked research claims:** `research/claims/CLAIM_LEDGER.csv`. Read it together with linked proofs; numerical checks do not establish analytic theorems.
- **Tracked source/scripts:** `research/scripts/` and `research/theorems/`. Many old scripts use absolute `/mnt/data` paths and are NOT portable without the original inputs.
- **Original user archives:** treat as immutable primary evidence, with checksum and original filename. Do not replace with a derived candidate.
- **Derived numerical artifacts:** store with a generation command, exact code version, source checksum, parameters, shape/dtype, and checksum. Do not infer equality from matching dimensions.
- **Conversation handoff files:** convenient snapshots, not an alternative authority to the claim ledger.

## Verified local handoff artifacts (checksum SHA256, bytes)

1. `singular_boundary_handoff_core_R3-IR-539.zip`: 261072 bytes; SHA256 `b3eafb36d8901a77491f326edd18a57ec48e1666b1677afb40f7b59bef87b632`. ZIP integrity check passed, 38 entries. Contains restored study source and current candidate matrix, scripts, manifest, README, but **not all original Stage26 observations**.
2. `singular_boundary_handoff_full.zip`: 137331691 bytes; SHA256 `2cbf21808b6a26dacbe81d72d06cfea65b5feae73294b2a0082f790b0d4a9100`. ZIP integrity check passed, 56 entries. Session archive with original uploads and working material. It must be copied into user-controlled persistent storage; merely linking a sandbox file does not ensure access from a new chat.
3. `m5_whitney_candidate_2026-10-30.npz`: 1836 bytes; SHA256 `55a0d1b731355b59d64ce5535d029913b72fe1bcea595e2375d1f90b98d47334`. This is **NOT** verified equivalent to the historical `global_whitney_11face.npz`.
4. Original large uploads, e.g. `Archive 4.zip`, `Sharpe_dissertation_v10.7.tar.gz`, 8 sweep NPZ files and Stage26 ZIPs, are enumerated with per-file hashes inside the core bundle's `FILE_MANIFEST.json`. They are NOT automatically hosted by GitHub.

## Recovery procedure for a branched/new conversation

1. Open this handoff page and the claims ledger on the exact GitHub branch, or a fixed commit. Note the last *verified* claim and commit.
2. Download or attach the **core handoff ZIP** (and full archive when original numerical datasets are needed) from durable Project or user-controlled storage, not an assumed prior `sandbox:` URL.
3. Unzip to a fresh workspace, verify `sha256sum` against this document, and check `FILE_MANIFEST.json` for the required source files.
4. Run the relevant checks in that workspace. Reconstruct missing artifacts only from a documented assembly recipe, and write a new separate filename rather than overwriting an earlier result.
5. Commit a new checkpoint note, portable script, and updated ledger as one auditable change set where possible. Record artifact hashes and link the persistent source; label assumptions, independent observations, and open proof gaps.
6. Every 5–10 checkpoints, make a new core bundle and copy to persistent user storage; store full experimental data in release assets/object storage or Git LFS, NOT as GitHub plain-text blobs.

## Current scientific stop sign

R3-IR-537 found an SPD quadrilateral Whitney candidate matrix but its eigenvalue extrema and edge 13 mass diagonal DO NOT match the earlier reported Whitney matrix. Until the historical assembly prescription and bytes are recovered, do not substitute candidate constants into R3-IR-528/529. Root-tree equivalence, actual physical refinement, uniform shrinking center-cap and the continuum Yang–Mills mass gap remain OPEN.

## Recommended repository layout

```
research/
  claims/CLAIM_LEDGER.csv
  handoff/RECOVERY.md
  theorems/
  scripts/
  datasets/
    README.md       # provenance + SHA256, small committed artifacts or external durable URIs
  environments/
    requirements.lock  # record pinned Python numerical environment when captured
```

Do not claim that this manifest means the local ZIPs were uploaded to GitHub. Their checksums are verified locally; their long-term storage outside this runtime remains a user action unless a connected storage provider is used.
