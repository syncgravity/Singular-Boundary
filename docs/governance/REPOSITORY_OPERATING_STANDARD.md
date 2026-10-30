# Repository operating standard

Canonical branch: `main`. Audit branch integrated by non-force fast-forward on 2026-10-30; preserve historical commits.

Use `docs/current/` for current proof status; `research/theorems/` for named results; `research/claims/CLAIM_LEDGER.csv` for claim state and evidence; `scripts/` for verification; `data/` and `sources/` for provenance. Preserve old paths until citations are mapped.

Every proof check-in must distinguish proved, conditional, numerical, countermodel, and open; include the assumptions, source theorem, test instructions, and ledger entry. Confirm the written commit by fetching it and checking `main` after each transaction. Local ChatGPT ZIPs are not GitHub commits. Large binaries require Git LFS or a checksummed immutable archive; hash manifests alone do not preserve bytes. No force-push to main.

Unresolved: reconcile all October 29–30 Library research bundles and historical raw data, hash by hash. Completed-cage interacting-current, covariance, mass-gap, and reconstruction gates remain open.
