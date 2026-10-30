# R3-IR — Cycle susceptibility and magnetic submodularity audit

The mathematical proof is `PROOF_REPORT.md`; the deterministic reproducibility checker is `verify_cycle_susceptibility.py`. It tests exact two-level physical positivity, center-flux parity and opposite sign of the mixed susceptibility, a rebuilt 3-face/10-edge Z5 Penrose spatial incidence fixture, exact Gaussian mixed derivative via integral quadrature and numerical finite differences, and the full mixed-cycle magnetic deletion comparison.

The true SU(2) nonlinear theorem established here is a Cauchy/positive-resolvent reduction to the nonnegative diagonal cycle-response budget. The favorable all-coupling submodularity theorem is **Gaussian tangent only**. The positive two-level counterexample is not an SU(2) lattice gauge Hamiltonian. No physical mass gap or uniform nonlinear bulk deletion theorem is claimed.

Run `python verify_cycle_susceptibility.py` with Python, NumPy, SciPy, and SymPy. No Monte Carlo. Historical Stage7/26 and Q14 source archives are unchanged.
