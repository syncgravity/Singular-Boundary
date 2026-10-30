# The Singular Boundary — Joint spin-network gate (2026-10-29)

This package provides a rigorous SU(2) two-face relative-color electric block, its nonzero full-time cross response, a nonperturbative multi-face Wilson variational upper energy, a gap-free electric cutoff tail and a **conditional, fully certified** finite-volume Ritz/cap protocol.

**It does not contain the computed full-coupling eight-face continuous SU(2) spectrum and does not prove generic Penrose cap survival or the continuum mass gap.** All deterministic verification scripts are self-contained and use NumPy/SciPy. The preceding tree-gauge and class-leakage scripts are included solely for cross-checks.

- `PROOF_REPORT.md`: SN-1 to SN-5, exact scope and proofs.
- `CERTIFICATION_PROTOCOL.md`: executable next stage for genuine eight-face physical spin-network computation.
- `verify_spin_network_two_face.py`: exact SU(2) Haar Gram and electric block.
- `verify_multiface_trial_and_tail.py`: SU(2) nonperturbative multi-face trial and spectral cutoff.
- `verify_ritz_certification.py`: finite-dimensional a posteriori theorem regression.
- `verify_su2_class_leakage.py`, `verify_exact_tree_gauge_q8.py`: unchanged preceding checks, for comparison; Q8 is not a continuum SU(2) approximation.
- `VERIFY_LOG.txt` and `SHA256SUMS.txt`: executed outputs and manifest.

Run `python verify_spin_network_two_face.py` and the other Python scripts. The pending repository patch (R3-IR-373–405) remains **uncommitted** unless a GitHub write is later authorized.
