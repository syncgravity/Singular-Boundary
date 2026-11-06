# P2 · Gap-independent local Fisher information and nontrivial Wilson marginals in finite cubic SU(2)

**Date:** November 6, 2026 (UTC)  
**Claim level:** source-qualified exact finite-model theorem, with a **volume-uniform** fixed-bare-coupling estimate and thermodynamic subsequential consequences. **NOT** a uniform weak-coupling/continuum Yang–Mills gap theorem, a Penrose construction, or a gravitational UV result. Independent referee-level verification is required before theorem promotion.

## Research question and change relative to previous evidence

The preceding finite Wilson ground-state audit (`R3_FINITE_WILSON_MARGINAL_HARNACK_AND_TWO_SCALE_SUM_RULE_2026-11-06.md`, draft PR #68) gives a true-vacuum pointwise marginal Harnack bound involving the *entire* spatial lattice, `64F/g0^4 + E log(101/99)`. That bound is not uniform in the volume. This note proves a **different kind of local estimate**, independent of the *total* number of cells/links and not dependent on a full interacting spectral gap. Its constant still grows as `g0^-4`, so it does not establish the required asymptotically free continuum limit.

## 1. Precise source model

Let \(\Gamma\) be any finite connected open 3D cubical lattice, with set \(E\) of oriented links and set \(F\) of unit plaquettes. Work on \(L^2(SU(2)^E,d\mu)\) with normalized product Haar measure and its gauge-invariant sector. The full original-link Wilson/Kogut–Susskind Hamiltonian is

\[
H=\alpha\sum_{e\in E} C_e+\beta\sum_{p\in F} (1-\tfrac12\chi_1(U_p)),\qquad
\alpha=\frac{g_0^2}{2h}>0,\quad\beta=\frac2{g_0^2h}>0,
\]

where \(C_e=-\Delta_e\ge0\), \(\chi_1=\mathrm{tr}_{\mathbf 2}\), and every magnetic term belongs to \([0,2\beta]\). The normalized ground state \(\Omega>0\) is unique, smooth, strictly positive and gauge invariant at **each finite lattice** by positivity improvement of the compact elliptic heat semigroup. Write \(\nu=\Omega^2d\mu\). The metric normalization is \(C\chi_n=n(n+2)\chi_n/4\).

**Boundary convention:** open cubical graph, with each plaquette consisting of four *distinct* link variables. No repeated-link quotient faces or periodic one-cell plaquettes are used in the proof. Interior link incidence satisfies \(d(e):=|\{p:e\in\partial p\}|\le4\).

## 2. A local variational link-excision lemma (no mass-gap input)

**Proposition L (exact local interacting-vacuum kinetic bound).** For any subset \(S\subseteq E\) of original elementary links, put \(F(S)=\{p:\partial p\cap S\ne\varnothing\}\). Then

\[
\boxed{\alpha\sum_{e\in S}\int|\nabla_e\Omega|^2d\mu\le\beta|F(S)|.}\tag{L}
\]

In fact the same proof establishes the stronger **local electric–magnetic tradeoff**

\[
\boxed{\alpha\sum_{e\in S}\int|\nabla_e\Omega|^2d\mu
+\beta\sum_{p\in F(S)}\int(1-\chi_1(U_p)/2)\Omega^2d\mu
\le\beta|F(S)|.}\tag{L+}
\]

Equivalently, the local electric energy does not exceed
\(\frac\beta2\sum_{p\in F(S)}\langle\chi_1(U_p)\rangle_\nu\).
This also certifies the **sum** of plaquette-character expectations around each selected link is nonnegative, without asserting that every individual plaquette expectation has a separate positive lower bound.

In particular, for a single link \(e\),

\[
\boxed{\alpha\int|\nabla_e\Omega|^2d\mu\le\beta d(e)\le4\beta.}\tag{L1}
\]

**Proof.** Delete the electric terms \(\alpha C_e\) for \(e\in S\) and all magnetic plaquettes touching \(S\); call the remaining Hamiltonian \(H_{\setminus S}\). It depends only on variables outside \(S\), commutes with the remaining gauge action and has a normalized nonnegative ground state \(\Omega_{\setminus S}\) of energy \(E_{\setminus S}\). Since the reduced Hamiltonian is bounded below by its ground energy,

\[
E_0(H)=\langle\Omega,H\Omega\rangle\ge E_{\setminus S}
   +\alpha\sum_{e\in S}\langle\Omega,C_e\Omega\rangle
   +\sum_{p\in F(S)}\langle\Omega,V_p\Omega\rangle.
\]

Use the normalized trial state \(1_S\otimes\Omega_{\setminus S}\), where \(1_S\) is Haar-constant on the deleted links. It is gauge invariant since the reduced Hamiltonian and its positive ground state are gauge invariant. Its deleted electric expectation is zero. Each omitted fundamental plaquette contains at least one deleted elementary link **exactly once**, so its character has zero Haar mean and its magnetic expectation is precisely \(\beta\). The variational principle gives \(E_0(H)\le E_{\setminus S}+\beta|F(S)|\). Subtract the two inequalities. No bound involving \(E_1-E_0\), the global volume, or the source-response derivative was assumed. QED.

**Scope and strength.** For a single interior edge in a 3D cubic lattice, \(d(e)=4\), independent of the size of the surrounding box. The upper bound is not uniform as \(g_0\to0\); in the stated normalization \(\beta/\alpha=4/g_0^4\).

## 3. The exact physical Wilson-loop marginal inherits local Fisher control

Let \(C\) be any simple oriented loop of distinct original links, of arbitrary length \(L_C\ge4\), including a loop of fixed physical perimeter carried by progressively many elementary links. Define its group-valued ordered holonomy \(X=U_C\in SU(2)\), and let \(\rho_C dU\) be the pushforward of \(\nu\) to \(X\), using Haar measure \(dU\) as reference. Under product Haar the same pushforward is Haar, so

\[
\rho_C(U)=\mathbb E_{\mu}[\Omega^2\mid U_C=U],\qquad
\int\rho_CdU=1,\quad\rho_C>0.
\]

**Proposition F (local Fisher bound).** For **every** edge \(e\) traversed once by \(C\),

\[
\boxed{
\int_{SU(2)}|\nabla\sqrt{\rho_C}|^2dU
\le\int|\nabla_e\Omega|^2d\mu
\le\frac{\beta}{\alpha}d(e).
}\tag{F1}
\]

Consequently, for an open 3D cubical mesh,

\[
\boxed{\int|\nabla\sqrt{\rho_C}|^2dU\le\frac{16}{g_0^4},\qquad
\int \rho_C|\nabla\log\rho_C|^2dU\le\frac{64}{g_0^4}.}\tag{F2}
\]

**Proof.** Fix all original link variables except a selected \(e\in C\). The map \(U_e\mapsto U_C=A U_e^{\pm1}B\) is a normalized Haar-preserving **isometry** of SU(2) for the bi-invariant metric. This gives a smooth, Haar-measure-preserving disintegration \(\mu=dU\,d\lambda(y)\) in which the original ground-state amplitude is a Hilbert-valued function \(U\mapsto\Omega_U\in L^2(d\lambda)\). Since \(\rho_C(U)=\|\Omega_U\|_{L^2(d\lambda)}^2\), the derivative-of-norm inequality gives \(|\nabla\sqrt{\rho_C(U)}|^2\le\|\nabla_U\Omega_U\|_{L^2(d\lambda)}^2\). The latter is the selected original-link gradient square. Integrate in \(U\), use Proposition L and \(\beta/\alpha=4/g_0^4\). This argument uses exactly one original link from the contour, so its constant is **independent of the number \(L_C\) of edges forming the same physical loop**. QED.

The same argument applies to a finite vector \((X_1,\ldots,X_k)\) of **disjoint coarse path products**: select one original edge \(e_i\) from each product, set \(S=\{e_i\}\), and obtain

\[
\sum_{i=1}^k\int_{SU(2)^k}|\nabla_{X_i}\sqrt{\rho_{X_1,\dots,X_k}}|^2
\le \frac\beta\alpha|F(S)|\le\frac{4k\beta}{\alpha}.
\tag{F3}
\]

This includes the eight disjoint physical boundary products used in the preceding cubic P/Q construction. The bound is **local in the retained holonomies** but still not uniform along asymptotically free refinement.

## 4. A nontrivial volume-uniform Wilson variance bound

SU(2), with the bi-invariant Laplacian fixed above and normalized Haar measure, is a fixed compact three-dimensional Riemannian manifold. Let \(C_S\ge1\) denote **any fixed, finite** geometric Sobolev constant satisfying

\[
\|u\|_{L^6(SU(2))}^2\le C_S\bigl(\|\nabla u\|_2^2+\|u\|_2^2\bigr).
\tag{S}
\]

No numerical or sharp value for \(C_S\) is claimed. By (F2), putting
\(K(g_0)=C_S(1+16/g_0^4)\),

\[
\boxed{\|\rho_C\|_{L^3}\le K(g_0).}\tag{V1}
\]

For SU(2) Haar-distributed \(U\), the trace \(W=\chi_1(U)\) has the explicit probability density
\(p_0(w)=\sqrt{4-w^2}/(2\pi)\) on \([-2,2]\), bounded by \(1/\pi\). Given any \(m\in[-2,2]\) and \(r>0\), Hölder gives

\[
\nu_C\{|W-m|\le r\}\le \|\rho_C\|_3
\,\mu\{|W-m|\le r\}^{2/3}
\le K(g_0)(2r/\pi)^{2/3}.
\]

Choose \(m=\mathbb E_{\nu_C}W\) and \(r=\pi/[2(2K(g_0))^{3/2}]\). The probability inside the trace band is at most \(1/2\). Therefore

\[
\boxed{\operatorname{Var}_{\nu_C}(W)
\ge\frac{r^2}{2}=
\frac{\pi^2}{64\,C_S^3\,(1+16/g_0^4)^3}>0.}\tag{V2}
\]

This is **uniform in the volume R and the elementary length L_C** at any fixed positive bare coupling, for a simple physical contour. Unlike the previous global Harnack variance estimate, it does not contain \(E\) or \(F\). It becomes weak as \(g_0\to0\), so it does not demonstrate continuum Wilson nontriviality at asymptotically free scaling.

**Standard external mathematical inputs only:** the compact-manifold Sobolev/Rellich theorems (for example, [MIT 18.155 microlocal analysis notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), §15) and the SU(2) Weyl-integration trace law (e.g. [Sutherland's SU(2) lecture notes](https://swc-math.github.io/aws/2016/2016SutherlandNotes.pdf)). Neither source independently proves Proposition L or F, which are the new finite-model variational deductions here.

## 5. Genuine infinite-volume subsequential consequence at fixed lattice spacing

Hold \(h>0\) and \(g_0(h)>0\) **fixed**, and consider any increasing sequence of finite open cubical boxes containing the same geometrically fixed local loop \(C\). The positive normalized marginals \(\rho_{h,R}(U)\) have the **uniform H¹ bound on their square roots** from (F2), independent of R. By Rellich–Kondrachov compactness on SU(2), after extraction,

\[
\sqrt{\rho_{h,R_j}}\to\sqrt{\rho_{h,\infty}}\text{ strongly in }L^2(SU(2)),\qquad
\rho_{h,R_j}\to\rho_{h,\infty}\text{ strongly in }L^1.
\tag{T1}
\]

The limiting density has mass one and belongs to \(L^3\), with the same (F2)/(V1) bounds. The Wilson trace variance remains at least the strictly positive number (V2). Likewise, the joint coarse-product density in (F3) is precompact in \(L^1(SU(2)^k)\) for every **fixed** k.

For the centered variance-normalized Wilson observable \(f_C=(W-\mathbb EW)/\sqrt{\operatorname{Var}(W)}\), the exact first spectral moment from the previous theorem is

\[
-C'_{h,R}(0)=\alpha L_C
\frac{\mathbb E_{\nu_{h,R}}(1-W^2/4)}{\operatorname{Var}_{\nu_{h,R}}(W)}.
\]

Using the positive lower bound (V2) and \(0\le1-W^2/4\le1\), at fixed h, g0 and contour C,

\[
\boxed{0\le-C'_{h,R}(0)\le
M_{h,C}:=\alpha L_C\frac{64C_S^3(1+16/g_0^4)^3}{\pi^2},}\tag{T2}
\]

uniformly in R. The corresponding **normalized positive spectral measures** \(d\sigma_{h,R}(E)\) obey

\[
\sigma_{h,R}([S,\infty))\le M_{h,C}/S\quad(S>0),
\qquad 1-C_{h,R}(t)\le t M_{h,C}.
\tag{T3}
\]

They are tight and admit weakly convergent **subsequences** as R→∞ at fixed h, with normalized nontrivial local states and locally uniform finite-time correlation limits on compact t intervals. **No uniqueness of the infinite-volume state, no control of the spectral support near zero, no h→0 limit, no nontrivial OS 4D reconstruction and no positive continuum mass gap follows.** A finite first-moment bound is an *ultraviolet tail control*, not a lower spectral-support bound.

## 6. Independent computational checks and limitations

The accompanying independent verifier reconstructs the exact n³ cubic edge/face incidence and link-degree histogram for n∈{1,2,3,4,8,16,32}, checks \(\sum_e d(e)=4F\), and verifies the maximal local degree four. A separate **one-plaquette gauge-invariant SU(2)** Peter–Weyl character rotor (four original links, not a 3D interacting vacuum computation) uses the exact tridiagonal Wilson Hamiltonian in χ_n. For six distinct ratios β/α it tests the one-link variational energy inequality and the exact Wilson spectral first-moment identity with independently diagonalized correlation measures. It also checks the SU(2) Haar trace density and band-mass inequality over 35 cases.

These checks are valuable regression tests and demonstrate coherent Casimir/character conventions. The volume-independent local inequality, Sobolev variance certificate, and R→∞ compactness are proved by the analytic arguments above; no test exhausts the infinite-dimensional or infinite-volume theorem.

## 7. Updated proof dependencies and precise next target

- **Completed finite and volume-uniform-at-fixed-coupling subcriterion:** local interacting link kinetic bound (L) and Wilson-holonomy Fisher bound (F). This removes the entire-volume factor from the previous marginal argument without using the interacting gap.
- **Completed fixed-spacing subsequential subcriterion:** local vacuum marginals and Wilson trace spectral measures have nontrivial, volume-independent compactness at fixed h, g0. Their limits need not be unique.
- **Still OPEN (P2/T2/T3):** establish boundary-local estimates **uniform along the running weak-bare-coupling trajectory g0(h)→0**, for physically smeared/renormalized Wilson observables and the complete time-dependent shorted/Schur form. The current \(g_0^{-4}\) bound blows up; tightness at fixed h is not enough.
- **Still OPEN (P4/P5):** physical-time, dense gauge-invariant infrared spectral exclusion and nontrivial 4D OS reconstruction.
- **Separate and OPEN:** a genuine source-certified refining 3D quasicrystalline SU(2) regulator and the physical gravitational ultraviolet fluctuation operator.

**Do not promote any P0–P5 continuum gate based on this result.** Treat the new result as one rigorous finite-source, thermodynamic *subsequence* lemma at fixed lattice spacing, subject to mathematical review of the local gauge-invariant trial state and conditional Haar disintegration.
