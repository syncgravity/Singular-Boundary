# Simultaneous seven-plaquette link-spin proof gate — 2026-10-29

This package is a standalone continuation of the 433-state eight-face SU(2) Wilson audit.

- `PROOF_REPORT.md`: exact nested higher-spin shell + simultaneous high outer-link no-go theorem.
- `verify_joint_outer_gate.py`: reproducibly assembles and diagonalizes the full 433-state magnetic matrices augmented by seven exact single-plaquette character towers through spins 1,2,4,8; computes rigorous finite-dimensional tensor class Ritz upper bounds; checks the geometry and explicit SU(2) concentration constants.
- `basis.npz`, `magnetic_0.npz`, ... `magnetic_7.npz`: verified exact SU(2) Haar-contraction data from `singular_boundary_complete_433_wilson_magnetic_2026-10-29.zip`.
- `RESULTS.csv`: numerical Ritz spectra, tower weights, and known-channel residual floors.
- `VERIFY_LOG.txt`: passing execution log.
- `SHA256SUMS.txt`: package file digest manifest.

Dependencies: Python 3, NumPy, SciPy. Run `python verify_joint_outer_gate.py` from the package directory. The process uses exact analytic matrix elements, with double-precision Ritz eigenvalues; it does not diagonalize the full untruncated SU(2) Hamiltonian.

**No GitHub write was attempted:** repository check-in remains subject to the user's authorization status. The proposed next claim sequence is R3-IR-435–440.
