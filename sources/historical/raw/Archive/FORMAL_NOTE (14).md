# Continuum-stable Wilson polymer expansion: exact finite-scale construction and uncrossed admission gate

26 October 2026. Technical proof audit. **This note does not claim a convergent Penrose continuum expansion or a Yang–Mills mass gap.**

## 1. Regulator and exact finite-scale effective action

Let K_h be a finite spatial Penrose rhombus complex crossed with temporal lattice intervals, with uniformly bounded plaquette-to-link incidence. Let beta_p(h)=c_p/(g_3^2 h), 0<c_-<=c_p<=c_+, and time spacing a_t=kappa h with bounded positive kappa. Let S_h(U)=sum_p beta_p(1-(1/2)Tr W_p). For a chosen local gauge-equivariant coarse map pi_k and retained variables Y, define the **pushforward density** when a smooth local gauge/Haar disintegration is provided:

Z_{k}(Y)=int_{pi_k^{-1}(Y)} e^{-S_h(U)} dnu_{k,Y}(U),  F_k(Y)=-log Z_k(Y).

No claim that the fiber is a product or that dnu is Haar on every fiber. If gauge-fixing is used, include Faddeev-Popov/Jacobian determinants in dnu. Gauge invariance F_k(gY)=F_k(Y) follows only for an equivariant map and invariant disintegration.

For localized sources O_i coupled to t_i, exact partial derivatives of log Z_k(Y;t) at zero give conditional connected cumulants of O_i under the **actual** conditional Wilson fiber law. Their magnitude/decay is not controlled by the identity alone.

## 2. Background subtraction and exact finite-volume support decomposition

Choose a prescribed gauge-invariant local extraction A_k(Y) (local curvature terms, normalized counterterms, and compatible background Gaussian determinant). Define R_k=F_k-A_k. Given a finite collection of retained edge or block coordinates I and conditional/Haar averaging projections E_A onto variables A (which commute for fixed product-Haar reference), define

Psi_A = sum_{B subset A} (-1)^(|A|-|B|) E_B R_k,

with E_B R_k obtained by Haar-integrating all retained coordinates outside B. Then R_k=sum_{A subset I}Psi_A exactly, and E_{A\{i}}Psi_A=0 for i in A. (The constant term is included.) Note that bare coordinate Haar projections generally need not preserve *local* gauge invariance of each Psi_A if the retained coordinates carry shared vertex transformations; a gauge-invariant block-coordinate algebra, covariant projections, or orbit averaging is required. Exactness does not imply geometric connectedness, localization or smallness. The trivial bound ||Psi_A||infty<=2^|A| ||R_k||infty is inadequate.

To obtain genuine polymers, use a forest interpolation or linked-cumulant decomposition with respect to cuttable couplings **once the reference conditional measure, interpolation and boundary maps have been specified**. Connectedness then follows from the linked-cluster formula, but no decaying activity bound follows merely from formal connectedness.

## 3. Exact local frustration-moment identity and circularity test

For a selected link e, condition on other links: S_e(u)=B_e-u.k_e; F_e=B_e-|k_e| and Z_e=e^{-B_e} z(|k_e|), z(x)=2 I_1(x)/x. For a sparse set J with disjoint incident plaquette supports, the conditional Z factorizes; the diluted partition ratio is exactly the exterior expectation of a product of e^{B_e-B'_e}z(k'_e)/z(k_e). Hence

log(Z_full(beta')/Z_full(beta)) <= C |J|(1+log lambda) + log E_eta exp(sum_e(F_e-F'_e)).

To establish an O(|J|log lambda) comparison one still must bound the latter exponential moment to that order. It is NOT a consequence of the minimization or conditional fluctuation comparison. For opposed equal staples, F_e-F'_e=2 theta lambda pointwise; the full exterior probability may suppress these fields, but that requires a separate theorem. Assuming the exponential-moment bound as an RG input is tantamount to assuming the needed local free-energy/large-field control; it cannot be presented as a proof from the Wilson action.

## 4. A precise polymer convergence admission test

Let G_k be the effective coarse block adjacency graph with degree at most Delta, and assume that rigorous integration and local extraction yield a compatible hard-core polymer representation with activities w_k(Gamma), Gamma connected. Define

N_k(a)=sup_{z in G_k} sum_{Gamma contains z} |w_k(Gamma)| exp(a |Gamma|).

Assume |w_k(Gamma)|<=q_k^{|Gamma|} and the rooted connected-set count is bounded by A_Delta^n (A_Delta=e(Delta+1) is conservative). Then

N_k(a) <= [A_Delta exp(a) q_k] / [1-A_Delta exp(a) q_k]

whenever A_Delta exp(a) q_k<1. Moreover, for incompatibility given by sharing or bordering one block, if N_k(a)<=a/(Delta+1) (with a>=1, for example) the Kotecky--Preiss condition follows by charging each incompatible polymer to one of at most (Delta+1)|Gamma| coarse sites. This is an **implication theorem**. Wilson w_k(Gamma) are not presently known to obey any such q_k uniformly in k,h,volume.

A **complete** continuum-stable induction needs: (i) gauge-equivariant coarse maps and fiber measures; (ii) scale-uniform small-field/background covariance and determinants; (iii) unconditional thin-contour and mixed good/bad pattern bounds; (iv) local extraction plus bounded higher connected cumulants; (v) activity bound q_k with A_Delta exp(a)q_k uniformly below convergence threshold; (vi) positivity and transfer/Hamiltonian reconstruction; (vii) separate IR spectral-gap and observability estimates. Neither UV stability nor convergence of a polymer expansion alone implies (vii).

## 5. Controlled domain already available, and physical trajectory

For the original plaquette expansion e^{-beta d}=1+f, the singleton activity is w({p})=e^{-beta} 2I_1(beta)/beta-1, tending to -1 when beta tends to infinity. Hence no weak-polymer activity on the bare variables for beta~1/h. The small-beta finite-volume expansion is volume uniform if its explicit KP norm is small; it does not cover the physical large-beta continuum family. The exact planar Wilson character convolution is not a surrogate for the joint spacetime RG.

## 6. Deliverable and conclusion

**Established:** exact finite-scale effective-action definitions, conditional cumulant identities, supported Möbius decomposition on a specified reference coordinate product, exact local frustration identity, and quantitative abstract rooted-polymer convergence implication.

**Not established:** gauge-equivariant fiber disintegration and local extraction with uniform constants on arbitrary Penrose spacetime blocks; noncircular uniform exponential-moment/contour control; residual activity q_k bound across scales; compatible Hamiltonian reconstruction; continuum R3/R2 mass gap.

Immediate noncircular research task: prove a scale-local conditional free-energy inequality for a genuine gauge-compatible coarse fiber by comparison with a background minimum **whose exterior excess action is controlled in the full interacting measure**, including thin/frustrated defects. This cannot be inferred from local minimization alone.

Reference: T. Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories*, Commun. Math. Phys. 102 (1985), 255-275, DOI 10.1007/BF01229380. This concerns UV stability in its stated setting, not a Penrose continuum mass-gap theorem.
