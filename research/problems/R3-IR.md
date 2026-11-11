# R3-IR — Hamiltonian neutral-sector spectral estimates

**Status:** Substantial finite-volume results exist; the full interacting volume/cutoff-uniform neutral-sector estimate remains **open** in reviewed sources.

Primary starting points: `sources/historical-notes/R3_THEOREM_OBSTRUCTION_AND_MULTISCALE_GATE.md`, `FORMAL_THEOREMS.md`, `FORMAL_CHARACTER_BLOCKING_AND_R2_AUDIT.md`, `FORMAL_R3_R2_PROOF_AUDIT.md`, and local Wilson frame audits. Consult their exact hypotheses before extending them. No automatic equivalence with R3-PRISM.


## Conditional weighted trace–gradient Bochner block (2026-11-10)

[Theorem record](../theorems/R3_IR_CONDITIONAL_WEIGHTED_TRACE_GRADIENT_BOCHNER_BLOCK_2026-11-10.md) records the conditional one-link weighted Poincaré estimate, the exact product-manifold trace commutator, and the resulting weighted trace-energy inequality. The diagonal coercive skeleton has \(c=11/120\), \(c_{\rm tr}=\frac34e^{-49\pi/144}\approx0.2575101\), and leakage \(\ell=4c_{\rm tr}(49/576)^2/3\approx0.00248474\). It does not close the full trace evolution: the remainder contains \(A_2\), \(A_{3,w}\), and \(T_wK_w\), with \(K_w\) the trace-free/mixed Hessian sector.

**Next obligations:** evaluate the local plaquette row bound \(A_2\); bound the ordered weighted third-derivative contraction \(A_{3,w}\); derive the trace-free/mixed Hessian evolution; and verify the full coupled \(3\times3\) quadratic form. This remains a finite open-strip result and is not PF-I16, a 3D transfer theorem, or a continuum gap result.


## H2-weighted trace-to-K calculation and audit (2026-11-10)

[Provisional calculation and audit](../theorems/R3_IR_H2_WEIGHTED_TRACE_TO_K_COUPLING_AUDIT_2026-11-10.md) records the one-output-weight convention, the candidate trace-to-K Hessian block coefficient \(C_{TK}^{\rm cand}<0.007845234\), and the previously derived third-dressing forcing coefficient \(0.049941328\). The additional ordered-curvature estimate \(0.000288844\), its proposed combined forcing coefficient \(0.050230172\), and the Schur diagnostic are explicitly **provisional**, pending exact curvature-contraction and ordered-index incidence audits. They are not promoted to certified constants.

**Next obligations:** independently verify the trace-to-K Schur row/column counts; derive the ordered SU(2) curvature contraction with its exact symmetrization and trace-free projection; bound the K-to-K Hessian-of-dressing and curvature terms; then test the complete coupled energy form. The displayed three-sector diagnostic is not a full Hessian contraction theorem.


## Full one-output Hessian energy bypass — candidate audit (2026-11-10)

[Transcript reconciliation and full-Hessian energy audit](../audits/R3_IR_FULL_HESSIAN_ENERGY_BYPASS_AUDIT_2026-11-10.md) identifies a possible alternative to the provisional trace-to-K Schur route. It combines the existing weighted gradient rate, conditional trace Poincare estimate, product-curvature damping of the mixed/trace-free Hessian, a local block-Schur bound for \(A=\nabla^2S_g\), and the archived ordered third-dressing tensor estimate. Under the stated operator identities and a still-to-be-verified Codazzi curvature contraction, the candidate (2\times2) energy form has (a\approx0.08918193), (b\approx0.22708350), (C_G\le0.16615103), and positive diagnostic eigenvalue \(\lambda\approx0.05017091\).

**Status:** candidate only. The full covariant Hessian evolution, weighted Schur sums, ordered tensor weight transfer, and SU(2) curvature contraction must be independently checked in the exact frame and common weighted norm. If verified, this would bypass the separate trace-to-K block calculation for the reference semigroup; it would not prove nonlinear fixed-point closure, pointwise interacting Hessian control, the physical spin-network all-orders recurrence, or any continuum gap. Keep PR #106 in draft review and do not promote a theorem or claim ID.
