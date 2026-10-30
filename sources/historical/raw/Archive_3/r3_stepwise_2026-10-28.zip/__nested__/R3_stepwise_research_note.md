# R3 stepwise audit: incidence, collar, and correlated Gibbs comparison
28 October 2026. **Not an unrestricted R3 closure.**

## 0. Source and normalization
Primary inputs inspected: `Branch · Branch · Compare Continuum Mass Gaps.txt`, `R3_geometry_and_annealed_comparison.md`, `penrose_complete_catalogue.npz`, `square_strict_catalogue.npz`, sample Stage 26 archive inventories. The catalogue arrays contain path/cycle data but do **not** identify the oriented space-time prism face words or the inserted Q/reference cavity action. The construction below is explicitly a **square-grid control geometry**, not an inferred Penrose prism.

Let \(c(H)=\operatorname{tr}(H)/2\), \(w_\lambda(H)=e^{-\lambda(1-c(H))}\), and \(R_Q=\mathbb E_{\mu_C}\prod_{p\in Q}w_\lambda(H_p)\) for a normalized cavity Gibbs measure \(\mu_C\). Thus \(0<R_Q\le1\).

## 1. Incidence reconstruction and admissibility
The reproducible `geometry_audit.py` creates a 2x2 spatial plaquette square complex over three temporal intervals (four time slices), with all spatial and temporal Wilson faces initially coupled. It contains 36 vertices, 75 independent unoriented edges **before gauge fixing**, and 52 faces (16 spatial, 36 temporal). Insert four temporal faces surrounding spatial face (0,0) in interval 1, removing their Wilson factors from the reference action.

Results: each inserted face has **zero strictly exclusive Haar edges** (edges appearing in no other face); two inserted faces have one edge absent from the cavity action but those edges are shared with other insertions. Thus the sufficient strict free-edge theorem cannot be applied to this particular fully-coupled control without additional arguments. The face-adjacency collars contain 4, 22, 46, and 52 faces for radius 0, 1, 2, 3. Those are finite-size facts; they DO NOT prove a bounded collar uniform across an expanding Penrose complex.

There is no claim that this geometry matches the actual 12-prism R3 model. Its 52 faces are intentionally a different construction.

## 2. Collar-relaxed comparison: a precise condition
A collar-only proof must establish the following *quantitative* property, not merely a bounded number of faces: an event \(A_Q\) in the actual cavity probability space (or a transported set under an explicitly analyzed change of variables) such that

\[\mu_C(A_Q)\ge e^{-a|Q|}(1+\lambda)^{-b|Q|}, \qquad
\sum_{p\in Q}(1-c(H_p))\le d|Q|/\lambda\quad\text{on }A_Q.\]

Then restricting the expectation to \(A_Q\) gives
\[R_Q \ge e^{-(a+d)|Q|}(1+\lambda)^{-b|Q|}.\]

This elementary implication is **conditional**, and does not establish \(A_Q\). For any proposed transport, one must calculate the Jacobian/Radon–Nikodym ratio, losses in all preexisting face factors, boundary holonomy constraints, and number of preimages. A local gauge transformation alone leaves closed-plaquette traces invariant and cannot repair a frustrated plaquette holonomy.

## 3. Correlated Gibbs-averaged route: new rigorous sufficient criterion
Define \(D_Q=\sum_{p\in Q}(1-c(H_p))\ge0\), evaluated under the **actual correlated cavity Gibbs law** (even though Q is omitted from the cavity action). Then
\[R_Q=\mathbb E_{\mu_C}e^{-\lambda D_Q}\ge e^{-\lambda\mathbb E_{\mu_C}D_Q}\]
by Jensen's inequality. Consequently, if a geometry- and volume-independent constant \(K\) gives
\[\mathbb E_{\mu_C} D_Q\le K |Q|\frac{1+\log(1+\lambda)}{\lambda},\qquad \lambda\ge1,\]
then
\[-\log R_Q\le K|Q|(1+\log(1+\lambda)).\]
This is a verified **sufficient criterion**, not an already-proved bound on the cavity expectation. It is stronger than necessary: sparse near-flat Gibbs events could yield the desired ratio even when the mean deficit is too large. It avoids independent-Haar assumptions and shows exactly which expectation must be estimated for an especially simple annealed proof.

An alternate sufficient criterion is \(\mu_C(D_Q\le K|Q|\log(1+\lambda)/\lambda)\ge e^{-a|Q|}(1+\lambda)^{-b|Q|}\). Restricting the expectation then produces the R3 logarithmic estimate. This small-ball formulation is weaker and likely more flexible than bounding the mean.

## 4. The obstruction survives correlated averaging
Take a single U with cavity law \(d\mu\propto e^{\lambda c(U)}dU\) and insert \(w_\lambda(-U)=e^{-\lambda(1+c(U))}\). Exact calculation:
\[R=\frac{\int e^{\lambda c(U)} e^{-\lambda(1+c(U))}dU}{\int e^{\lambda c(U)}dU}=e^{-\lambda}\frac{\lambda}{2I_1(\lambda)}\asymp \lambda^{3/2}e^{-2\lambda}.\]
Here the cavity Gibbs law is genuinely integrated, yet frustration survives, so Gibbs averaging alone is not a theorem. The value is a toy local Wilson construction, **not** a demonstrated admissible Penrose prism boundary condition.

## 5. Decision and exact remaining proof obligation
1. **Target incidence missing:** obtain original 3-step 12-prism oriented edge/face words, the exact Q and S_C, exterior/fixed boundary convention, and whether spacetime topological identifications are imposed.
2. **Free-edge route:** run the already specified leaf/matching test on that actual incidence graph. Gauge-fixing and conditioning must be accounted for, not inferred from raw unoriented edges.
3. **Collar route:** construct a local set or transport with uniform (in ambient volume) polynomial mass and bounded inserted deficits; check whether curvature/boundary frustration prohibits it.
4. **Annealed route:** prove either the mean-deficit criterion or the small-ball criterion for the **correlated** cavity Gibbs law, potentially using a finite-energy/conditional regularity estimate. Neither criterion is verified for the target geometry.
5. **Mass-gap implications:** even closing this insertion inequality does not by itself establish a transfer gap, thermodynamic-limit gap, or 4D continuum Yang–Mills existence/mass gap.

## Audit conclusion
Step 1 is completed only for a fully specified surrogate complex, and the true R3 incidence remains unidentified. Step 2 identifies concrete obstructions rather than establishing a collar map. Step 3 yields a rigorous, explicit Gibbs-averaged sufficient criterion. Step 4 remains an open geometric/probabilistic estimate. No unsupported Penrose admissibility or continuum closure is asserted.
