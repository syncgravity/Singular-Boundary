# R3-IR — Exact-length Casimir split and fixed-radius tame nested fusion (2026-11-03)

**Status:** conditional original-link SU(2) finite-open-square-strip estimate, NOT complete nonlinear Banach closure or Yang–Mills mass gap. Expanded proof, verifier, log and hashes: conversation research package R3_IR_EXACT_LENGTH_SPIN_MOMENT_TAME_2026-11-03.zip.

## Inherited hypotheses

The physical original-link electric Poisson fusion is \(\mathcal B=K^{-1}Q\Gamma_K\) with \(0<a_0\le a_e\le a_*\), \(R=a_*/a_0\). For Gauss-invariant Fourier coefficients on face intervals \(I,J\), assume the previously recorded strong matrix Peter–Weyl bound
\[
\|\mathcal B(f_I,g_J)\|_{P_\sigma}\le C_0|E(I)\cap E(J)|\|f_I\|_{P_\sigma}\|g_J\|_{P_\sigma},\quad C_0=24(1+R).
\]
Set
\[
\|F\|_{A_{\kappa,\sigma}}=\sup_x\sum_{I\ni x}e^{\kappa|I|}\|f_I\|_{P_\sigma},\qquad \kappa>0,\;\sigma\ge0.
\]
Write \(G^{[s]}\) for the Fourier coefficient sectors whose maximum original-link representation label equals \(s\), and introduce the **summed-spin-moment anchored norm**
\[
\boxed{\|G\|_{T_{\kappa,\sigma}}=\sum_{s\ge0}(1+s)\|G^{[s]}\|_{A_{\kappa,\sigma}}.}
\]
This is stronger than the original anchored norm; notably the sum over sectors lies *outside* the anchor supremum.

## Improved counting for inner histories of exactly m faces

Each original link belongs to at most \(2m\) such intervals. For a fixed nonzero outer Casimir energy \(q=\sum_ec(n_e)\) and \(q_J=\sum_{e\in E(J)}c(n_e)\),
\[
\sum_{|J|=m}q_J\le2mq,\qquad \#\{J:|J|=m,\;q_J>q/2\}\le4m.
\]
The previous cumulative-cutoff estimate allowed a quadratic rather than linear number of exceptional inner intervals. Repeating the bounded-inner Casimir proof yields, for maximum inner spin s,
\[
\|\mathcal B_{\mathrm{nested}}(F,G_{m,s})\|_{A_{\kappa,\sigma}}
\le e^{-\kappa m}\,[4Rs+4C_0m(3m+1)]\,\|F\|_{A_{\kappa,\sigma}}\|G_{m,s}\|_{A_{\kappa,\sigma}}.
\]

## Fixed-spin-radius tame theorem

Put \(t=e^{-\kappa}\) and
\[
C_{\mathrm{nest}}^{\mathrm{tame}}(\kappa)
=4R\frac{t}{1-t}+8C_0\frac{t(2+t)}{(1-t)^3}.
\]
Then for ordered nested history pairs (inner G, outer F),
\[
\boxed{
\|\mathcal B_{\mathrm{nested}}(F,G)\|_{A_{\kappa,\sigma}}
\le C_{\mathrm{nest}}^{\mathrm{tame}}(\kappa)
\|F\|_{A_{\kappa,\sigma}}\|G\|_{T_{\kappa,\sigma}}.
}
\]
**No loss of spatial weight or spin-analytic radius**, and the constant is independent of strip length, inner/outer interval widths and all representation degrees. Proof: decompose G by exact m and s; \(\|G_{m,s}\|_A\le\|G^{[s]}\|_A\). Sum \(m\) using \(\sum_{m\ge1}t^m=t/(1-t)\), \(\sum_{m\ge1}m(3m+1)t^m=2t(2+t)/(1-t)^3\), then sum s using the norm T.

Combining with the prior crossing/end-joining theorem gives
\[
\boxed{
\|\mathcal B_{\mathrm{hist}}(F,G)\|_A\le
C_{\mathrm{cross}}\|F\|_A\|G\|_A
+C_{\mathrm{nest}}^{\mathrm{tame}}(\|F\|_A\|G\|_T+\|F\|_T\|G\|_A),
}
\]
where \(C_{\mathrm{cross}}=4C_0[(1-t)^{-1}+3t(1-t)^{-2}]\). Therefore \(\mathcal B_{\mathrm{hist}}:T\times T\to A\) is bounded **but \(T\times T\to T\) is not proved**. It is a tame estimate rather than a closed nonlinear Banach algebra.

For \(\delta>0\), \(u=e^{-\delta}\), the stronger analytic space embeds into T:
\[
\|G\|_{T_{\kappa,\sigma}}\le(1-u)^{-2}\|G\|_{A_{\kappa,\sigma+\delta}}.
\]
The converse fails in general: a single-face tail normalized to \(P_\sigma\)-sector amplitudes proportional to \(s^{-3}\) has finite T norm but no positive extra spin-analytic radius. Thus a stronger **polynomial spin moment**, not exponential radius loss, suffices for one unrestricted fusion application.

## Precise open objective

Prove output spin-moment preservation (possibly via a graded \(T^{(r)}\) family), or construct a rigorous counterexample. Until a \(T\)-valued nonlinear recurrence is controlled, volume-uniform interacting vacuum, \(\lambda=1\) gap, full 3D spatial dynamics and the nontrivial 4D continuum Yang–Mills mass gap remain unproved.

## Verification

An exact Fraction and incidence checker passed **90,005** finite assertions (including exact-length exceptional energy counts and generating-series comparisons). The infinite-dimensional SU(2) Fourier estimate is inherited and not formally checked here. Full report and reproducibility package remain attached to the conversation.
