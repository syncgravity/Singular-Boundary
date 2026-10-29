# The Singular Boundary — Local heat-kernel Harnack and deleted-face center-ball lower bound

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction. **Scope:** exact finite, interacting, gauge-invariant SU(2) Wilson ground-state theorem on arbitrary finite edge-to-edge rhombus disks, including fully cycle-surrounded interior faces. The bound is uniform in the number of other faces but is **exponentially weaker** than the polynomial small-ball lower bound necessary for the prior bulk deletion program. A separate SU(2) rotor countermodel proves that this weakness cannot be repaired using only the local potential's sup norm, ground-state positivity, and center symmetry. **OPEN:** full nonlinear bulk deletion scaling, Penrose small-ball polynomial bound, fixed-support Wilson–angle covariance, physical mass gap, quartic resolvent and continuum reconstruction.

## I. Setup, normalizations and exact heat kernel

Let \(G=SU(2)\), with normalized Haar probability measure and the bi-invariant Laplace–Beltrami generator normalized so \(-\Delta\chi_j=j(j+1)\chi_j\). On the complete edge Hilbert space \(L^2(G^{E_h})\), consider

\[
 H_h^{(-f)}=\sum_{e\in E_h}a_e(-\Delta_e)+\sum_{g\in F_h\setminus\{f\}}b_gd_g,
 \qquad d_g=1-\tfrac12\operatorname{ReTr}W_g\in[0,2],\quad a_e,b_g>0.
\]

The unique strictly positive normalized ground-state wavefunction \(\Omega_f^-\) is Gauss invariant. It is understood as a positive function on the *full* product-link space; the heat semigroup and its individual factors may act on the unreduced space, but the resulting ground-state observable bounds hold for the physical vacuum.

For an edge \(e\), split the Hamiltonian as \(H^{(-f)}=T_e+H_{\neg e}+V_e\), where \(T_e=a_e(-\Delta_e)\), \(H_{\neg e}\) acts only on other edge variables, and \(V_e=\sum_{g\ne f:e\in\partial g}b_gd_g\) satisfies \(0\le V_e\le B_e\), with

\[
 B_e=2\sum_{g\ne f:e\in\partial g}b_g.
\]

On a rhombus complex with at most two magnetic faces incident to any edge, each target edge of a deleted face has **at most one** remaining incident magnetic face. Thus \(B_e\le 2b_g\) for that neighbor, with \(B_e=0\) for an edge newly private after deletion.

Write \(k_s(x,z)\) for the *strictly positive, normalized* \(SU(2)\) heat kernel of \(e^{s\Delta}\), and define \(m_s=\min_{x,z}k_s(x,z)>0\), \(M_s=\max_{x,z}k_s(x,z)<\infty\). Compactness gives these finite constants for every \(s>0\). Their character expansion, used only for finite deterministic checks, is \(k_s(p)=\sum_{n=0}^\infty(n+1)e^{-sn(n+2)/4}U_n(p)\).

## II. Theorem LH-1: volume-independent pointwise one-edge Harnack

For every \(e\in E_h\), every \(t>0\), and any two full link configurations \((x_e,\mathbf y)\) and \((x'_e,\mathbf y)\) differing only on edge \(e\), the **true nonlinear deleted vacuum** satisfies

\[
 \boxed{\frac{\Omega_f^-(x_e,\mathbf y)}{\Omega_f^-(x'_e,\mathbf y)}
 \le R_e(t):=e^{tB_e}\frac{M_{a_et}}{m_{a_et}}.}\tag{LH-1}
\]

By symmetry the inverse ratio obeys the same inequality. Importantly, **no dependence on the other \(|E_h|-1\) electric links, their magnetic interactions, or the size of the face patch enters \(R_e\)**.

*Proof.* By Feynman–Kac or positivity-preserving Trotter domination, for every nonnegative function \(F\),
\[
 e^{-tB_e} e^{-t(T_e+H_{\neg e})}F
 \le e^{-t H^{(-f)}}F\le e^{-t(T_e+H_{\neg e})}F.
\]
Since \(T_e\) and \(H_{\neg e}\) act on disjoint link variables, the endpoint-variable heat operator factorizes. For \(F=\Omega_f^-\), set \(G_{t,\mathbf y}(z)=(e^{-tH_{\neg e}}\Omega_f^-)(z,\mathbf y)\). It is nonnegative and independent of the *initial* edge value. The ground-state eigen-equation yields
\[
 e^{-tB_e}\int k_{a_et}(x_e,z)G_{t,\mathbf y}(z)dz
 \le e^{-t E_0^-}\Omega_f^-(x_e,\mathbf y)
 \le\int k_{a_et}(x_e,z)G_{t,\mathbf y}(z)dz.
\]
Bounding the heat kernel by \(m_{a_et}\) and \(M_{a_et}\), then comparing with \(x'_e\), proves LH-1. The bound is independent of the gauge constraint because Feynman–Kac is applied on the full edge product to a physical positive eigenfunction. \(\square\)

## III. Theorem LH-2: unconditional all-bulk deleted-vacuum marginal minorization

Fix any edge \(e\in\partial f\). For fixed remaining links, the map \(U_e\mapsto W_f\) is a left/right Haar translation, perhaps composed with inversion. Therefore the Haar probability of \(\{d_f\le\delta\}\) under this one-edge variation is exactly

\[
 H_{\mathrm{SU2}}(\delta)=\frac{\arccos(1-\delta)-(1-\delta)\sqrt{2\delta-\delta^2}}{\pi},\quad 0\le\delta\le2.
\]

LH-1 bounds the ratio of the conditional weights \(\Omega_f^-{}^2\) between *any* two choices of the target edge. Hence the conditional face-class marginal is minorized by \(R_e(t)^{-2}\) times SU(2) Haar. Averaging over all other link variables proves

\[
 \boxed{\mathbb P_{\Omega_f^-}(d_f\le\delta)
 \ge H_{\mathrm{SU2}}(\delta)\left[e^{-t B_e}\frac{m_{a_et}}{M_{a_et}}\right]^2.}\tag{LH-2}
\]

LH-2 holds for **every** target face in the nonlinear model and for all \(t>0\); select the best edge and optimize \(t\). More generally, the pushforward density \(F_f(p)=d\rho_f^-/d\rho_{\mathrm{Haar}}\) obeys the pointwise bound \(R_e(t)^{-2}\le F_f(p)\le R_e(t)^2\) almost everywhere, and its maximum/minimum ratio is \(\le R_e(t)^2\). Thus the *one-sided logarithmic amplitude oscillation* on any cap-scale annulus is \(\le\log R_e(t)\). This is an oscillation bound and must not be confused with a total-variation or positive-current integral bound.

If \(B_e=0\), let \(t\to\infty\). The heat kernel tends uniformly to Haar so \(R_e(t)\to1\), proving **exact Haar face holonomy**, consistent with the earlier private-edge theorem.

## IV. Penrose refinement and optimized heat-kernel scale

Standard two-sided compact-Lie-group heat-kernel estimates imply the existence of absolute constants \(c_0,c_1>0\), fixed by the SU(2) metric normalization, such that for \(0<s\le1\),
\[
 \log(M_s/m_s)\le c_0+c_1/s.
\]
It follows from LH-2 that for any target edge with \(a_e\ge a_->0\) and \(B_e\le 2\beta_+h^{-2}\), choosing \(t=h\) (for small enough \(h\)) gives
\[
 \boxed{\mathbb P_{\Omega_f^-}(d_f\le\delta)
 \ge H_{\mathrm{SU2}}(\delta)\exp(-C/h),}\tag{LH-3}
\]
where \(C\) is independent of total face count, the target face position, and the deleted-vacuum environment. More generally, optimizing \(t\) yields \(R_e\le\exp[C(1+\sqrt{B_e/a_e})]\), valid with universal constants for \(B_e\ge0\) (and the exact limit \(R_e=1\) for \(B_e=0\)).

For the flat-holonomy scale \(\delta_h=\kappa_f^{-1}\asymp h\), the Haar factor is \(H_{\mathrm{SU2}}(\delta_h)\asymp h^{3/2}\), hence
\[
 \boxed{m_f^-\ge c h^{3/2}\exp(-C/h).}\tag{LH-4}
\]

**Classification:** genuine interacting, all-interior-face, volume-uniform lower bound. **Limitation:** LH-4 is exponentially weaker than the polynomial \(ch^s\) lower bound required by the previous magnetic-deletion theorem. Inserting LH-4 into that theorem gives at best \(\Delta_f=O(h^{-2})\), not the required \(O(h^{-1}\operatorname{polylog}(1/h))\). It is important not to describe this result as closing the bulk deletion, cap-current or mass-gap obligation.

## V. Theorem LH-3: center-even SU(2) local-potential countermodel proves sharpness of the Harnack exponent

Consider the exact SU(2) class-function rotor, with \(p=\frac12\operatorname{Tr}U\),
\[
 \mathsf H_\kappa=-a\Delta+a\left[2\kappa p^2+\kappa^2 p^2(1-p^2)\right],\qquad \kappa\ge1.
\]
The potential is smooth, nonnegative, bounded by \(O(a\kappa^2)\), and invariant under the center operation \(p\mapsto-p\). Since
\[
 \Delta e^{-\kappa p^2}
 =e^{-\kappa p^2}\left[-\frac\kappa2+2\kappa p^2+\kappa^2p^2(1-p^2)\right],
\]
\(\psi_\kappa=Z_\kappa^{-1/2}e^{-\kappa p^2}\) is the exact unique positive ground state, with energy \(a\kappa/2\). For \(h=1/\kappa\), the center-cap probability obeys
\[
 \mathbb P_{\psi_\kappa}(1-p\le h)
 \le C h\exp[-2/h+O(1)],
\]
using \(Z_\kappa\ge c\kappa^{-1/2}\). The positive cap-scale radial current is \(\mathfrak T^{(a_h)}_\kappa=\kappa\cos^2(a_h/2)=\kappa-\tfrac12\), where \(a_h=\arccos(1-h)\). Thus the \(e^{-C/h}\) scale of LH-3 cannot be improved from **only** positive ground-state structure, center symmetry and a local potential upper bound \(O(h^{-2})\).

**Scope warning:** \(\mathsf H_\kappa\) is an explicitly constructed SU(2) local rotor with a *quadratic center-even class potential*, not a Wilson magnetic-deleted lattice Hamiltonian. It therefore does **not** refute the desired stronger bound for the actual Penrose deleted vacuum; it isolates the additional nontrivial model-specific cancellation/geometry that any such proof must exploit.

## VI. Deterministic checks and next mathematical obligation

The companion Python script verifies symbolically the exact group Laplacian and rotor eigenfunction identity, computes Haar-normalized cap probabilities and radial-current values at \(\kappa=5,10,20,40\), checks heat kernel positivity and normalization for \(s=0.5,1\), and logs the numerical results. No Monte Carlo simulation or historical Stage7/26 data modifications were performed.

The remaining sufficient condition is a local near-center density/current improvement from \(\log R_e=O(h^{-1})\) to \(\mathfrak O_{f,a_h}=o(h^{-1/4})\), or the previously identified cap-scale outward-current/shell-Fisher pair. LH-3 shows this cannot follow from a *generic* local potential sup bound or center symmetry alone. The correct next direction is to use the **specific neighboring Wilson-plaquette compatibility around the deleted face** to obtain cancellation in the local face-flux transport or to compare the full environment-conditioned heat kernel along gauge-compatible simultaneous link variations. The true small-ball bound, full nonlinear bulk magnetic-deletion estimate, fixed-support covariance, interacting physical mass gap and continuum reconstruction all remain OPEN.