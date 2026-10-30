R3 crossing transport / adaptive Haar geodesic surgery (2026-10-27)

Run in this extracted directory:
  OPENBLAS_NUM_THREADS=1 python gaussian_joint_audit.py
  python validate_jacobian.py
  python multiscale_collar.py
  python adaptive_surgery.py
  # exploratory non-Gaussian Wilson Gibbs Monte Carlo (slow):
  python wilson_geodesic_probe.py --radii 5 --lambdas 8 16 32 --burn 100 --stride 10 --samples 10

Includes source Penrose geometry, 14-face cavity construction, certified optimized 24-mode basis,
59-pivot exact Tietze presentation, scripts, and quantitative certificates.

The compact SU2 adaptive map is rigorously action nonincreasing and has a controlled Jacobian
and at most four inverse branches, but NO absolute Gibbs tail in the local minimum is proved.
The Gaussian projected-curvature concentration theorem is ONLY for the linearized quadratic gauge model.
