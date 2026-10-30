# Exact mixed spatial–temporal Wilson blocking: coefficient identity and a non-smallness theorem

Date: 2026-10-26. Scope: finite SU(2) Wilson spacetime gauge theory on square/Penrose bounded-incidence rhombic complexes. The result applies to a two-plaquette sub-block with one spatial and one temporal plaquette meeting at a shared link; it does NOT purport to evaluate the full Penrose effective action with all other incident plaquettes present.

## 1. Wilson coefficient functional, exact and gauge invariant

Let B be a finite set of integrated links and Y the retained links. On a finite spacetime complex with plaquette Wilson couplings beta_p>=0 define

 Z_B(Y;beta) = integral_{SU(2)^B} exp(sum_p beta_p p(U_p(X,Y))) dX,
 F_B(Y;beta) = -log Z_B(Y;beta).

The log exists, is real analytic in finite-dimensional positive beta, and is gauge invariant under transformations of the retained boundary variables compatible with the original local gauge action. For source plaquettes p_i and all n>=1,

 partial_{beta_{i1}} ... partial_{beta_{in}} log Z_B(Y;beta) = kappa_n(p_{i1},...,p_{in} | Y),

the conditional joint cumulant in the EXACT interior-link Wilson distribution at fixed retained boundary Y. In particular the mixed second derivative is the connected covariance. These are exact dynamical coefficients, not assumed small.

Any orthonormal gauge-invariant boundary spin-network basis {S_alpha} gives an EXACT L2 coefficient prescription

 c_alpha = integral F_B(Y) conjugate(S_alpha(Y)) dY

(where invariant Haar measure is used on the retained boundary links), and F_B=sum_alpha c_alpha S_alpha in L2. At finite B smoothness of F_B implies good spectral convergence, but no uniform-in-beta, volume or cutoff bound follows.

## 2. Exact mixed spatial–temporal face block

Take one spatial face and one temporal face meeting in exactly one shared link U, with remaining ordered boundary paths A and B so that W_s=AU and W_t=U^{-1}B. Put V=AB, v=p(V)=Tr(V)/2. Then

 Z_{t,s}(V)=integral exp[t p(AU)+s p(U^{-1}B)]dU
 = z(sqrt(t^2+s^2+2ts v)), z(x)=2 I_1(x)/x, z(0)=1.

Proof: identify SU(2) with unit quaternions in R4. Each normalized fundamental trace is the restriction of a linear functional of the shared unit quaternion. Sum of the two linear functionals has Euclidean squared magnitude t^2+s^2+2ts p(AB); Haar integration of its exponential is z(norm). The retained fused holonomy is invariant under endpoint gauge conjugation; hence the induced interaction is genuinely gauge invariant.

The full induced interaction is Phi_{t,s}(V)=-log Z_{t,s}(V) (up to an additive constant). It contains ALL generated SU(2) representations. The mixed source kernel satisfies d_t d_s log Z=Cov(p_s,p_t | V).

## 3. No-go for an unsubtracted, uniformly small effective action

For t=s=T and V=I, the argument of z is 2T. For V=-I it is 0. z(x) is increasing for x>=0 (moment generating function for a nondegenerate symmetric variable). Thus

 osc_V Phi_{T,T} = log z(2T)
 = 2T -(3/2)log(2T)+(1/2)log(2/pi)+O(1/T).

For any additive renormalization constant c,

 ||Phi_{T,T}-c||_infty >= (1/2) log z(2T).

Hence along t=s=T(h)=c_0/h (the equal-order anisotropic 2+1 Wilson trajectory), the nonconstant effective boundary potential is at least O(1/h) in sup norm. Any proposed polymer norm that includes this complete local boundary interaction without subtracting relevant/marginal pieces and dominates its uniform norm cannot be bounded by a cutoff-independent small number.

This is a precise limitation on naive norms; it does NOT preclude a multiscale expansion which explicitly separates large local gauge-field terms, performs scale-dependent rescaling, and bounds only the residual connected interactions. It does NOT prove a no-go for the complete exterior-coupled Penrose Wilson RG.

## 4. Weak-coupling versus physical coupling trajectory

At fixed finite beta, the exact face character expansion is
 e^{beta p(W)} = z(beta) sum_{j=0,1/2,...} (2j+1) r_j(beta) chi_j(W),
 r_j(beta)=I_{2j+1}(beta)/I_1(beta).

Spin/edge intertwiners integrate the mixed spatial-temporal faces. The usual absolute polymer expansion around the product Haar measure is controlled for sufficiently small local beta in bounded-degree complexes, but at beta~h^-1 the basic local activities e^{beta}-1 diverge and the fundamental r_{1/2}(beta) tends to 1. Thus neither naive strong-coupling norm is cutoff-uniform.

## 5. Correct renormalized target

Partition effective interactions at coarse scale into (i) relevant local terms consisting of gauge-invariant discretizations of electric and magnetic field energies and their required counterterms, and (ii) a residual connected boundary-polymer potential Psi. Only then attempt an estimate of the form

 sup_z sum_{Gamma contains z} exp(alpha |Gamma| + m diam Gamma) ||Psi(Gamma)|| <= epsilon

with uniform constants after field-strength rescaling, gauge fixing on small-field cells, and quantitative control of large-field tails. The coefficient functionals must come from -log of the exact interior integral (as in Section 1), rather than being stipulated. Control of the relevant coefficients, gauge-invariant source reconstruction, and uniform temporal Hamiltonian reconstruction are separate prerequisites.

This kind of multiscale ultraviolet construction is related to Balaban's work on three-dimensional lattice pure gauge ultraviolet stability (Commun. Math. Phys. 102 (1985) 255–275, DOI: 10.1007/BF01229380). That literature does not by itself establish the missing Penrose infrared gap or the proposed residual polymer bound.

## 6. Numerical coefficient check

For T=1,2,5,10,20,50,100 respectively, osc Phi=log z(2T) is approximately 0.46413447, 1.58509042, 6.28076592, 15.26136953, 34.23139463, 92.86268445, 191.82485289. Computed via exponentially scaled modified Bessel I_1.

## 7. Status

PROVED: exact full finite-block log-partition cumulant identities; mixed spatial–temporal two-face boundary kernel; divergent unsubtracted local boundary potential at strong bare beta; consequent failure of naive small-total-interaction norms on this sub-block.

NOT PROVED: cutoff-uniform residual polymer norm for full Penrose blocks; transfer of Balaban-type multiscale estimates to this nonperiodic discretization; joint continuum Hamiltonian reconstruction; graded-frame lower bound uniform in h and volume; R3/R2 mass gap.
