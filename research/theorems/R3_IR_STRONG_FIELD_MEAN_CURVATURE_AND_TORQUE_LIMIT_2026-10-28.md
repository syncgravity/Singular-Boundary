# R3-IR — A volume-uniform mean-curvature estimate and a sharp limitation for connector torques

**Date:** 2026-10-28. **Research status:** new exact variational inequalities for finite SU(2) Wilson Hamiltonians; the nonlinear *local* transport-torque expectation and uniform interacting physical gap remain **OPEN**. Only read-only exact/symbolic calculations. No simulation or historical artifact was altered.

## 1. Origin and conventions

This follows `research/theorems/R3_IR_NONLINEAR_COLLECTIVE_DIRICHLET_2026-10-28.md`. It tests whether that report's pure-connector identity

\[
|\nabla_e\mathcal Q_v|^2=64|S_{A_e}\times S_{\bar A_e}|^2
\]

can be controlled by a *newly established* estimate on the actual interacting vacuum, without assuming clustering, a Poincaré inequality or a mass gap.

Let \(G=(V,E,F)\) be a finite oriented SU(2) spatial face complex, every face consisting of **four distinct edges**, every edge incident to at least one face (decoupled dangling edges can be treated separately), with \(a_e>0,b_f\ge0\). Write

\[
H_G=\sum_e a_e(-\Delta_e)+\sum_fb_fd_f,\qquad
p(U)=\tfrac12\operatorname{ReTr}U,\quad d_f=1-p(W_f),
\]

on \(L^2(SU(2)^E)\); \(-\Delta p=3p/4\). The unique positive normalized ground state \(\Omega_G\) is gauge invariant. \(d\nu_G=\Omega_G^2dU\) therefore computes **physical** gauge-invariant vacuum expectations, although the variational test function below is defined on the *full* link Hilbert space and need not be gauge invariant. Put \(A=\sum_ea_e\), \(B=\sum_fb_f\).

## 2. Theorem MC-1 — global strong-field trial estimate (independently proved)

For every such finite complex,

\[
\boxed{0\le E_0(G)\le \min\left\{B,\;\frac3{\sqrt2}\sqrt{AB}\right\},\qquad
\boxed{\sum_fb_f\,\mathbb E_{\nu_G}d_f\le E_0(G)\le\frac3{\sqrt2}\sqrt{AB}.}
\]

### Proof (including the trial-state constants)

On one SU(2) link, set \(\psi_\kappa(U)=Z_\kappa^{-1/2}e^{\kappa p(U)}\), \(Z_\kappa=\int e^{2\kappa p(U)}dU\), \(\kappa>0\). Write \(r_\kappa=\int p|\psi_\kappa|^2dU\). The density of \(y=1-p(U)\in[0,2]\) is proportional to

\[
y^{1/2}\sqrt{2-y}\,e^{-2\kappa y}\,dy.
\]

Compare with a Gamma(shape \(3/2\), rate \(2\kappa\)) variable \(Y\). Conditioning \(Y\le2\) can only lower its expectation, and reweighting this conditional law by the decreasing factor \(\sqrt{2-y}\) lowers the expectation again (the negative covariance of an increasing and decreasing function). Consequently

\[
\boxed{0\le1-r_\kappa=\mathbb E_{\psi_\kappa^2}y\le\frac3{4\kappa}.}
\]

The normalized Laplacian and integration by parts give the **exact** one-link kinetic energy

\[
\int|\nabla\psi_\kappa|^2dU=\kappa^2\mathbb E|\nabla p|^2
=\frac{3\kappa}{8}r_\kappa\le\frac{3\kappa}{8}.
\]

The one-link distribution is central, so \(\mathbb E_{\psi_\kappa^2}U=r_\kappa I\) and \(\mathbb E U^{-1}=r_\kappa I\). With the tensor-product trial \(\Psi_\kappa(U)=\prod_e\psi_\kappa(U_e)\), every simple oriented four-link face satisfies \(\mathbb E p(W_f)=r_\kappa^4\). Because \(r_\kappa\in[0,1]\),

\[
\langle\Psi_\kappa,H_G\Psi_\kappa\rangle
=\frac{3\kappa r_\kappa}{8}A+(1-r_\kappa^4)B
\le\frac{3\kappa}{8}A+\frac3\kappa B.
\]

Optimize at \(\kappa=\sqrt{8B/A}\) to obtain \(E_0\le(3/\sqrt2)\sqrt{AB}\). The constant trial state also gives \(E_0\le B\). The actual ground-state electric and magnetic energies are nonnegative, so \(\sum_fb_f\mathbb E_{\nu_G}d_f\le E_0\). This establishes both claims, without a coupling smallness condition or any assumed vacuum mixing. \(B=0\) follows directly by the constant vacuum. QED.

## 3. Corollary MC-2 — a uniform strong-field *density* of nearly flat faces

If all electric coefficients are \(a_e=a>0\) and all magnetic coefficients are \(b_f=b>0\), then

\[
\frac1{|F|}\sum_f\mathbb E_{\nu_G}d_f
\le\frac3{\sqrt2}\sqrt{\frac{a|E|}{b|F|}}.
\]

Since all edges belong to a face and each quadrilateral has four edges, \(|E|\le4|F|\), hence

\[
\boxed{\mathbb E_{\nu_G}\Big[\frac1{|F|}\sum_fd_f\Big]
\le3\sqrt2\sqrt{a/b},}
\]

**uniformly in the size and topology of the face complex** (provided all faces have four distinct edges). Markov's inequality also gives, for any \(\delta>0\),

\[
\nu_G\left\{U:\frac1{|F|}\sum_fd_f\ge\delta\right\}
\le\frac{3\sqrt2}{\delta}\sqrt{a/b}.
\]

For the **specified dual-area** Penrose trajectory (not source-certified as every Stage-26 coefficient), let \(h\) be the physical edge length,

\[
 a_e=\frac{g_3^2}{2w_e},\qquad
 b_f=\frac4{g_3^2h^2\sigma_f},\qquad
\sigma_f\in\{\sin(\pi/5),\sin(2\pi/5)\},\quad
\varphi=\frac{1+\sqrt5}{2}.
\]

With the one-sided boundary dual-area rule \(w_e\in[\sigma_-/2,\sigma_+]\), one has \(a_e\le g_3^2/\sigma_-\), \(b_{\max}=4/(g_3^2h^2\sigma_-)\), \(b_{\min}=4/(g_3^2h^2\sigma_+)\). Substituting these and \(|E|\le4|F|\) into MC-1 yields

\[
\boxed{\mathbb E_{\nu_{h,G}}\Big[\frac1{|F|}\sum_fd_f\Big]
\le\frac{3\varphi}{\sqrt2}\,g_3^2 h.}\tag{MC2-P}
\]

The bound holds **uniformly over finite admissible face patches** along this specified trajectory. It shows vacuum plaquette curvature is small *on average in face density*, as \(g_3^2 h\to0\). It does **not** show fixed-face curvature is small uniformly, bound long Wilson transport, show quantum continuum measure convergence, or prove a spectral mass gap. In particular, \(\sum_fd_f\) may still be extensive.

## 4. Theorem MC-3 — pointwise no-go for converting mean curvature into a local torque bound

Consider a simply connected planar rhombus disk with \(|F|\to\infty\), containing the three-face Penrose seed of the preceding connector audit. Fix two selected faces separated by a *pure connector* tree edge \(e\); extend the graph and rooted tree while keeping this witness. Choose their two based holonomies as \(i\sigma_x\) and \(i\sigma_y\), and set every other based face holonomy to \(I\). Such assignments are realizable because the oriented face holonomies give independent coordinates in a simply connected disk after tree gauge fixing. For normalized source weights \(v_1=v_2=1/\sqrt2\), the exact pure-connector identity gives

\[
|S_{A_e}\times S_{\bar A_e}|^2=\frac14,\qquad
\boxed{|\nabla_e\mathcal Q_v|^2=16,}\qquad
\boxed{\frac1{|F|}\sum_fd_f=\frac2{|F|}.}
\]

Therefore their ratio is \(8|F|\), and **no** constant independent of disk size can satisfy

\[
|\nabla_e\mathcal Q_v|^2\le C\left(|F|^{-1}\sum_fd_f\right)
\]

*pointwise for every gauge configuration*. This does **not** disprove an interacting Gibbs/ground-state **expected** torque estimate; it proves the new global mean-curvature estimate MC-2 alone cannot imply such a bound by pointwise absorption. The positive physical ground-state density may strongly suppress the specific exceptional configuration.

## 5. Consequences for the spectral proof ledger

- **Independently proved:** MC-1 global physical-vacuum energy and weighted curvature bound by a non-gauge-invariant variational trial; MC-2 average strong-magnetic curvature bound, including the specified Penrose scaling; MC-3 exact pointwise connector-torque non-absorption by global mean curvature.
- **Still open:** face-local curvature moment bounds; nonabelian pair/fourth-order joint ground-state moments; a path-local or tree-independent transport inequality; source variance lower bounds; all-scale interacting physical spectral gap and R2 continuum reconstruction.
- **Next noncircular lemma:** find a **localized** ground-state estimate for a fixed plaquette or finite face region with constants independent of the ambient patch, and then a **joint curvature/transport bound** compatible with the ND-1 connector torque. A global average alone is now proved insufficient; if no such estimate holds, preserve the obstruction and consider more local gauge-covariant source constructions.

## 6. Integrity and verification

`verify_variational_curvature.py` checks the optimized trial constants, the geometric coefficient envelope, the 3-seed canonical incidence count, and the pointwise torque/average ratio with exact symbolic arithmetic. It performs **no Monte Carlo**, no numerical fit, no historical source regeneration. All historical source artifacts remain immutable. The three canonical rhombi are only a finite spatial fixture, not the full R3-PRISM Q14 temporal cavity.