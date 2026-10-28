# R3-IR: Exact nonlinear coupling-averaged variance collapse for area-smeared Penrose Wilson fields

Date: 2026-10-28. Evidence: independently proved finite-volume nonlinear SU(2) result; coupled-shape parameter average and almost-everywhere refinement statement. **Does not prove variance collapse at the distinguished physical multipliers (1,1), nontrivial continuum existence, or a positive mass gap.** No Monte Carlo, no changes to historical sources.

## Model, physical source, assumptions

Let G_h be a finite face-complete planar SU(2) rhombus complex. Each face has four edges, and each edge belongs to at most two faces. The one-link electric Casimir -Delta has first nonzero eigenvalue 3/4. Let F_h be the total number of faces, and assume F_h*h² <= A0 for a fixed A0. Let D_h be ANY face subset, including a fixed interior physical region. Its faces have areas h² sigma_j for j in {-,+}, with 0<sigma_-<=sigma_+ and fixed shape factors. The electric weights satisfy 0<a_e<=a_max independent of h. All background magnetic weights are nonnegative and bounded by 2 beta_max/h². In D_h, define D_j=sum_{f in D_h,shape j}(1-p_f) and positive baseline coupling b_j=beta_j/h², beta_j>0. Define H_h(s)=sum_e a_e(-Delta_e)+sum_{f not in D_h} b_f(1-p_f)+sum_j s_j b_j D_j, for s=(s_-,s_+) in [1,2]². Let E_h(s) be its ground energy, Omega_h(s) its unique positive gauge-invariant ground vector, K_s=H_h(s)-E_h(s), and Q_s=I-|Omega_h(s)><Omega_h(s)|. At s=(1,1), the Hamiltonian has the declared original geometric Wilson couplings. The two-parameter variation away from (1,1) is a *deformed family*: it does not preserve the original single-coupling geometric prescription.

The area-smeared source for the (piecewise-constant) physical test 1_D is A_h=h sum_{f in D_h} sigma_f p_f. This equals h^(-1) sum_{f in D_h} Area_f p_f. The centered source is A_h-<A_h>_s = -h sum_j sigma_j (D_j-<D_j>_s). Let V_h(s)=Var_s(A_h), M1_h(s)=<Q_s A_h Omega_s,K_s Q_s A_h Omega_s>, and chi_h(s)=2<Q_s A_h Omega_s,K_s^(-1)Q_s A_h Omega_s>.

## Theorem CR-1: exact spectral response and first moment

Every finite H_h(s) has compact resolvent and a unique positive ground vector. All real parameter derivatives are analytic locally and satisfy

d_j E_h=b_j <D_j>_s,
-d_j² E_h=2 b_j² <Q_s D_j Omega_s, K_s^(-1) Q_s D_j Omega_s>.

For the bounded gauge-invariant multiplication source A_h the ground-state transform gives
M1_h(s)=sum_e a_e int |nabla_e A_h|² |Omega_s|² dU.
Using |nabla_e p_f|<=1/2 and at most two faces per edge,
M1_h(s) <= 4 a_max sigma_+² F_h h².

The vacuum-orthogonal spectral measure mu_A yields Cauchy-Schwarz
V_h(s)² <= M1_h(s) (chi_h(s)/2).

## Theorem CR-2: integrated susceptibility bound in two coupling parameters

Let beta_max bound EVERY baseline magnetic coefficient times h². The finite graph total electric and magnetic weights obey A_tot=sum_e a_e<=4a_max F_h and B_tot(s)<=2 beta_max F_h/h². The previously proved global trial inequality gives for all s in [1,2]²
0 <= E_h(s) <= (3/sqrt(2))*sqrt(A_tot B_tot(s)) <= 6 F_h sqrt(a_max beta_max)/h.

For fixed other coupling, E_h is nonnegative, nondecreasing and concave in s_j, so
integral_{s_j=1}^2 (-d_j² E_h) ds_j = d_j E_h(1)-d_j E_h(2)
 <= d_j E_h(1) <= E_h(s_j=1)-E_h(s_j=0)
 <= 6 F_h sqrt(a_max beta_max)/h.
The last comparison is valid even with all other magnetic terms present, since they remain nonnegative; the trial bound applies at s_j=1 and the ground energy at s_j=0 is nonnegative.

Let T_ij(s)=2<Q_s D_i Omega_s,K_s^(-1)Q_s D_j Omega_s>, a positive semidefinite 2x2 matrix. Since A_h is centered as -h sum_j sigma_j D_j,
chi_h(s)=h² sigma^T T(s) sigma
 <= 2h² sum_j sigma_j² T_jj(s)
 =2h² sum_j (sigma_j²/b_j²)(-d_j² E_h(s)).

Integrating over the full unit square gives
integral_[1,2]² chi_h(s) ds
 <= 12 F_h h² sqrt(a_max beta_max)/h * sum_j sigma_j²/b_j².
Using b_j=beta_j/h² this is
<=12 (F_h h²) sqrt(a_max beta_max) h³ sum_j sigma_j²/beta_j².

Combining with the first moment and spectral Cauchy yields the **nonlinear interacting variance theorem**

integral_[1,2]² V_h(s)² ds
 <= C (F_h h²)² h³ <= C A0² h³,

where an explicit permissible constant is
C=24 a_max^(3/2) sigma_+² sqrt(beta_max) (sigma_-²/beta_-²+sigma_+²/beta_+²).

No positivity of an *interacting* spectral gap uniform in h, no Gaussian approximation and no spatial/temporal mixing was assumed.

## Corollary CR-3: generic-coupling variance triviality

For any epsilon>0, the Lebesgue measure of coupling pairs s in [1,2]² satisfying V_h(s)>epsilon is at most C A0² h³/epsilon². For every predetermined geometric refinement h_n with sum_n h_n³<infinity (e.g. dyadic h_n=h0*2^(-n)), Tonelli yields sum_n V_{h_n}(s)²<infinity for almost every fixed s, hence V_{h_n}(s)->0. This concerns the exact nonlinear SU(2) vacuum for almost every fixed *deformed* coupling pair; it does **not** prove V_{h_n}(1,1)->0.

## Corollary CR-4: a precise additional gate at the distinguished physical point

Suppose additionally the functions V_h(s) have a uniform (in h and volume) Lipschitz constant L on [1,2]² in the sup norm. A nonnegative V with V(1,1)=v would exceed v/2 on a quadrant of side min(1,v/(2L)). The integrated CR-2 theorem then forces v=O(h^(3/4)) (or better if L=0). Thus a uniform coupling-response modulus would promote the almost-everywhere theorem to the physical point. **Such a modulus is not proved.** Its derivative is a connected inverse-energy three-source susceptibility; assuming it without derivation would be a hidden version of interacting temporal control.

Analyticity for each finite h does not imply a uniform modulus. Analytic spikes can concentrate near (1,1) on shrinking coupling neighborhoods. The exact model-dependent behavior at the distinguished point remains open.

## Critical limits and reproducibility

This result constrains a specific unrenormalized area-smeared, h^(-1) source supported on D_h. It does not show that the actual physical Wilson theory has a trivial continuum, and it does not control every smooth signed test function. It uses an intentionally deformed two-parameter coupling family (thin and thick rhombus classes), while the intended physical model sits at (1,1). No inference about mass-gap positivity or negativity follows.

Deterministic exact check: scripts/audit/verify_coupling_averaged_variance.py, including a two-level Kato susceptibility identity, symbolic h-scaling and the Lipschitz-to-pointwise exponent. Original Penrose and square numerical chains and archival certificates remain untouched.

Next critical theorem: a model-derived, regulator-uniform coupling-response modulus for the physical source *or* an independent fixed-coupling nonlinear covariance estimate, with correct boundary and temporal energy normalization.