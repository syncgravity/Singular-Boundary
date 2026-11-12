# PF-I16 — Exact one-rhombus bilinear resolvent smoothing and its multi-loop threshold

**2026-11-09 research audit.** Source model: an actual accepted four-edge Penrose–Fibonacci rhombus and original-link SU(2) Casimir, as in PF-I15/PF-I16. No cubic or Voronoi surrogate; the comparison two-independent-loop calculation below is *not* substituted for the authentic coupled source geometry. Complete detailed proof, executable checker, and SHA-256 manifest: Library, \`/The Singular Boundary/Proof Audits/PF_I16_ONE_LOOP_BILINEAR_2026_11_09.zip\`.

## Exact one-rhombus inverse-nonlinearity estimate

Let \(A_f=\sum_{e\in\partial f}a_e>0\). A gauge-invariant function depending solely on the four-edge simple loop holonomy is a class function on SU(2), and its electric operator is \(K_f=A_f C\), with \(C\chi_n=n(n+2)\chi_n/4\). The Haar-mean-zero inverse has a central convolution kernel
\[
R_{A_f}(U)=\frac4{A_f}\sum_{n\ge1}\frac{n+1}{n(n+2)}\chi_n(U).
\]
Peter–Weyl orthogonality and an exact telescoping sum prove
\[
\boxed{\|R_{A_f}\|_2^2=\frac{16}{A_f^2}\sum_{n\ge1}\frac{(n+1)^2}{n^2(n+2)^2}
=\frac{16}{A_f^2}\left(\frac{\pi^2}{12}+\frac1{16}\right).}
\]
For arbitrary smooth gauge-invariant one-loop class functions \(F,G\), original-link Cauchy–Schwarz gives \(\|\Gamma_K(F,G)\|_1\le\sqrt{\mathcal E_K(F,F)\mathcal E_K(G,G)}\). Young's convolution inequality then yields the **exact universal local bilinear bound**
\[
\boxed{\|K_f^{-1}P_0\Gamma_K(F,G)\|_2\le
\frac4{A_f}\sqrt{\frac{\pi^2}{12}+\frac1{16}}\,
\sqrt{\mathcal E_K(F,F)\mathcal E_K(G,G)}.}
\]
For unit electric links \(A_f=4\) the prefactor is \(0.9407268644107668\). This solves the one-loop **L² target** problem left open in PF-I16's high-spin forcing audit. It does not show that the output has controlled H¹ norm, so it is not an iterable Banach fixed-point theorem.

## Two-independent-loop comparison — the same Young-kernel proof fails

On **comparison** product SU(2)\(\times\)SU(2), with \(K=4C_U+4C_V\), the reduced inverse kernel has squared L² norm bounded below by
\[
\sum_{n,m=1}^{N}
\frac{(n+1)^2(m+1)^2}{[n(n+2)+m(m+2)]^2}.
\]
The shell \(N\le n,m<2N\) supplies \(N^2\) summands, each at least \(1/144\), showing divergence as \(N\to\infty\). Thus the identical L¹→L² convolution-kernel estimate is unavailable for two independent holonomies. **This does not prove unboundedness of** \(K^{-1}P_0\Gamma\) on multi-loop states, nor does it settle the genuinely overlapping rhombi, for which joint original-link recoupling may yield additional structure.

## Verification and gates

Independent SymPy evaluation verifies the exact inverse-kernel series; cutoff sums through \(N=512\) confirm convergence on one loop and divergence on independent two-loop comparison space, and shell inequalities pass. This is finite local functional analysis, not a replay of all eight historical crops. No original input data, canonical proof certification or Observatory gate was modified.

**OPEN:** iterable spin-network-weighted/analytic uniform bound for coupled overlapping original source rhombi, interacting uniform Poincaré inequality, source-derived physical time/energy normalization, continuum/OS reconstruction, and four-dimensional Yang–Mills mass gap.