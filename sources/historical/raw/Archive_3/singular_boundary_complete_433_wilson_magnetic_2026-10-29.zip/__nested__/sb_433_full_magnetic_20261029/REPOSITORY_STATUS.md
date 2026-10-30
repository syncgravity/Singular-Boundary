# Repository check-in status

**Not committed.** This local result extends the pending R3-IR-373–427 patch with claims R3-IR-428–434. The repository's previous GitHub write authorization was declined, and no write was attempted in this turn.

Recommended future authorized destinations:
- `research/theorems/R3_IR_COMPLETE_433_WILSON_MAGNETIC_AND_TARGET_SPINONE_2026-10-29.md` — `PROOF_REPORT.md`
- `research/notes/R3_IR_433_MATRIX_REPRODUCIBILITY_2026-10-29.md` — `README.md`
- `scripts/audit/build_433_exact.py`, `scripts/audit/target_spin1_433.py`, `scripts/audit/verify_saved_433_matrices.py`, `scripts/audit/certify_spin1_minpoly.py` — corresponding scripts
- `research/data/433_fundamental_shell_2026-10-29/` — saved `.npz` matrices and Ritz data, if repository storage policy allows
- `research/claims/CLAIM_LEDGER.csv` — append only missing R3-IR-428–434 rows, without replacing existing entries.

Before applying this local patch, retrieve the live branch, check paths and existing ledger IDs, and do not overwrite conflicting work. All numerical results describe **projected Galerkin vectors**; no full eight-face ground-state cap certificate or continuum gap is claimed.
