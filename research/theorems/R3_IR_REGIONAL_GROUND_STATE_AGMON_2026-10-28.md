# The Singular Boundary — Regional ground-state Agmon exclusion of coherent curvature excursions

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`.

**Evidence status:** New exact finite-regulator theorem for the actual nonlinear SU(2) Wilson *ground state*; the strong-field Penrose scaling corollaries are conditional on explicitly stated coefficients, face geometry, and the previously audited regional comparison. The fixed-support connected covariance, source-specific quartic resolvent, infinite-physical-volume spectrum, Stage 7/26 source correspondence, and R2 continuum all remain **OPEN**. No Monte Carlo or replacement historical data.

## 1. Source and model

Dependencies rechecked against the current GitHub audit branch: `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md` (ER-1 regional cut Hamiltonian and trial upper bound), `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md` (fundamental SU(2) gradient identity), `R3_IR_GAUGE_INVARIANT_COHERENT_COVARIANCE_WITNESS_2026-10-28.md` (positive gauge-invariant trial superposition and its limitations), and `R3_IR_MESOSCOPIC_SOURCE_COMPRESSION_2026-10-28.md` (first-moment-only limitation). A canonical three-face Z^5 Penrose **spatial** incidence fixture is used for the symbolic audit; it is not the original temporal Q14 cavity.

Let G be any finite face-complete spatial rhombus complex, four distinct links per face and each link in at most two faces. On the finite compact SU(2) link space with product Haar measure define

    H = sum_e a_e(-Delta_e) + sum_f b_f d_f,
    d_f=1-(1/2)ReTr W_f in [0,2],  0<a_e<=a_max,

with the usual fundamental Casimir `-Delta chi_(1/2)=(3/4)chi_(1/2)`. Fix a nonempty face region D, with `b_f>=beta_min/h^2` for f in D and all other b_f nonnegative. Let `S=union_{f in D} boundary(f)` and `C(D)` be faces outside D touching S. Set

    H_out = sum_{e not in S} a_e(-Delta_e) + sum_{g not in D union C(D)} b_g d_g,
    E_out=inf spectrum(H_out), E0=inf spectrum(H),
    Delta_D=E0-E_out>=0,
    E_D=(3/sqrt(2))sqrt(A_S B_D)+2B_C,

where `A_S=sum_{e in S}a_e`, `B_D=sum_{f in D} b_f`, `B_C=sum_{g in C(D)} b_g`. By the already audited regional product-link trial, `Delta_D<=E_D`; the theorem below also holds *without* that trial if the exact Delta_D is used instead.

The finite Hamiltonian has a unique strictly positive, vertex-gauge-invariant vacuum Ω (finite link-group positivity improving). Denote its actual Born probability law by `nu(dU)=Omega(U)^2 dU`. Let

    X(U)=sum_{f in D}d_f(U),       0<=X<=2|D|.

This is a **total** regional curvature observable, not the earlier signed, centered area-smeared field.

## 2. Theorem AG-1: exact regional ground-state barrier and Agmon tail

For **any** `L>=2h^2 Delta_D/beta_min` and 

    lambda_h=(1/h)sqrt(beta_min/(32 a_max)),

one has the exact nonperturbative estimate

    E_nu[ X exp(2 lambda_h (X-2L)) 1_{X>=2L} ]
       <= (64 a_max/beta_min) h^2/L.                 (AG-1)

Consequently, for every t>=0,

    nu[X>=2L+t] <= [64 a_max h^2/(beta_min L(2L+t))]
                    exp(-2 lambda_h t).            (AG-2)

If additionally `4 lambda_h L>=1`, then

    E_nu[X^2 1_{X>=2L}] <= (128 a_max/beta_min) h^2. (AG-3)

The theorem does **not** assume a uniform interacting spectral gap, Gaussian comparison, spatial clustering, reflection symmetry, or any trace-covariance bound. It applies to the **true** finite-volume interacting ground state Ω at arbitrary positive Wilson magnetic coupling compatible with the declared local lower bound.

### Proof, with every constant

1. The cut Hamiltonian satisfies the quadratic-form inequality `H>=H_out+(beta_min/h^2)X`. Hence, for any smooth real multiplier f,

       <fΩ,(H-E0)fΩ> >= E_nu[((beta_min/h^2)X-Delta_D) f^2].

   The *exact* ground-state transform gives

       <fΩ,(H-E0)fΩ> = E_nu[Gamma(f)],
       Gamma(f)=sum_e a_e |nabla_e f|^2.

   This is where true ground-state eigenfunction structure, absent from the earlier trial-state witness, enters essentially.

2. The fundamental SU(2) identity `|nabla_e p_f|^2=(1-p_f^2)/4 <= d_f/2` on e in boundary(f), together with link multiplicity<=2 and four edges per face, gives the **pointwise** inequality

       Gamma(X) <= 4 a_max X.                       (AG-4)

3. Let the scalar cutoff `chi(x)` vanish for x<=L, equal `(x-L)/L` for L<x<2L, and equal one for x>=2L. Put `f(U)=exp(lambda_h(X-2L))chi(X)`. It is a bounded Lipschitz multiplier on the finite compact link configuration manifold. Standard smooth approximation (or Sobolev chain rule) justifies the ground-state identity. On support of f, `X>=L` and `Delta_D<=beta_min L/(2h^2)` imply

       (beta_min/h^2)X-Delta_D >= beta_min X/(2h^2).

   From the chain rule and `(u+v)^2<=2u^2+2v^2`,

       Gamma(f) <= 2lambda_h^2 f^2 Gamma(X)
                    + (2/L^2) 1_{L<X<2L}
                      exp(2lambda_h(X-2L)) Gamma(X).

   By (AG-4) and choice of lambda_h, `2lambda_h^2 Gamma(X)<=beta_min X/(4h^2)`. Subtracting this absorbed term from the barrier inequality yields

       (beta_min/(4h^2)) E_nu[X f^2]
           <= (8 a_max/L^2) E_nu[X exp(2lambda_h(X-2L)) 1_{L<X<2L}]
           <= (8a_max/L^2) (2L)=16 a_max/L.

   Since chi=1 above 2L, this proves AG-1.

4. On `{X>=2L+t}`, `X exp(2lambda_h(X-2L)) >= (2L+t)exp(2lambda_h t)`. Markov's inequality with AG-1 proves AG-2. If `4lambda_h L>=1`, the function `x exp(-2lambda_h(x-2L))` is decreasing for x>=2L; it is bounded there by `2L`. Therefore `X^2 1_{X>=2L} <=2L X exp(2lambda_h(X-2L))1_{X>=2L}` and AG-1 implies AG-3. QED.

## 3. Corollary AG-2: fixed-physical-support Penrose large deviations

Assume a fixed physical interior region D_R, fixed R>0 and a complete collar, with O(h^-2) faces, `a_e` uniformly bounded, and `beta_min/h²<=b_f<=beta_max/h²`. The regional trial energy bound gives `E_D=O_R(h^-3)`, without reference to the energy of the rest of the ambient graph. Choose

    L_h=max{2h² E_D/beta_min, h^-1}.

Then `L_h=Theta_R(h^-1)` for sufficiently small h, and `4lambda_h L_h>=1`. Thus for **the actual interacting vacuum**

    nu[X>=2L_h+t] <= C_R h^4 exp(-c t/h)/(1+t/(2L_h)), t>=0,
    E_nu[X² 1_{X>=2L_h}] <= C h².                  (AG-5)

In particular, for any fixed rho>0 and any region with `X_max>=rho h^-2`,

    nu[X>=rho h^-2] <= poly(h) exp[-c_rho h^-3]

for h sufficiently small, since `rho h^-2-2L_h` is order h^-2. The estimate remains valid if the event is empty, and is uniform over ambient graph size as long as the chosen region and collar permit the same E_D bound.

For any real bounded `|q_f|<=q_max`, the scalar-subtracted alpha=3/2 Wilson field is `B_h=-h^(1/2)sum_D q_f d_f`. The true-vacuum contribution of the above far-excursion event to its **uncentered second moment** satisfies

    E_nu[B_h² 1_{X>=2L_h}]
      <= h q_max² E_nu[X²1_{X>=2L_h}]
      <= (128 a_max q_max²/beta_min) h³.          (AG-6)

This excludes the large all-faces-curved branch that was admissible in the previous positive trial-wavefunction example **from the actual ground state**, up to these rigorous tail bounds. The previous trial state's total energy envelope alone could not achieve this, because the true ground-state identity was unavailable for that state.

## 4. What is *not* proved

The cutoff `2L_h=O_R(h^-1)` lies at the same scale as the allowed mean total curvature. The interval `0<=X<2L_h` still permits coherent fluctuations of order h^-1: their squared magnitude is of order h^-2, much larger than the desired `o(h^-1)` upper bound for `Var(sum q_f d_f)`. Therefore AG-1/AG-6 do **not** establish fixed-support connected covariance collapse or a positive spectral gap. They exclude unusually large coherent nonflat excursions, not collective fluctuations among moderately curved configurations.

For `alpha=3/2`, the required variance theorem remains

    Var_Omega(sum_{f in D_R} q_f d_f)=o(h^-1).      (OPEN)

The next noncircular obligation is a **moderate-curvature connected-covariance bound** within `X<=O_R(h^-1)` or an independent source-specific coercive/Poincare estimate proved from the actual Hamiltonian. Neither can be replaced by a gap assumption. The second quartic resolvent and R2 quantum continuum remain separate open gates. The Stage7/26 equality to the declared Hamiltonian remains an unresolved source-provenance requirement.

## 5. Reproducibility

The accompanying read-only `verify_regional_agmon.py` checks the exact coefficient algebra, absorption, exponential tail, second moment, fundamental SU(2) Casimir identity, and authentic three-rhombus spatial-seed incidence using symbolic and exact arithmetic. It does **not** verify an original Q14 temporal certificate, simulate SU(2), or establish the full theorem from finitely many tests: the proof is the operator argument above.