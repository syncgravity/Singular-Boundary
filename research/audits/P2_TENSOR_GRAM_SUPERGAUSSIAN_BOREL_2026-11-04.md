# P2 — Exact tensor-Gram physical Poisson reduction and super-Gaussian Banach-entire Borel continuation

**2026-11-04.** Two rigorous **restricted** results for the corrected original-link finite open straight SU(2) strip in one fixed independent-face trace-expansion Peter–Weyl norm. **Full derivation, executable physical Fourier engine and two regression scripts, execution logs and SHA-256-checked archive:** \`p2_tensor_gram_supergaussian_borel_2026-11-04.zip\` in the research conversation. This is **not** a computed large-width physical Schatten asymptotic, physical same-grade theorem, Borel summability, interacting vacuum, or four-dimensional continuum Yang–Mills mass gap.

## A. Polynomial-rank Gram formula for every fixed-depth physical gauge-invariant response

For even outer width N and inner spin degree m≥3, take the true residual-Gauss-invariant balanced coefficient F_N and separately invariant χ_m(U_j). Its output face degrees are c_j=l∈{m−1,m+1}, c_i=1 elsewhere, with corrected physical K_c=D_c Id+H_c, D_c=3(N−1)+l(l+2), H_c(X)=−2Σ_{i,a}J_i^a XJ_{i+1}^a. The global Haar mode Q does not remove these nonconstant sectors.

Let P_{j,l} denote product with χ_m followed by local SU(2) CG isometric projection, H_{j,l}=P_{j,l}(F_N⊗I_{m+1}), and B_i(X)=Σ_a J_i^aXJ_{i+1}^a. The **exact physical Poisson source** is
\[
\boxed{Y_{j,l}=\frac{3+m(m+2)-l(l+2)}2H_{j,l}
+\sum_{i\in\{j-1,j\}\cap[1,N-1]}
[B_i(H_{j,l})-P_{j,l}(B_i(F_N)\otimes I_{m+1})].}\tag{A1}
\]
Proof: the polarization identity gives the scalar (3N+m(m+2)−D_c)/2, plus mixed-link actions on every bond. For each bond not touching j, the local CG projection commutes with B_i, cancelling the two mixed-link terms **exactly**. Thus the source requires only its immediate two-bond collar. In (A1) distinguish B_i acting in the outer input representation from B_i acting in the fused output.

P-34 supplies an exact Haar product-rank cubature for F_N with K_N=ceil((N+1)/2)(2N+1)^2 rank-one tensor terms. The inner character has m+1 basis terms; each product/CG projection maps rank-one tensors to rank-one tensors. Each B_i generates three rank-one tensor terms. Equation (A1) thus has ≤13(m+1)K_N terms. The q-th original-link Neumann approximation D_c^(-1)Σ_{p=0}^q(−H_c/D_c)^pY, with H_c acting by at most 3(N−1) rank-one term expansions, has an **exact** factorization \(\sum_{\nu=1}^{r}u_\nu v_\nu^\dagger\), all u,v tensor products, with
\[
\boxed{r\le13(m+1)\Big\lceil\frac{N+1}{2}\Big\rceil(2N+1)^2\sum_{p=0}^q[3(N-1)]^p.}\tag{A2}
\]
For U=[u_ν], V=[v_ν], let A=U†U, B=V†V. **Exact nuclear norm Gram identity**
\[
\boxed{\|UV^\dagger\|_{S_1}=\operatorname{tr}\sqrt{A^{1/2}BA^{1/2}},\quad
A_{\nu\mu}=\prod_i\langle u_{\nu,i},u_{\mu,i}\rangle,\
B_{\nu\mu}=\prod_i\langle v_{\nu,i},v_{\mu,i}\rangle.}\tag{A3}
\]
Coefficients are absorbed into U columns. Thus a *fixed* q and a fixed output sector admit polynomial-sized Gram matrices rather than dense Fourier matrices of dimension 2^(N−1)(l+1). Over all 2N disjoint output sectors this remains polynomial-sized at fixed q. This is an **algebraic-operation/rank reduction**, not a certified finite-precision or polynomial-bit-complexity trace-norm solver. For an O(1) absolute response-error target as m→∞ with N≈m², q=O(log m) may be needed, and the naive Gram dimension is then quasi-polynomial; for an O(m) *relative-scale* comparison fixed q may suffice if a strict lower/upper asymptotic margin can be proved.

The previous analytic Neumann bracket for the **full physical response** remains valid:
\[
|R_{N,m}-R_{N,m,[q]}|
\le\frac{9Nm}{2(3N+m^2-4)}
\frac{\alpha_{N,m}^{q+1}}{1-\alpha_{N,m}},\quad
0\le\alpha_{N,m}\le\tfrac12.
\]
**This archive does not evaluate R_[q] in the N≈m² regime or give a physical same-grade conclusion.**

## B. Banach-entire formal Borel map with super-Gaussian history weights

P-31 proved exact historywise stabilization of the infinite-row *formal magnetic-source score*, P-33 proved each fixed-history Borel component entire, and P-37 supplied its explicit bound. On the bilateral infinite row, fix κ>0, σ≥0, a>0 and define the **super-Gaussian anchored history Banach norm**
\[
\boxed{\|F\|_{a,3;\kappa,\sigma}
=\sup_x\sum_{I\ni x}e^{\kappa |I|-a|I|^3}P_\sigma^{(1)}(f_I).}\tag{B1}
\]
The space is weaker on long histories than the original anchored L^(1) but stronger than the fixed-history product Fréchet topology. For each fixed history I of length L, the actual formal Borel component satisfies
\[
P_\sigma^{(1)}(\widehat S_{\infty,I}(\xi))
\le\frac{e^{B_L|\xi|}-1}{4(2+6L)},\quad
B_L=\frac{16}3e^\sigma L(2+6L)
\le b_\sigma L^2,\quad b_\sigma=\frac{128}3e^\sigma.
\]
Exactly L history intervals of length L contain any fixed anchor. Therefore
\[
\boxed{\|\widehat S_\infty(\xi)\|_{a,3;\kappa,\sigma}
\le\sum_{L\ge1}\frac{L\,e^{\kappa L-aL^3}}{4(2+6L)}
(e^{B_L|\xi|}-1)<\infty\quad(\xi\in\mathbb C).}\tag{B2}
\]
The sum converges uniformly for ξ in compact sets, yielding an **entire Banach-valued** map. The inequality
\(b_\sigma R L^2-aL^3\le-aL^3/2+16b_\sigma^3R^3/(27a^2)\) yields an explicit entire-growth order ≤3 majorant:
\[
\boxed{\|\widehat S_\infty(\xi)\|_{a,3;\kappa,\sigma}
\le\frac14\exp\!\left(\frac{16b_\sigma^3|\xi|^3}{27a^2}\right)
\sum_{L\ge1}\frac{L}{2+6L}e^{\kappa L-aL^3/2}.}\tag{B3}
\]
The actual differentiated Borel–Volterra identity continues to hold **on each history coordinate**, and the matched components belong to (B1). We **do not assume or prove** that the nonlinear history Poisson map is continuous as a bilinear map on this weaker Banach norm, or that its convolution is automatically a Bochner integral in (B1).

**Interpretation:** This strengthens the old merely Fréchet-entire continuation to an explicit Banach-space entire map, but at the cost of **super-Gaussian suppression of long histories**. The order-three growth majorant is far too large to prove positive-ray Laplace integrability; the global *original* anchored norm, a positive interacting vacuum and continuum mass gap remain unresolved. Embedded finite volumes still fail to converge in the global sup-anchor norm already at order one because newly added singleton sources remain a fixed positive distance apart.

## Independent regression

Full self-contained physical Fourier and tensor-Gram script: six small N=2 coefficient-output sectors (m=3/4, both positions), plus N=4,m=3 interior sector outputs; source/Gram checks reproduce the actual corrected physical output to ≈10⁻¹⁵, test 40-term local-overlap Gram nuclear reconstruction with differences <10⁻⁹, and verify q=1 Neumann tensor factorization at N=2,m=3. The separate Borel checker passed 5,000 exact Catalan bounds, 1,000 exact-form window inequalities, 132 Young-inequality tests, and a finite weighted sum comparison. Full logs and SHA-256 checked ZIP are in the companion archive. Finite tests validate the implementations; the displayed identities and estimates are proven analytically.

**Next:** stable/interval-certified Gram trace-norm evaluation or a valid trace-class dual certificate for N≈m², and a stronger analytic continuation/growth theorem in **physically sufficient** anchored weights rather than suppressing long histories.
