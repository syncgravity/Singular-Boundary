# PF-I16 — Uniform electric inverse and exact high-spin carré-du-champ obstruction

**2026-11-09 source-faithful finite original-link SU(2) audit.** Complete proof, executable verifier, output and SHA-256 manifest are preserved in Library as \`/The Singular Boundary/Proof Audits/PF_I16_HIGH_SPIN_RESOLVENT_2026_11_09.zip\`. No cubic/Voronoi surrogate; the calculation uses a genuine four-edge accepted PF source rhombus and the same original-link Casimir as PF-I15. Auxiliary coefficients are not source-derived physical kinetics.

## A. Uniform reduced electric inverse

For any finite authenticated accepted source graph, with unit-height original edges, no simple cycles shorter than four, at least one four-edge rhombus, and \`a_e>=a0>0\`, PF-I15's cycle characterization gives
\[
\inf\operatorname{spec}(K|_{\mathbf1^\perp})=\frac34\min_{\ell\,\mathrm{simple\,cycle}}\sum_{e\in\ell}a_e\ge3a_0,
\qquad
\boxed{\|K^{-1}P_0F\|_2\le(3a_0)^{-1}\|P_0F\|_2.}
\]
This finite auxiliary *linear* Poisson estimate is uniform in source volume at fixed a0. It does not bound the nonlinear forcing \`Gamma_K(S_j,S_{n-j})\`.

## B. Exact unbounded H¹ × H¹ → L² nonlinear forcing, on one authentic loop

Take an accepted genuine simple four-edge source rhombus with four unit electric coefficients. On its ordered SU(2) holonomy write \`chi_n\` for the normalized spin-n/2 character. \`K chi_n=n(n+2)chi_n=:lambda_n chi_n\`, and character fusion gives \`chi_n²=sum_{k=0}^n chi_{2k}\`. The positive carré du champ \`Gamma_K(F,F)=[2F KF-K(F²)]/2\` has **exact** spectral expansion
\[
\boxed{\Gamma_K(\chi_n,\chi_n)=\sum_{k=0}^n[n(n+2)-2k(k+1)]\chi_{2k}.}
\]
Haar orthogonality and an exact finite polynomial sum yield
\[
\boxed{\|\Gamma_K(\chi_n,\chi_n)\|_2^2=
\frac{n(n+1)(n+2)(7n^2+14n+4)}{15}.}
\]
Normalize \`u_n=chi_n/sqrt(lambda_n)\`. These are Haar-mean-zero gauge-invariant functions with \`E_K(u_n,u_n)=1\`, but
\[
\boxed{\|\Gamma_K(u_n,u_n)\|_2^2
=\frac{(n+1)(7n^2+14n+4)}{15n(n+2)}
\sim\frac7{15}n\to\infty.}
\]
Thus **no** uniform (indeed, no fixed-one-rhombus) constant \`C\` can give \`||Gamma_K(F,F)||_2 <= C E_K(F,F)\` for arbitrary gauge-invariant finite-energy F. The naive route "uniform electric inverse + H¹ energy bounds ⇒ L²-contractive score recurrence" is invalid. This is a counterexample to a proposed norm bound, **not** to convergence of the actual physical score, or to a spectral gap.

## C. Exact smoothing for this family; do not overinterpret the obstruction

With the constant mode projected out, the inverse response is
\[
K^{-1}P_0\Gamma_K(u_n,u_n)
=\sum_{k=1}^{n}\frac{\lambda_n-2k(k+1)}{4k(k+1)\lambda_n}\chi_{2k}.
\]
Therefore
\[
\boxed{\lim_{n\to\infty}\|K^{-1}P_0\Gamma_K(u_n,u_n)\|_2^2
=\frac{\pi^2}{48}-\frac3{16}\approx0.0181167583560.}
\]
The norm tends to \`0.1345985080\`. The inverse *does* smooth the specific high-spin sequence. We have **not** proved that the inverted bilinear map is unbounded or bounded for arbitrary inputs. It would be false to infer divergence of the inverted recurrence from the forcing counterexample alone.

## Verification and remaining gate

Companion Python verifier performs exact sympy polynomial summation plus 1,100-node SU(2) class-Haar quadrature at indices \`n=1,2,4,8,16,32,64,128\`; all tests passed. Exact formulas, not quadrature, constitute the proof. The source geometry is inherited from prior accepted-rhombus records; no fresh replay of all eight original source crops occurred in this audit.

**Next gate:** establish a rigorous uniform cluster estimate in a stronger spin-network-weighted / analytic norm (or direct inverse-plus-product norm), respecting low-spin SU(2) recoupling and local source incidence. The coupled interacting Poincare inequality, source-determined time/energy scales, continuum/OS reconstruction and physical 4D Yang–Mills mass gap all remain **OPEN**. Canonical main, original data and Observatory gate statuses unchanged.
