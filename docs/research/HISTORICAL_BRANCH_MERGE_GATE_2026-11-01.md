# Historical-branch reconciliation gate — 2026-11-01

**Status: evidence collection; no theorem or historical branch wholesale merged.**

## Source refs inspected

- Canonical `main`: ledger blob `29fec994bd0f9c65ba0c0be91cea374f51763985`
- Historical `audit/2026-10-28-independent-reconstruction`: ledger blob `e8ebdd08af49cc7bf4bb0230a402b9fec895515e`
- An actual GitHub branch comparison shows the historical branch is hundreds of commits ahead and behind main; comparison API presents at most 300 file entries. This is **not a complete file-by-file audit** and must not be described as one.
- The documentation navigation branch was merged earlier as PR #3. Its files now exist on main.
- The reproducibility branch contains a verifier and workflow document; PR #2 remains draft pending testing.

## Automated ledger audit (raw line comparison)

There are `613` distinct claim IDs on the audit branch and `415` on main. The inspection finds:

| Class | Count |
| --- | ---: |
| `MAIN_ONLY` | 15 |
| `CONFLICTING_CONTENT` | 15 |
| `DUPLICATE_ID` | 3 |
| `AUDIT_ONLY` | 213 |

There are `9` extra rows reusing an existing ID on the historical branch and `3` on main.

**Critical collision:** `R3-IR-373` means the interacting radial fiber energy decomposition on the historical branch but an incomplete-cage conditional Haar result on main. Similar differences appear for `R3-IR-374` through `R3-IR-390`. Thus claim IDs were reused for **different mathematical propositions**: do not simply append, merge by ID, or treat a conflict as a later revision. Allocate immutable disambiguated historical aliases with a crosswalk only after reading each source theorem and its commit history.

Historical duplicate identifiers include `R3-IR-530`, `R3-IR-538`, `R3-IR-539`, and `R3-IR-561`–`565`; main repeats `R3-IR-378`–`380`. All repeated entries carry different row text.

## Decision

Preserve both ledgers as-is on their historical refs. Do not overwrite the canonical ledger, assert common IDs express common theorems, or propagate conflicting rows automatically. The companion [machine-readable collision inventory](CLAIM_LEDGER_BRANCH_COLLISIONS_2026-11-01.csv) identifies every nonidentical, branch-only and repeated ID for line-level follow-up.

## Required next checks before selective ports

1. Retrieve **full** changed-path and commit inventories via paginated Git trees or local Git, because GitHub compare truncates the large divergence.
2. For conflicting claim IDs, inspect theorem body, source commit, relevant correction and whether the exact result already exists in the main theorem index. Assign disambiguated IDs without rewriting historical rows.
3. Audit branch-only scripts against executable dependencies and raw input availability; rerun tests on an isolated checkout; report failures rather than upgrading evidence status.
4. Verify original-asset manifests and binary SHA-256 with actual remote byte readback; distinguish Library from Git.
5. Resolve or supersede PR #2 only after malformed ZIP and directory traversal tests, bundle-specific manifest checks and CI.
6. Submit a separate narrowly scoped PR for each verified theorem/code/data import; use append-only provenance crosswalks rather than force-pushing or altering old records.

**Scientific status unchanged:** P0–P5 unresolved gates remain open as documented in the current checkpoint.
