# R3-IR — Uniform radial Fisher and complete center jets do not prevent collar depletion

**Date:** 2026-10-31. **Classification:** Rigorous radial SU(2) counterfamily to a *proposed implication* of the one-link Fisher theorem. This is **not a counterexample to the actual Wilson ground-state eigen-equation** and does not establish or refute a continuum mass gap.

## Theorem (FA-1)

Let \(\omega(u)=2\sin^2u/\pi\), \(0\le u\le\pi\), be normalized SU(2) Haar class-angle density. There is a family \(\Psi_\delta\in C^\infty([0,\pi])\), \(0<\delta\le 1\), with all of the following properties:

1. \(\Psi_\delta>0\), \(\Psi_\delta(\pi-u)=\Psi_\delta(u)\), and \(\int_0^\pi\omega\Psi_\delta^2du=1\).
2. On fixed neighborhoods of \(u=0,\pi\), independent of \(\delta\), \(\Psi_\delta\equiv1\). Thus **all endpoint derivatives and endpoint values agree with Haar exactly**.
3. \(\sup_{0<\delta\le1}\int_0^\pi\omega(u)|\partial_u\Psi_\delta(u)|^2du<\infty\). Equivalently, the full probability-weighted radial score Fisher information is uniformly bounded.
4. Nevertheless, \(\mathfrak T_\delta=\int_0^{\pi/2}[\partial_u\log\Psi_\delta(u)]_+du\ge\log(1/\delta)\to\infty\).

In addition, for a fixed interior interval \(J\subset(0,\pi/2)\), \(\inf_J\Psi_\delta=\delta\), so no positive lower bound depending only on the uniform Fisher bound, complete endpoint jets, reflection symmetry, and normalization follows.

## Proof

Choose nonnegative smooth cutoffs \(\chi,\xi\in C_c^\infty((0,\pi))\), each invariant under reflection \(u\mapsto\pi-u\), with disjoint supports. Arrange \(\chi\equiv1\) on a fixed nonempty interior interval \(J\subset(0,\pi/2)\), \(0\le\chi\le1\), and \(\xi\not\equiv0\) supported further toward the equator. Both vanish in fixed center neighborhoods. For \(0<\delta\le1\), let \(g_\delta=1-(1-\delta)\chi\), and put \(\Psi_\delta=g_\delta+c_\delta\xi\), with \(c_\delta\ge0\) uniquely chosen to satisfy Haar normalization.

Indeed, \(\int\omega g_\delta^2\le1\), and the quadratic function \(c\mapsto\int\omega(g_\delta+c\xi)^2\) strictly increases for \(c\ge0\) to infinity; its initial value is at most 1, so there is a unique nonnegative solution. Since \(g_\delta\ge\delta\) and \(g_\delta\le1\), the compensation coefficients are uniformly bounded: for example \(c_\delta^2\int\omega\xi^2\le\int\omega\Psi_\delta^2=1\), as all summands are nonnegative. Therefore

\[
\int_0^\pi\omega|\Psi_\delta'|^2du
\le 2\int\omega|\chi'|^2du+2\bigl(\int\omega\xi^2du\bigr)^{-1}\int\omega|\xi'|^2du.
\]

All derivatives at both endpoints vanish because the bumps do. On the interval \(J\), \(\Psi_\delta=\delta\); at the end of the \(\chi\)-support on the way toward the equator, before the disjoint \(\xi\)-support, \(\Psi_\delta=1\). The total positive logarithmic variation between these points is at least \(\log(1/\delta)\), proving the last assertion. The squared score weighted by \(\omega\Psi_\delta^2\) is precisely \(\int\omega|\Psi_\delta'|^2\). QED.

## Wilson relevance and limitations

The exact one-link bridge gives \(I_{\rm ang}(f)\le4S_{0,e}\), and the charged-sector theorem controls \(S_{0,e}\) by the local Wilson coefficients. FA-1 proves that **a uniform bound on this probability-weighted Fisher information, even combined with all center endpoint jets, cannot by itself bound the unweighted positive score current**. Consequently, no proof can close the radial current gate by applying only these inequalities and center smoothness. A truly model-specific input is necessary, such as an upper bound on the positive excess conditional fiber energy from its nonlinear eigen-equation, an interior conditional density lower bound, or a direct one-sided flux comparison.

FA-1 does **not** assert that these constructed \(\Psi_\delta\) solve the actual completed-cage deleted-face Wilson eigen-equation. Their engineered scalar effective potentials may grow as \(\delta\downarrow0\). There is no proof here of \(\sup_{f\in D_R}\mathfrak T_{f,h}=o(h^{-1/4})\), connected covariance or continuum Yang–Mills mass gap.

## Reproduction

`verify.py` constructs explicit compactly supported symmetric smoothstep cutoffs, solves the single scalar normalization equation, and numerically checks six values \(\delta=10^{-1},\ldots,10^{-6}\). Results are in `results.json`. The universal claim is the analytic proof above; the script is an independent numerical consistency check. The smoothstep implemented by `np.clip` is C² rather than C-infinity at its joins; the analytic theorem uses C-infinity bump functions, with the numerical C² approximations supplying checks of the same inequalities.