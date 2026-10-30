# Repository check-in instructions

Branch: audit/2026-10-28-independent-reconstruction
Repository: syncgravity/singular-boundary

GitHub connector denied write authorization during this conversation. These files are staged locally only. Do not claim that the repository is updated.

- Copy `PROOF_REPORT.md` into `research/theorems/R3_IR_CONNECTED_WILSON_MIXED_FSUM_SKEIN_AND_CENTER_EVEN_NOGO_2026-10-29.md`.
- Copy `verify_skein_spectral.py` into `scripts/audit/verify_connected_wilson_mixed_fsum.py`.
- Copy `ADDITIONAL_SEMIGROUP_AUDIT.md` into `research/theorems/R3_IR_CONNECTED_WILSON_MIXED_FSUM_SHORT_TIME_ADDENDUM_2026-10-29.md`.
- Copy `verify_semigroup_short_time.py` into `scripts/audit/verify_mixed_semigroup_short_time.py`.
- Append the five data rows in `CLAIM_LEDGER_ADDITIONS.csv` to `research/claims/CLAIM_LEDGER.csv`, confirming no duplicate identifiers first.
- Run both scripts with Python plus numpy, scipy, sympy.
- Review file differences and commit to the audit branch (not main).

The patch does not include an automated git write, because the connected GitHub authorization was declined.
