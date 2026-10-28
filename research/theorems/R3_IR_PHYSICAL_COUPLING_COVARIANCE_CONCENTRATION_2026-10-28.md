# R3-IR — Physical-coupling covariance concentration and necessary mesoscopic coherence

**Date:** 2026-10-28. **Scope:** exact consequences of a previously proved *interacting* Penrose regional mean-curvature estimate at the distinguished (undeformed) coupling. No Monte Carlo, no new Yang–Mills sample data, and no physical mass-gap or nontrivial continuum-field claim. Originals and main preserved.

## Source and assumptions

Primary upstream source: `research/theorems/R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md` (MI-3), based on `R3_IR_STRONG_FIELD_MEAN_CURVATURE_AND_TORQUE_LIMIT_2026-10-28.md`. Treat its declared geometric coefficients as assumptions, **not** independently Stage26-certified action data. A finite, face-complete Penrose rhombus regulator has physical edge length h and a physical interior disk D_R of radius fixed R>0, with a complete collar. Its exact, positive SU(2) Wilson Hamiltonian has a unique gauge-invariant ground state Omega, and nu=Omega²dU is its probability measure. Write p_f=(1/2)ReTr(W_f), d_f=1-p_f in [0,2], and let phi=(1+sqrt(5))/2 denote the *golden ratio*, distinct from a real bounded test function varphi(x).

The upstream MI-3 theorem states, for R/h>1,
  delta_h := |D_R|^(-1) sum_{f in D_R} E_nu[d_f]
  <= (3phi/sqrt(2)) g3² h +16phi² (R/h+1)/(R/h-1)².
For h<=R/2 this implies delta_h<=K_R h, with
  K_R=(3phi/sqrt(2))g3²+96phi²/R.
If each rhombus area lies in [sigma_-h²,sigma_+h²] and every face center is within R, disjoint face interiors imply |D_R| h²<= 4pi R²/sigma_- for h<=R/2.

## Theorem CC-1: finite-volume interacting covariance trace concentration

Define the *true, undeformed* physical-vacuum covariance matrix on the face set D_R:
  C_h(f,g)=E_nu[(p_f-Ep_f)(p_g-Ep_g)].
C_h is positive semidefinite. Since 0<=d_f<=2,
  Var(p_f)<=E[(p_f-1)²]=E[d_f²]<=2E[d_f].
Therefore
  Tr C_h <= 2|D_R|delta_h <=2K_R h |D_R|.                         (CC-1)
No spatial or temporal mixing, gauge fixing, finite-volume mass gap lower bound, or Gaussian approximation is used.

For any fixed exponent 0<eta<1 (after expressing h in fixed physical units), the number of eigenvalues of C_h exceeding h^eta is at most
  N_h^{high}(eta)<=2K_R |D_R| h^(1-eta).
Thus the **fraction** of covariance eigenvectors with eigenvalue >h^eta vanishes as h→0. On the orthogonal complement of these exceptional directions, every coefficient vector w obeys
  Var( sum_f w_f p_f ) <= h^eta ||w||_2².
For w_f=h sigma_f varphi(x_f), ||w||²<=sigma_+² ||varphi||_infty² |D_R|h², which is uniformly bounded. These exceptional directions depend on the unknown interacting covariance; the theorem does **not** construct a particular smooth physical continuum field.

## Theorem CC-2: random-sign source collapse at the *distinguished physical coupling*

For fixed real bounded varphi supported on D_R, let epsilon_f be independent uniform signs (auxiliary deterministic-proof randomization of observable coefficients only, never an MCMC of U). Define the centered signed physical Wilson source
  A_h^epsilon = h sum_{f in D_R} sigma_f varphi(x_f) epsilon_f (p_f-Ep_f).
Exact finite sign averaging annihilates all off-diagonal covariances:
  E_epsilon Var_nu(A_h^epsilon)
   =h² sum_f sigma_f² varphi(x_f)² Var_nu(p_f)
   <=2sigma_+²||varphi||_infty² (|D_R|h²) K_R h.                  (CC-2)
Consequently E_epsilon Var<=[8pi R² sigma_+² K_R/sigma_-]||varphi||_infty² h.
There exists at least one deterministic sign assignment obeying this bound. For each 0<eta<1, the fraction of assignments whose variance exceeds h^eta is O(h^(1-eta)). Along a predetermined dyadic refinement, almost every independent sign sequence has variance→0 (Borel–Cantelli).

For every finite physical Hamiltonian K=H-E0≥0 and centered A, its Euclidean connected source correlation satisfies 0<=C_A(t)=<AΩ,e^(-tK)AΩ><=Var(A), for every t>=0. Thus all the above signed-source statements also control correlations **uniformly over positive physical time**, in absolute amplitude. They do **not** establish a model-independent exponential decay rate or a positive mass gap.

## Theorem CC-3: the necessity of mesoscopic off-diagonal correlations

Let A_h(varphi)=h sum_f sigma_f varphi(x_f) (p_f-Ep_f) be the original **unsiged, smooth** source. Decompose its variance into V_near(h,rho) from face pairs with Euclidean center separation <=rho and V_far from all other pairs.

Each face g with center within rho of a given face f lies within the ball of radius rho+2h about x_f, and has area >=sigma_-h². Hence the maximal number of such faces is
  M(h,rho)<= pi(rho+2h)²/(sigma_- h²).
By positive semidefinite covariance, |C_fg|<=sqrt(C_ff C_gg)<=(C_ff+C_gg)/2. Summing over symmetric near-neighbor pairs and applying CC-1 gives the exact bound
  |V_near(h,rho)|
  <= h² sigma_+²||varphi||_infty² M(h,rho) Tr C_h
  <= [8pi² R² sigma_+² K_R/sigma_-²]||varphi||_infty²
     (rho+2h)²/h.                                                   (CC-3)
Therefore, for any scale rho_h with h<=rho_h and (rho_h+2h)²/h→0 (e.g. rho_h=h^(2/3) in fixed units), V_near(h,rho_h)→0, **at the exact physical coupling**.

If a physical smooth Wilson test field has liminf Var(A_h(varphi))>=v>0, then necessarily liminf V_far(h,rho_h)>=v for every such rho_h. Persistent physical variance requires coherent contributions from face pairs beyond every near-pair scale rho_h=o(sqrt(h)) (with h<<rho_h). This is a necessary *covariance* statement, not evidence that such correlations exist.

## Theorem CC-4: mean flatness and a bounded first moment do not eliminate coherent modes

An exact abstract static covariance witness shows why one cannot infer smooth-source variance collapse from CC-1 alone. For h=1/m and F=m² face labels, let Z_h be one Bernoulli variable with probability q_h=h² and set p_f=1−2Z_h for **all** f. Then E[d_f]=2h² (stronger than the proven O(h)), and the unsiged normalized source with sigma_f=varphi_f=1 satisfies
  Var[h sum_f p_f]=4(1−h²)→4.
Its random-sign averaged variance is only 4h²(1−h²)→0. The covariance has rank one: all surviving variance is in a fully coherent face mode. This is **not** claimed to be the SU(2) Wilson interacting ground-state measure, and it does not invalidate the Hamiltonian-specific first-moment bound. It proves the *logical insufficiency* of diagonal/mean-flatness information alone.

## Consequence for the mass-gap research program

At the undeformed physical coupling, the critical h^(-1) area-smeared Wilson source cannot retain nonzero variance through spatially independent or uniformly short-range local fluctuations. Its survival would require coherent spatial covariance tails; their **sign and size** remain open, as do the nonlinear pointwise variance, uniform temporal spectral separation, and R2 reconstruction.

An exact useful *next theorem* would show, without assuming the desired gap, that for a fixed smooth varphi,
  h² sum_{f,g:|x_f-x_g|>rho_h} sigma_f sigma_g varphi_f varphi_g Cov_nu(p_f,p_g) →0
at a scale rho_h=o(sqrt(h)). Together with CC-3, this would give Var(A_h(varphi))→0 at (1,1). A stronger sufficient hypothesis is a regulator-uniform, ground-state covariance row-sum control of order o(1/h) times individual variance; this is not currently established and cannot be introduced as a free mixing assumption. Alternatively retain the possibility of a coherent nontrivial field and derive its full spectral measure rather than choosing triviality in advance.

**Evidence status:** CC-1/2/3 derived independently from MI-3 under the declared geometric coefficients and complete interior-collar conditions. CC-4 is an exact rational abstract covariance witness. None establishes or refutes the Yang–Mills mass gap. No simulations, historical reconstructions, or replacement datasets.
