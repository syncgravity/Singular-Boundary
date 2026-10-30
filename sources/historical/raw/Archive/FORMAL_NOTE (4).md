# Local nonflat gauge and large-field contours: rigorous scope (26 October 2026)

## Setting
Let K be a finite oriented 3D spacetime cell complex with bounded degrees, each plaquette bounded by at most four links (after suitable subdivision), and SU(2) Wilson action S(U)=sum_p beta_p(1-p(W_p)), p(W)=Tr(W)/2. For x,y in SU(2) let d(x,y) be their geodesic distance in [0,pi], so d(I,W)=theta and 1-p(W)=1-cos(theta). Fix a simply connected local subcomplex Q with a rooted spanning tree T and a prescribed system of combinatorial spanning surfaces Sigma_e for each non-tree edge e, satisfying partial boundary relation of the fundamental tree cycle C_e; let M_Q=max_e |Sigma_e|. This is an **explicit geometric hypothesis** that must be verified for Penrose spacetime blocks and is not guaranteed by simple connectivity alone.

## Theorem 1. Local axial gauge with a nonflat retained background
Gauge-transform the tree links to identity. For a non-tree edge e the resulting U_e is (up to inverse and conjugations) a product of plaquette holonomies transported to the root over Sigma_e, in an order determined by a shelling of the surface. Assuming such a shelling exists, triangle inequality and conjugation invariance of SU(2) geodesic distance imply
  d(I,U_e^T) <= sum_{p in Sigma_e} d(I,W_p) <= M_Q max_{p in Q} d(I,W_p).
If 1-p(W_p)<=delta<=1 on Q, then d(I,W_p)<= (pi/sqrt(2))*sqrt(delta) (a conservative bound); hence max_e d(I,U_e^T)<= (pi/sqrt(2))*M_Q sqrt(delta).
The same statements hold around a nontrivial specified background V_e by applying the tree construction to relative transports U_e V_e^{-1}, provided relative plaquette holonomies are controlled. This is not a global flatness conclusion. At overlaps of patches, gauge-transition data must be retained, rather than set to one.

## Theorem 2. A Wilson-specific local Hessian difference
In any fixed smooth system of exponential link coordinates, the 4-link plaquette function f_p(U)=1-p(W_p) has bounded third derivatives on compact SU(2)^4. Hence for two link backgrounds A and B whose corresponding link entries obey max_{e in partial p}d(A_e,B_e)<=eta, the Hessian bilinear forms satisfy
 |H_p(A)[X,X]-H_p(B)[X,X]| <= C beta_p eta sum_{e in partial p}|X_e|^2.
After summing plaquettes, bounded incidence gives
 |H(A)[X,X]-H(B)[X,X]| <= C D beta_max eta sum_e |X_e|^2.
This does **not** bound the relative form perturbation uniformly without a suitable local coercivity estimate. If H_ref[X,X] >= mu_Q sum_e |X_e|^2 in the same coordinate norm, then relative perturbation <= C D beta_max eta/mu_Q. This conclusion is conditional on the stated coercivity and on gauge fixing. For a background adapted to plaquette curvature, one must compare its own covariant Hodge energy rather than assume it is close to the trivial background over a macroscopic Q.

Combining theorems 1 and 2 on a patch of M_Q faces yields sufficient condition C D (beta_max/mu_Q) M_Q sqrt(delta) <1. This may be useful on mesoscopic patches but does not prove cutoff-uniformity: beta_max/mu_Q and M_Q must be bounded together on the specified discretization. In particular, the previous delta=lambda^{-1/2} gives link deviation O(M_Q lambda^{-1/4}).

## Theorem 3. Exact contour probability identity and its current limitation
For any finite plaquette set X and threshold delta, define L_X={1-p(W_p)>delta for all p in X}. For any t with 0<=t<=min_{p in X} beta_p, the exponential Markov inequality gives
 mu_beta(L_X) <= exp(-t delta |X|) Z(beta-t 1_X)/Z(beta),
where Z(beta)=int exp[-sum_p beta_p(1-p(W_p))]dU. This is exact for the full spatial-temporal gauge theory. Equivalently,
 log[Z(beta-t1_X)/Z(beta)] = int_0^t sum_{p in X} E_{beta-s1_X}[1-p(W_p)] ds.
Thus if a new, **uniform local defect estimate** E_{beta-s1_X}[1-p(W_p)] <= q for p in X and all s in [0,t], then
 mu_beta(L_X) <= exp[-t(delta-q)|X|].
This is a genuine exponential connected-set contour theorem under a verifiable probabilistic hypothesis, with **no global-volume factor**. In particular t=theta beta_min for 0<theta<1 gives exp[-theta beta_min (delta-q)|X|]. The prior spatially averaged defect estimate is insufficient for the required pointwise bound, especially after selectively lowering couplings on X. No such uniform local defect bound is established for the Penrose 2+1D Wilson measure here.

## Theorem 4. Exact one-face tail in free-boundary 2D reference theory, as a comparison control
For a single SU(2) face under d rho_beta(W)=exp[-beta(1-p(W))]dW/Z_1(beta), where Z_1(beta)=exp(-beta) 2 I_1(beta)/beta,
  rho_beta{1-p>delta} <= e^{-beta delta}/Z_1(beta).
For beta>=1, the SU(2) Laplace integral gives Z_1(beta)>=c beta^{-3/2}, hence
  rho_beta{1-p>delta} <= C beta^{3/2} exp(-beta delta).
Because face holonomies are independent in a simply connected planar disk with free boundaries, for any set X,
  P(all p in X large) <= [C beta_max^{3/2} exp(-beta_min delta)]^{|X|}
for uniform comparable beta. This is a genuine connected-set exponential bound **in the 2D reference theory only**, not in 2+1D.

## Why the 3D local-defect hypothesis is substantive
Condition on all external links adjoining a target plaquette. Temporal link staples can create an effective SU(2) field favoring a nontrivial or frustrated target holonomy. A uniform defect estimate for every exterior conditioning is therefore false without an energetic dominance restriction. The unconditioned local defect estimate along the physical scaling might still be true, but is not supplied by finite-volume averaged bounds. Neither this note nor the previously proved large-field density estimate establishes polymer Peierls suppression in the physical 3D theory.

## Geometry audit
Penrose rhombi provide uniform *local* shape regularity (two prototiles). They do not by themselves imply bounded-area fillings for all tree loops inside arbitrary 3D spacetime block boundaries, spectral equivalence of the literal Wilson Hessian and an FEEC Hodge Laplacian, or background-covariant invertibility. These must be checked for the actual block family.

## R3/R2
Proved: exact local axial-gauge curvature-accumulation estimate under the filling hypothesis; compact-group Wilson Hessian Lipschitz bound; exact full-action contour partition-function identity; contingent contour suppression given a pointwise diluted-coupling defect bound; exponential tail in planar free-boundary reference model.
Unproved: cutoff-uniform covariant Hessian on Penrose spacetime blocks, pointwise diluted-coupling defect bound in 3D, physical connected large-field polymer expansion, uniform R3, continuum R2.
