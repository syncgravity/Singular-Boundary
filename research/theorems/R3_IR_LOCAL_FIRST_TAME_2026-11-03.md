# R3-IR — Local-first fixed-radius spin-moment tame fusion audit
**2026-11-03. Conditional finite original-link SU(2) straight-strip theorem only.** Expanded report, executable checker, log, and SHA256 manifest: conversation artifact R3_IR_LOCAL_FIRST_TAME_2026-11-03.zip. No interacting mass gap or continuum Yang–Mills proof is claimed.

## Local-first norm and correction
The previous T^(r) norm put the sum over max-spin sectors OUTSIDE the anchor supremum, creating a possible output-sector counting cost. Instead put the Fourier spin sum INSIDE each anchor:
\[
\|F\|_{L^{(r)}_{\kappa,\sigma}}
=\sup_x\sum_{I\ni x}e^{\kappa|I|}
\sum_{\mathbf n}d_{\mathbf n}e^{\sigma|\mathbf n|}
(1+\max_e n_e)^r\|A_{I,\mathbf n}\|_{S_1}.
\]
Then L^(0)=A exactly and L^(r)<=T^(r). This is a norm-ordering repair, not an independent interacting physics result.

## Explicit inherited assumptions
Corrected original-link SU(2) electric operator, nonconstant gauge-invariant free spectral gap, coefficientwise projective matrix Peter–Weyl trace-class multiplication/bilinear bound, and the exact-length good/exceptional nested Casimir splitting, all on finite open simply connected straight square strips. Let R=a*/a0, C0=24(1+R), t=e^(-kappa), kappa>0, sigma>=0.

## Conditional graded tame theorem, with no exponential-radius or spatial-weight loss
Define
\[
C_{\rm cross}=4C_0\left(\frac1{1-t}+\frac{3t}{(1-t)^2}\right),\qquad
C_{\rm nest}=4R\frac{t}{1-t}+8C_0\frac{t(2+t)}{(1-t)^3}.
\]
For all integers r>=0,
\[
\boxed{\begin{aligned}
\|\mathcal B_{\rm hist}(F,G)\|_{L^{(r)}}\le{}&
C_{\rm cross}\|F\|_{L^{(r)}}\|G\|_{L^{(r)}}\\
&+C_{\rm nest}\left(
\|F\|_{L^{(r)}}\|G\|_{L^{(r+1)}}
+\|F\|_{L^{(r+1)}}\|G\|_{L^{(r)}}\right).
\end{aligned}}
\]
There is NO factor counting all output max-spin labels. Every CG output obeys u<=s+t, and (1+u)^r<=(1+s)^r(1+t)^r; the projective Fourier norm sums all outputs at a fixed anchor before the supremum. Crossing interactions need no spin-moment loss. Nested interactions require one extra spin moment in the inner input due to the differentiated fundamental sector and the Casimir good/exceptional split. The original nested exact-length counting bound #exceptional<=4m and its t^m history factor are used.

The constants do not grow with strip length, history width, or maximum spin. For r=1 this establishes the symmetric tame map L^(1) x L^(2) -> L^(1), **not** fixed-grade L^(1) x L^(1) -> L^(1). No ordinary nonlinear fixed-point or volume-uniform interacting vacuum convergence theorem is established.

## Important audit limits
Proof uses inherited **coefficientwise** matrix Peter–Weyl control; a function-level norm estimate alone does not justify moving sector weights through a Clebsch–Gordan sum. All histories and original-link physical channels must be retained; in particular low-energy nested Wilson-loop outputs may not be projected away. The exact finite checker is not a formal proof of those analytic operator inputs.

## Verification and next objective
The local archive includes an executable exact checker reporting **8,864,177** integer/rational checks (max-spin inequalities, straight-strip original-link incidence and exceptional energy counts, anchored sum/sup counterexample, and generating-series coefficients). The next target is a direct fixed-grade L^(1) x L^(1) test for low-energy/high-spin nested channels, or a controlled graded nonlinear convergence mechanism. Nontrivial R4 theory, uniform physical interacting gap, and continuum mass gap remain open.