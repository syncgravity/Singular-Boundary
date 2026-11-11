# R3-IR — Hamiltonian neutral-sector spectral estimates

**Status:** Substantial finite-volume results exist; the full interacting volume/cutoff-uniform neutral-sector estimate remains **open** in reviewed sources.

Primary starting points: `sources/historical-notes/R3_THEOREM_OBSTRUCTION_AND_MULTISCALE_GATE.md`, `FORMAL_THEOREMS.md`, `FORMAL_CHARACTER_BLOCKING_AND_R2_AUDIT.md`, `FORMAL_R3_R2_PROOF_AUDIT.md`, and local Wilson frame audits. Consult their exact hypotheses before extending them. No automatic equivalence with R3-PRISM.


## Conditional weighted trace–gradient Bochner block (2026-11-10)

[Theorem record](../theorems/R3_IR_CONDITIONAL_WEIGHTED_TRACE_GRADIENT_BOCHNER_BLOCK_2026-11-10.md) records the conditional one-link weighted Poincaré estimate, the exact product-manifold trace commutator, and the resulting weighted trace-energy inequality. The diagonal coercive skeleton has \(c=11/120\), \(c_{\rm tr}=\frac34e^{-49\pi/144}\approx0.2575101\), and leakage \(\ell=4c_{\rm tr}(49/576)^2/3\approx0.00248474\). It does not close the full trace evolution: the remainder contains \(A_2\), \(A_{3,w}\), and \(T_wK_w\), with \(K_w\) the trace-free/mixed Hessian sector.

**Next obligations:** evaluate the local plaquette row bound \(A_2\); bound the ordered weighted third-derivative contraction \(A_{3,w}\); derive the trace-free/mixed Hessian evolution; and verify the full coupled \(3\times3\) quadratic form. This remains a finite open-strip result and is not PF-I16, a 3D transfer theorem, or a continuum gap result.
