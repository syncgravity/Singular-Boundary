# P2: Full corrected-electric physical Schatten dual and factorial source-order Borel algebra

**2026-11-04.** Model: corrected original-link SU(2) electric operator on finite open straight square strips in a single independent-face trace-expansion PW norm. Two restricted theorems: a **full-inverse** nuclear lower certificate for the true Gauss-invariant high-spin response; and a **bounded factorial source-order Banach algebra with continuous Borel evaluation**, together with a precise limitation of scalar-majorant order-weight schemes for physical evaluation. **Neither theorem gives the N≈m² response asymptotic, infinite-volume Borel summability, interacting vacuum, OS reconstruction or 4D Yang–Mills mass gap.** Expanded derivation, self-contained actual physical Fourier engine, tensor-local one-Haar verifier, 40,000 exact order-pair checks, execution log, SHA256 manifest and ZIP integrity: companion conversation archive \`p2_full_dual_factorial_2026-11-04.zip\`.

## A. Positivity yields an unconditional *full-inverse* physical Schatten lower bound

Take even outer width N, the true residual-Gauss-twirled balanced intertwiner F_N, and a separately gauge-invariant singleton character chi_m(U_j), m>=3. Each nonconstant output face degree tuple c has c_j=l in {m−1,m+1}, other c_i=1; different (j,l) sectors are disjoint. Let e(n)=n(n+2),
\[
K_{\bf c}=D_{\bf c}\mathrm{Id}+H_{\bf c},\quad D_{\bf c}=\sum_i e(c_i),\quad H_{\bf c}(X)=-2\sum_{i,a}J_{c_i}^aXJ_{c_{i+1}}^a,
\]
and let Y=GaussTwirl(Z) be the true physical output Poisson source, where Z is the *untwirled* local two-bond collar source from P-42. Since every J is Hermitian, every left/right superoperator is self-adjoint on Hilbert–Schmidt space. Moreover, with
\[
\alpha_{\bf c}=\frac{\sum_{i=1}^{N-1}\sqrt{e(c_i)e(c_{i+1})}}{2D_{\bf c}}\le\tfrac12,
\quad \|H_{\bf c}\|_{S_2\to S_2}\le D_{\bf c}\alpha_{\bf c},
\]
the actual K is strictly positive self-adjoint, with maximum eigenvalue <=D(1+alpha). Thus
\[
\langle Y,K^{-1}Y\rangle_2\ge \frac{\|Y\|_2^2}{D_{\bf c}(1+\alpha_{\bf c})}.
\]
Gauge twirl is unital completely positive, so \|Y\|op<=\|Z\|op. Therefore W=Y/\|Z\|op is a **valid Schatten dual observable** with operator norm <=1, and
\[
\boxed{\|K_{\bf c}^{-1}Y\|_{S_1}\ge
\frac{\|Y\|_{S_2}^2}{D_{\bf c}(1+\alpha_{\bf c})\|Z\|_{\mathrm{op}}}.}\tag{A1}
\]
**Unlike earlier q=0 certificates, this applies directly to the full inverse with NO Neumann-tail subtraction.** The numerator is the already independently proved one-Haar scalar \|Y\|2²=<Z,GaussTwirl(Z)>; the denominator requires only a three-face local operator norm. At sigma=0 and moment grade one, the ratio of dimension/moment weights for each output sector is \((l+1)^2/[4(m+1)^3]\). These independent lower contributions sum over j,l, with the common history factor e^-kappa applied afterward.

**Complete actual physical Fourier regressions** (history discount omitted):
| N | m | full-inverse dual lower (A1) | exact full-response numerical S1 norm |
|---:|---:|---:|---:|
| 2 | 3 | 0.0183706462 | 0.0723909692 |
| 2 | 4 | 0.0163799329 | 0.0612580952 |
| 4 | 3 | 0.0162848125 | 0.1291250095 |
| 4 | 4 | 0.0154881690 | 0.1169833274 |

Wider one-Haar/local-collar **double-precision formula evaluations** for a single interior insertion (sum of l=m±1): ≈0.00105939312 at (N,m)=(10,3), and ≈0.00051535863 at (16,4), excluding e^-kappa. These are numerical values of a rigorously valid lower-bound **formula**, **not interval-certified decimal enclosures** and not the complete N-site sum. They do not establish a large-m lower bound growing with m.

**Additional all-even-width HS source suppression.** The twirled balanced input satisfies \|F_N\|2²=1/(N+1). Local CG compression is HS-contractive, tensoring with the spin-m character identity costs sqrt(m+1), each input bond has HS multiplier <=3/4, each mixed output bond <=3(m+1)/4, and the scalar source multiplier <=m+2. Hence for each j,l,
\[
\boxed{\|Y_{j,l}\|_2^2\le\frac{25}{4}\frac{(m+2)^2(m+1)}{N+1}.}\tag{A2}
\]
This bounds the **Hilbert–Schmidt** response source, not its nuclear norm: increasing rank prevents a direct same-grade inference.

## B. Factorial source-order weighting is a closed local Borel algebra

Work on source-provenance degree-n history families F_n with the ORIGINAL exponential spatial anchored norm \(L_{\kappa,\sigma}^{(1)}\), representation degree cap <=n, and full history union labels. From the direct all-history graded Poisson theorem P-23, at kappa=log4,
\[
\|\mathcal B(F_n,G_m)\|_{L^{(1)}}\le h_{nm}\|F_n\|_{L^{(1)}}\|G_m\|_{L^{(1)}},
\quad h_{nm}=\frac{88}{3}+6(n+m+2).
\]
Define the complete factorial source-order Banach space
\[
\boxed{\|F\|_{\mathfrak Y_\rho}=\sum_{n\ge1}\frac{\rho^n}{n!}\|F_n\|_{L^{(1)}}.}\tag{B1}
\]
Since \(\binom{n+m}{n}\ge n+m\) for integers n,m>=1,
\[
\frac{h_{nm}}{\binom{n+m}{n}}
\le6+\frac{88/3+12}{n+m}\le\boxed{\frac{80}{3}},
\]
with equality at n=m=1 **for the certified scalar majorant**. Therefore
\[
\boxed{\|\mathcal B(F,G)\|_{\mathfrak Y_\rho}\le\frac{80}{3}\|F\|_{\mathfrak Y_\rho}\|G\|_{\mathfrak Y_\rho}.}\tag{B2}
\]
The fundamental source's weighted norm is \(\rho(16/3)e^\sigma\) at kappa=log4. The quadratic small-ball criterion gives a **source-order-labelled formal fixed point** whenever
\[
\boxed{0<\rho<\frac9{5120}e^{-\sigma}.}\tag{B3}
\]
Unlike the prior Gaussian order topology, the **first Borel evaluation** is continuous: for |\xi|<=rho,
\[
\boxed{\left\|\sum_{n\ge1}F_n\xi^n/n!\right\|_{L^{(1)}}\le\|F\|_{\mathfrak Y_\rho}.}\tag{B4}
\]
This directly recovers the independently proved local uniform Borel disk. The evaluated Borel transform satisfies its **differentiated Volterra equation**, not the simple quadratic fixed-point equation, because factorial evaluation does not preserve the ordinary Cauchy product. It does NOT yield continuation past the local disk or evaluate the original physical score \(\sum_n S_n\) at lambda=1.

## C. Precise barrier for the *existing scalar-majorant order-weight strategy*

Let w_n>0 be any simple order weights for which the **present certified scalar majorant** h_nm=C+d(n+m+2), d>0, satisfies \(\sup_{n,m}h_{nm}w_{n+m}/(w_nw_m)\le H<\infty\). At m=1, \(w_{n+1}\le (H w_1/(dn))w_n\), and hence
\[
\boxed{w_n\le w_1\frac{(H w_1/d)^{n-1}}{(n-1)!}.}\tag{C1}
\]
Direct physical evaluation of arbitrary coefficient arrays at any nonzero lambda would require \(\sup_n|\lambda|^n/w_n<\infty\), contradicting this factorial upper bound. Thus **within this scalar-majorant-compatible class of order-weighted sequence norms**, bounded bilinearity and continuous *untransformed* physical evaluation cannot coexist. This is **not** an obstruction theorem for the true physical SU(2) bilinear map on a smaller source-reachable space; cancellation or improved sector bounds could change the conclusion.

## Regression and research boundary

Standalone companion ZIP contains complete corrected physical Fourier and tensor-local one-Haar modules; a full-inverse dual verifier checking four complete output sums and source HS bounds, plus wider N=10,16 source evaluations; 40,000 exact rational factorial-majorant pairs and exact Borel-radius checks; passing logs and SHA256SUMS.txt. All tests executed and ZIP integrity passed. This report avoids claiming numerically *interval-certified* bounds from ordinary double precision.

**Next physical objective:** obtain a rigorous N≈m² lower or upper asymptotic on the true nuclear response using (A1), preferably a closed rational/asymptotic one-Haar numerator and local op-norm estimate. **Next analytic objective:** stronger structure for positive-ray Borel continuation and/or evaluation-continuous physical reconstruction, beyond the current scalar graded majorant. No interacting vacuum, reflection-positive continuum construction or 4D Yang–Mills mass gap is proved.
