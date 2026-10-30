# The Singular Boundary

**Canonical private research repository** for the Singular Boundary dissertation, quasicrystalline and Penrose constructions, finite-volume SU(2) gauge theory, Wilson Hamiltonians, spectral/infrared analysis, continuum mass-gap investigation, numerical results, counterexamples, and historical provenance.

> **Scientific status — 2026-10-30:** Substantial finite-volume results and conditional comparisons are recorded, but **a four-dimensional interacting continuum Yang–Mills mass-gap proof has not been established**. See the [canonical proof map](docs/current/CANONICAL_RESEARCH_STATE_2026-10-30.md). This repository is an evolving research record, not an announcement of a Millennium Prize solution.

## Start here

| Purpose | Canonical record |
| --- | --- |
| Latest proved/conditional/open claims | [Current research state](docs/current/CANONICAL_RESEARCH_STATE_2026-10-30.md) |
| Claim-by-claim status | [Research claim ledger](research/claims/CLAIM_LEDGER.csv) |
| Exact known original files awaiting intake | [20-item archival intake register](sources/source-manifests/ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv) |
| All known historical source families still missing | [Historical archive backlog](sources/source-manifests/HISTORICAL_ARCHIVE_BACKLOG_2026-10-30.md) |
| Locally upload immutable originals | [Git LFS intake and clean-clone verification](docs/governance/LOCAL_GIT_LFS_INTAKE_RUNBOOK.md) |
| Missing sources and provenance gaps | [Reconciliation gap tracker](docs/evidence/SOURCE_RECONCILIATION_GAPS_2026-10-30.csv) |
| Verbatim conversation/attachment reconstruction | [Sequential conversation provenance protocol](docs/governance/SEQUENTIAL_CONVERSATION_PROVENANCE_PROTOCOL.md) |
| Repository governance | [Operating standard](docs/governance/REPOSITORY_OPERATING_STANDARD.md) |

## Research tracks (maintain distinct)

- [R3-PRISM](research/problems/R3-PRISM.md) — twelve-prism Wilson insertion; original source words and boundary specification remain missing.
- [R3-IR](research/problems/R3-IR.md) — physical gauge-neutral Hamiltonian, magnetic deletion, completed-cage estimates, spectral source-inserted response, and connected infrared covariance.
- [R2](research/problems/R2.md) — time normalization, spatial continuum, quantum reconstruction, and mass-gap obligations.
- [D1](research/problems/D1.md) — production-action/source certification and Stage 7–26 computational provenance.

The finite-graph SU(2) covariant Laplacian is not the interacting continuum mass-gap proof. An incomplete-cage Haar property does **not** establish the same property for a completed magnetic cage. Existing completed-cage positivity has nonuniform constants; the required interacting uniform radial-current/correlation/reconstruction gates remain open. Keep operator conventions, dimensions, regularization choices and physical-vs-reference models explicit.

## Repository organization

- `research/theorems/` — theorem statements with exact assumptions, scope, proofs and limitations.
- `research/claims/` — claim IDs, status, source/proof pointers and supersession history.
- `research/problems/` — separate open proof tracks.
- `scripts/` — reproducible simulations, validators and research verification tools.
- `docs/current/` — current state (older documents may be dated snapshots).
- `docs/evidence/` — source audits, verification reports and unresolved gaps.
- `docs/governance/` — archival, review and provenance rules.
- `sources/source-manifests/` — original-source hashes, recovery registers, intake statuses.
- `sources/conversations/` — future verbatim ordered conversation exports with source IDs and attachments (do not reconstruct missing verbatim text).
- `data/raw/` — original binary archives via Git LFS once uploaded and independently read back.

## Archive the complete historical record

Preserve original messages, attached files, original datasets, checks, failed experiments, retractions, counterexamples, conditional results, code, logs, and analytical notes. Do not silently replace historical assertions with newer versions. Record chronological supersession explicitly.

**Two layers must remain separate:** (1) immutable original evidence and (2) curated mathematical claims. Every new theorem/claim must identify hypotheses, mathematical status (proved / conditional / numerical / countermodel / open), exact source(s), code/data reproducibility, and counterclaims or corrections.

See [the original-byte intake register](sources/source-manifests/ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv) for **20 specifically identified originals** and [the broader backlog](sources/source-manifests/HISTORICAL_ARCHIVE_BACKLOG_2026-10-30.md) for the original 602-file prepared import, 188 `NOTES.zip` members, Stage 19–35 ZIP chain, recent theorem proof packages, transcript exports, and other assets. Categories may overlap and must be deduplicated by SHA-256 during import.

A CSV manifest or Git LFS pointer alone does not prove the original bytes are remotely preserved. An original is archived only when an authenticated upload **and fresh-clone byte readback** match original size and SHA-256. Do not claim all history is checked in until individual coverage is verified.

The [local Git LFS runbook](docs/governance/LOCAL_GIT_LFS_INTAKE_RUNBOOK.md) contains commands. `.gitattributes` already declares LFS handling for `data/raw/**`, `*.zip`, `*.npz`, and `*.tar.gz`.

## Scientific and history integrity

- Do not force-push, rewrite canonical `main`, delete original observations or rerun historical Monte Carlo merely to replace an unavailable original.
- The independent 602-file prepared tree is **not** already merged into GitHub; preserve the GitHub ancestry when importing original bytes.
- Read theorem hypotheses and the claim ledger before quoting a headline result. Keep the original R3-PRISM and R3-IR programs logically distinct unless an explicit argument connects them.
- Check both true interacting Wilson ground states and reference/Gaussian countermodels for correct labels.
- See [historical status snapshot](docs/current/STATUS.md) for Oct 28 context, not the current conclusion.
- A successful data archival check-in improves reproducibility; it does not close the current continuum mass-gap proof.

## How to contribute recovered material

As each historical chat becomes available, preserve a verbatim source export and attachment manifest, register its provenance, reconcile its claims and tests with the claim ledger, and link any newly resolved proof obligations. As each binary original is recovered, perform the SHA-256, Git LFS upload, fresh-clone retrieval, and status update. Commit incrementally to make changes reviewable and preserve history.

## Paper 3 / Wilson-transfer / R3-IR / R2 conversation provenance (26–30 Oct 2026)

The [dated retrospective chronology](sources/conversations/2026-10-26_TO_2026-10-30_PAPER3_WILSON_R3R2_RETROSPECTIVE_CHRONOLOGY.md) and [claim crosswalk](research/theorems/R3_R2_CONVERSATION_CLAIM_CROSSWALK_2026-10-30.md) preserve the evolving program, original failed approaches, Stage26 findings and later D1 correction. [Source byte intake](sources/source-manifests/THIS_CONVERSATION_RECOVERED_ORIGINALS_2026-10-30.md) describes 90 locally verified original files awaiting actual remote Git/LFS upload. **This is not a native full-conversation transcript and not a completed remote archive.** The interacting neutral infrared and quantum continuum gap gates remain open.
