# The Singular Boundary — Exact nonlinear deleted-face fiber equation and center-mass monotonicity criterion

**Date:** 2026-10-29. **Model status:** Exact finite, interacting, gauge-invariant SU(2) Wilson ground-state factorization and scalar Schrödinger equation; an explicitly **conditional** Haar-order small-ball theorem requiring a new sign property of the exact fiber energy. The sign condition is **not** derived from the full nonlinear Penrose Hamiltonian. No continuum mass gap is claimed.

## 1. Model and Haar face-coordinate calculus

Consider any finite, face-complete simply connected SU(2) rhombus disk, imposing Gauss invariance at all vertices, with positive electric coefficients `a_e` and arbitrary nonnegative magnetic terms on faces other than a chosen interior face `f`. The *magnetic-deleted* Hamiltonian is

`H_f^- = T + V_-`, where `T = sum_e a_e (-Delta_e)` and `V_- = sum_{g != f} b_g (1-p_g)`.

Let `Omega` be its unique normalized strictly positive smooth physical ground state, `E0` its ground energy, and `p=p_f=ReTr(W_f)/2`. Write `A_f=sum_{e in boundary f} a_e`. Under full product Haar measure `m`, the pushforward of `p` has the exact Haar class density

`rho_0(p)=2 sqrt(1-p²)/pi` for `-1<p<1`.

The electric generator `L0=sum_e a_e Delta_e` obeys the *closed* one-dimensional identities

`L0 p = -3 A_f p/4`, `Gamma(p)=sum_e a_e |grad_e p|² = A_f (1-p²)/4 =: g(p)`, and `(rho_0 g)'=rho_0 (-3 A_f p/4)`.

These identities hold regardless of magnetic interactions, shared edges or the number of other faces.

## 2. Theorem EF-1: Exact nonadiabatic fiber-energy decomposition

Define the positive relative class-marginal density and its square root

`F(p)=E_m[Omega² | p]`, `psi(p)=sqrt(F(p)) >0`.

Factor the **actual** ground state into `Omega(U)=psi(p(U)) Phi(U)`, with `E_m[Phi²|p]=1`. The normalized conditional state `Phi` retains *all* environmental and collective degrees of freedom, including every order-one transverse mode. The factorization is exact, not an approximation or adiabatic projection.

First, conditioning and Haar integration by parts yield the crucial vanishing conditional cross term:

`E_m[ sum_e a_e Phi grad_e Phi . grad_e p | p ] =0` almost everywhere.

**Proof.** For any compactly supported test `q(p)`, integrate the divergence of `q(p) Phi² grad p`. The result is

`2 int rho_0 q E_m[sum_e a_e Phi grad Phi .grad p|p] dp = - int rho_0 (q' g +q L0 p) dp`.

The right-hand side is zero by `(rho_0 g)'=rho_0 L0p`. Arbitrary `q` establishes the conditional identity.

Consequently, for every real differentiable scalar multiplier `eta(p)`, the full Wilson form on the **physical gauge-invariant** state `eta(p) Phi` decomposes exactly:

`<eta Phi,H_f^- eta Phi> = int rho_0(p) [ g(p)|eta'(p)|² + U_f(p) eta(p)² ] dp`, where

`U_f(p):=E_m[sum_e a_e |grad_e Phi|² + V_- Phi² |p] >=0`.

There are no hidden cross terms. This `U_f` is the *exact nonadiabatic conditional fiber energy*: it includes the entire nonlinear magnetic environment, interactions across shared links, the p-dependent conditional wavefunction, its longitudinal gradients, and the slow collective modes.

Taking `eta=psi` gives the actual ground energy. Varying `eta` while holding the already normalized conditional state `Phi` fixed is an admissible physical variation. Ground-state stationarity implies the exact weak Sturm–Liouville equation

`-(1/rho_0) d/dp (rho_0 g psi')+U_f(p) psi(p)=E0 psi(p)`.

In principal class angle `u=arccos p` (`0<u<pi`), `omega_0(u)=2 sin²(u)/pi`, `Psi(u)=psi(cos u)`, this becomes

`-(A_f/4) [Psi''(u)+2 cot(u)Psi'(u)] + U_f(cos u)Psi(u) = E0 Psi(u)`.

Writing `v(u)=sin(u)Psi(u)` gives the *ordinary* one-dimensional equation

`-(A_f/4) v''(u) + [U_f(cos u)-A_f/4] v(u)=E0 v(u)`, `v(0)=v(pi)=0`.

The center-flux involution for the deleted Hamiltonian maps `p -> -p` and preserves `Omega`, `H_f^-` and the Haar form. Therefore `F(-p)=F(p)`, `psi(-p)=psi(p)`, `U_f(-p)=U_f(p)` a.e. In angle, `Psi(pi-u)=Psi(u)` and `Psi'(pi/2)=0`. Positive endpoint smoothness gives the natural no-current conditions `omega_0 Psi' -> 0` at `u=0,pi`.

**Scope:** The equation is exact, but the effective fiber energy `U_f` is a functional of the unknown actual ground state. It is not a prescribed potential, and no independent monotonicity or Harnack bound for it is established here.

## 3. Theorem EF-2: Effective single-crossing condition implies exact Haar-order center-ball mass

Assume, **as an additional independent hypothesis for the actual deleted vacuum**, that on `0<u<pi/2` the function `U_f(cos u)-E0` changes sign at most once, from nonpositive to nonnegative. A sufficient stronger condition is that `u -> U_f(cos u)` is nondecreasing on `[0,pi/2]`.

The exact radial equation gives the flux relation

`(A_f/4) omega_0(u) Psi'(u)=int_0^u omega_0(s) [U_f(cos s)-E0]Psi(s) ds`.

Both endpoint fluxes at `u=0` and `u=pi/2` vanish. The integrand has at most one change from negative to positive, hence every partial integral is nonpositive. Therefore **`Psi'(u)<=0` for all `u in (0,pi/2)`**. This is a genuine monotone-likelihood-ratio conclusion for the exact marginal, not a comparison with a Gaussian state.

Since `Psi²` is nonincreasing and `int_0^{pi/2} omega_0 Psi²=1/2` by center parity, the weighted Chebyshev rearrangement inequality gives, for every `0<alpha<=pi/2`,

`P_Omega(0<=u<=alpha)>=int_0^alpha omega_0(u) du`, and symmetrically for `pi-alpha<=u<=pi`.

For `alpha_h=arccos(1-h)`, the sharp lower bound for each SU(2) center ball is therefore

`m_f^-(h)=P_Omega(d_f<=h) >= m_H(h)`

`m_H(h)=[alpha_h-(1-h)sqrt(2h-h²)]/pi = (4 sqrt(2)/(3 pi)) h^(3/2)(1+O(h))`.

This is precisely the polynomial center-ball lower bound sufficient for the previously proved all-bulk magnetic-deletion theorem, with an optimal Haar prefactor. In particular, if the single-crossing hypothesis is established uniformly for every interior face at the physical refinement couplings, the existing deletion-energy theorem gives `sup_f Delta_f=O(h^-1 log(1/h))`, full extreme-defect rarity at threshold `h^(3/4)`, and fixed-support Wilson–angle remainder equivalence. **These final implications remain conditional.**

Under EF-2 the deleted-vacuum marginal also dominates Haar for every radial observable increasing in `|p|`; this is an exact family of monotone-correlation consequences.

## 4. Theorem EF-3: Center parity and a closed scalar radial equation do not enforce the sign condition

A separate center-even gauge-invariant SU(2) rotor Hamiltonian `H_lambda=T+lambda p²`, `lambda>0`, has a unique strictly positive center-symmetric ground state and satisfies the same closed Haar radial diffusion identity. Its potential `lambda cos²(u)` is **largest** at SU(2) centers and smallest at the equator, reversing the EF-2 sign.

An even positive variational trial of angular width `lambda^-1/4` around `u=pi/2` gives `E0(H_lambda)<=C sqrt(lambda)` for `lambda>=1` (with a fixed electric coefficient). Since the potential is nonnegative, `E p²<=E0/lambda<=C lambda^-1/2`. For `h<=1/2`, on the center ball `p>=1-h`, `p²>=(1-h)²`, so

`P(p>=1-h) <= C lambda^-1/2/(1-h)²`.

Taking `lambda=h^-4` yields `P(p>=1-h)=O(h²)=o(h^(3/2))`. This is a **genuine positive rotor ground-state comparator** that violates the Haar-order cap lower bound despite exact center parity, without being the actual magnetic-deleted Penrose Hamiltonian. It illustrates why the model-specific *direction* of the fiber energy matters.

## 5. Key remaining proof obligation

Prove on the exact nonlinear deleted-vacuum conditional state `Phi_f` that its fiber energy satisfies the single-crossing condition of EF-2, or derive a quantitative approximate sign/flux condition sufficient for polynomial small-ball mass. The previous adjoint heat-kernel diamagnetism proves a favorable sign only for the *harmonic normal-mode trace*, not for `U_f` after including the nonlinear slow fiber modes and nonadiabatic kinetic terms. Those contributions remain open. No uniform gap, nonlinear continuum field or quartic resolvent is proved.

## 6. Verification

The companion `verify_exact_deleted_fiber.py` checks the Haar class identity, conditional cross-term cancellation by symbolic integration-by-parts, both center cap formulas, a constructed exact factorization with nontrivial conditional state, the flux monotonicity on center-favoring and center-avoiding rotor operators, and the pure-electric deleted SU(2) one-face benchmark. The mathematical steps are independent of finite truncation or Monte Carlo, and no historical Stage7/26 data are modified.
