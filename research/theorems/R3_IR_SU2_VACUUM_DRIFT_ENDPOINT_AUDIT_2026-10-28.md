# The Singular Boundary — Nonlinear SU(2) vacuum-score sign, drift nonmonotonicity, and a circularity audit

**Date:** October 28, 2026. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Program:** R3-IR fixed-physical-support Wilson covariance, **not** a proof of the interacting Penrose continuum mass gap. No Monte Carlo, historical source mutation, or source-level identification of Stage 7/26 with the declared Hamiltonian.

## Audited dependencies

Directly inspected the branch versions of `R3_IR_MODERATE_CURVATURE_EFFECTIVE_DRIFT_2026-10-28.md` (DR-1–DR-4, especially DR-8), `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md` (VF-1–VF-8), `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1), and `research/claims/CLAIM_LEDGER.csv`. The local symbolic verifier checks the authentic canonical three-rhombus **spatial** Z^5 seed (ten edges), not the historical temporal Q14 cavity. An original Stage 26 coefficient match remains unproved.

## NS-1. Exact interacting SU(2) one-plaquette vacuum-score sign

Take one four-link open SU(2) plaquette with uniform positive electric coefficient `a>0` and magnetic Wilson coefficient `b>0`. Gauge invariance reduces the physical Hilbert space to SU(2) class functions `f(p)`, where `p=1/2 Tr U in [-1,1]` and Haar measure has density `rho_0(p)=2 sqrt(1-p^2)/pi`. With the fundamental Casimir `(-Delta) chi_(1/2)=3/4 chi_(1/2)`, the exact Hamiltonian reads

`H_b f= -a(1-p^2) f'' +3a p f'+ b(1-p)f`.

The finite-volume positivity-improving semigroup has a unique smooth positive class ground state `Omega_b(p)` and energy `E_b`. The constant normalized Haar wavefunction is a trial with energy exactly `b`, so `0<E_b<b`: strictness follows because the constant function is not an eigenfunction when `b>0`. The regular ground-state equation is the Sturm–Liouville identity

`-a rho_0^(-1) [rho_0(1-p^2) Omega_b']' +b(1-p)Omega_b=E_b Omega_b`.

Define the probability-flux-like quantity

`J(p)=a rho_0(p)(1-p^2)Omega_b'(p)`.

It satisfies exactly

`J'(p)=[b(1-p)-E_b] rho_0(p) Omega_b(p)`.

The factor `b(1-p)-E_b` changes sign precisely once at `p_*=1-E_b/b in (0,1)`. Regularity at p=±1 gives J(-1)=J(1)=0. Thus J first increases strictly from zero and then decreases strictly back to zero; J(p)>0 for every p in (-1,1). Consequently

**`Omega_b'(p)>0` throughout `(-1,1)` for every `b>0`.**

This is a *genuine nonlinear ground-state score sign theorem* on the one-plaquette physical Hilbert space, not a Gaussian approximation. A positive score, however, does not imply that the conditional source drift has a negative derivative.

## NS-2. Exact force derivative has both signs at strong positive coupling

For the actual vacuum law `nu_b=Omega_b^2 rho_0(p)dp`, the ground-state diffusion generator is

`L_b f= a[(1-p^2)f''-3pf'] +2a(1-p^2)(log Omega_b)' f'`.

Set `u=(log Omega_b)'`, and denote the drift of p by

`beta_b(p)=L_b p = -3ap+2a(1-p^2)u(p)`.

The logarithmic ground-state equation gives the Riccati relation

`a(1-p^2)[u'+u^2]=3ap u+b(1-p)-E_b`.

Substitution yields an **exact nonlinear force derivative**

**`beta_b'(p)=-3a+2ap u(p)-2a(1-p^2)u(p)^2+2b(1-p)-2E_b`.**

Regularity of the eigenvalue ODE at the two endpoints gives

`u(-1)=(2b-E_b)/(3a)` and `u(1)=E_b/(3a)`.

Therefore

**`beta_b'(-1)=-3a+(8/3)b-(4/3)E_b >= -3a+(4/3)b`,**

**`beta_b'(1)=-3a-(4/3)E_b < 0`.**

In particular if `b>9a/4`, then `beta_b'(-1)>0` but `beta_b'(1)<0`; by continuity the drift is **not** globally nonincreasing on the physical interval. Its slope is positive on a nonempty interval close to the anti-flat SU(2) center element, and the interacting ground-state density is strictly positive there (though it may be very small).

For `Y_h=h(1-p)`, let `b_{Y,h}(y)=-h beta_b(1-y/h)`. By the chain rule `b_{Y,h}'(y)=beta_b'(1-y/h)`, so global negative-slope coercivity fails on the entire y support for `b=beta/h^2` and sufficiently small h. In the previous DR-8 criterion the chosen fixed moderate interval necessarily contains `[0,2h]` for all small h; hence even this elementary strong-field interacting SU(2) system **violates the global pointwise sufficient condition**. It nonetheless satisfies `Var_nu(Y_h)<=h^2=o(h)` simply by bounded range. The implication DR-8=>DR-9 remains valid; the error would be to treat DR-8 as universally true, necessary, or plausible without a measured core restriction.

## NS-3. Why global convexity heuristics cannot bypass the score

With the standard SU(2) Laplacian normalization, SU(2) is the round S^3 of radius two (`-Delta p=3p/4`). Its radial coordinate function obeys the Riemannian Hessian identity

`Hess p=-(p/4)g`, hence for the magnetic Wilson potential `V=b(1-p)`:

**`Hess V=(b p/4)g`.**

At p=1 this is positive, whereas at p=-1 it is negative, of size b/4. For `b=beta/h^2`, the negative curvature diverges like h^-2 in the anti-flat sector. Thus global geodesic convexity of the **magnetic potential** does not hold; one cannot invoke a uniform Bakry–Emery lower curvature bound based only on V. This observation is not a theorem about the Hessian of the *full effective vacuum potential* `-2log Omega_b`, which must be analyzed separately.

## NS-4. Exact regression/coercivity identity and the circularity concern

Return to a general finite interacting Penrose Wilson Hamiltonian, its actual vacuum measure nu, and any real, smooth, bounded curvature test `Y_h=h sum_D q_f(1-p_f)`. Write the exact ground-state generator `L_h`, its pushforward drift `b_h(y)=E_nu[L_hY_h|Y_h=y]`, the source Dirichlet first moment `M1_h=E_nu Gamma(Y_h)`, and `V_h=Var_nu(Y_h)>0`. Exact invariance/integration by parts gives

`E_nu L_hY_h=0`, and **`-Cov_nu(Y_h,b_h(Y_h))=M1_h`.**

Therefore the linear-regression effective inward slope is **exactly**

**`kappa_eff(h) := -Cov(Y_h,b_h(Y_h))/Var(Y_h) = M1_h/V_h`.**

This is also the **arithmetic mean excitation energy in the vacuum source's spectral measure**, because for `A_h=Y_h-E_nuY_h`, `V_h=||A_h Omega_h||²` and `M1_h=<A_h Omega_h,(H_h-E0)A_h Omega_h>`. It is a source-weighted energy mean, NOT the physical spectral gap.

Under the previous VF-8 nonnegative macroscopic test hypotheses, independently `c h <=M1_h<=C h`. Thus

**`Var_nu(Y_h)=o(h)` if and only if `kappa_eff(h)->infinity`.**

The equivalence is an **algebraic reformulation**, not a new method for proving concentration. It shows that simply naming or postulating a diverging *regression* slope adds no independent substance; the proof must independently bound the actual score's conditional variation or a connected covariance. The stronger pointwise DR-8 condition would imply the result but, by NS-2, is not generally valid across the entire source support even in simple one-plaquette SU(2).

The earlier DR-4 conclusion remains valid: if `Var(Y_h)>=v h` and `M1_h<=C h`, nonzero source weight lies below a fixed finite physical energy `2C/v`, fully compatible with a positive mass gap. Conversely, variance collapse would shift the average source excitation energy to infinity while its first moment stays O(h); this may signal that the candidate normalized observable becomes trivial and is logically distinct from proving a nonzero continuum mass gap.

## Status and next genuinely independent obligation

- **Proved on the genuine one-plaquette nonlinear SU(2) physical space:** strictly positive increasing vacuum function for b>0, exact derivative of the interacting conditional drift, explicit sign change for b>9a/4, and sign-indefinite magnetic Hessian.
- **Proved on arbitrary finite interacting SU(2) Wilson models:** exact source-weighted energy regression identity `kappa_eff=M1/Var`.
- **Conditional on prior Penrose coefficient/geometry inputs:** the equivalence of growing regression slope to o(h) variance in the VF-8 nonnegative-source class.
- **Not proved:** even a high-probability *core-restricted* uniform inward drift bound for the actual multi-plaquette Penrose vacuum, a shrinking fixed-support connected covariance, full parity-resolved quartic response, Stage7/26 Hamiltonian provenance, R3-IR infinite-volume physical mass gap or R2 continuum reconstruction.

**Revised proof target:** Rather than imposing a globally monotone conditional force, establish a model-specific **probability-weighted, local-in-curvature** bound that discards the rare anti-flat configurations using a separately proved tail estimate, and quantify the remaining conditional connected covariance by an independently derived Hamiltonian inequality. Do not treat an effective-regression slope defined as M1/Var as that independent inequality: it is exactly the target in disguise. The previous regional Agmon estimate excludes only excursions of the **total** curvature above order h^-1 on fixed physical support; it does not automatically excise every anti-flat single-face event at moderate total curvature. Any required new local tail must be proved.

## Deterministic verification

`verify_drift_endpoint.py` checks the exact one-plaquette SU(2) Casimir/Sturm–Liouville and Riccati algebra, both endpoint slopes, strict parameter threshold using the constant Haar Rayleigh trial, the source-rescaling derivative, the intrinsic SU(2) Hessian normalization, and the original canonical three-rhombus Z^5 spatial incidence (ten edges). It does not numerically solve the Penrose SU(2) ground state and is not a statistical test. No historical files were altered.