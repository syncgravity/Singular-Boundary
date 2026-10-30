# The Singular Boundary — Exact deleted-vacuum marginal Fisher identity and SU(2) center-capacity obstruction

**Date:** 2026-10-29. **Scope:** exact finite nonlinear Gauss-invariant SU(2) Wilson ground-state marginal identity, sharp functional-analytic obstruction from true positive gauge-invariant *trial states*, and a quantitative (conditional) vacuum-comparison transfer criterion. **Not established:** a uniform polynomial near-center small-ball lower bound for the true deleted ground state, nonlinear bulk deletion scaling, complete continuum reconstruction, or positive all-sector physical mass gap. This proof does not modify the historical Stage 7/26 archives.

## 1. Setting and exact radial ground-state score identity

Let the physical Hamiltonian on a finite face-complete planar rhombus disk be H^-=T+V^- with T=sum_e a_e(-Delta_e), a_e>0, and V^-=sum_{g neq f} b_g(1-p_g), with target-face magnetic term deleted, p=p_f=(1/2)Re Tr W_f. Let Omega^->0 be its unique normalized real gauge-invariant ground state and nu=(Omega^-)² dHaar. Write A_f=sum_{e in boundary f}a_e. Our SU(2) fundamental Casimir convention gives, **exactly and pointwise for any target face with shared links**:

L_0 p = -3 A_f p/4,    Gamma_0(p) = A_f(1-p²)/4,
where L_0=sum a_e Delta_e, Gamma_0(F)=sum a_e |grad_e F|².

Let rho_0(p)=2sqrt(1-p²)/pi be the Haar density of p, and let rho(p)=rho_0(p)F(p) be the true deleted-vacuum pushforward density. F is strictly positive and smooth in the interior (finite-dimensional elliptic ground state and compact group geometry), with weak derivatives where appropriate. Define
T_f(U)=sum_{e in boundary f}a_e |grad_e log Omega^-(U)|²,
J(U)=sum_{e in boundary f}a_e grad_e p . grad_e log Omega^-(U).

For every real smooth phi(p), Haar integration by parts and the vacuum ground-state transform give
int phi'(p) Gamma_0(p) rho(p) dp = -int phi(p)[L_0 p+2 E_nu(J|p)]rho(p)dp.
The bare Haar identity has (Gamma_0 rho_0)'=(L_0 p)rho_0. Therefore the *exact interacting conditional-score identity* is

 (A_f/4)(1-p²) (log F)'(p) = 2 E_nu(J | p)       (MI-1)

for rho-almost every p in (-1,1). In angle u=arccos p, the Haar class density is omega_0(u)=2 sin²(u)/pi, 0<=u<=pi, and the same F is the angular Radon–Nikodym derivative.

Conditional Cauchy–Schwarz and |J|²<=Gamma_0(p) T_f imply

 (A_f/4) int_0^pi |d/du log F(cos u)|² F(cos u) omega_0(u) du <= 4 E_nu T_f.       (MI-2)

Equivalently, for v(u)=sqrt(F(cos u)),

 (A_f/4) int_0^pi |v'(u)|² omega_0(u)du <= E_nu T_f.                             (MI-3)

This is an **exact finite nonlinear interacting-vacuum Fisher-information inequality**, with no gap or Gaussian assumptions, and includes fully shared interior faces. It is a consequence of the full ground-state equation; it is not a Harnack or pointwise estimate. The earlier regional cut comparison can bound the right-hand side by a regional energy increment, but that increment grows with h and does not establish near-center mass.

Deleted-face center parity sends p -> -p, so F(p)=F(-p); thus any center-ball lower bound is identical at +I and -I. The exact center ball radius h in deficit d=1-p has Haar probability

 m_H(h) = [arccos(1-h) -(1-h)sqrt(2h-h²)]/pi = (4sqrt(2)/(3pi)) h^(3/2)(1+O(h)).     (MI-4)

## 2. Zero-capacity obstruction: positive gauge-invariant trial states with energy excess o(1)

The SU(2) group is a 3-sphere with Haar radial density omega_0(u)~(2/pi)u² near the center. A point has zero H¹ capacity in dimension three. Consequently MI-2/MI-3 cannot force a lower bound on a ball shrinking toward a center element. The following explicit construction makes that failure quantitative.

Consider a one-plaquette SU(2) lattice (or the target holonomy as a separate gauge-invariant class variable), with its magnetic term deleted and pure-electric physical Hamiltonian H_0=T, whose exact vacuum is Omega_0=1 and ground energy zero. Fix 0<h<h_0 sufficiently small, let r=4sqrt(h), eps=exp(-1/h), and choose the C¹ smoothstep s(t)=0 for t<=0; s(t)=3t²-2t³ for 0<t<1; s(t)=1 for t>=1. Define the positive center-even class multiplier

 g_h(u)=eps+(1-eps) s((min(u,pi-u)-r)/r),
 psi_h(U)=g_h(arccos((1/2)Re Tr W))/sqrt(N_h),
 N_h=int_0^pi g_h(u)² omega_0(u)du.

Every psi_h is strictly positive, normalized, Gauss-invariant, and invariant under the deleted center flip. The function is constant eps on both caps u<=r and pi-u<=r, and equals one away from caps u<2r and pi-u<2r. Since |s'|<=3/2, the elementary bounds on sin²u give

 1-N_h <= (32/(3pi)) r³,            ||psi_h-Omega_0||² = O(r³),
 <psi_h,H_0 psi_h> = (A_f/4N_h) int |g_h'|² omega_0 du <= (A_f/4N_h)(21/pi)r =O(A_f sqrt(h)).  (MI-5)

The exact Haar small ball A_h={1-p<=h} satisfies u<=arccos(1-h)<r for h sufficiently small, hence

 Pr_{psi_h}(A_h) = eps² m_H(h)/N_h <= C h^(3/2) exp(-2/h).                      (MI-6)

By contrast Pr_{Omega_0}(A_h)=m_H(h)~(4sqrt(2)/(3pi))h^(3/2). Thus a family of positive center-even **approximate** pure-electric ground states has vanishing *absolute* energy excess and converges in L² to the exact vacuum, yet its center-ball probability is suppressed by exp(-2/h) relative to the exact ground state. Its weighted marginal Fisher energy also tends to zero. These trial states are **not exact eigenstates**: MI-6 does not refute the desired estimate for the actual interacting Penrose deleted vacuum. It proves that a route using solely the existing Fisher/Dirichlet energy and evenness is insufficient, even with a substantially stronger O(sqrt(h)) energy budget.

The center-flux parity is essential only to keep the construction within the same symmetry sector, not for its energy estimate. The obstruction depends on the **capacity of shrinking caps** and survives any attempt to infer an h-dependent pointwise lower density from an unweighted H¹ estimate alone.

## 2b. A sharp *positive* capacity-scale sufficient criterion for the true deleted vacuum

There is a new rigorous path to a polynomial flat-ball lower bound which does **not** require pointwise Harnack control. Let `w_h(u)=sqrt(F_h(cos u))`, normalized so `int w_h² omega_0=1`, and define its radial *square-root Fisher/Dirichlet energy*

`J_h = int_0^pi |w_h'(u)|² omega_0(u)du`.

Because radial functions on SU(2) are radial functions on the round 3-sphere, the standard normalized compact-Sobolev embedding `H¹(S³) -> L⁶(S³)`, together with the S³ Poincare inequality and normalization, gives (for `J_h<=1`)

`||w_h-1||_{L^6(omega_0)} <= C_S sqrt(J_h)`.

For any Haar measurable class cap `C_h={1-p<=h}` of Haar mass `m_H(h)`, Holder and the triangle inequality imply

`|sqrt(m_h^-) - sqrt(m_H(h))| <= C_S m_H(h)^(1/3) sqrt(J_h)`, hence

**`m_h^- >= m_H(h) [1-C_S m_H(h)^(-1/6) sqrt(J_h)]_+²`.**  (MI-11)

Since `m_H(h)=Theta(h^(3/2))`, **`J_h=o(h^(1/2))`** is sufficient to prove the sharp *Haar-order* lower bound

**`m_h^- >= (1-o(1)) (4sqrt(2)/(3pi))h^(3/2)`**.                       (MI-12)

MI-3 supplies `J_h <= (4/A_f) E_nu T_f`, so the stronger sufficient hypothesis `E_nu T_f=o(A_f sqrt(h))` also works. But the actual deleted vacuum is **not** known to satisfy either bound. Unlike a mere `O(1)` Fisher estimate, this is a strictly shrinking energy threshold that matches the `Theta(sqrt(h))` capacity cost of suppressing the cap.

The explicit smoothstep family in §2 obeys `J_h=Theta(r)=Theta(sqrt(h))`, not `o(sqrt(h))`, while its cap mass is exponentially depleted. Thus the **power** `sqrt(h)` in the sufficient criterion is sharp at the level of SU(2) H¹ control, even though constants and actual-vacuum dynamics remain open. This is a genuine *conditional* small-ball theorem, rather than a consequence of the existing local energy estimates.

## 3. Precise comparison accuracy needed to transfer a polynomial center ball

For a normalized comparison state psi_h and the *actual* deleted ground state Omega_h^-, let P_h be multiplication by 1_{1-p_f<=h}. Then, by the triangle inequality,

 sqrt(m_h^-) = ||P_h Omega_h^-|| >= [||P_h psi_h|| - ||psi_h-Omega_h^-||]_+,

 m_h^- >= [sqrt(m_h^{comp}) - eps_h]_+², eps_h=||psi_h-Omega_h^-||.           (MI-7)

Therefore if a comparison model has m_h^{comp}>=c h^s, it suffices to prove eps_h=o(h^(s/2)) (with its phase aligned) to transfer the same polynomial order. For a Haar comparison m_h^{comp}=Theta(h^(3/2)), the **norm precision must be o(h^(3/4))**; mere o(1) vacuum convergence is insufficient.

More generally, at each finite deleted Hamiltonian let delta_h^- be its positive physical-sector excitation gap. For a normalized physical trial psi_h with nonnegative overlap with Omega_h^- and Rayleigh excess e_h=<psi_h,(H_h^--E0^-)psi_h>, spectral decomposition gives

 ||psi_h-Omega_h^-||² <= 2 e_h/delta_h^-,

 m_h^- >= [sqrt(m_h^{comp})-sqrt(2e_h/delta_h^-)]_+².                      (MI-8)

Hence sufficient energy accuracy is e_h=o(delta_h^- h^s), *and* an independent lower control on the deleted gap is needed to turn energy closeness into ground-state closeness. Prior collective-mode/center-odd theorems do not establish such a gap, and indeed allow a soft deleted center-odd doublet. MI-8 is a conditional transfer criterion, not a proof of the polynomial flat-ball bound.

## 4. An independent marginal Harnack criterion (not established)

Let F_h=rho_h^-/rho_0. If one could prove (independently from the Hamiltonian)

 osc_{0<=u<=pi} log F_h(cos u) <= C+s log(1/h),                              (MI-9)

then normalization int F_h omega_0=1 implies inf F_h>=e^-C h^s, and MI-4 yields

 m_h^->= c' h^(s+3/2).                                                       (MI-10)

MI-2 does **not** imply MI-9: the strictly positive center-even family in §2 has arbitrarily large log oscillation despite vanishing H¹ energy. The needed new dynamical input is therefore a **logarithmic-density oscillation/Harnack bound, a sufficiently precise multichannel vacuum comparison, or another model-specific local correlation inequality** that gives the same center-ball lower bound.

## 5. Verification and status

`verify_deleted_marginal_capacity.py` checks the Haar cap formula, exact radial SU(2) first-Casimir coefficient, the normalized smoothstep family, its center parity and H¹ Rayleigh energy bounds, stretched-exponential cap depletion, and the transfer-error exponent. It also checks the exact pure-electric SU(2) class character relation: each incident link contributes eigenvalue 3a_e/4, hence the four-link plaquette trace has E_p=3A_f/4=3a for a_e=1.

**PROVED:** MI-11/MI-12 as a sharp conditional Sobolev capacity-scale lower bound (requires J_h=o(sqrt(h))); MI-1 to MI-3 exact nonlinear deleted-vacuum score/Fisher identities; MI-4 exact Haar cap probability; MI-5/MI-6 explicit gauge-invariant zero-capacity trial obstruction; MI-7/MI-8 exact conditional vacuum-comparison precision; MI-9 => MI-10 conditional Harnack transfer.

**OPEN:** an actual deleted Penrose vacuum polynomial center-ball lower bound; a regulator-uniform conditional force/Harnack estimate; an accurate multichannel vacuum comparison retaining O(1) collective modes and center parity; the full nonlinear interior deletion energy; connected Wilson–angle remainder covariance; physical mass gap and continuum reconstruction. No mass-gap claim and no Gaussian-vacuum transfer are made.
