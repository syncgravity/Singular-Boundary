# The Singular Boundary — Four-neighbor SU(2) Wilson selection and irreducible mixed-response identity

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction. **Status:** exact finite-volume, fully nonlinear, all-vertex Gauss-invariant SU(2) selection theorems for a four-neighbor interior rhombus; exact gap-free full-coupling identity, but **no bound of its adverse sign**. This does not prove the uniform bulk deletion bound, fixed-support covariance, physical mass gap, quartic resolvent or continuum reconstruction.

## 1. Genuine physical Wilson setting

Let `G=SU(2)` on a finite simply connected edge-to-edge planar rhombus disk. Let `f` be a four-edge interior face with **four distinct edge-sharing neighbors** `g_1,...,g_4` (one per edge); the face complex is assumed regular, so distinct faces share at most one edge. The positive all-vertex Gauss-invariant Wilson Hamiltonian on the full link-product Hilbert space is

\[
H(\mathbf t)=\sum_e a_e(-\Delta_e)+\sum_{k\notin\{f,g_1,\ldots,g_4\}} b_k(1-p_k)
 +\sum_{i=1}^4 t_i b_{g_i}(1-p_{g_i}),\quad p_k=\tfrac12\operatorname{ReTr}W_k.
\]

The target `f` is magnetically deleted **throughout**; the other remaining plaquettes, including corner/outer faces and loops of adjacent Wilson interactions, are **not** discarded. Each `t_i` runs from zero to one; negative real values are permitted in the auxiliary analytic symmetry arguments because the potential remains bounded. For every fixed finite lattice and all finite real couplings, the positive heat semigroup has a unique normalized strictly positive gauge-invariant ground state `Omega_t`. Let

\[c_j(\mathbf t)=\langle\Omega_{\mathbf t},\chi_j(W_f)\Omega_{\mathbf t}\rangle,\qquad j\in\tfrac12\mathbb N_0.\]

The previously established deleted-target center-flux symmetry forces `c_j(t)=0` for all half-odd-integral `j` and all `t`. Write `F_a(t)=<k_a(W_f)>_t`, where `k_a=phi_a*phi_a^vee` is any positive class convolution cap minorant, with `alpha_a=int phi_a`, `nu_a=int phi_a^2`, `0<=k_a<=nu_a 1_{B_a}`, and `int k_a=alpha_a^2`.

## 2. Theorem FN-1: every neighboring-coupling coordinate hyperplane is exactly Haar

For each `i`, let `e_i` be the distinct common primal edge of `f` and `g_i`. If `t_i=0`, both faces that contain `e_i` have **zero magnetic coupling** (the target `f` is always deleted). Consequently the potential is independent of `U_{e_i}`, and the kinetic term `a_{e_i}(-Delta_{e_i})` separates exactly on the full product-link space. The unique positive ground state is independent of `U_{e_i}`. At fixed other links, the map `U_{e_i} -> W_f` is a Haar translation/inversion. Hence for **all values** of the remaining three couplings,

\[\boxed{\quad t_i=0\quad\Longrightarrow\quad \mathbb P_{\Omega_{\mathbf t}}(W_f\in A)=\operatorname{Haar}(A)\quad\forall A,\quad c_j(\mathbf t)=0\;(j>0),\quad F_a(\mathbf t)=\alpha_a^2.\quad}\tag{FN-1}\]

This is a **full-coupling, fully nonlinear physical theorem** on every coordinate hyperplane, not a perturbative estimate.

## 3. Theorem FN-2: independently even response in each neighboring coupling

For each neighbor `g_i`, the planar center 1-cochain/dual-path construction provides a unitary `S_{g_i}` acting by central `-I` flips on a chain of links, with `W_{g_i}->-W_{g_i}` and every other face holonomy unchanged. It preserves Haar measure, Gauss invariance, and all electric Laplacians, and fixes `chi_j(W_f)` and `k_a(W_f)`. Therefore

\[\boxed{\quad S_{g_i}H(t_1,\ldots,t_i,\ldots,t_4)S_{g_i}=H(t_1,\ldots,-t_i,\ldots,t_4)+2t_i b_{g_i}I.\quad}\tag{FN-2}\]

By uniqueness of the positive finite-volume ground state, `c_j(t)` and `F_a(t)` are separately **even in every `t_i`**, with the other three couplings arbitrary. Thus odd one-neighbor response derivatives vanish at `t_i=0` even when the other three neighbors are fully restored.

## 4. Theorem FN-3: representation-filtered vanishing up to order 2j **in every coordinate**

Fix one `i` and hold all other three couplings at arbitrary real values. At `t_i=0`, the selected edge `e_i` is private. In the Peter–Weyl expansion of `L²(G_{e_i})`, the positive ground state has only the trivial link-spin sector, and the unperturbed Hamiltonian and its reduced resolvent commute with all its link-spin projectors. The *only* magnetic multiplier containing this link is `p_{g_i}`, a fundamental SU(2) matrix coefficient. Every perturbative insertion of `t_i b_{g_i} p_{g_i}` changes the possible link spin by at most `1/2`. The target character `chi_j(W_f)` is a spin-`j` coefficient on `e_i`. Therefore a term joining ket order `m` to bra order `n-m` can have a nonzero Haar integral only if `j<=(n/2)`.

The exact one-variable derivative statement, valid with all other three couplings held **at their physical values** if desired, is

\[\boxed{\quad\left.\partial_{t_i}^{n}c_j(t_1,\ldots,t_4)\right|_{t_i=0}=0\quad\text{for each}\quad n<2j,\;i\in\{1,2,3,4\}.\quad}\tag{FN-3}\]

In the multivariate Taylor expansion near the fully deleted neighbor-star endpoint, every allowed monomial in an integer-spin `j` target character contains at least `t_1^{2j}t_2^{2j}t_3^{2j}t_4^{2j}`. The earliest **possible** total degree is `8j`; no assertion is made that the leading coefficient is nonzero in the actual Wilson vacuum. In particular, surviving spin 1 cannot respond before total degree 8, spin 2 before degree 16, etc. This is an exact nonlinear **representation-selection** statement independent of the number or couplings of magnetic faces outside the target's immediate neighbor star.

## 5. Theorem FN-4: exact, nonperturbative full-coupling eightfold mixed-response identity

For every fixed finite disk, all the finite-volume ground-state expectations above are smooth real functions in a neighborhood of `[0,1]^4`; the finite-volume ground state is simple, though its spectral gap need not be uniform in refinement. FN-1 yields `F_a(t)=alpha_a²` whenever any `t_i=0`. FN-2 yields `partial_i F_a(t)|_{t_i=0}=0`. Repeated fundamental theorem of calculus gives the **exact gap-free identity valid at physical full coupling**:

\[
\boxed{\quad F_a(1,1,1,1)-\alpha_a^2
 =\int_{[0,1]^4}\left[\prod_{i=1}^{4}(1-s_i)\right]
 (\partial_1^2\partial_2^2\partial_3^2\partial_4^2F_a)(s_1,s_2,s_3,s_4)\,d^4s.\quad}\tag{FN-4}\]

`Gap-free` here means the **identity itself** does not require a regulator-uniform gap; it does **not** assert any uniform numerical bound on its eightfold mixed derivative, which can contain products of many reduced resolvents.

More generally, repeated Taylor remainder with FN-3 gives, for each **integer** spin `j>=1`,

\[
\boxed{\quad c_j(\mathbf1)=\frac1{[(2j-1)!]^4}\int_{[0,1]^4}
 \left[\prod_i(1-s_i)^{2j-1}\right]
 (\partial_1^{2j}\partial_2^{2j}\partial_3^{2j}\partial_4^{2j}c_j)(\mathbf s)\,d^4s.\quad}\tag{FN-5}\]

Both identities are exact for the true nonlinear physical Hamiltonian; all exterior Wilson interactions remain present.

## 6. FN-5: a necessary genuinely four-neighbor adverse-response obstruction

Define the **eightfold mixed-response negative budget**

\[\mathcal N_a=\int_{[0,1]^4}\prod_i(1-s_i)\,[-(\partial_1^2\partial_2^2\partial_3^2\partial_4^2F_a)(\mathbf s)]_+\,d^4s.\]

Since `0<=k_a<=nu_a 1_{B_a}`, FN-4 proves

\[\boxed{\quad\mathbb P_{\Omega_{\mathbf1}}(W_f\in B_a)\ge\frac{[\alpha_a^2-\mathcal N_a]_+}{\nu_a}.\quad}\tag{FN-6}\]

For `a_h=acos(1-h)~sqrt(2h)`, `alpha_a²~h³`, and `nu_a~h^{3/2}`. If an **independent** Wilson-specific bound `sup_f N_{a_h}<=alpha_{a_h}²/2` were proved, FN-6 would imply the necessary polynomial `c h^{3/2}` deleted-face mass. **This condition is unproved.** FN-6 is not presented as a solution of the physical full-coupling response. It is a structural *connected-four-neighbor* reduction: one-, two-, and three-neighbor submodels leave the target exactly Haar, and only the interaction of all four neighboring Wilson couplings can alter its marginal.

## 7. Deterministic checks and scope

The companion script uses exact 3x3 shared-edge spatial geometry (nine faces, twenty-four links, central four-neighbor face), verifies all four incident edges become private after deleting the target and four neighbors, constructs independent dual-center flux paths to the exterior preserving target parity, and performs exact rational SU(2) character fusion/orthogonality checks. For the independent-link Haar tensor `int chi_j(U1U2U3U4) prod_i p(Ui)^(2j) dU_i`, the minimal nonzero group-theoretic overlaps are `1/6912` for spin 1, `1/8192000` for spin 2, and `1/5754585088` for spin 3. These are **Haar tensor tests**, not actual interacting ground-state Taylor coefficients.

**PROVED:** FN-1—FN-5 as exact finite nonlinear SU(2) statements; the conditional cap inequality FN-6. **OPEN:** the full-coupling mixed negative budget or the original normalized low-energy one-neighbor response bound; the all-bulk magnetic-deletion estimate, fixed-support connected Wilson-angle covariance, physical mass gap, quartic resolvent, and continuum reconstruction. No numerical diagonalization of the actual many-link SU(2) Wilson Hamiltonian is claimed; no Stage26 or historical data files are altered.

## 8. FN-6: exact positive rotor demonstrates selection does not fix the full-coupling sign

For `kappa>0` and four real interpolation parameters put `q(t)=t_1²t_2²t_3²t_4²`. The strictly positive center-even normalized SU(2) class amplitude `psi_t(p)=Z(t)^(-1/2) exp(-kappa q(t) p²)` has exact Haar density when any parameter vanishes and is even in every parameter. The SU(2) character decomposition of `p^(2n)` contains only integer spins at most `n`, so every spin `j` character coefficient of `psi_t²` has a Taylor expansion divisible by `q(t)^j=prod_i t_i^(2j)`. Thus **all** FN-1/FN-2/FN-3 selection properties hold. Moreover it is the unique positive ground state of the smooth nonnegative SU(2) class rotor

`H_t = -a Delta + a[2 kappa q(t) p² + kappa² q(t)² p²(1-p²)]`, with ground energy `a kappa q(t)/2`.

Yet for `kappa=h^(-1)` at the full endpoint `t=(1,1,1,1)`, its center cap `p>=1-h` is exponentially suppressed relative to Haar. Hence even the **complete four-neighbor spin-selection hierarchy**, strict positive ground-state structure, and Haar behavior on all four coupling hyperplanes are insufficient **by themselves** to guarantee a full-coupling polynomial center cap. This comparator's potential is **not a sum of linearly restored Wilson plaquette terms**, and it is emphatically **not** a counterexample to the actual SU(2) Wilson Hamiltonian; it demonstrates that genuinely Wilson-specific dynamics are still needed.
