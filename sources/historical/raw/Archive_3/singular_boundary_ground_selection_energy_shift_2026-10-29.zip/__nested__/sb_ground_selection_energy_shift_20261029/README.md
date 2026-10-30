# Ground-state selection by a positive center-cap energy shift

This package contains a theorem for **the actual nonlinear finite SU(2) Wilson magnetic-deleted Hamiltonian** that transforms a positive center-cap *ground-energy difference* into a lower bound on the true ground-state cap probability. It needs two certified ground-energy enclosures and a bounded source-block coupling; it does **not** presume a physical excitation gap.

`PROOF_REPORT.md`: ES1–ES9, exact hypotheses and limitations. `verify_energy_shift_certificate.py`: deterministic continuous SU(2) even-character rotor check, exact positive source moments, sharp two-cap and compactly supported SU(2) convolution certificates. `INDICATOR_CAP_CERTIFICATES.csv` and `SOFT_CAP_CERTIFICATES.csv`: numerical examples. `VERIFY_LOG.txt`: actual script output. `SHA256SUMS.txt`: internal hashes.

Run `python verify_energy_shift_certificate.py` with NumPy and SciPy installed. It does **not** solve the interacting connected eight-face model. The only rigorous Haar-order cap values obtained here concern a free deleted SU(2) rotor; the actual connected Penrose energy-difference estimate remains **OPEN**.

No remote GitHub operation was attempted. The repository-oriented addendum is separately packaged, with unnumbered claim statuses to avoid collisions with existing audit-branch IDs.
