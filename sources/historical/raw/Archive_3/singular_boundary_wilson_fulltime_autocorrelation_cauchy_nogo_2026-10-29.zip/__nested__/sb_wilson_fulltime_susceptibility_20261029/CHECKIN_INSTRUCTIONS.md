# Repository check-in instructions

Repo: `syncgravity/singular-boundary`, branch: `audit/2026-10-28-independent-reconstruction`.

The last GitHub write attempt in the current conversation was denied authorization. No further write was attempted without renewed authorization; **these are local staged artifacts only**.

When authorized:

1. Add `PROOF_REPORT.md` as `research/theorems/R3_IR_WILSON_FULLTIME_AUTOCORRELATION_AND_CAUCHY_NOGO_2026-10-29.md`.
2. Add `verify_fulltime_susceptibility.py` as `scripts/audit/verify_wilson_fulltime_susceptibility.py`.
3. Add any uncommitted prior mixed-skein/short-time package work (claim IDs 373–377) from `singular_boundary_mixed_fsum_checkin_and_short_time_2026-10-29.zip` first, if still absent.
4. Check that claim IDs 378–382 are not already present; append `CLAIM_LEDGER_ADDITIONS.csv` to `research/claims/CLAIM_LEDGER.csv` with CSV schema validation.
5. Run the script with Python, NumPy and SciPy. Verify SHA256 manifest and all statuses on the audit branch; do not merge automatically.
