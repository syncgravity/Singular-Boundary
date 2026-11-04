# P2: corrected extremal-spin obstruction and a volume-uniform local Borel germ

**2026-11-04.** Corrected original-link SU(2) on finite open straight square strips, in a *single face-coordinate* dimension-weighted trace-expansion Peter–Weyl nuclear norm. Two separate mathematical results: (A) a **genuine same-spin-grade counterexample on the full coefficient-matrix algebra**, not gauge-invariant; (B) a **volume-uniform Gevrey-1 / analytic local Borel-transform theorem for the formal gauge-invariant fundamental-source score**, contingent on the direct graded inequality established in the preceding P2 audit. Neither result constructs an interacting vacuum, proves Borel summability, a lattice spectral gap at physical coupling, OS reconstruction, or a 4D Yang–Mills mass gap. Complete expanded report, two independent executed scripts, logs and SHA-256 manifest are archived in conversation artifact **p2_extremal_counterexample_and_local_borel_2026-11-04.zip**.

## A. Corrected physical superoperator and the same-grade obstruction

The corrected original-link face-coordinate operator is \(K=4\sum_i C_i+2\sum_{i,a}R_i^aL_{i+1}^a\), with \(e_n=n(n+2)\) and Fourier cross-link superoperators \(\mathscr D_{i,i+1}(X)=-\sum_aJ_{n_i}^a XJ_{n_{i+1}}^a\). Use the **noncentral**, non-gauge-invariant SU(2) matrix coefficient \(u(U)=U_{21}\). The degree-n coefficient \(u^n\) has trace-expansion rank-one matrix \(|+\rangle\langle-|\), nuclear norm 1. On tensor products of this extremal orientation, the transverse spin-ladder terms **vanish**, giving the exact *actual-superoperator* eigenvalue
\[
\mathscr D_{i,i+1}(X)=\tfrac14 n_i n_{i+1}X,\quad
\boxed{E(\mathbf n)=\sum_i n_i(n_i+2)+\tfrac12\sum_i n_i n_{i+1}.}
\]
**Correction to a rejected preliminary calculation:** the tempting product of \(U_{11}\) coefficients is *not* an eigenfunction of the corrected shared-link superoperator; its transverse action generates another Fourier coefficient. Only the explicitly tested \(U_{21}\) extremal orientation is used here.

For outer history \(I=[1,N]\), set
\[
F_N=[I]\otimes\prod_{i=1}^N u(U_i),\qquad
G_{N,m}=\sum_{j=1}^N[\{j\}]\otimes u(U_j)^m.
\]
\(F_N\) is an electric eigenfunction with \(E_F=(7N-1)/2\), and each inner singleton has energy \(m(m+2)\). The exact product after insertion at any interior site j is an eigenfunction of energy \(E_F+m^2+5m\), while at either endpoint its energy is \(E_F+m^2+9m/2\). The *complete original-link* carré du champ therefore has scalar coefficient \(-3m/2\) at an interior site and \(-5m/4\) at an endpoint. The source and response are nonconstant in every channel, and Q does not remove them. Their outputs have distinct face-degree multisectors and all retain union history I.

For \(\kappa>0,\sigma\ge0\), integer spin grade r≥0, use
\[
P_\sigma^{(r)}(f)=\sum_{\mathbf n}\big[\prod_i(n_i+1)\big]e^{\sigma\sum_i n_i}(1+\max_i n_i)^r\|A_{\mathbf n}\|_{S_1},\quad
\|F\|_{L^{(r)}}=\sup_x\sum_{I\ni x}e^{\kappa|I|}P_\sigma^{(r)}(f_I).
\]
Here \(\|F_N\|_{L^{(r)}}=2^{N+r}e^{\kappa N+\sigma N}\), \(\|G_{N,m}\|_{L^{(r)}}=(m+1)^{r+1}e^{\kappa+\sigma m}\), and each output Fourier block has dimension \(2^{N-1}(m+2)\), nuclear coefficient norm one before the inverse multiplier and moment \((m+2)^r\). Thus the **exact** normalized bilinear ratio is
\[
\boxed{\begin{aligned}
\mathfrak R^{(r)}_{N,m}
=e^{-\kappa}\left[\frac{m+2}{2(m+1)}\right]^{r+1}
\left[\frac{3m(N-2)}{7N-1+2m^2+10m}
+\frac{5m}{7N-1+2m^2+9m}\right].
\end{aligned}}\tag{A}
\]
The PW analytic-radius factor cancels *exactly* (no loss in \(\sigma\)). Taking \(N=m^2+2\):
\[
\boxed{\lim_{m\to\infty}\frac{e^\kappa\mathfrak R^{(r)}_{m^2+2,m}}m
=\frac1{6\cdot2^r}>0.}\tag{B}
\]
In particular \(\mathfrak R^{(1)}\sim e^{-\kappa}m/12\). Consequently, **no all-history same-grade \(L^{(r)}\times L^{(r)}\to L^{(r)}\) boundedness** holds for the *full face-coordinate matrix-coefficient algebra* at any fixed finite r. This directly establishes that a spin-moment loss is not just an artifact of the previous **matrix-space** Casimir split.

**Critical physical boundary:** \(U_{21}\) is not invariant under residual simultaneous gauge conjugation. This theorem **does not** disprove same-grade boundedness on the **physical Gauss-invariant intertwiner subspace**; that problem remains open. No original-link/face norm equivalence is used.

## B. Exact source-order spin cap for the gauge-invariant fundamental score

Use the formal score equation from \`R3_IR_SOURCE_MULTIGRADING_LINKED_HISTORY_2026-11-03.md\`:
\[
S(\lambda)=\lambda A+\mathcal B_{\rm hist}(S(\lambda),S(\lambda)),\quad
A=-K^{-1}QV,\qquad V=-\tfrac12\sum_{j}\chi_1(U_j).
\]
Because \(K\chi_1(U_j)=3\chi_1(U_j)\),
\[
A=\sum_j[\{j\}]\otimes\chi_1(U_j)/6,\qquad
\boxed{M=\|A\|_{L^{(1)}_{\kappa,\sigma}}=\tfrac43e^{\kappa+\sigma}.}
\]
The factor comes from trace-expansion \(d_1\|I_2\|_1=4\), first moment 2 and coefficient 1/6. This **anchored** source norm is independent of the number of plaquettes.

Expand \(S(\lambda)=\sum_{n\ge1}\lambda^nS_n\) by the *formal* quadratic recursion. At each fundamental source leaf, the degree is one on exactly one face; \(K^{-1}Q\) preserves face-degree multisectors, and every SU(2) Clebsch–Gordan output satisfies \(c_i\le a_i+b_i\). Hence **each formal order n**, including histories with disconnected minimal spin support, has \(\max_i c_i\le n\). Therefore
\[
\boxed{\|S_n\|_{L^{(2)}}\le(n+1)\|S_n\|_{L^{(1)}}.}\tag{C}
\]
This source-order cap is a selection-rule induction, not an unverified extra hypothesis.

## C. Volume-uniform Gevrey-1 and local Borel-transform analyticity

Invoke the **directly proved** all-history graded inequality in \`research/audits/DIRECT_FACE_NESTED_CASIMIR_CLOSURE_2026-11-04.md\` (in the same face PW norm):
\[
\|\mathcal B(F,G)\|_{L^{(1)}}\le C\|F\|_1\|G\|_1+
24t(\|F\|_1\|G\|_2+\|F\|_2\|G\|_1),
\]
where \(t=e^{-\kappa}\), \(H_\kappa=\sup_{m\ge1}(2+6m)e^{-\kappa m/2}\), \(C=8/(1-t)+24t/(1-t)^2+4\sqrt t H_\kappa\). With \(a_n=\|S_n\|_{L^{(1)}}\), (C) and the formal recursion imply
\[
a_1=M,\qquad
a_n\le[C+24t(n+2)]\sum_{i=1}^{n-1}a_i a_{n-i}.
\]
Put \(D=C/2+48t\), \(K_*=4D\). For every n≥2, \(C+24t(n+2)\le Dn\). The elementary factorial convolution
\[
n\sum_{i=1}^{n-1}(i-1)!(n-i-1)!\le4(n-1)!
\]
holds by reciprocal-binomial counting (for n≥4, the sum of reciprocal binomials is ≤3, and n/(n−1)≤4/3; n=2,3 direct). Induction proves **for all formal orders and all finite strip sizes**:
\[
\boxed{\|S_n\|_{L^{(1)}}\le M^nK_*^{n-1}(n-1)!.}\tag{D}
\]

Thus the **first Borel transform** \(\widehat S(\xi)=\sum_{n\ge1}S_n\xi^n/n!\) **actually converges as an \(L^{(1)}\)-valued analytic germ**, uniformly over finite strip lengths, whenever
\[
\boxed{|\xi|<(MK_*)^{-1}.}\tag{E}
\]
Indeed \(\|\widehat S(\xi)\|_{L^{(1)}}\le-K_*^{-1}\log(1-MK_*|\xi|)\). At the explicit history exponent \(\kappa=\log4\), \(t=1/4\), \(H_\kappa=4\), \(C=88/3\), \(24t=6\), \(D=80/3\), \(K_*=320/3\), \(M=(16/3)e^\sigma\), so
\[
\boxed{R_{\rm Borel}\ge\frac9{5120}e^{-\sigma}.}\tag{F}
\]

**Precise limits:** (D) and (E) concern the **formal source-generated coefficients** and the **local Borel germ**. They do **not** show analytic continuation along any Laplace ray, suitable large-\(\xi\) bounds, Borel summability, that a Borel sum equals a positive interacting vacuum at \(\lambda=1\), a positive interacting spectral gap, three-dimensional regulator transport, OS axioms, or the continuum Yang–Mills mass gap.

## Exact verification and next research targets

Companion ZIP contains \`verify_physical_extremal.py\`: explicit Pauli-spin **physical shared-link** matrix superoperators, lengths 2–5, inner degrees 1–4, and exact-rational ratios through m=200. \`verify_source_graded_gevrey.py\`: 248 factorial convolution checks, 119 exact graded majorant orders through n=120, and 1,521 CG spin caps. Both completed successfully. SHA-256 and ZIP integrity are checked.

**Next:** determine whether a *gauge-invariant* extremal/intertwiner construction retains the linear high-spin obstruction; separately investigate Borel-transform analytic continuation, growth, and potential Stokes behavior, instead of confusing a local germ with a Borel sum.