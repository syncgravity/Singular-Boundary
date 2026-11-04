# R3-IR — Graded output spin-moment audit (2026-11-03)

**Conditional finite-strip result, NOT nonlinear closure or Yang–Mills mass gap.** Expanded proof and 569,745-check verifier: conversation package R3_IR_GRADED_OUTPUT_SPIN_MOMENT_AUDIT_2026-11-03.zip.

## Input and norm
For the corrected original-link SU(2) physical electric Poisson fusion with connected-history lifting on finite open straight square strips, assume the inherited full-history tame estimate
\[
\|\mathcal B(F,G)\|_A\le C_{\rm cross}\|F\|_A\|G\|_A+C_{\rm nest}(\|F\|_A\|G\|_{T^{(1)}}+\|F\|_{T^{(1)}}\|G\|_A).
\]
The A norm has fixed spatial-history \(\kappa>0\) and spin-analytic radius \(\sigma\ge0\). Let \(F^{[s]}\) contain sectors whose maximum original-link spin label is s. Define
\[
\|F\|_{T^{(r)}}=\sum_{s\ge0}(1+s)^r\|F^{[s]}\|_A,\quad r\ge0.
\]
The sum over spin sectors is OUTSIDE the spatial-anchor supremum, so \(T^{(0)}\) can be strictly stronger than A.

## Sector-count correction and output estimate
SU(2) Clebsch–Gordan rules give max output spin \(u\le s+t\) for input sectors with max spins s,t. Spin-sector projection contracts A, but different sector projections may peak at different anchors. Thus
\[
\|\mathcal B(F^{[s]},G^{[t]})\|_{T^{(r)}}\le(1+s+t)^{r+1}\|\mathcal B(F^{[s]},G^{[t]})\|_A.
\]
The extra output-sector counting power cannot be silently dropped.

## Conditional graded tame theorem
Since \(1+s+t\le(1+s)(1+t)\), the prior tame estimate yields
\[
\boxed{\begin{aligned}
\|\mathcal B_{\rm hist}(F,G)\|_{T^{(r)}}\le{}&
C_{\rm cross}\|F\|_{T^{(r+1)}}\|G\|_{T^{(r+1)}}\\
&+C_{\rm nest}\big[\|F\|_{T^{(r+1)}}\|G\|_{T^{(r+2)}}
+\|F\|_{T^{(r+2)}}\|G\|_{T^{(r+1)}}\big].
\end{aligned}}
\]
Every constant is independent of strip length. Spatial and spin-exponential weights are unchanged, but polynomial spin grade is lost. At r=1, the output first moment is controlled by input second and third moments. This does NOT establish T^(1) × T^(1) to T^(1).

## Proof dependency and next target
Apply the inherited A-valued crossing and ordered-nested estimates to each input max-spin sector pair, then use the output sector-count lemma and sum. This is conditional on the earlier physical Peter–Weyl local estimate and nested Casimir argument; finite arithmetic checks do not verify those analytic hypotheses.

The graded map is NOT a closed infinite-order nonlinear score recurrence. Repeated binary trees may need arbitrarily high polynomial grades, so convergence requires quantitative moment-growth estimates, a sharper sectorwise bound, or a renormalized graded fixed point. Test whether a locally anchored spin-sector norm avoids the extra grade and whether physical electric denominators compensate the remaining inner spin factor. Interacting λ=1, 3D spatial dynamics, nontrivial continuum R4 Yang–Mills and mass gap all remain open.

Verification: 569,745 deterministic checks of exact grade inequalities, original-link incidence bounds, and a toy demonstration that sector-sum and anchor-supremum cannot be interchanged.