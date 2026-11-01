# R3-IR — Wilson heat-kernel Harnack control of transport-orbit density

**2026-10-31. Finite-volume theorem; no regulator-uniform anti-depletion.**

Let X=SU(2)^E with product Haar measure, \(H=-\sum_e a_e\Delta_e+V\), \(a_e>0\), and bounded real continuous retained-face Wilson magnetic potential \(V\). Let \(\Omega>0\) be the normalized ground state with \(H\Omega=E_0\Omega\). Set \(\Delta V=\sup_X V-\inf_X V\). Write \(k_s(g,h)\) for the strictly positive normalized SU(2) heat kernel for \(-\Delta\) at time \(s>0\), and \(\mathcal R(s)=(\max_{g,h}k_s(g,h))/(\min_{g,h}k_s(g,h))\in[1,\infty)\).

## WH-1: Pairwise Wilson Harnack comparison

For every \(x,x'\in X\), \(t>0\), and \(S(x,x')=\{e:x_e\ne x'_e\}\),

\[
\frac{\Omega(x)}{\Omega(x')}\le \exp(t\Delta V)\prod_{e\in S(x,x')}\mathcal R(a_e t).
\]

**Proof.** The Feynman–Kac bridge representation yields the pointwise kernel domination \(e^{-t\sup V}K_t^0(x,y)\le K_t^V(x,y)\le e^{-t\inf V}K_t^0(x,y)\), where \(K_t^0(x,y)=\prod_e k_{a_et}(x_e,y_e)\). Since \(\Omega=e^{tE_0} e^{-tH}\Omega\), positive \(\Omega(y)\) lets us compare the two kernel integrals at \(x,x'\). All factors for links with \(x_e=x'_e\) cancel in the pointwise free-kernel ratio. Each remaining factor is bounded by \(\mathcal R(a_et)\). This proves the inequality. The reverse ratio follows by exchanging \(x,x'\).

## WH-2: Transport-orbit density ratio

If a smooth potential-preserving Haar transport action \(T_g\) changes links only within a fixed set \(S\subseteq E\) for each orbit (the set may depend on the orbit and tree), then

\[
\boxed{R_z=\frac{\max_g\Omega(T_gz)^2}{\min_g\Omega(T_gz)^2}
\le \inf_{t>0}\exp(2t\Delta V)\prod_{e\in S}\mathcal R(a_et)^2.}
\]

This is a bound on the **actual** finite-volume Wilson vacuum, requiring no unknown spectral gap and no prior assumption on \(R_z\). For the standard Wilson potential \(V=\sum_{k\ne f}b_k(1-p_k)\) with \(b_k\ge0\), \(\Delta V\le2\sum_{k\ne f}b_k\). The upper bound thus may grow exponentially with total magnetic coupling and with the changed-link count; its refinement uniformity is **not** established. It also does not replace the distinct electric generator constant \(C_Y\), which depends on full Jacobian support, including unchanged links.

For comparison, the normalized SU(2) heat kernel admits character series \(k_s(\theta)=\sum_{n=0}^\infty (n+1)e^{-sn(n+2)/4}\sin((n+1)\theta)/\sin\theta\); \(\mathcal R(s)\to1\) as \(s\to\infty\), but \(\mathcal R(s)\to\infty\) as \(s\downarrow0\). Taking large \(t\) therefore trades improved heat smoothing against \(t\Delta V\).

## WH-3: Weighted orbit Poincaré consequence

Combining with the previously established weighted-orbit Poincaré inequality, on an orbit for which \(\sum_a|Y_aq|^2\le C_Y\Gamma_0(q)\),

\[
\operatorname{Var}_{w_z}(q)\le\frac{4C_Y}{3}\left[\inf_{t>0}e^{2t\Delta V}\prod_{e\in S}\mathcal R(a_et)^2\right]\mathbb E_{w_z}[\Gamma_0(q)].
\]

The factor is finite for each finite cage. The bound does **not** control the signed unweighted radial current nor imply the continuum gap.

## Verification scope

`verify.py` evaluates the SU(2) character heat kernel at five times (sampled angles; sampled extrema are *not certified* maxima/minima) and tests the underlying positive-kernel integral comparison on 5,000 randomized finite-dimensional positive kernels, with no violations. The actual theorem uses analytical heat-kernel extrema, not the sampled approximations, and the tests are not ground-state computations.

**Open:** find refinement-uniform bounds exploiting local retained-face Wilson structure rather than global \(\Delta V\); bound the signed radial current, connected covariance, continuum Yang–Mills mass gap.