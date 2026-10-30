# Exact continuous-SU(2) eight-face Ritz benchmark

This package contains a full analytic proof report, two deterministic executable Python regressions, their actual output, and an archive hash manifest.

Execute:

```bash
python verify_eight_face_joint_ritz.py
python verify_local_spin_resolution.py
```

Dependencies: Python 3.11+, NumPy and SciPy.

`verify_eight_face_joint_ritz.py` constructs an exact **35×35 compression** of the true Gauss-invariant continuous SU(2) eight-face Wilson Hamiltonian: 29 normalized fundamental face trace products and six normalized shared-edge relative-color states. It calculates Ritz energies for genuinely asymmetric electric/magnetic coefficients and verifies a **rigorous variational energy-scale obstruction**. The numerical eigensolver is ordinary double precision, **not interval arithmetic**; the proved energy-scale obstruction does not rely on its eigenvalues.

`verify_local_spin_resolution.py` verifies the SU(2) character Jacobi spectrum and necessary `n_max=Omega(b^(1/4))` scaling for product-class cutoffs. This cutoff theorem is **not** asserted for arbitrary joint spin networks.

This is **not** a certified eight-face full-coupling ground state, not the complete electric-cutoff matrix, not an accurate eight-face cap marginal, not a Penrose numerical simulation, and not a mass-gap proof. The target cap expectation is exactly Haar **within this insufficient basis**, which is a basis artifact.
