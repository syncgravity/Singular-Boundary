# R3 — Infrared Response in the Penrose SU(2) Hamiltonian
26 October 2026

## Scope and result
This note addresses R3 separately from R2. The principal new result is a rigorous finite-volume, gap-free spectral-weight criterion that bounds the infrared static susceptibility, together with a precise no-go statement for obtaining the required spatial decay from locality alone. No arbitrary-coupling or continuum R3 estimate is proved for the actual interacting Wilson ground state.

## Setup
On a finite Penrose rhombus graph, H = sum_e a_e(-Delta_e)+sum_f b_f(1 - (1/2) ReTr W_f), a_e>0, b_f finite, is self-adjoint on L2(SU(2)^E); the gauge-invariant sector is reducing. With the unique positive gauge-invariant normalized ground state Omega and E0, set K=(H-E0)|_{Omega-perp}>0, with spectral projection P_I. For bounded gauge-invariant self-adjoint local observables A_X,V_Y, let a=Q A_X Omega, v=Q V_Y Omega. The static susceptibility is chi_XY=-2 Re <a,K^{-1}v>. Its infrared portion is chi_XY(<eta)=-2 Re <a,K^{-1}P_(0,eta)v>.

### Theorem R3-SW — rigorous infrared spectral-weight bound
Define cumulative low-energy weights F_A(s)=||P_(0,s] a||^2 and F_V(s)=||P_(0,s] v||^2. Suppose for 0<s<=eta that F_A(s)<= C_A s^(1+alpha) and F_V(s)<=C_V s^(1+alpha), alpha>0, with constants independent of volume in a fixed physical normalization. Then
  |chi_XY(<eta)| <= 4 sqrt(C_A C_V) eta^alpha /(1-2^(-alpha)).
Proof: decompose (0,eta] into disjoint bands I_n=(eta 2^(-(n+1)),eta 2^(-n)] for n>=0. The spectral theorem and Cauchy–Schwarz give
 |<a,K^{-1}P_I_n v>| <= (2^(n+1)/eta) ||P_I_n a|| ||P_I_n v|| <= (2^(n+1)/eta) sqrt(F_A(eta 2^-n) F_V(eta 2^-n))
 <= 2^(n+1) sqrt(C_A C_V) eta^alpha 2^(-n(1+alpha)) = 2 sqrt(C_A C_V) eta^alpha 2^(-n alpha).
Summing n, multiplying by 2 from the susceptibility formula yields
  |chi_XY(<eta)| <= 4 sqrt(C_A C_V) eta^alpha/(1-2^(-alpha)).
This last (smaller) constant is correct and is the one to use. The integral converges for alpha>0. The theorem is valid with no lower bound on the first excitation energy. For matrix elements in common gauge-invariant symmetry sectors, the same proof holds after inserting sector projections.

### Corollary R3-SP — sufficient spatially decaying *band* estimate
If, more strongly, each dyadic band obeys
 |<a,K^{-1}P_I_n v>| <= C_XY exp(-mu r) eta^alpha 2^(-n alpha)
with alpha,mu,C_XY uniform, then |chi_XY(<eta)| <= 2 C_XY exp(-mu r) eta^alpha/(1-2^(-alpha)). This is a sufficient local infrared-response lemma but its band hypothesis has NOT been established. Without this cross-weight hypothesis, R3-SW has no spatial-decay factor: two-point infrared responses cannot be deduced from local one-point spectral weights alone.

### Alternative criterion using the imaginary-time covariance
For finite volume, inverse-energy response = int_0^infty <a, exp(-tK) v> dt. Its low-energy contribution is integral of <a, exp(-tK) P_(0,eta) v> over t. Direct control of connected imaginary-time correlators in a way integrable for all t would give R3. Standard real-time Lieb–Robinson estimates cannot by themselves control the large-t integral.

## Two essential qualifications
(1) Spectral weight s^(1+alpha) is a substantive infrared *input*, not derived here from the Wilson Hamiltonian. Generic bounded local observables do not satisfy it uniformly without further dynamics; at finite volume small eigenvalues can have appreciable local overlap. The spatial-band bound is still stronger. A uniform R3-SW bound with no r decay does not establish equilibrium boundary locality.
(2) Even uniform, exponential static response for a restricted local observable set would not certify a gap for every physical excitation. An excitation may be dark to the chosen operators, or a small-energy topological/global sector may evade local detection.

## Gauge and C5 considerations
The physical Hilbert space is the Gauss-invariant subspace. A_X,V_Y must be gauge invariant, and ground-state uniqueness is finite-volume only. Exact weighted graph isomorphisms intertwine K, spectral projections and the weights F_A, so the criterion is C5 covariant across admitted tilings. Neither C5 nor the parent-space complex structure J bounds F_A(s) or the cross-band matrix elements. A vanishing spectral overlap enforced by a genuine symmetry-sector selection rule removes particular terms, but cannot bound all symmetry-allowed low-energy sectors.

## Non-circular independent proof obligations
R3a: prove gauge-invariant localized low-energy *weight* estimates using a method not relying on the gap (e.g. exact Ward identities with quantitative constants; controlled strong-coupling linked-cluster expansion). These are open for arbitrary Wilson couplings.
R3b: prove cross-band matrix element decay with physical separation, not merely a bound on each local vector separately. This is open beyond regimes with established perturbative stability.
R3c: establish local-observable completeness sufficient to address entire vacuum-orthogonal sector, including global cycles and boundary sectors; otherwise local susceptibility does not prove a full mass gap.
R2 separate: choose a continuum trajectory H_(G,a), consistent physical units, renormalized Wilson observables, eta physical, r physical and uniformity in a. Bare b_f(a) growing as a->0 defeats naive uniform LR estimates; this is not an R3 proof.

## Literature checked
Henheik & Wessel (2026), Response Theory for Locally Gapped Systems, Journal of Statistical Physics 193:151, DOI 10.1007/s10955-026-03703-1: introduces intrinsic local dynamical gap and proves response under it. The paper explicitly restricts presentation to finite-dimensional local spaces and bounded operators; therefore cannot be used unchanged for on-link L2(SU2) and unbounded electric Laplacians. https://link.springer.com/article/10.1007/s10955-026-03703-1

## Verdict
R3 is not proved for arbitrary-coupling Penrose SU(2), fixed-cutoff uniformly in spatial volume, or along a continuum trajectory. R3-SW is a genuine gap-free spectral-weight estimate, and R3-SP identifies additional necessary distance-sensitive input. No positive continuum mass gap is claimed.