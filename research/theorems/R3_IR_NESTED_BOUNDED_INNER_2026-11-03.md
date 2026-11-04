# R3-IR — Bounded-inner nested-history Casimir split (2026-11-03)

**Scope:** finite open straight square SU(2) strips, original-link gauge-invariant coefficients. **Conditional** on the prior strong projective Fourier multiplication and fixed-spin-radius local bilinear estimate. This is not unrestricted anchored closure, an interacting spectral-gap theorem, or a continuum Yang–Mills proof. Full source, verification, and hashes: R3_IR_NESTED_BOUNDED_INNER_2026-11-03.zip in the conversation.

Let \(\mathcal B=K^{-1}Q\Gamma_K\) for \(K=-\sum_e a_e\sum_{j=1}^3X_{ej}^2\), \(0<a_0\le a_e\le a_*\), and assume
\[
\|\mathcal B(f_I,g_J)\|_{P_\sigma}
\le C_0 |E(I)\cap E(J)|\|f_I\|_{P_\sigma}\|g_J\|_{P_\sigma},
\quad C_0=24(1+a_*/a_0).
\]
Use \(\|F\|_{\mathrm{anch},\kappa,\sigma}=\sup_x\sum_{I\ni x}e^{\kappa|I|}\|f_I\|_{P_\sigma}\). Consider the nested ordered pairs \(J\subseteq I\), preserving the output history \(I\) and all physical recoupling channels. Suppose every nonzero inner coefficient \(g_J\) has \(|J|\le M\) and each original-link SU(2) spin label \(\le s\). There are no size or spin restrictions on outer coefficients.

## Theorem (restricted same-weight nested closure)
\[
\boxed{
\|\mathcal B^{J\subseteq I}_{\mathrm{nested}}(F,G)\|_{\mathrm{anch},\kappa,\sigma}
\le e^{-\kappa}\left[4(a_*/a_0)s+2C_0M(M+1)(3M+1)\right]
\|F\|_{\mathrm{anch},\kappa,\sigma}\|G\|_{\mathrm{anch},\kappa,\sigma}.
}
\]
This constant is independent of total strip size, outer history size and outer spin. No spin-radius or history-weight loss.

### Proof
Fix outer original-link representation sector \(\mathbf n\) with \(q=\sum_e n_e(n_e+2)/4>0\) and define \(q_J=\sum_{e\in E(J)}n_e(n_e+2)/4\). On each output from multiplying by an inner \(g_J\), original-link labels outside \(E(J)\) stay unchanged.

If \(q_J\le q/2\), every output sector has electric eigenvalue at least \(a_0q/2\). With inner spin cap s, \(\|\Gamma_K(f_{\mathbf n},g_J)\|_{P_\sigma}\le(3a_*s/4)\sum_{e\in E(J)}n_e\|f_{\mathbf n}\|_{P_\sigma}\|g_J\|_{P_\sigma}\). Each original link is incident to at most two faces, so \(\sum_{J:e\in E(J)}\|g_J\|_{P_\sigma}\le 2e^{-\kappa}\|G\|_{\rm anch}\); also \(\sum_e n_e\le4q/3\). Thus the sum over these good J is at most \(4(a_*/a_0)s e^{-\kappa}\|f_{\mathbf n}\|\|G\|_{\rm anch}\).

For exceptions \(q_J>q/2\), a link belongs to at most \(D=M(M+1)\) connected intervals of length at most M. Therefore \(\sum_Jq_J\le Dq\) and the number of exceptional J is at most \(2D\). The inherited local estimate bounds each by \(C_0(3M+1)\|f_{\mathbf n}\|\|g_J\|\), and each \(\|g_J\|\le e^{-\kappa}\|G\|_{\rm anch}\). Sum exceptional contributions, outer sectors, and outer histories \(I\ni x\); since output history remains I, the anchored estimate follows.

## Limitations and next obligation
The constant grows with M and s, and the true nonlinear recurrence generates arbitrarily large inner histories and spins. Therefore this does not close the full nested map at fixed spatial weight, nor imply volume-uniform score convergence, the interacting \(\lambda=1\) gap, 3D extension, or the 4D continuum mass gap. The next target is a weighted summation over unbounded inner length/spin, treating low-energy recoupling channels exactly and avoiding a renewed radius/weight loss.

Verification: 15,980 finite exact-rational incidence, Casimir, exception-count and selected scalar inequalities passed. These checks do not independently prove the representation-theoretic operator input.