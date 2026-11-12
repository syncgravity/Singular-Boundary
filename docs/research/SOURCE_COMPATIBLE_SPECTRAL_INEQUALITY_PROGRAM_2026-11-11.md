# Source-compatible interacting spectral inequality: canonical proof program

**Status:** central theorem OPEN. This document specifies architecture and evidence classes; it does not prove the inequality.

**Canonical geometry:** source-native coupled-\(\mathbb Z^5\) / intrinsic \(2+2\) construction.  
**Preservation:** no historical branch, theorem record, archive, or claim identity is deleted, merged, silently rewritten, or promoted by this architecture change.

## 1. The one theorem

Let \(h\) index source-compatible refinements and \(R\) physical finite volumes. Let \(\mathcal H_{h,R}^{\rm phys}\) be the Gauss-invariant Hilbert space of the source-derived SU(2) regulator, \(H_{h,R}\) its physically normalized Hamiltonian, and \(\Omega_{h,R}\) its actual normalized interacting ground state. Set

\[
d\nu_{h,R}=|\Omega_{h,R}|^2dU,\qquad
\mathcal E_{h,R}(f,f)=\sum_e\alpha_{e,h,R}
\int|\nabla_e f|^2d\nu_{h,R}.
\]

Here \(dU,\nabla_e,\alpha_{e,h,R}\) must be fixed by the same authenticated link variables, metric, Hamiltonian and physical time normalization. Prove

\[
\boxed{\operatorname{Var}_{\nu_{h,R}}(f)
\le m_*^{-1}\mathcal E_{h,R}(f,f),\quad m_*>0}
\tag{SI}
\]

for every admissible gauge-invariant \(f\) in a stated common core and then the closed form domain, with \(m_*\) independent of \(h\) and \(R\) in physical units. Specify boundary conditions and the order of thermodynamic/refinement limits. If the physical generator has additional terms or a different quadratic form, derive the correct form rather than assuming this one.

The exact finite ground-state transform identifies the spectral Rayleigh quotient with the Dirichlet form:

\[
\langle f\Omega_{h,R},(H_{h,R}-E_{0,h,R})f\Omega_{h,R}\rangle
=\mathcal E_{h,R}(f,f).
\]

This identity is the common bridge, not uniformity. A finite positive gap does not prove (SI).

## 2. Six canonical gates

| Gate | Required certificate | Exit condition | Status |
|---|---|---|---|
| S0 — source/refinement | Authenticated coupled-\(\mathbb Z^5\)/\(2+2\) geometry, accepted links/faces, physical metric, refining family and boundary maps | One source-native regulator family fixed | OPEN |
| S1 — physical dynamics | SU(2) variables, Gauss law, magnetic interaction, electric coefficients, time/clock, self-adjoint Hamiltonian and positive/reflection-positive transfer derived from source | One physical generator and transfer structure | OPEN |
| S2 — interacting vacuum | Actual finite-volume ground state, common measure, compatible domains/disintegration | Vacuum used by every estimate identified | OPEN |
| S3 — uniform inequality | (SI) for all gauge-invariant functions, uniform in refinement and volume | Explicit \(m_*>0\) in physical units | OPEN — CENTRAL TARGET |
| S4 — infrared | Physical low-frequency exclusion, correlation/transfer control and thermodynamic persistence | Positive physical gap survives infinite volume | OPEN |
| S5 — continuum | Tightness, nontriviality, locality, covariance, reflection positivity, OS reconstruction and gap persistence | Nontrivial 4D continuum YM with positive reconstructed gap | OPEN |

### S0-H source-geometry finding — 2026-11-11

The claimed perpendicular configuration-space torus in Paper 2 §3.3 is not a valid quotient: \(\pi_\perp(\mathbb Z^5)\) is dense in \(\mathbb R^2\), including on the sum-zero rank-four lattice. Its quotient is non-Hausdorff, not \(\mathbb T^2\). The compact \(u\)-coordinate / KK interpretation therefore cannot be used as the source certificate for a physical compact spatial direction. The exact four-vector proof and verifier are recorded in [the P0-H quotient audit](../../research/audits/P0_COUPLED_Z5_INTERNAL_QUOTIENT_DENSITY_AUDIT_2026-11-11.md).

A possible 3D cut-and-project reinterpretation \(E_{\rm phys}=V_{72^\circ}\oplus\mathbb R e_u\), \(E_{\rm int}=\mathbb R e_v\) is mathematically distinct: it projects the decagonal window to one internal dimension, changes the accepted point set, breaks \(C_5\), and treats \(u\) as extended space rather than a compact circle. It is only a candidate geometry. It still requires finite-region cellulations, boundary/refinement maps, incidence and Hodge data, and a compatible source-derived SU(2) action. **S0 remains OPEN.**

The sequence is a dependency order. A result can discharge a sub-obligation at another gate, but cannot bypass prerequisites.

## 3. Analytical lanes: different mechanisms for the same target

Each lane must identify the exact term or estimate in (SI) it supplies, with model and assumptions attached.

### A — PF-I16 source-native local interaction (primary candidate)

Exact finite seven-class four-face coefficients, single-face dressing/shared-link residual identities and universal connected-support counting are source-level inputs. The universal rooted count is \(784^{k-1}\); the sharper \(16^{k-1}\) is finite-crop only.

Still required: independent four-factor group-multiplication mixed-Hessian sign/trivialization/orientation certificate; recomputed third-order estimate; fourth-order partition cancellation; spatial connected/tree decay; all-orders activity majorant. S1 physical Hamiltonian and kinetic/time normalization are separate prerequisites. Auxiliary coupling estimates are not physical estimates until S1 is derived.

Potential S3 contribution: local conditional influence/Dirichlet comparison estimates for the actual \(\nu_{h,R}\), followed by a global all-functions coercivity argument. Local cluster summability alone is not (SI).

### B — signed radial current / completed cage

Alternate S3 mechanism through signed current identities, deletion/cage comparisons and cutoff estimates. Established within stated scope: exact signed cumulative-flux identity; finite-volume completed-cage positivity; restricted cut-cage perturbative comparison; planar U(1) deleted-face Haar-flatness.

Open: interacting SU(2) current estimate, regulator-uniform cumulative-flux control, non-Abelian transport/electric-operator defect and cutoff-shell absorption. Finite-volume constants are nonuniform. It enters S3 only after proof for the same source-derived vacuum and form.

### C — original-link Peter–Weyl / Borel–Volterra

Exact finite open-chain Peter–Weyl gap, low-order fusion/disconnected-output coefficients, source multigrading, local-history Borel components entire in the stated topology, and conditional Gevrey-1 recurrence estimate are established within their scopes.

Obstruction: finite-strip score radius
\[
\rho_N=\frac{3e^{-\sigma}}{16N(2+6N)}
\]
shrinks with width. No width-uniform anchored norm, positive-ray Borel–Laplace reconstruction, ordinary \(\lambda=1\) convergence or uniform interacting chain gap is established. Do not identify this resolvent with PF-I16 unless operator, measure and activity estimates are explicitly matched.

### D — R3-IR full-Hessian reference semigroup

A conditional finite-dimensional analytic template for gradient/Hessian evolution under a common weighted reference measure. Established within scope: ordered Hessian evolution with curvature corrections; audited local geometry/incidence for the finite straight strip; common-measure/domain compatibility; conditional one-output weighted gradient–Hessian contraction with \(\lambda_{\min}>0.4955484\) on the stated finite strip and bounded-incidence extension above \(0.4800\).

Boundary: finite product-SU(2) strip/reference semigroup, not the PF source Hamiltonian or interacting vacuum. No strip-length-uniform scalar \(L^2\) gap, source dynamics, nonlinear fixed point or continuum gap follows. Reuse only after geometric, generator, measure and domain equivalence is proved.

### E — prism/Whitney and cubic Wilson-flow controls

Comparison models/adversarial controls for geometry, gauge covariance, locality, vacuum estimates and failure modes. These are not the canonical coupled-\(\mathbb Z^5\)/\(2+2\) regulator. A projected cubical skeleton, Voronoi complex, prism complex or cubic lattice is not interchangeable with source links. Import requires a proved equivalence of variables, incidence, metric/Hodge weights, Gauss law, Hamiltonian, physical time, transfer positivity and limiting observables. Until then: comparison/obstruction only.

### F — f-sum / positive spectral weight

Potential S4 input after transfer and observables are authenticated. A moment lower bound or positive spectral weight does not alone exclude support arbitrarily close to zero. A separate uniform low-frequency exclusion is required.

## 4. No cross-route constant laundering

Combine constants only after a written equivalence certificate proves the same:
1. finite regulator and refinement map;
2. link/face variables, gauge action and Gauss-invariant test space;
3. Hamiltonian/generator and magnetic interaction;
4. physical electric coefficients and derivative metric;
5. vacuum measure and boundary conditions;
6. physical time/transfer normalization;
7. norm, domain and order of limits.

If any item differs or is unproved, label the result COMPARISON-ONLY. Never add PF-I16 activity constants to cubic-flow, prism or R3-IR coercivity constants. Never infer a physical mass from helical observer frequencies, finite electric cycle gaps or finite-strip contraction rates.

## 5. Required dossier for every S3 contribution

Every new result must state:
- exact source, regulator, finite complex, variables and boundary conditions;
- physical \(H_{h,R}\), \(\alpha_{e,h,R}\), derivative metric, time units and magnetic term, or mark auxiliary;
- exact \(\nu_{h,R}\) and its relation to the true interacting vacuum;
- test class (all gauge-invariant functions or a named restricted class);
- inequality, constants and dependence on \(h,R\), coupling and geometry;
- proof of refinement/volume uniformity in physical units;
- exact theorem/file dependencies and assumptions;
- obstructions and counterexamples;
- derivation, independent audit, deterministic checker/log/hash where appropriate;
- precise S0–S5 sub-obligation discharged.

Use explicit evidence labels: EXACT-FINITE, CONDITIONAL, SOURCE-REPORTED, NUMERICAL, COMPARISON-ONLY, OBSTRUCTION, OPEN. Computation corroborates; it does not replace proof. Indexing is not certification.

## 6. Non-circular work order

1. Authenticate S0/S1: source-native regulator, physical Hamiltonian, electric normalization, magnetic interaction, time/clock and positive/reflection-positive transfer.
2. Continue PF-I16 only along its actual dependencies: certify the four-factor mixed-Hessian/orientation estimate and recompute third order; then prove fourth-order cancellation, spatial tree decay and all-orders activity majorant.
3. Synthesize one S3 theorem using estimates already expressed in the same source, measure, generator, metric and test-function space. Prove all-functions coercivity.
4. Prove S4 low-frequency exclusion and thermodynamic persistence; f-sum moments alone are insufficient.
5. Construct nontrivial 4D continuum Schwinger functions, perform OS reconstruction and prove the reconstructed spectrum retains a positive lower edge.

Reject as circular any task that re-derives a certified finite identity without a newly identified gap, promotes restricted test-class control to all-functions coercivity, imports constants across models without the seven-part equivalence certificate, or uses a finite positive gap as evidence of refinement/volume uniformity.

## 7. Explicit non-claims

This architecture does not establish S0–S5, (SI), a physical mass gap or a continuum theory. It does not merge Penrose, cubic, prism, Borel and R3-IR models. It does not reinterpret helical observer ratios as energies or certify all theorem-indexed records. All gates remain OPEN until independently reviewed proof dossiers meet their exit conditions.

## 8. Source navigation

- [PF-I16 current source-native work](../../README.md)
- [R3-IR full-Hessian adversarial audit](../audits/R3_IR_ADVERSARIAL_FULL_HESSIAN_ENERGY_INEQUALITY_AUDIT_2026-11-11.md)
- [R3-IR local geometry/incidence audit](../audits/R3_IR_LOCAL_GEOMETRY_SOURCE_AND_INCIDENCE_AUDIT_2026-11-11.md)
- [R3-IR bounded-incidence extension](../audits/R3_IR_BOUNDED_INCIDENCE_ANALYTIC_EXTENSION_2026-11-11.md)
- [Yang–Mills interface](../../observatory/yang-mills-proof.html)
- [Proof Atlas](../../observatory/graph.html)

This is the canonical architecture specification. Individual source dossiers remain authoritative for their own mathematical statements; this synthesis does not overwrite them.
