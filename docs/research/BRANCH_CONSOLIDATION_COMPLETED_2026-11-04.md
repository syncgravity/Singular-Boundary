# Historical branch consolidation completion — November 4, 2026

**Result: all ten non-main branch heads are Git ancestors of canonical `main`.** Verified by live GitHub comparison after merging, every branch reports zero commits behind main. Branch names were retained as historical pointers; no new branch was created, no force update or deletion was performed.

## Actual merges

1. **Historical audit**, original head `eafaa6d2fb288d1bd92de2dfe7a63167100f4cd6`: true two-parent merge `ad6c83ae7fa0a760432c69977da139a072ba2695` includes 307 previously absent original paths, comprising 202 theorem files, 94 research scripts and 11 other historical records, at their unchanged original Git blob SHAs. The main README and main `research/claims/CLAIM_LEDGER.csv` were kept intact. The historical ledger's exact blob `e8ebdd08af49cc7bf4bb0230a402b9fec895515e` was already available at `research/evidence/ledger_snapshots/CLAIM_LEDGER_AUDIT_2026-11-01.csv`. The old README was also preserved at `sources/branch-merge/audit-2026-10-28/README.md` without replacing the current one.

2. **Handoff verifier**, original head `630ee91f13c0b857b5b5a496a45c623453f0361c`: true two-parent merge `0140d06dcf75fde545b0973847c1a8f0db338d9d`, with `main`'s current tree kept unchanged (no theorem, ledger, README or security verifier overwritten). Older differing file versions remain recoverable through the second parent's Git history.

3. **Eight other branches** were already ancestors of the merged main history; their ancestry was verified, not duplicated in unnecessary merge commits.

## Every branch verified

| Non-main branch head | Git commit | Commits behind merged main |
|---|---|---:|
| `audit/handoff-verifier-security-tests-2026-11-01` | `01d87b30441a63358864cd10ad96e6508858355e` | 0 |
| `audit/source-and-original-inputs-2026-11-01` | `0de099867b1f70a1c6a62595df69b13a8aed0897` | 0 |
| `audit/source-trace-381-392-2026-11-01` | `40d06c7144ef4e8efd66da85e0190ed1f1670117` | 0 |
| `audit/theorem-source-certification-batch01-2026-11-01` | `5e06b556c0ac3b9525437120cdec10592ad8ff36` | 0 |
| `audit/2026-10-28-independent-reconstruction` | `eafaa6d2fb288d1bd92de2dfe7a63167100f4cd6` | 0 |
| `docs/research-navigation-provenance-2026-11-01` | `add0f2f1d40d8370b5a82d83ddd898fb0214ba62` | 0 |
| `fix/reproducible-research-handoff-2026-10-30` | `630ee91f13c0b857b5b5a496a45c623453f0361c` | 0 |
| `reconcile/claim-identity-crosswalk-2026-11-01` | `b55943eb5bafe47d39415baba12df01506e6b716` | 0 |
| `reconcile/historical-branches-2026-11-01` | `5060286eb7def96f22e404ddb6e5b3364a100412` | 0 |
| `reconcile/immutable-ledger-snapshots-2026-11-01` | `dd7505dd05172a0dbda925b8944768a0524fc41a` | 0 |

## Guardrails for duplicate IDs and original material

- **No theorem body was overwritten.** The main tree now has **740 distinct theorem Markdown files**; the existing 335-record categorized historical theorem index was *augmented* in `docs/research/THEOREM_INDEX.md` with 405 additional direct links. Its historical sections remain intact.
- **No claim row was overwritten, deduplicated or silently adjudicated.** The two historical ledgers remain distinct in the preserved source history and the existing audit/main ledger snapshots. Claim IDs already known to collide, including `R3-IR-373` through `R3-IR-390`, still require proposition-level reconciliation. Mechanical crosswalk aliases are present at `docs/research/HISTORICAL_FLAG_IDENTITY_CROSSWALK_2026-11-01.csv` and `docs/research/HISTORICAL_SOURCE_ENTRY_ALIASES_2026-11-01.csv`. Historical certification remains blocked, **but branch integration no longer is**.
- A merge-parent relationship preserves branch commits, not proof validity and not missing external large ZIP/NPZ original bytes. Companion archival and scientific certification gates remain separately open.
- Do not remove historical branch refs until a separately authorized cleanup and integrity review; retention is intentional, not evidence that work remains unmerged.

## Verification commands/logic

Queried GitHub branches; for each non-main tip X, fetched the GitHub comparison `X...main`; `behind_by=0` for all ten. Read back the merged main tree (2464 blobs immediately after the historical merge, before subsequent index updates), including 740 theorem files. Checked the README and claim ledger exact conflict blob IDs. No full scientific regression suite was executed as part of Git history consolidation.

**Decision:** Canonical development and new changes should target `main` without branching for archive migration. Source/proposition certification is a separate next step and must not be mistaken for unfinished Git consolidation.
