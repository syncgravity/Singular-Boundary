# P2 — Summed physical Gauss sectors and an infinite-strip local Borel germ

**2026-11-04. Exact restricted mathematical results in the corrected original-link finite SU(2) straight-strip model, consistently in the independent-face trace-expansion Peter–Weyl norm.** Full 11 KB analytic report, physical Fourier engine, independent matrix and formal-history verification, logs and SHA-256 manifest are available in the associated archive p2_sum_local_borel_audit_2026-11-04.zip. **Not a physical same-grade theorem or no-go, an interacting infinite-volume vacuum, Borel summability, or a Yang–Mills continuum mass gap.**

## The summed gauge-invariant response: disjoint sectors, not cancellation

For even N, take the balanced residual-Gauss-invariant twirled face-degree-(1,…,1) intertwiner F_N (P-26, coefficient trace norm 1). Let
\[
G_{N,m}=\sum_{j=1}^N[\{j\}]\otimes\chi_m(U_j),\quad m\ge3.
\]
Each inner input is **separately** Gauss-invariant. The corrected physical operator \(K=4\sum_i C_i+2\sum_{i,a}R_i^aL_{i+1}^a\) preserves each output PW degree tuple, and \(Q\) removes only the global Haar constant.

The only degrees after fusion at site j are l=m−1,m+1, with all other faces remaining degree one. Since m≥3, l≠1. Hence the 2N sector tuples are **pairwise distinct**. Their trace-nuclear norms add exactly even after applying the complete physical inverse. With the anchored history norm L^(r), any κ>0, σ≥0 and integer r≥0,
\[
\boxed{
\frac{\|\mathcal B_{\rm hist}(F_N,G_{N,m})\|_{L^{(r)}}}
{\|F_N\|_{L^{(r)}}\|G_{N,m}\|_{L^{(r)}}}
=e^{-\kappa}\sum_{j=1}^N
\frac{P_\sigma^{(r)}(\mathcal B(F_N,\chi_m(U_j)))}
{P_\sigma^{(r)}(F_N)P_\sigma^{(r)}(\chi_m)}.
}\tag{1}
\]
There is **no cancellation across insertion positions** in this particular norm. The case m=2 is excluded because its l=1 output coincides with untouched spectator degree one and may collide across sites.

### Spectator-energy improvement

Every output retains N−1 spectator degree-one faces: \(D_{\rm out}=3(N-1)+l(l+2)\ge3N+m^2-4\). The true original-link coefficient inverse satisfies \(\|K^{-1}_{\rm out}\|_{1\to1}\le2/D_{\rm out}\); the direct fixed-face source collar costs at most \(9m/2\) times the input projective norms. SU(2) CG pinching and exponential/max-spin weights are submultiplicative. Therefore
\[
\boxed{
\frac{\|\mathcal B_{\rm hist}(F_N,G_{N,m})\|_{L^{(r)}}}
{\|F_N\|_{L^{(r)}}\|G_{N,m}\|_{L^{(r)}}}
\le e^{-\kappa}\frac{9Nm}{3N+m^2-4}.
}\tag{2}
\]
This is sharper than the previously established single-pair \(9m/(m^2-1)\), but grows like \(9e^{-\kappa}m/4\) along N∼m². **An upper bound permitting divergence proves neither divergence nor boundedness.** A true physical no-go needs a *lower* bound along N∼m², while physical same-grade closure needs an independent uniform upper bound.

Complete summed physical Fourier output norms, at σ=0, grade r=1, **before** the history factor e^(−κ):

| Even width N | inner degree m=3 | m=4 |
|---|---:|---:|
| 2 | 0.072390969229 | 0.061258095150 |
| 4 | 0.129125009532 | 0.116983327351 |

The independent verifier reuses the exact previously audited Gauss-twirl, full left/right original-link superoperator and CG inverse and recomputes every nonconstant output block. These finite widths do not test large-N asymptotics.

## Formal thermodynamic-limit stabilization and analytic local Borel germ

For any finite face interval Λ, the history-labelled formal fundamental-source score is \(S_\Lambda(\lambda)=\lambda A_\Lambda+\mathcal B_{\rm hist}(S_\Lambda,S_\Lambda)\), with \(A_\Lambda=\sum_{j\in\Lambda}[\{j\}]\chi_1(U_j)/6\).

In the corrected face-coordinate electric operator, zero spectator degrees are preserved, and mixed link terms vanish when one adjacent face degree is zero. Thus enlarging Λ **does not change the operator on a fixed nonconstant degree sector supported inside a history I**. As an output carries the exact union-history label, its coefficient on history I depends solely on source leaves inside I. By induction on source order n,
\[
\boxed{S_{\Lambda,n,I}=S_{\Lambda',n,I}\quad\text{for all }\Lambda,\Lambda'\supseteq I.}\tag{3}
\]
At order n, |I|≤n and the maximum face representation degree is ≤n. Define an infinite bilateral straight-row history coefficient \(S_{\infty,n,I}\) using (3). There are only finitely many possible length≤n histories containing a fixed anchor; the infinite-row anchored norm is well-defined and the history-family space is complete.

The previously **directly proved graded** finite-strip tame estimate (P-23) and source-order degree cap (P-25) give an infinite-row uniform bound
\[
\boxed{\|S_{\infty,n}\|_{L^{(1)}}\le M^nK_*^{n-1}(n-1)!,\quad
M=\tfrac43e^{\kappa+\sigma},\quad K_*=4(C_{\rm same}/2+48e^{-\kappa}).}\tag{4}
\]
Hence the **formal** infinite-strip Borel series \(\widehat S_\infty(\xi)=\sum_{n\ge1}S_{\infty,n}\xi^n/n!\) converges in L^(1) and L^(2) whenever |ξ|<1/(MK_*), including \(|\xi|<9e^{-\sigma}/5120\) at κ=log4. With z=MK_*|ξ|<1,
\[
\boxed{\|\widehat S_\infty(\xi)\|_{L^{(1)}}\le-\log(1-z)/K_*,\quad
\|\widehat S_\infty(\xi)\|_{L^{(2)}}\le[z/(1-z)-\log(1-z)]/K_*.}\tag{5}
\]
The graded bilinear map justifies the **actual analytic identity** within this local disk:
\[
\boxed{\widehat S_\infty(\xi)=\xi A_\infty+
\frac{d}{d\xi}\int_0^\xi
\mathcal B_{\rm hist}(\widehat S_\infty(\eta),\widehat S_\infty(\xi-\eta))\,d\eta.}\tag{6}
\]
This is an infinite-row *formal-coefficient Borel germ*, not a nonperturbative interacting vacuum.

### Global anchored-norm truncations do not converge

Embed each finite Λ family by zero on histories outside Λ. Adding one site j changes the first-order source by a singleton component with fixed anchored norm:
\[
\boxed{\|A_{\Lambda\cup\{j\}}-A_\Lambda\|_{L^{(1)}_{\kappa,\sigma}}=\tfrac43e^{\kappa+\sigma}.}\tag{7}
\]
Thus these finite-volume sequences are not Cauchy in the **global sup-anchor norm**. The infinite-family construction uses exact **historywise stabilization plus uniform bounds**, not global-norm convergence of volume truncations. It makes no claim about a thermodynamic-limit physical measure or Borel continuation along a Laplace ray.

## Independent verification and next obligations

The companion integrity-tested ZIP contains a **self-contained physical Fourier engine**, the summed-response script, execution log and verified SHA-256 manifest. The matrix script checks four complete sums, output-sector noncollision and physical inverse residuals. A separate support-tree counter (explicitly *not* SU(2) amplitude simulation) verifies history-local stabilization to order six. Exact-rational bounds and degree/order inequalities are checked through order 120.

**Next physical gate:** prove a matching uniform lower or upper bound on the complete response (1) for N=m²+O(1), using total-spin recoupling or tensor-network transfer methods instead of dense 2^N matrices. **Next Borel gate:** extend the *actual infinite-row local germ* (6) along a ray with uniform growth control; local analyticity cannot be promoted to Borel summability by assumption. No interacting λ=1, OS, continuum or mass-gap conclusion follows.