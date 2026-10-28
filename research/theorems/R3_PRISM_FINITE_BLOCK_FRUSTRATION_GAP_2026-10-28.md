# R3-PRISM: two-sided finite Wilson-block frustration-gap theorem

**2026-10-28 | internally derived, proof supplied | original Penrose insertion NOT source certified.** This sharpens the compatible-minimizer *sufficient* theorem in the archived \`r3_compatibility_theorem_2026-10-28/RESEARCH_NOTE.md\`. It is **not** a proof of the R3 twelve-prism or R3-IR physical spectral gap.

## Setup

Let \(m\) independent SU(2) links have normalized product Haar measure; fix all exterior link values \(\eta\). Let \(C_B\) contain \(n\) cavity face words, \(Q\) contain \(q\ge1\) inserted words, all of length \(\le L\). Give the cavity dimensionless action \(D_C(U;\eta)=\sum_{p\in C_B}t_p(1-\mathrm{ReTr}H_p/2)\) with \(0\le t_p\le B_0\) and insertion \(D_Q(U;\eta)=\sum_{p\in Q}s_p(1-\mathrm{ReTr}H_p/2)\) with \(0\le s_p\le A_0\). Physical Wilson weights are \(\exp[-\lambda D_C]\) and \(\exp[-\lambda(D_C+D_Q)]\). Only faces depending on the \(m\) integrated links are included in \(C_B\); exterior-only cavity factors cancel.

Define \(R_\lambda(\eta)=Z_{C+Q}/Z_C\) and the **classical insertion-frustration gap**

\[
\Delta(\eta)=\min_U[D_C(U;\eta)+D_Q(U;\eta)]-\min_U D_C(U;\eta)\ge0.
\]

## Theorem and proof

Put \(\gamma_L=8/(3\pi^3L^3)\). For all \(\lambda\ge1\) and every fixed exterior \(\eta\),

\[
\boxed{\gamma_L^m\lambda^{-3m/2}
e^{-\lambda\Delta-(B_0 n+A_0q)/2}
\le R_\lambda(\eta)\le
\gamma_L^{-m}\lambda^{3m/2}
e^{-\lambda\Delta+B_0n/2}.}\tag{FG1}
\]

In particular,

\[
|-\log R_\lambda(\eta)-\lambda\Delta(\eta)|
\le m\{\tfrac32\log\lambda+\log(1/\gamma_L)\}
 +\tfrac12(B_0n+A_0q).\tag{FG2}
\]

**Proof.** For either of the smooth total actions \(S=D_C\) and \(S=D_C+D_Q\), choose a global minimizer \(U_*\) on the compact product group. Vary each link along \(U_e(t)=U_{*,e}\exp(tX_e)\), \(|X_e|\le\epsilon=(L\sqrt\lambda)^{-1}\). Every face has at most \(L\) factors and its normalized trace has second derivative of absolute value at most \(L^2\epsilon^2\), also with reversed or repeated edges. The first derivative of the total action vanishes at its minimizer. Taylor's theorem implies \(\lambda[S(U(1))-\min S]\le(B_0n+A_0q)/2\), or \(B_0n/2\) for the cavity alone. By SU(2) Weyl-Haar measure, the ball of radius \(\epsilon\) around any link has probability at least \((8/(3\pi^3))\epsilon^3=\gamma_L\lambda^{-3/2}\). Restricting the \(m\)-link integral to the product ball yields \(Z_S\ge(\gamma_L\lambda^{-3/2})^m \exp[-\lambda\min S-(\mathrm{sum\ coefficients})/2]\). Conversely \(Z_S\le\exp(-\lambda\min S)\). Divide in both directions. QED.

### Precise consequence

For fixed finite \(m,n,q,L,\eta\) and \(\lambda\)-independent normalized couplings,
\[
\lim_{\lambda\to\infty}\frac{-\log R_\lambda(\eta)}{\lambda}=\Delta(\eta).
\]
A pointwise logarithmic lower comparison \(R_\lambda(\eta)\ge\exp[-Kq(1+\log\lambda)]\) for some finite \(K\) holds **if and only if \(\Delta(\eta)=0\)**. If every \(s_p>0\), this is equivalent to existence of a cavity global minimizer for which *all inserted holonomies are \(I\)*. Therefore any admitted exterior with \(\Delta>0\) rules out the unrestricted pointwise version. If \(m\le bq,n\le aq\) with uniform geometry/couplings and \(\Delta=0\) for every admitted exterior, FG1 proves the desired support-local bound with explicit constants. When the exterior/couplings vary with \(\lambda\), the quantitative condition is instead \(\sup_\eta \lambda\Delta_\lambda(\eta)=O(q(1+\log\lambda))\) given \(m,n=O(q)\).

**Annealed comparison remains separate.** Positive conditional \(\Delta\) on some boundary configurations does not disprove an average over *correlated* exterior Gibbs data. Vanishing \(\Delta\) only on a zero-mass set does not prove such an average. The archived annealed two-face example illustrates that exact-compatible-minimizer events may have zero probability although the annealed ratio remains bounded. An independent near-flat Gibbs-event or local transport estimate is still necessary.

The historical 37-independent-link Haar count gives a formal \(3m/2=111/2\) polynomial exponent on a fixed block under \(\Delta=0\), but is **not** an ambient-uniform estimate. Neither FG1 nor a partition-ratio estimate implies an interacting transfer-operator spectral gap without a separate theorem.

### Sources

- Historical four-spatial-face/three-step mention: \`Branch · Branch · Compare Continuum Mass Gaps.txt\`, SHA-256 \`b75a371a07e29826432fde37e573cf00f15e130260d889997729083f2fcd8496\`.
- Historical compatible-minimizer sufficient theorem: \`r3_compatibility_theorem_2026-10-28/RESEARCH_NOTE.md\`, SHA-256 \`a315b99ebd1251dec42c0c2dfda9303d9ef0e3868fdca04524150bbef1265399\`.
- Historical annealed counterexample: \`r3_annealed_compatibility_2026-10-28/RESEARCH_NOTE.md\`, SHA-256 \`64a0e82cbc7f7bd36d065c1230effa26c072a2ab6899f15d4bead9a4bb12b8f2\`.

A longer formal proof and source-location report are in the immutable local handoff bundle \`singular_boundary_r3_frustration_gap_2026-10-28.zip\` (SHA-256 \`ec71cc62af4d971419f1e235dded9f6e47b49e70876568ce7eccd72532386a4a\`). The large source import is not yet on GitHub.