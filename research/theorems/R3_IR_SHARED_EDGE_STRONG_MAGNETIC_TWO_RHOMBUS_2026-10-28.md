# The Singular Boundary — Nonperturbative strong-magnetic shared-edge SU(2) covariance

**Date:** 2026-10-28. **R3-IR status:** exact two-rhombus nonlinear Wilson Hamiltonian asymptotic theorem with a rigorous semiclassical (large-magnetic-coupling) ground-state limit; the harmonic oscillator is derived from the nonlinear operator, not substituted for it. This does not establish a regulator-uniform estimate for a growing Penrose patch, a fixed-time continuum field, a full physical gap or the historical Stage7/Stage26 correspondence.

## 1. Precise two-face physical model

Take exactly two edge-adjacent, simply connected open rhombi with seven distinct spatial edges and six vertices. Impose SU(2) Gauss invariance at **all** vertices. Let the shared edge have electric coefficient `s>0`, and the sums of the three exclusive-edge electric coefficients be `r_1>0`, `r_2>0`. All individual electric coefficients are strictly positive. The magnetic coefficients on the two faces are **equal**, `b>0` (the nonuniform strong-field problem is not claimed here). The full nonlinear Hamiltonian, on the physical Gauss-invariant Hilbert space, is

`H_b = sum_edges a_e (-Delta_e) + b (d_1+d_2)`, `d_i=1-p_i`, `p_i=(1/2) ReTr W_i`, and `-Delta chi_(1/2)=3 chi_(1/2)/4`.

Let `Omega_b` be its unique strictly positive normalized physical vacuum, `nu_b=Omega_b² dHaar`, `E0(b)` its ground energy, `K_b=H_b-E0(b)`. Set `A_i=r_i+s`, and

`M=[[A_1,-s],[-s,A_2]]`, `det M=r_1 r_2+s(r_1+r_2)>0`.

Changing one face orientation conjugates M by `diag(1,-1)` and changes the sign of `M_{12}`, but not the covariance coefficient. For convenience orient both faces so the common edge enters their boundaries in opposite directions, giving `M_{12}=-s`.

## 2. Theorem SF-1 — Strong-field vacuum limit on the physical quotient

The maximal-tree gauge fixing identifies physical wavefunctions with functions on `SU(2)²` invariant under *simultaneous conjugation*, with product Haar measure. The face holonomies are independent Haar variables **only at the level of reference measure**; the electric kinetic form still couples them through the shared edge. The pushed-forward kinetic energy is a smooth uniformly elliptic quadratic form on `SU(2)²`, restricted to simultaneous-conjugation invariants. Its symbol at `(I,I)` is the 6-by-6 block matrix `M tensor I_3`. This follows exactly by differentiating the two face holonomies with respect to each of the seven links: an exclusive link contributes to one face, while the shared link contributes with opposite signs to both.

Use exponential coordinates `g_i=exp(i x_i·sigma/2)` near the identity. Then `d_i=|x_i|²/8+O(|x_i|^4)`, and the Haar Jacobian is smooth, positive, and equals its flat value plus `O(|x|²)`; the electric quadratic form has leading symbol `M tensor I_3` plus `O(|x|)` coefficients. Set `x_i=b^(-1/4) y_i`, and conjugate the rescaled local wavefunction into Lebesgue `L²(R^6)` including the Haar Jacobian.

The rescaled physical forms `b^(-1/2) H_b` converge on compactly supported smooth test functions to the simultaneously SO(3)-invariant restriction of the oscillator

`H_inf = -sum_{i,j=1}² M_ij (nabla_{y_i}·nabla_{y_j}) + (|y_1|²+|y_2|²)/8`.

The vacuum has a unique normalized positive limit `psi_inf(y)`, proportional to `exp[-(1/(2 sqrt(8))) sum_{alpha=1}³ y_alpha^T M^(-1/2) y_alpha]`. Its probability covariance per Cartesian color is `Sigma_y=sqrt(2) M^(1/2)`. It is simultaneously rotation-invariant and belongs to the physical sector.

**Uniform localization, the key non-Gaussian step.** A gauge-invariant trial `exp[-c sqrt(b)(d_1+d_2)]` gives `E0(b)<=C sqrt(b)` with C independent of b>=1. The exact ground-state transform, `H_b>=b X` for `X=d_1+d_2`, and the exact SU(2) gradient bound `Gamma(X)<=4 a_max X` imply for `0<=t<1/sqrt(a_max)`, with `F_b(t)=E_nu exp(t sqrt(b) X)`,

`(1-a_max t²) F_b'(t) <= [E0(b)/sqrt(b)] F_b(t)`,

and therefore `F_b(t) <= exp[(C/sqrt(a_max)) artanh(t sqrt(a_max))]`, uniformly in b. Because `d_i` bounds squared geodesic distance to the identity on SU(2) from below, this yields uniform Gaussian tails for the rescaled variables y and every fixed polynomial moment. Separately `E_kin<=E0<=C sqrt(b)` gives an H¹_loc bound on the rescaled ground states by ellipticity; Rellich compactness plus the exponential tails gives *strong* global L² convergence along subsequences. The Γ-limit inferior of the quadratic form bounds every such limit below by H_inf, while compactly supported test functions of psi_inf prove the matching limsup for ground energies. Uniqueness and positivity of the oscillator ground state identify **every** subsequence with psi_inf, hence the whole family converges. Uniform exponential moments promote this to convergence of polynomial moments of total degree <=4 (indeed any fixed degree).

Thus the following limits are theorems for the **nonlinear** SU(2) physical ground state, with no assumption of Gaussian comparison:

`E0(b)/sqrt(b) -> [3/(2 sqrt(2))] tr M^(1/2)`,

`sqrt(b) E_nu[d_i] -> (3 sqrt(2)/8) (M^(1/2))_ii`,

`b Cov_nu(d_i,d_j) -> (3/16) [(M^(1/2))_ij]^2` (for i,j in {1,2}).

## 3. Theorem SF-2 — Strict positive strong-field shared-edge covariance

The explicit 2x2 positive matrix square-root identity gives

`M^(1/2) = [M+sqrt(det M) I]/sqrt(tr M+2 sqrt(det M))`.

Therefore

**`lim_(b->infty) b Cov_nu(p_1,p_2) = lim b Cov_nu(d_1,d_2) = (3 s²)/[16 (A_1+A_2+2 sqrt(A_1 A_2-s²))] > 0.`** (SF-2)

Hence `Cov_nu(p_1,p_2)>0` for all sufficiently large b, for any fixed positive electric coefficients and any shared-edge coupling s>0. It vanishes at leading order when s=0, as required by the disconnected product reference. We do **not** assert positivity for all intermediate couplings, or a convergence rate beyond `o(b^-1)` without a separate remainder theorem.

For all seven electric coefficients equal to a, `M=a[[4,-1],[-1,4]]`. Consequently

`lim b Cov(p_1,p_2) = 3a/[16(8+2 sqrt(15))] = (3a/32)(4-sqrt(15)) = 0.011907811293... a`.

The local mean deficit and diagonal variance have likewise explicit strong-field limits:

`lim sqrt(b) E[d_i]=(3 sqrt(2 a)/16)(sqrt(3)+sqrt(5))`,

`lim b Var(d_i)= (3a/32)(4+sqrt(15))`,

and the cross-to-diagonal covariance ratio tends to `(4-sqrt(15))/(4+sqrt(15))>0`.

## 4. Theorem SF-3 — Physical excitation energy and fixed-time consequence for the *two-face* model

Uniform ellipticity and the confining potential also give compactness of any sequence of normalized excited eigenstates of energy `O(sqrt(b))`. The same min-max Γ-convergence argument yields convergence of every fixed indexed eigenvalue of `H_b/sqrt(b)` to the oscillator spectrum in the simultaneous-rotation-invariant sector. The oscillator one-quantum excitations transform as three-vectors and are **not** Gauss invariant; its first physical excitation consists of two quanta in the lowest normal mode. If `lambda_-(M)>0` is the lowest eigenvalue of M, then

**`lim_(b->infty) [E_1^phys(b)-E0(b)]/sqrt(b) = sqrt(2 lambda_-(M)) >0`.** (SF-3)

For two rhombi with equal seven electric coefficients, `lambda_-=3a`, and the limit is `sqrt(6a)`. In particular the *two-face* physical gap grows as `sqrt(b)` and cannot provide a fixed-energy source-survival mechanism by itself. For the fixed two-face Wilson source `W=q_1d_1+q_2d_2` with fixed weights, `Var(W)=O(b^-1)` and for every fixed t>0,

`0<= <(W-<W>)Omega_b, exp[-t(H_b-E0)](W-<W>)Omega_b> <= O(b^-1) exp[-c t sqrt(b)]`.

The conclusion concerns this fixed two-face physical Hilbert space only: it is **not** a uniform physical gap for a growing Penrose patch.

## 5. Reproducible deterministic checks and geometry

The independent exact verifier constructs the 2-face incidence matrix and its actual shared-link signed overlap; computes M, the eigenvalues 3a and 5a at equal electric coefficients; checks its algebraic 2x2 square root; evaluates Gaussian fourth moments independently by degree-four-exact deterministic six-dimensional Gauss-Hermite quadrature; verifies positivity and decoupling s=0; and checks the original three-face ten-edge Z^5 **spatial** Penrose seed. These checks confirm the *limit coefficients*, not the uniform ellipticity, ground-state compactness, or spectrum by finite calculation; those steps are mathematical arguments above. Historical Stage7/Stage26 source identity and temporal Q14 remain unverified and source files unchanged.

## 6. Critical path

**Proved for a fixed true nonlinear two-face Wilson vacuum in the strong magnetic limit:** oscillator limit justified by localization, compactness and min-max; strict positive shared-edge covariance of order b^-1; diagonal variance and mean-deficit limits; two-face physical excitation threshold at order sqrt(b). This complements the separately proved **weak-magnetic** shared-edge perturbative covariance and isolates both ends of coupling, with no assertion of positivity between them.

**Not proved for the refining connected Penrose sequence:** a uniform many-face semiclassical comparison, a sum of long-range connected covariances, fixed-time source survival, an h-independent physical gap in the infinite-volume limit, quartic resolvent, or full continuum construction. At b=beta/h² the local adjacent covariance is `c h²+o(h²)` for this **isolated two-face model**, which alone cannot determine macroscopic Wilson-field survival. The most direct next obligation is a volume-uniform nonlinear comparison of connected two-face covariance to the actual many-face interacting vacuum, with control of cancellations from longer-distance correlations and excited modes; the finite two-face theorem is a benchmark, not a transfer principle.