R3: direct compact-SU2 fixed-volume weak-coupling 24-mode theorem and a deterministic adaptive-coercivity no-go.

Key artifacts:
  FORMAL_NOTE.md -- complete precise statements and proof, including order of limits
  theorem_certificate.json -- checked constants, quantitative scopes
  exact_rational_no_go.json -- exact nonzero rational compatibility witness
  nonlinear_no_go_probe.json -- SU2 quaternion optimization checks, not the proof
  flat_adjoint_rank_certificate.json -- 16 nontrivial SU2 flat-background rank checks
  bianchi_certificate.json -- independent 14-face nonabelian Bianchi factor accounting

Reproduce from this directory:
  OPENBLAS_NUM_THREADS=1 python no_go_gaussian.py
  OPENBLAS_NUM_THREADS=1 python certify_rational.py
  OPENBLAS_NUM_THREADS=1 python nonlinear_pivot_counterexample.py
  OPENBLAS_NUM_THREADS=1 python flat_rank_SU2.py
  python verify_bianchi.py
  python theorem_summary.py

Dependencies: numpy, scipy, sympy, numba. All Penrose generation and prior Tietze scripts bundled.
IMPORTANT: A volume-independent finite beta threshold, arbitrary-support R3 inequality, and continuum mass gap remain OPEN.
