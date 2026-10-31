# R3-IR-539 — Historical M5 Whitney matrix mismatch cannot be fixed by scalar normalization

Audited the existing `singular_boundary_handoff_core.zip` (35 ZIP entries, archive integrity check passed), recovered the exact candidate `m5_whitney_candidate_2026-10-30.npz` and its M5 geometry source. Historical matrix `global_whitney_11face.npz` is NOT in either core bundle nor mounted separately; earlier historical numeric summaries are cited only as prior reported diagnostics, not independently reverified inputs.

For the verified candidate SPD matrix, comparison with reported historical values yields three incompatible required global scalar factors:

- minimum eigenvalue: historical/candidate = **0.729902965970**
- maximum eigenvalue: historical/candidate = **0.485027987334**
- edge-13 diagonal: historical/candidate = **1.119638182080**.

Thus no uniform multiplicative normalization can reconcile the candidate with all three historic diagnostics. This does **NOT** prove which construction is correct; changes in Whitney element definition, local coordinate metric, cell weights, assembly/boundary convention, or more complex geometric transforms remain possible. Candidate SHA-256: `55a0d1b731355b59d64ce5535d029913b72fe1bcea595e2375d1f90b98d47334`; full handoff SHA-256: `2cbf21808b6a26dacbe81d72d06cfea65b5feae73294b2a0082f790b0d4a9100`. These hashes identify the exact bytes of the stored files checked in this run.

The portable validation is `research/scripts/audit_whitney_normalization.py`: run it from a directory containing the candidate NPZ, or place the NPZ alongside the script. This is an **audit of incompatibility of three reported diagnostics**, not a reproduction of the unavailable historical mass matrix.

Next: locate actual historical 30×30 NPZ/assembly source; investigate geometry conventions without modifying the candidate; once reconciled, run actual Penrose two-tree gauge-invariant principal-form comparison and physical multilevel refinement. Shrinking center-cap bound and continuum Yang–Mills mass gap remain OPEN.
