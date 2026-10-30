# The Singular Boundary — nonlinear Wilson-angle source audit

## Evidence and status
- **MA-1 and MA-2**: analytic theorems for the actual finite interacting SU(2) ground state, under the declared regional comparison, magnetic lower bound, and complete-collar geometry. Improves vacuum-only shrinking-support threshold from gamma > 2/3 to gamma > 1/2. Does **not** improve operator-norm bounds for all low-energy states.
- **SD-1**: exact strictly positive gauge-invariant *trial-state* obstruction on fixed positive physical support. It is not a ground state and not a Yang–Mills counterexample.
- **CG-1**: exact fixed-support connected-kernel formula; the required nonlinear vacuum cumulant estimate remains OPEN.

Files: `PROOF_REPORT.md` and `verify.py`.

Run: `python verify.py` (SciPy and NumPy installed).

Verifier: deterministic SU(2) Haar quadrature and analytic product-measure factorization; no Monte Carlo, no temporal Stage26 reconstruction, no original file modifications.
