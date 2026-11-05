# P2 — Exact fusion multiplicity barrier and energy-weighted local commutator domain

**Private audit — 2026-11-04.** This follows P-71/P-72 in the corrected original-link SU(2) straight-strip model. A complete expanded report, two executed independent scripts, logs, SHA-256 manifest and integrity-tested ZIP are preserved in **Library → The Singular Boundary → Proof Audits**, under \`P2_FUSION_COMPLEXITY_AND_WEIGHTED_DOMAIN_2026-11-04.md\` and \`p2_fusion_complexity_weighted_domain_2026-11-04.zip\`. These claims are **not** a full N≈m² physical inverse, interacting infinite-volume dynamics, uniform spectral gap, or 4D continuum Yang–Mills proof.

## P-73 — Exact integer SU(2) fusion dimensions quantify why full Schur inversion alone cannot scale

For a genuine output tuple with one degree \ell=m±1 and N−1 fundamental degrees,
\[
\mathcal H_{N,\ell}=V_{\ell/2}\otimes(V_{1/2})^{\otimes(N-1)}
=\bigoplus_{L}V_{L/2}\otimes\mathbb C^{d_L}.
\]
The exact SU(2) fusion rule gives d^(1)_L=1_(L=\ell) and d^(r+1)_L=d^(r)_(L−1)+d^(r)_(L+1), with absent or negative labels interpreted as zero, respecting parity. Thus the simultaneous-conjugation invariant matrix algebra has
\[
\boxed{\dim_{\mathbb C}\mathrm{End}_{SU(2)}(\mathcal H_{N,\ell})=\sum_L d_L^2}
\]
and the Fourier Hilbert dimension is \(\sum_L(L+1)d_L=(\ell+1)2^{N-1}\).

**Verified exact integer counts:**

| N | m | \ell | Fourier dimension | Full invariant operator dimension |
|---:|---:|---:|---:|---:|
|10|3|2|1536|30056|
|10|3|4|2560|45560|
|16|4|3|131072|100490220|
|16|4|5|196608|140810370|
|36|6|5|206158430208|71687931432655401192|
|36|6|7|274877906944|93977718977341668952|

The recurrence also passed N=100,m=10 without constructing Fourier matrices. Exact dimensions are **not** lower bounds for source-dependent compressed Krylov subspaces, nor evidence that each invariant coordinate must be evaluated. They demonstrate that **unrestricted full invariant-space inversion is itself intractable**. Local CG fusion avoids dense Fourier basis construction but must additionally exploit the short genuine corrected Poisson collar source, bounded-depth electric iteration, structured compression and Schatten-1 certificates. The P-67 sufficient q=O(log m) does not alone guarantee polynomial algorithmic complexity.

## P-74 — A local SU(2) gauge-invariant Casimir projection has a uniformly bounded graph-weighted second commutator

Use the **actual corrected two-face interacting** Hamiltonian
\[
H=4(C_1+C_2)+2\sum_{a=1}^3R_1^aL_2^a+\lambda(V_1+V_2),\quad V_i=-\chi_1(U_i)/2,
\]
and the gauge-invariant protected F=P_0⊗I, P_0 the first-face spin-zero spectral projection. Let D=[V_1,P_0]. Then [H,F]=λD⊗I is bounded but the **ordinary** second commutator is unbounded (P-72). Nevertheless, on the finite PW core
\[
[H,[H,F]]=\lambda[4C_1,D]\otimes I+\lambda^2[V_1,D]\otimes I
+2\lambda\sum_a[R_1^a,D]\otimes L_2^a.
\]
The first-face commutators are bounded because D connects only the vacuum and fundamental sectors. The SU(2) Casimir identity implies \(\|L_2^a(1+C_2)^{-1/2}\|\le1\). Therefore
\[
\boxed{\|[H,[H,F]](1+C_2)^{-1/2}\|
\le |\lambda|\|[4C_1,D]\|+\lambda^2\|[V_1,D]\|
+2|\lambda|\sum_a\|[R_1^a,D]\|<\infty.}
\]
The bound is **uniform in adjacent spin cutoff** and establishes mapping boundedness from the neighbor-Casimir graph domain into Hilbert space. It **does not** prove a norm-C² orbit, invariant all-time graph algebra, full infinite-volume generator, unique state, gap, or Borel/OS continuum theorem. Independent finite-spin checks at λ=.25,1,2 and neighbor doubled-spin degrees 1,2,4,8,16,32,64,128 verify the weighted bound while the raw norm grows.

## Scientific boundary and next objectives

The research record's previous turn reported a working *uncommitted* local fusion tensor implementation, source-specific direct contractions and selected N=m² source coefficients. Those working files were **not available in this execution environment**; this audit **does not falsely claim to reproduce them**. Rebuild and commit their source-specific tensor contraction verification before any stronger complete physical result.

Physical: use true corrected-source low-rank tensor representation and P-67 induced S1 tail with a source-adapted compressed Krylov/Gram method. Dynamical: construct a gauge-compatible all-time interacting automorphism in a controlled representation/energy-weighted topology and prove its generator/core. **Positive interacting gap, positive-ray Borel reconstruction and 4D continuum YM mass gap remain OPEN.**