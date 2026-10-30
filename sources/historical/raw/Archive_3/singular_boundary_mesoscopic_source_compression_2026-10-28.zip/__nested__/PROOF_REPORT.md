# R3-IR — Strong mesoscopic source control and covariance obstruction

Date: October 28, 2026. Exact finite nonlinear SU(2) result, conditional on the previously stated geometric coupling hypotheses. The macroscopic connected-covariance and continuum mass-gap obligations remain open.

## 1. Exact all-band compression

For a finite face-complete SU(2) rhombus Hamiltonian

\[H=\sum_e a_e(-\Delta_e)+\sum_f b_f d_f,\quad d_f=1-\tfrac12\mathrm{ReTr}(W_f)\in[0,2],\]

fix a face region D and set S=union of its edges and C(D)=exterior faces touching S. Let \(E_D=3\sqrt{A_S B_D}/\sqrt2+2B_C\) as in ER-1; assume \(b_f\geq\beta_{\min} h^{-2}\) for f in D. Let \(P_{\leq\eta}\) denote the vacuum-referenced energy spectral projection, including restriction to the physical gauge-invariant space. For bounded real coefficients \(|q_f|\leq q_*\), define

\[A_{h,\alpha}=h^{2-\alpha}\sum_{f\in D}q_f p_f,\qquad B_{h,\alpha}=A_{h,\alpha}-h^{2-\alpha}\sum_{f\in D}q_f I=-h^{2-\alpha}\sum_{f\in D}q_f d_f.\]

**Theorem SC-1.** On the entire low-energy subspace,

\[\boxed{\|B_{h,\alpha}P_{\leq\eta}\|^2\leq\frac{2q_*^2}{\beta_{\min}}|D|h^{6-2\alpha}(E_D+\eta).}\]

**Proof.** The pointwise inequality \(|\sum q_fd_f|^2\leq q_*^2(\sum d_f)^2\leq 2q_*^2|D|\sum d_f\) follows from Cauchy–Schwarz and \(d_f^2\leq2d_f\). By ER-1, for each normalized low-energy vector, \(\sum_{f\in D} b_f\langle d_f\rangle\leq E_D+\eta\). Since \(b_f\geq\beta_{\min}h^{-2}\), insertion into the positive-operator expectation and taking the supremum proves the claim. No gap, Gaussian comparison, or covariance decay is assumed.

For any spectral projection P_I orthogonal to P_low, \(\|P_I A P_{\leq\eta}\|\leq\|B P_{\leq\eta}\|\). For any normalized \(\psi\) in that subspace, \(\operatorname{Var}_\psi(A)\leq\|B\psi\|^2\). Two such source covariances are bounded by the geometric mean of their variance estimates. These statements hold in the full Hilbert space and in its gauge-invariant reducing sector.

## 2. Penrose shrinking-support theorem

Assume the declared geometrical coefficient bounds \(a_e\leq a_*\), \(\beta_*/h^2\leq b_f\leq\beta^*/h^2\), rhombus area at least \(\sigma_-h^2\), with the selected centered face ball D_R having a complete interior collar, \(h\leq R\leq R_0\). The area comparison and previous MI-3 collar count imply

\[|D_R|\leq\frac{4\pi}{\sigma_-}\frac{R^2}{h^2},\qquad |C(D_R)|\leq\frac{16\pi}{\sigma_-}\frac R h.\]

The regional energy increment satisfies \(E_{D_R}\leq(C_0R^2+C_1R)/h^3\), where

\[C_0=\frac{12\sqrt2\pi}{\sigma_-}\sqrt{a_*\beta^*},\qquad C_1=\frac{32\pi\beta^*}{\sigma_-}.\]

Therefore SC-1 implies the exact uniform estimate (with C depending on fixed coefficient and radius bounds)

\[\boxed{\|B_{h,\alpha}P_{\leq\eta}\|^2\leq C[(R^4+R^3)h^{1-2\alpha}+\eta R^2h^{4-2\alpha}].}\]

For the \(\alpha=3/2\) candidate normalization and fixed physical energy ceiling \(\eta\), let \(R(h)=\ell^{1-\gamma}h^\gamma\), \(2/3<\gamma<1\). Then

\[\boxed{\|B_{h,3/2}P_{\leq\eta}\|=O(h^{(3\gamma-2)/2})\to0.}\]

The vacuum-centered source also tends to zero, with at most twice the displayed norm. For \(2/3<\gamma<3/4\), the global elementary operator norm bound \(O(R^2h^{-3/2})\) can diverge, while the low-energy compression vanishes. This improves the previous ER-4 theorem from a selected ultraviolet-band bound to **every orthogonal energy band**, but only for shrinking physical supports.

## 3. Logical sharpness of the curvature method

On a simply connected rhombus disk, tree gauge fixing permits freely prescribed based face holonomies. Choose one random Bernoulli Z with probability \(\mathbb P(Z=1)=h/R\): either all face holonomies are I (Z=0), or all are a fixed trace-zero SU(2) matrix (Z=1). Then each face has deficit d_f=Z, so \(\mathbb E d_f=h/R\), consistent with the regional bound's boundary term. With \(|D_R|\asymp R^2/h^2\) and all q_f=1, the \(\alpha=3/2\) scalar-subtracted source has

\[\operatorname{Var}(B)=h|D_R|^2\frac hR\left(1-\frac hR\right)\asymp\frac{R^3}{h^2}.\]

At \(R=h^{2/3}\), this remains order one, showing the exponent threshold cannot be improved from the regional mean-deficit bound alone. This is an **abstract gauge-configuration ensemble**, not the actual interacting vacuum or excited eigenstate. Its energy and f-sum properties are not authenticated. It does not disprove more sophisticated Hamiltonian-specific covariance estimates.

## 4. Evidence statuses and critical path

- **Independently proved:** SC-1 exact finite-volume operator compression, given the already checked ER-1 regional energy comparison.
- **Conditionally proved on geometry/couplings:** SC-2 refinement rates for embedded Penrose disks with complete collars.
- **Exact logical obstruction:** the coherent face-ensemble witness demonstrates insufficiency of mean-deficit information alone.
- **Open:** macroscopic fixed-support (R fixed) connected excited-state covariance, source-specific quartic resolvents, Stage 7–26 coupling identity, quantum-continuum reconstruction and the positive infinite-volume physical mass gap. For fixed R and alpha=3/2, SC-2 grows as O(h^-2) and is insufficient.

**Next independently necessary proof task:** derive a fixed-support *connected-compensation* estimate, e.g. for the appropriate vacuum or low-energy state, \(\operatorname{Var}_\psi(\sum_{f\in D_R}q_fd_f)=o(h^{-1})\) for the \(\alpha=3/2\) source. It must exploit the nonlinear Wilson dynamics beyond a first curvature moment; it cannot be assumed as a mixing or Poincaré hypothesis. A vacuum variance result would not by itself close the parity-resolved quartic response or mass gap.

Original numerical chains and historical sources were not modified. Verifier: `verify_mesoscopic_compensation.py`, deterministic exact geometry and symbolic checks only.
