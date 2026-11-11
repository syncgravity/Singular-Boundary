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


## Common-measure and smooth-core extension (2026-11-11)

[Common-measure and smooth-core audit](../audits/R3_IR_COMMON_MEASURE_SMOOTH_CORE_FINITE_STRIP_EXTENSION_2026-11-11.md) checks that the conditional one-link laws disintegrate the same Gibbs measure μ_g that symmetrizes L=Δ+2∇S_g·∇; the weighted gradient Bochner, trace/Poincaré, and ordered Hessian estimates can therefore be combined in one L²(μ_g) space. It records the weighted tensor integration-by-parts cancellation, the compact-manifold Friedrichs realization with C∞ core and D(L)=H², and the extension from smooth data to H² initial data (and positive-time smoothing from L²).

**Conditional consequence:** assuming the ordered evolution and local coefficient certificates in the 2026-11-11 full-Hessian audit, the one-output weighted energy satisfies
\[
G_w(t)^2+H_w(t)^2\le e^{-2\lambda_{\rm cand}t}
\big(G_w(0)^2+H_w(0)^2\big),\qquad
\lambda_{\rm cand}>0.0699034.
\]
A finite-strip H²-source derivative resolvent corollary is recorded separately; no strip-length-uniform scalar gap is inferred.

**Status:** common-measure and smooth-core compatibility are closed for the conditional finite-strip reference estimate. The coefficient chain remains conditional; no theorem/claim ID is promoted. The provisional three-sector calculation remains paused. No nonlinear fixed point, volume-uniform residual response, physical-coupling gap, 3D transfer, or continuum mass gap follows.


## Adversarial full-Hessian energy inequality audit (2026-11-11)

[Adversarial audit](../audits/R3_IR_ADVERSARIAL_FULL_HESSIAN_ENERGY_INEQUALITY_AUDIT_2026-11-11.md) independently rederives the ordered drift Hessian identity with the stated covector commutator convention; checks the SU(2) mixed/trace-free curvature damping; verifies that the conditional trace Poincaré estimate enters as a lower bound on a parallel component of the full tensor Dirichlet form (not as a closed trace-sector evolution); and recomputes the one-output Schur, symmetrized Codazzi, and \(2\times2\) energy constants.

**Audit result:** no missing factor of two, sign, or index-order term was found in the combined differential inequality under the explicit hypotheses. With \(C_H<0.0304266282264\), \(C_3<0.049941326676\), \(C_R<0.060153181039\), and \(C_G=C_3+C_R<0.110094507715\), the conservative quadratic form has \(\lambda_{\min}>0.0699034\).

**Residual dependencies:** the ordered plaquette connection-correction certificate, scalar fixed-point derivative bounds on the full plaquette range, straight-strip incidence assumptions, conditional one-link Poincaré input, weighted Bakry–Émery certificate, and metric/sign convention must remain explicit. This is a conditional finite-strip reference semigroup proposition only. The provisional three-sector calculation remains paused; no theorem/claim ID is promoted, and no nonlinear fixed point, volume-uniform residual response, physical-coupling gap, or continuum mass gap follows.


## Local geometry and strip-incidence source audit (2026-11-11)

[Local geometric certificates and straight-strip incidence audit](../audits/R3_IR_LOCAL_GEOMETRY_SOURCE_AND_INCIDENCE_AUDIT_2026-11-11.md) resolves the remaining local source dependencies for the conditional full-Hessian estimate on the specified finite open straight SU(2) strip. It reconstructs the ordered connection-correction formula for \(\nabla\operatorname{Hess}p_f\), establishes the \(3/4\) entrywise bound without slot symmetry, strengthens the scalar derivative tail by a positive majorant uniform for \(|g|\le10^{-3}\), and proves the all-\(N\) incidence counts \(24,288\) from \(E(f_m)=\{v_m,v_{m+1},t_m,b_m\}\). The one-output \(6/5\) transfer is then explicit.

The independent exact verifier and log are:
- [verifier](../audits/verify_R3_IR_local_geometry_source_audit_2026-11-11.py)
- [execution log](../audits/R3_IR_LOCAL_GEOMETRY_SOURCE_AUDIT_2026-11-11.log)

**Updated local constants:** \(C_3<0.049941305\), \(C_H<0.030426617\), \(C_R<0.060153182\), \(C_G<0.110094486\), and \(\lambda_{\min}(Q)>0.0699034\).

**Status:** ordered local geometry, scalar derivative enclosure, SU(2) metric/curvature normalization, and straight-strip incidence now pass source-level review for this model. The weighted Bochner and conditional trace-Poincaré inputs remain imported from their named certificates; the common-measure and smooth-core extension is recorded above. The result remains a conditional finite-strip reference semigroup proposition. No theorem/claim ID is promoted; no interacting or continuum claim follows.

## Consolidated conditional full-Hessian finite-strip proposition (2026-11-11)

[Conditional full-Hessian finite-strip semigroup proposition](../audits/R3_IR_CONDITIONAL_FULL_HESSIAN_FINITE_STRIP_PROPOSITION_2026-11-11.md) consolidates the finite open straight SU(2) strip assumptions, exact ordered Hessian evolution, common Gibbs measure, imported weighted Bochner and conditional trace–Poincaré hypotheses, local third-tensor and Hessian-dressing constants, curvature/Codazzi forcing, quadratic-form margin, and smooth-core/semigroup extension.

**Conditional conclusion:** for the isolated dressing regime \(|g|\le10^{-3}\), the one-output weighted derivative energy obeys
\[
G_w(t)^2+H_w(t)^2
\le e^{-2\lambda_*t}\bigl(G_w(0)^2+H_w(0)^2\bigr),
\qquad \lambda_*>0.0699034,
\]
for \(H^2\) initial data on each finite open straight strip, and by positive-time smoothing for \(L^2\) data away from time zero. The rate is independent of strip length under the stated uniform local hypotheses; norm-equivalence constants need not be.

**Status:** a consolidated conditional proposition, not a promoted theorem or claim. The weighted Bochner and conditional one-link trace–Poincaré estimates remain imported analytic hypotheses. No nonlinear interacting fixed point, pointwise interacting Hessian bound, volume-uniform residual response, physical-coupling gap, 3D transfer, continuum limit, or continuum mass gap follows. The provisional three-sector trace-to-K calculation remains paused; PR #106 stays draft and main remains unchanged.

## Sharpened weighted Bochner and conditional trace–Poincaré inputs (2026-11-11)

[Sharpened analytic-input audit](../audits/R3_IR_SHARP_WEIGHTED_BOCHNER_AND_TRACE_POINCARE_2026-11-11.md) reuses the global positive-majorant derivative enclosure from the local-geometry audit to replace the coarse score envelope \(49/576\) by \(B_*<0.000333528\), and \(q_* = \|s_g'\|_\infty+\|s_g''\|_\infty<0.000333722619\). It rederives, rather than imports, the two analytic inputs:
- weighted Bochner rate \(c_*>0.4983981314\);
- conditional one-link trace Poincaré \(c_{\rm tr,*}>0.7468631508\), with leakage \(\ell_*<1.108\times10^{-7}\).

The accompanying [arithmetic verifier](../audits/verify_R3_IR_sharp_weighted_analytic_inputs_2026-11-11.py) and [log](../audits/R3_IR_SHARP_WEIGHTED_ANALYTIC_INPUTS_2026-11-11.log) check the propagated constants. Keeping the already-audited local Hessian and third-tensor terms, the full-Hessian energy matrix has \(\lambda_{\min}>0.4955484\). The consolidated proposition has been updated accordingly.

## Bounded-incidence extension and three-sector decision (2026-11-11)

[Bounded-incidence extension audit](../audits/R3_IR_BOUNDED_INCIDENCE_ANALYTIC_EXTENSION_2026-11-11.md) derives degree-\(r\) versions of the weighted Bochner and conditional one-link inequalities for finite product-SU(2) four-link plaquette complexes. With the conservative degree-four incidence bounds (the maximum link-face incidence of an open 3D cubic plaquette complex), the full-Hessian energy matrix remains positive with \(\lambda_{\min}>0.4800\). The [verifier](../audits/verify_R3_IR_bounded_incidence_extension_2026-11-11.py) and [log](../audits/R3_IR_BOUNDED_INCIDENCE_EXTENSION_2026-11-11.log) reproduce both degree two and degree four.

**Scope boundary:** this is a conditional finite-dimensional product-link reference-measure extension. It is not a 3D transfer theorem or a result for a regulator until its action, link variables, plaquette supports, incidence, metric, and boundary identifications are checked against the model-class hypotheses.

**Research decision:** the provisional trace-to-\(K\) three-sector calculation is not appropriate as the next step for the current reference-semigroup objective. The sharpened trace coercivity and full-Hessian curvature decomposition already close the one-output energy with a large positive margin. Keep the three-sector record dormant as a cross-check; reopen only for a different norm, non-product geometry, loss of bounded incidence, or an interacting estimate not covered by this argument. No theorem/claim ID is promoted.


## 3D regulator transfer audit and degree-eight finite-complex extension (2026-11-11)

[Model-transfer audit](../audits/R3_IR_3D_REGULATOR_TRANSFER_AUDIT_2026-11-11.md) compares the current bounded-incidence reference estimate against the historical coupled-Z5 dissertation geometry, the extruded-prism candidate, the illustrative 3+2 projected cubical 2-skeleton, the Voronoi proposal, and the cubic reference.

For the finite illustrative projected-Z5 **2-skeleton**, the source geometry has four-link square faces and maximum link-face incidence r=8. A separate rational verifier gives the conditional product-link reference energy bound
\[
\lambda_{\min}(Q_8)>0.1972.
\]
The finite geometry has 1,700 square faces incident to more than two selected cubes (maximum six), so its selected 3-cells are not a manifold cellulation. It is not a source-authenticated regulator or a refinement family.

The transfer audit also records why the current product-metric theorem does not automatically apply to the dense-Whitney prism electric form or the polygonal-face Voronoi model. The historical dissertation's coupled-Z5 split is kept distinct from the later illustrative 3+2 split. No theorem/claim ID is promoted; P0 physical regulator certification remains open.
