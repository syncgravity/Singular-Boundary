# R3-IR — Genuine SU(2) coherent-wavefunction witness and limits of the fixed-support covariance method

**Date:** 2026-10-28. **Claim status:** exact finite SU(2) gauge-invariant *trial-wavefunction construction* and a rigorous obstruction to inferring covariance collapse from the existing **energy envelope + mean-curvature + carré-du-champ** estimates alone. This is **not** an eigenstate or a counterexample to a gap in the actual interacting Hamiltonian. No simulations or historical data have been altered.

## Source dependency and provenance

Current private GitHub audit branch `audit/2026-10-28-independent-reconstruction` inspected before the proof. Relevant historical-derived notes: `R3_IR_STRONG_FIELD_MEAN_CURVATURE_AND_TORQUE_LIMIT_2026-10-28.md` (MC-1), `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md` (FS-1), `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md` (ER-1), `R3_IR_MESOSCOPIC_SOURCE_COMPRESSION_2026-10-28.md` (SC-1), and `R3_IR_PHYSICAL_COUPLING_COVARIANCE_CONCENTRATION_2026-10-28.md` (CC-1). Their declared Penrose Hamiltonian coefficients have *not* been independently identified with every original Stage 7/26 simulation coefficient. The exact canonical three-rhombus Z^5 spatial fixture used in the verifier has three faces and ten edges; it is **not** the temporal Q14 cavity.

## Model

Take a finite connected simply connected embedded planar rhombus disk `G_h=(V_h,E_h,F_h)` of face edge length h, with every edge in at most two four-edge faces. Assume a bounded fixed physical domain, with `c_0 h^-2 <= F_h <= C_0 h^-2` and bounded area shape factors `0<sigma_-<=sigma_f<=sigma_+`. Work on the *actual* link Hilbert space `L²(SU(2)^E, dU)` with physical vertex-gauge group and

`H_h = sum_e a_e (-Delta_e) + sum_f b_f (1-p_f),  p_f(U)=(1/2)ReTr(W_f(U))`,

`0<a_e<=a_max`, `0<=b_f<=beta_max h^-2`, and `-Delta chi_j=j(j+1)chi_j`. Let `d_f=1-p_f` and `Gamma(A)=sum_e a_e |grad_e A|²`.

A smooth nonnegative physical test function phi, not identically zero, has fixed support away from any patch boundary, and define `q_f=sigma_f phi(x_f)`, `q_f` uniformly bounded, and the `alpha=3/2` source

`A_h = h^(1/2) sum_f q_f p_f`.

Assume the ordinary face-center Riemann sum `I_h=h² sum_f q_f -> I_phi=integral phi(x) dx>0`. This holds for the stated embedded fixed-domain refinement when phi has compact interior support.

## Theorem CW-1: fully gauge-invariant coherent positive trial states

For kappa>0, define `Z_kappa=int_SU2 exp(2kappa p(U)) dU = I_1(2kappa)/kappa`, with modified Bessel I_1, and

`Psi_±(U)=Z_kappa^(-F_h/2) exp(±kappa sum_f p_f(U))`.

Each is a **normalized, strictly positive, vertex-gauge-invariant** smooth wavefunction, rather than an arbitrary distribution on face traces. On a simply connected planar disk, maximal-tree gauge fixing leaves `E-(V-1)=F` independent SU(2) chord variables, and triangular elimination along a dual spanning tree transforms them to the based face holonomies preserving product Haar. Therefore the face traces are independent under product link Haar, justifying the normalization and all one-face moment calculations below. This factorization is *not asserted* for a spatial surface with handles or extra topological constraints.

Put `r_kappa = int p(U) exp(2kappa p(U))/Z_kappa dU`, `u_kappa = int p(U)^2 exp(2kappa p(U))/Z_kappa dU`. The exact SU(2) link metric gives

- `E_+(p_f)=r_kappa`, `E_-(p_f)=-r_kappa`;
- `1-r_kappa <=3/(4kappa)` (the earlier MC-1 one-link estimate);
- `u_kappa-r_kappa²=O(kappa^-2)` for kappa large, by the Haar class-angle density and Laplace's estimate;
- `E_± |grad_e p_f|²=3r_kappa/(8kappa)` for each edge of face f; and
- `s_h=<Psi_+,Psi_-> =Z_kappa^(-F_h)`.

For kappa=h^-1, `s_h` is exponentially small in `F_h/h`: indeed `Z_kappa>=c exp(kappa)` for large kappa, from the Haar-positive set p>=1/2. Thus `s_h=o(h^n)` for each n>0.

Choose any rarity exponent `1<=p<=3`, set `epsilon_h=h^p`, and define the normalized strictly positive physical trial wavefunction

`Phi_h = [sqrt(1-epsilon_h) Psi_+ + sqrt(epsilon_h) Psi_-]/sqrt(N_h)`

with `N_h =1+2 sqrt(epsilon_h(1-epsilon_h)) s_h`.

## Theorem CW-2: same energy/curvature/gradient scaling, but arbitrary coherent variance survival

For the above *genuine SU(2)* trial states,

**(a)** ` <Phi_h,H_h Phi_h> =O(h^-3)` for every 1<=p<=3.

**(b)** `F_h^-1 sum_f <Phi_h,d_f Phi_h> =O(h)`.

**(c)** `<Phi_h,Gamma(A_h) Phi_h>=O(1)`.

**(d)** The exact asymptotic variance is

**`Var_{Phi_h}(A_h)=4 I_phi² h^(p-3)(1+o(1))+O(h)`**.

In particular, p=3 yields a *strictly positive finite limit* `4 I_phi²`, whereas p=1 gives variance growing like `4 I_phi² h^-2`. The latter matches the order of the existing fixed-support, regionally derived positive-deficit upper estimate, exhibiting its sharpness within the class of positive physical trial states obeying the same global envelopes.

### Complete proof of energy and gradient estimates

The face-coordinate Haar factorization gives `E_± p_f =±r_kappa`. For either sign, with `∇_e Psi_±=±kappa Psi_± sum_{f:e in boundary f} ∇_e p_f`, the maximum edge incidence two and `(sum_{i=1}^m v_i)^2<=m sum|v_i|²` yield

`<Psi_±,H_E Psi_±> <= 2kappa² sum_f sum_{e∈boundary f} a_e E_±|∇_e p_f|² <=3 a_max kappa r_kappa F_h`.

The magnetic expectation in Psi_+ is `(1-r_kappa) sum_f b_f<= 3 B_total/(4kappa)`, and in Psi_- it is `(1+r_kappa) B_total<=2B_total`, with `B_total<= beta_max F_h/h²=O(h^-4)`. For kappa=h^-1, `E_+=O(h^-3)` and `E_-=O(h^-4)`. Since `H_h>=0` as a quadratic form and `N_h>=1`, the form triangle inequality gives

`<Phi_h,H_h Phi_h> <=2[(1-epsilon_h)E_+ + epsilon_h E_-] <=C[h^-3+h^(p-4)]=O(h^-3)` for p>=1.

For each face, the exact mixed density gives

`<Phi_h,d_f Phi_h> =[(1-eps)(1-r)+eps(1+r)+2 sqrt(eps(1-eps)) s_h]/N_h`.

With `1-r=O(h)`, `eps<=h`, and negligible `s_h`, this is O(h). This proves (b). For the Wilson source,

`Gamma(A_h) <=4 a_max q_max² h sum_f d_f`

pointwise, from `|grad_e p_f|²=(1-p_f²)/4<=d_f/2` and edge multiplicity at most two. Taking the Phi expectation proves (c), since `h F_h O(h)=O(1)`.

### Exact variance formula and asymptotics

Write `Q_h=sum_f q_f`, `m_h=h^(1/2) r_kappa Q_h`, `v_h=h (u_kappa-r_kappa²)sum_f q_f²`, and `v_H=h sum_f q_f²/4`. Haar independence and the fact that `Psi_+ Psi_-=s_h` is constant give

`<Phi_h,A_h Phi_h> =[(1-2eps)m_h]/N_h`,

`<Phi_h,A_h² Phi_h> =[m_h²+v_h+2sqrt(eps(1-eps))s_h v_H]/N_h`.

These are **exact** at finite h. Since `sum q_f²=O(h^-2)`, `v_h=O(h)` for kappa=h^-1, and `s_h` is superpolynomially small,

`Var_{Phi_h}(A_h)=v_h+4eps(1-eps)m_h² +o(h^n)` for any fixed n (the negligible terms may carry polynomial prefactors). Since `m_h²=h r_kappa² Q_h²` and `h² Q_h->I_phi`, the stated asymptotic follows.

## Exact logical scope and next gate

This witness does NOT solve the fixed-support covariance problem at the true interacting vacuum, does not produce a low-energy eigenvector at excitation O(1), and does not contradict ER-1 or the physical sector projection. Although its total energy is on the **same scale** as the available variational upper bound on the true ground energy, no small **energy excess above E0** has been proved. The source-gradient estimate (c) is a state expectation and not by itself the exact vacuum f-sum identity in an arbitrary trial state.

It proves that **positivity, SU(2) gauge invariance, a volume-order ground-energy envelope, mean curvature O(h), and an O(1) source-gradient expectation cannot imply the desired fixed-support connected covariance bound.** A valid proof for the true vacuum must use its minimizing/eigenstate structure more sharply, for example by deriving a relative-energy penalty or an exponential/tail exclusion of coherent curvature excursions. That estimate would need to be proved, not assumed as a mixing axiom.

Recommended next theorem: an **energy-localized coherent-excursion exclusion** for the true vacuum or fixed-energy physical sector, quantified using a positive quadratic fluctuation of a macroscopic Wilson source and a noncircular local kinetic comparison. The required bound is `Var_{Omega_h}(sum_f q_f d_f)=o(h^-1)` for alpha=3/2. The present trial example explains why energy and first curvature moments alone do not give it. It does not imply the true vacuum has such rare tails.

**Proof statuses:** CW-1 and CW-2 independently proved for explicit gauge-invariant finite-regulator SU(2) trial wavefunctions. Transfer to actual interacting vacuum: OPEN. R3-IR full physical and continuum gap: OPEN. Original Stage 7/26 action source identity: unresolved provenance.

**Reproducibility:** `verify_coherent_trial.py` checks the Bessel normalization derivative, fundamental SU(2) Casimir, exact superposition variance formulas, rarity exponents and canonical 3-seed incidence. It performs no simulation. Historical files untouched.