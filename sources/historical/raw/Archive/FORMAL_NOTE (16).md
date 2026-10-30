# Joint thermal-excess bound and the unresolved SU(2) frustration estimate

October 26, 2026. Research note for The Singular Boundary.

## Scope

We consider an arbitrary finite 2+1-dimensional spacetime cell complex, including Penrose spatial complexes, with SU(2) Wilson weights \(\beta_p\ge0\). A selected set \(J\) of edges is *plaquette-separated* if no plaquette contains two edges of \(J\). Conditional on every unselected edge, the Wilson measure factorizes in the selected edge variables.

## Theorem 1: exact joint thermal-excess exponential moment

For each selected edge \(e\), write the incident action as \(S_e(u;v)=B_e-u\cdot k_e(v)\) with \(B_e=\sum_{p\ni e}\beta_p\), \(\kappa_e=|k_e|\), and compatible minimum \(F_e=B_e-\kappa_e\). Set \(T_e=S_e(U_e;V)-F_e=\kappa_e(1-U_e\cdot n_e)\), where \(n_e=k_e/\kappa_e\) if \(\kappa_e>0\), and \(T_e=0\) otherwise.

For \(0<\theta<1\), with \(z(x)=2I_1(x)/x\),
\[
\mathbb E\left[e^{\theta\sum_{e\in J}T_e}\mid V\right]
=\prod_{e\in J}\left[e^{\theta\kappa_e}\frac{z((1-\theta)\kappa_e)}{z(\kappa_e)}\right]
\le C_\theta^{|J|},
\]
where \(C_\theta=\sup_{x\ge0}e^{\theta x}z((1-\theta)x)/z(x)<\infty\). This supremum is finite by continuity at zero and the large-argument asymptotic \(z(x)=\sqrt{2/\pi}\,e^xx^{-3/2}(1+O(x^{-1}))\). In particular the large-\(x\) ratio tends to \((1-\theta)^{-3/2}\). Averaging over the exterior gives the same uniform joint bound without conditional independence assumptions on the exterior.

Hence for all \(r>0\),
\[
\mu\bigl(\sum_{e\in J}T_e\ge r|J|\bigr)
\le\exp[-|J|(\theta r-\log C_\theta)].
\]
This is independent of UV cutoff, total volume, Penrose nonperiodicity, and the values of positive spatial and temporal plaquette couplings.

## Proposition 2: exact separation of the remaining obstruction

Writing \(S_J=\sum_{e\in J}S_e\) and \(F_J=\sum F_e\), we have \(S_J=F_J+T_J\). The same integral gives
\[
\mathbb E[e^{\theta S_J}]= \mathbb E_{\eta_\beta}[ e^{\theta F_J}\prod_{e\in J}e^{\theta\kappa_e}z((1-\theta)\kappa_e)/z(\kappa_e)].
\]
Since the bracketed factor is at least 1 and at most \(C_\theta\),
\[
\mathbb E_{\eta_\beta}e^{\theta F_J}
\le \mathbb E_\mu e^{\theta S_J}
\le C_\theta^{|J|}\mathbb E_{\eta_\beta}e^{\theta F_J}.
\]
For proportional dilution \(\beta'_p=(1-\theta)\beta_p\) on plaquettes incident to \(J\), the middle expression equals exactly \(Z(\beta')/Z(\beta)\). Thus the desired exponentially bounded frustration moment is equivalent up to \(O(|J|)\) in logarithms to the thin-support free-energy ratio. There is no independent proof here of either estimate for arbitrary \(J\) in the full 2+1D nonabelian theory.

## Explicit caveat

The local conditional distribution may have \(F_e=2\lambda\) if two equally weighted staples oppose. The estimate above controls \(S_e-F_e\), not the exterior probability of this frustration. Statements of uniform SU(2) Wilson-loop coupling monotonicity must not be imported from cited Abelian Ginibre results without a SU(2)-specific proof.

## What would suffice

It is enough to establish for some fixed \(\theta\in(0,1)\) a *noncircular* uniform bound
\[
\sup_{h,G,J}\frac1{|J|}\log\frac{Z(\beta^{(\theta,J)})}{Z(\beta)}\le C(1+\log\lambda_h).
\]
This would give the requested \(O(|J|\log\lambda_h)\) exponential moment and its expectation consequence via Jensen. It is not established by conditioning, thermal concentration, or background minimization. Further connected cumulant and RG-scale estimates are independent requirements.
