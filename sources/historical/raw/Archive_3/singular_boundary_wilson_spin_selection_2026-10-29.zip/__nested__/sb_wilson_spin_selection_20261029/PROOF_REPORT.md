# The Singular Boundary — Exact SU(2) bridge spin-selection and uniform small-coupling cap survival

**Date:** 2026-10-29. **Program:** R3 independent reconstruction. **Scope:** an exact physical Hilbert-space SU(2) Wilson theorem at every finite simply connected rhombus disk, with an explicitly gap-dependent and *cap-radius-uniform* polynomial small-ball theorem along a restricted part of the neighboring-face coupling interpolation. **PROVED OBSTRUCTION:** the double-deleted physical gap has a uniform *upper* bound and so the perturbative window is at most `O(h^2)`; **OPEN:** extending control to physical endpoint `t=1` by other means, complete bulk magnetic-deletion energy, fixed-support covariance, and continuum mass gap.

## A. The exact double-deleted bridge

Fix two distinct edge-sharing faces `f` (target) and `g` (neighbor). At most two faces may touch an edge. Delete *both* magnetic terms from the finite Gauss-invariant SU(2) Hamiltonian and write

\[
H_0=\sum_e a_e(-\Delta_e)+\sum_{k\ne f,g}b_k(1-p_k),\qquad
H(t)=H_0+t b_g(1-p_g),\quad b_g>0,\qquad p_k=\tfrac12\mathrm{ReTr}W_k.
\]

Let `e` be the common primal link. The potential of `H_0` is **independent of `U_e`**, and the electric Laplacian on `e` separates. The unique normalized positive ground state `Omega_0` is independent of `U_e` in the full product-link representation and is physical Gauss invariant. Denote by `delta_0>0` the **finite-volume physical ground-state spectral gap of `H_0`**, *not* a regulator-uniform gap. Scalar terms do not affect ground projections; hence the projectors of `H(t)` equal those of

\[
\widetilde H(t)=H_0-tB,\qquad B=b_g p_g,\quad\|B\|\le b_g.
\]

For an SU(2) irreducible representation of spin `j`, use the unnormalized character `chi_j` of dimension `d_j=2j+1`. Define the true finite physical Wilson-character expectation along the interpolation

\[
c_j(t)=\langle\Omega_t,\chi_j(W_f)\Omega_t\rangle.
\]

`Omega_t` is the positive physical ground state for real `t` near zero and for `0<=t<=1`. Its `H_0` eigenprojector has an analytic continuation near zero. The f-center flux string, which leaves all non-target magnetic faces unchanged, gives `c_j(t)=0` for every half-odd-integer spin `j` and all real `t`.

## B. Theorem SS-1: exact SU(2) representation-order selection

**For every spin `j>0` and every integer derivative order `0<=n<2j`,**

\[
\boxed{\qquad c_j^{(n)}(0)=0.\qquad}\tag{SS-1}
\]

In particular, for the center-even surviving integer spins,

\[
\boxed{c_1(t)=O(t^2),\quad c_2(t)=O(t^4),\quad c_3(t)=O(t^6),\quad\ldots}\tag{SS-2}
\]

**Proof.** The link Peter–Weyl decomposition decomposes the physical Hilbert space by its selected-link SU(2) Casimir. Since `H_0` has no potential dependence on `U_e` and its electric kinetic operator is a sum of independent link Casimirs, every link-spin projector commutes with `H_0` and with its reduced resolvent. The positive ground state of `H_0` lies entirely in the link-spin-zero sector. Multiplication by `p_g` carries, on the shared link `e`, exactly the **fundamental spin-1/2 matrix coefficient**, with all other links treated as coefficient variables; hence one factor of `B` changes the possible link spin by at most `1/2`. The `n`-th order eigenvector coefficient `psi_n` of a locally analytic intermediate-normalized ground state has link spins no larger than `n/2`, by induction in the resolvent perturbation recursion. The target Wilson character `chi_j(W_f)`, as a function of `U_e`, is a matrix coefficient in link representation `j`. By SU(2) Clebsch–Gordan orthogonality, a term `<psi_m,chi_j(W_f)psi_{n-m}>` can be nonzero only if `j<=ell_m+ell_{n-m}<=n/2`. Therefore all Taylor coefficients below order `2j` vanish in the unnormalized expectation and hence also in its ratio by the nonzero analytic norm. This proof is exact with **all** other nonlinear magnetic terms present and with full Gauss invariance. It does not assume a uniform gap. □

## C. Theorem SS-2: explicit finite-gap analytic coefficient bound

Let `P(t)` be the rank-one ground-state Riesz projector of `\widetilde H(t)` continued to complex `t`. On the circle in spectral parameter centered at `E_0` of radius `delta_0/2`, the unperturbed resolvent has norm at most `2/delta_0`. For

\[
|t|\le r:=\frac{\delta_0}{4b_g},
\]

the resolvent Neumann series is uniformly convergent with `|| (z-\widetilde H(t))^{-1}||<=4/delta_0`. Integration of the contour therefore gives `||P(t)||_1=||P(t)||<=2`, since `P(t)` has rank one. Define the holomorphic continuation `c_j(t)=Tr(chi_j(W_f)P(t))`, for which `|c_j(t)|<=2d_j` on `|t|=r`. By the vanishing coefficients in SS-1 and the Cauchy estimate, for real `|t|<=r/2`:

\[
\boxed{|c_j(t)|\le4d_j\bigl(4b_g|t|/\delta_0\bigr)^{2j}.}\tag{SS-3}
\]

The bound is **uniform in the number of other faces**, conditional on the explicitly displayed finite gap `delta_0`. It is not a regulator-uniform estimate because `delta_0/b_g` has not been controlled at refinement.

## D. Theorem SS-3: no loss of cap radius in the perturbative Haar lower bound

Let `a in (0,pi/2)` be arbitrary. Choose a real nonnegative central SU(2) bump `phi_a`, supported in the group geodesic cap `B_{a/2}`, with

\[
\alpha_a=\int\phi_a dU>0,\qquad \nu_a=\int\phi_a^2dU>0,
\qquad k_a=\phi_a*\phi_a^\vee.
\]

The positive convolution has `0<=k_a<=nu_a 1_{B_a}`, `\int k_a=alpha_a^2` and the exact character expansion

\[
\langle k_a(W_f)\rangle_t=\alpha_a^2+\sum_{j>0}\frac{\beta_j(a)^2}{d_j}c_j(t),\qquad\beta_j=\int\phi_a\chi_j.
\]

Center symmetry makes half-odd-spin contributions vanish, while `|beta_j|<=d_j alpha_a` for each remaining integer spin `j>=1`. Put `rho=4b_g|t|/delta_0`. For `rho<=1/2`, the SS-3 character bound yields

\[
\begin{aligned}
\langle k_a(W_f)\rangle_t
&\ge\alpha_a^2-4\alpha_a^2\sum_{j=1}^\infty(2j+1)^2\rho^{2j}\\
&=\alpha_a^2\left[1-4\frac{x(9-2x+x^2)}{(1-x)^3}\right],\quad x=\rho^2.
\end{aligned}
\tag{SS-4}
\]

At the fixed **finite-gap perturbative window**

\[
\boxed{0\le t\le \frac{\delta_0}{64b_g},\quad \rho\le1/16,}
\]

the bracket has the explicit positive lower bound

\[
\boxed{\quad\langle k_a(W_f)\rangle_t\ge 0.8578373627\,\alpha_a^2,\qquad
\mathbb P_{\Omega_t}(W_f\in B_a)\ge0.8578373627\frac{\alpha_a^2}{\nu_a}.\quad}\tag{SS-5}
\]

For the fixed scaled bump used in the preceding cap-response theorem, `alpha_a^2/nu_a\asymp a^3`. Thus for the physically relevant shrinking angular cap `a_h=arccos(1-h)\asymp sqrt(h)`, SS-5 proves

\[
\mathbb P_{\Omega_t}(d_f\le h)\ge c_\phi h^{3/2},
\qquad 0\le t\le\frac{\delta_0(h)}{64b_g(h)}.
\]

**This cap survival window is independent of the cap radius!** It improves the endpoint quadratic projector-norm method, which would demand an additional factor `h^(3/4)` in the permitted coupling. It exploits the detailed SU(2) representation-order selection and the positive Fourier weights of the cap source. **It does not reach `t=1`** unless an independent bound `delta_0(h)>=64b_g(h)` is proved; no such statement is asserted or expected from this argument.

## E. Theorem SS-4: an exact physical excitation shows the gap window cannot reach full coupling

The remaining possibility `delta_0(h)>=64 b_g(h)` is **excluded**, rather than merely unproved, under bounded electric coefficients. Since the shared edge is private in `H_0`, the `f` and `g` holonomies have *exact* Haar marginal in `Omega_0^2`. For either deleted face `k in {f,g}`, define the physical Gauss-invariant trial vector

\[
\Xi_k(U)=\chi_{1/2}(W_k(U))\Omega_0(U)=2p_k(U)\Omega_0(U).
\]

Haar character orthogonality on the private edge gives `⟨Omega_0,Xi_k⟩=0` and `||Xi_k||²=∫(2p_k)²dHaar=1`. The ground-state transform for the exact positive finite SU(2) vacuum gives

\[
\langle\Xi_k,(H_0-E_0)\Xi_k\rangle
 =\sum_{e'\in\partial k}a_{e'}\langle|\nabla_{e'}(2p_k)|^2\rangle_{\Omega_0^2}.
\]

For each incident link, the SU(2) bi-invariant gradient identity is `|∇_(e')(2p_k)|²=1-p_k²`. Haar `E(p_k²)=1/4` gives exactly

\[
\boxed{\frac{\langle\Xi_k,(H_0-E_0)\Xi_k\rangle}{\|\Xi_k\|^2}=\frac34 A_k,\qquad
\delta_0\le\frac34\min(A_f,A_g).}\tag{SS-6}
\]

With `A_f,A_g<=4a_+` and `b_g>=beta_- h^(-2)` this forces

\[
\boxed{\frac{\delta_0(h)}{64b_g(h)}\le\frac{3a_+}{64 beta_-}h^2.}\tag{SS-7}
\]

Thus the exact small-coupling cap survival window of SS-5 is provably **at most order `h²`** for the refining Wilson model, and can never contain the physical endpoint `t=1` for sufficiently small `h`. This establishes a rigorous obstruction to closing the all-bulk deleted-face cap probability via gap-based analytic continuation alone. A full-coupling proof needs a nonlinear, gap-insensitive cancellation, a different monotonicity, or a direct estimate of the low-energy mixed response.

## F. Deterministic independent test and rigor limits

The accompanying checker constructs, using **exact rational arithmetic**, the Rayleigh–Schrödinger coefficients in the orthonormal SU(2) character basis of the solvable one-link rotor `-Delta-t p`. It tests the general Clebsch–Gordan representation-order rule for spins `j=1/2,1,3/2,2,5/2,3`, verifies vanishing below order `2j` and computes the exact nonzero leading coefficients. It also checks the closed-form spin-series sum and constant in SS-5. The one-link rotor is a **representation selection comparator**, not a physical cycle-rich Penrose deleted vacuum; its half-odd-spin expectations need not vanish because it lacks the target center-flux symmetry of the actual deleted Hamiltonian. The physical finite-volume result is the analytic theorem above, not this comparator.

**PROVED:** the all-orders `t^(2j)` Wilson-character selection at the double-deleted endpoint; explicit finite-gap Taylor bound; cap-radius-uniform polynomial probability in the window `t<=delta_0/(64b_g)`; and the exact physical Rayleigh *upper* bound `delta_0<=3 min(A_f,A_g)/4`, excluding direct continuation of that window to `t=1` at small `h`. **OPEN:** prove a gap-insensitive way of carrying the cap bound to `t=1`, or directly control the normalized adverse low-energy cap-response of the actual cycle-rich Penrose deleted ground state; complete bulk magnetic deletion, fixed-support connected covariance, positive continuum mass gap, quartic resolvent, and continuum reconstruction.
