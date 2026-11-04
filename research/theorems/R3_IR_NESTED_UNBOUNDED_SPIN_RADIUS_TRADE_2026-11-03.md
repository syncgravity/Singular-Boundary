# R3-IR — Unbounded nested histories at fixed spatial weight with spin-radius loss

Research date 2026-11-03. **Conditional theorem for Gauss-invariant SU(2) on finite open straight square strips.** Expanded mathematical report, exact verifier, execution log, and checksums: R3_IR_NESTED_UNBOUNDED_SPIN_RADIUS_TRADE_2026-11-03.zip in current conversation.

## Inputs

Use corrected original-link electric K, \(0<a_0\le a_e\le a_*\), \(\mathcal B=K^{-1}Q\Gamma_K\). The history-aware version retains ALL physical output channels and labels each nested pair by union I∪J=I. The norms are
\[
\|f\|_{P_\sigma}=\sum_{\mathbf n}d_{\mathbf n}e^{\sigma|\mathbf n|}\|A_{\mathbf n}\|_{S_1},\qquad
\|F\|_{\mathrm{anch},\kappa,\sigma}=\sup_x\sum_{I\ni x}e^{\kappa|I|}\|f_I\|_{P_\sigma}.
\]
Inherited hypotheses: (i) same-spin-radius physical matrix Peter–Weyl local bilinear inequality, with \(C_0=24(1+a_*/a_0)\); and (ii) bounded-inner Casimir-splitting estimate with polynomial dependence on inner length and linear dependence on maximum inner spin.

## Nested theorem (arbitrary inner histories, with spin regularity loss)

Fix \(\kappa>0\), \(\sigma>\sigma'\ge0\), \(\delta=\sigma-\sigma'>0\), \(t=e^{-\kappa}\), \(u=e^{-\delta}\), \(R=a_*/a_0\). For the ordered nested operation with inner J⊆outer I,
\[
\boxed{\|\mathcal B_{\mathrm{nested,outerF}}(F,G)\|_{\mathrm{anch},\kappa,\sigma'}
\le A_{\kappa,\delta}\|F\|_{\mathrm{anch},\kappa,\sigma'}\|G\|_{\mathrm{anch},\kappa,\sigma},}
\]
where
\[
\boxed{A_{\kappa,\delta}
=4R\frac{t}{1-t}\frac{u}{(1-u)^2}
+4C_0\frac{t(4+5t)}{(1-t)^4}\frac{u}{1-u}.}
\]
Uniform in ambient strip length, all original-link spins, and all history widths. Same spatial history exponent \(\kappa\) on both sides; strict loss of **spin-analytic** radius.

### Proof
Decompose inner Fourier coefficient sectors by exact history length \(m\ge1\) and maximum nonzero original-link spin \(s\ge1\). Constant sectors make zero gradient contributions. For each \(G_{m,s}\), \(\sum_e n_e\ge s\) implies
\[
\|G_{m,s}\|_{\mathrm{anch},\kappa,\sigma'}\le u^s\|G\|_{\mathrm{anch},\kappa,\sigma}.
\]
The previous bounded-inner Casimir split improves its factor from \(e^{-\kappa}\) to \(t^m\) for exact inner length m, because nested union history is I. It therefore gives
\[
\|\mathcal B_{\mathrm{nested}}(F,G_{m,s})\|_{\kappa,\sigma'}
\le t^m[4Rs+2C_0m(m+1)(3m+1)]\|F\|_{\kappa,\sigma'}\|G_{m,s}\|_{\kappa,\sigma'}.
\]
Sum over m,s and use exact generating series
\[
\sum_{m\ge1}t^m=\frac{t}{1-t},\quad
\sum_{m\ge1}m(m+1)(3m+1)t^m=\frac{2t(4+5t)}{(1-t)^4},
\]
\[
\sum_{s\ge1}u^s=\frac{u}{1-u},\quad
\sum_{s\ge1}su^s=\frac{u}{(1-u)^2}.
\]
All converge for positive \(\kappa,\delta\). Completion extends the estimate to the stated Banach-scale domain.

## General all-history corollary

Combine both nested orientations (allow double-counting equal histories for an upper bound) and the previous fixed-\(\kappa,\sigma'\) crossing/end-joining theorem, whose constant is
\[
C_{\rm cross}(\kappa)=4C_0\left[\frac1{1-t}+\frac{3t}{(1-t)^2}\right].
\]
Then
\[
\boxed{\|\mathcal B_{\rm hist}(F,G)\|_{\mathrm{anch},\kappa,\sigma'}
\le [C_{\rm cross}(\kappa)+2A_{\kappa,\delta}]
\|F\|_{\mathrm{anch},\kappa,\sigma}\|G\|_{\mathrm{anch},\kappa,\sigma}.}
\]

## Limits and next task

This is not a same-\(\sigma\) bound. \(A_{\kappa,\delta}\) diverges when \(\delta\to0\), and repeated nonlinear tree iterations may exhaust analytic radius. Hence no claim of all-orders volume-uniform interacting vacuum, physical \(\lambda=1\) gap, three-dimensional spatial extension, OS reconstruction, or 4D continuum mass gap is made. The new result offers a **trade of spin regularity rather than spatial regularity** for arbitrary-history fusion, not a complete solution of nonlinear closure.

Next task: prove a radius-preserving energy-adapted recoupling estimate or a graded renormalized fixed-point theorem with controlled cumulative losses. Preserve all low-energy physical output channels.

## Verification
The reproducible exact-rational checker passed 4,471 tests covering the rational generating functions, partial sums and representative spin-sector inequalities. It does not re-prove the inherited SU(2) operator theorem or replace independent mathematical review.