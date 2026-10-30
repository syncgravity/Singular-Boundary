# A noncircular thin-support free-energy theorem on peelable faces, and the remaining interior obstruction

Date: 2026-10-26. Scope: finite SU(2) Wilson gauge systems including spatial and temporal plaquettes, on arbitrary bounded-incidence cell complexes (Penrose geometry is allowed). This is a restricted theorem, not a full Penrose interior mass-gap proof.

## 1. Framework

For oriented edges E and plaquettes P, write d_p(U)=1-(1/2)Tr W_p(U) in [0,2] and

Z(beta)=\int_{SU(2)^E} \exp[-\sum_{p\in P}\beta_p d_p(U)]\prod_{e\in E}dU_e, \quad \beta_p\ge0.

A plaquette p has a **private edge** e_p if e_p occurs exactly once in the oriented boundary of p and belongs to no other plaquette of the entire complex. Assume that each face in S has a private edge (necessarily these private edges are distinct). The exterior plaquette system may have arbitrary interactions, including temporal plaquettes and arbitrary boundary fields not depending on private edges. Such a property is generally not available for bulk plaquettes of a three-dimensional spacetime complex.

Define z(beta)=\int_{SU(2)}e^{beta p(U)}dU=2I_1(beta)/beta, z(0)=1, q(beta)=e^{-beta}z(beta).

## 2. Exact factorization theorem

**Theorem 1.** If the plaquettes in S have private edges, then

Z(beta)=\Big(\prod_{p\in S}q(beta_p)\Big) Z_{P\setminus S}(beta),

where Z_{P\setminus S} is the partition function obtained by deleting faces in S, with all remaining links integrated with Haar probability measure. All associated face holonomies W_p (p in S) are independent, with law e^{-beta_p d(W)}dW/q(beta_p), and independent of the remaining Wilson system in the sense that its observables not using private edges retain their deleted-face distribution after integration.

*Proof.* For each p in S, with all other edges held fixed, its holonomy equals U_{e_p}^{\pm1}C or CU_{e_p}^{\pm1}, depending on orientation. Haar invariance gives \int e^{-beta_p d_p}dU_{e_p}=q(beta_p), independent of C. No other plaquette depends on U_{e_p}. Repeating the integration proves the factorization. Joint moments with functions of W_p follow by the same Haar change of variable for each private edge. QED.

**Theorem 2 (uniform diluted free-energy bound on peelable faces).** For any 0<theta<1, dilute the couplings on any X subset S by beta'_p=(1-theta)beta_p. Then

log[Z(beta')/Z(beta)]=\sum_{p\in X}\log[q((1-theta)beta_p)/q(beta_p)] \le C_theta |X|,

where C_theta = \sup_{b\ge0}\log[q((1-theta)b)/q(b)]<\infty. Moreover,

\sum_{p\in X}\langle d_p\rangle_{beta'} \le C/[(1-theta)\beta_{\min}]\,|X|,

for beta_min>=1; C=\sup_{b>=0} b(1-I_2(b)/I_1(b))<infty.

*Proof.* The ratio is an exact product by Theorem 1. The function of b in C_theta is continuous at zero and has finite limit (3/2)log[1/(1-theta)] as b tends to infinity by q(b)=sqrt(2/pi)b^{-3/2}(1+O(1/b)). Likewise b\langle d\rangle_b=b[1-I_2(b)/I_1(b)] converges to 3/2 and is continuous on [0,infty). QED.

These estimates have no perimeter penalty and no ambient volume dependence; on beta_p~lambda they are stronger than O(|X|log lambda) and O(|X|log lambda/lambda), respectively.

## 3. Exact large-field contour bound for these faces

For any delta in (0,2),

P_beta(d_p>delta for all p in X) = \prod_{p\in X}P_{beta_p}(d>delta) \le \prod_{p\in X}[e^{-beta_p delta}/q(beta_p)].

For beta_p>=1 and beta_min, beta_max comparable, q(b)>=c b^{-3/2}, and hence

P_beta(\forall p\in X:d_p>delta)\le [C beta_{max}^{3/2} e^{-beta_{min}delta}]^{|X|}.

With beta_min >= c_- lambda, beta_max<=c_+ lambda and delta=lambda^{-1/2}, this is <=exp(-c sqrt(lambda)|X|) for sufficiently large lambda. This controls both adjacent and separated collections of **private-edge** faces, but does not cover connected interior plaquette surfaces.

## 4. Why the same argument stops at bulk links

If e is incident on many plaquettes, its conditional partition integral is e^{-B_e}z(kappa_e) with B_e=\sum_{p\ni e}beta_p and kappa_e=|\sum_{p\ni e}beta_p q_{ep}|. Exterior staple directions are constrained by other links. The minimizer penalty F_e=B_e-kappa_e can be O(lambda) for frustrated exteriors. No Haar variable can be changed to eliminate only one plaquette while preserving the others. The free-energy ratio for dilution on P(J) is exactly the moment of the compatible frustration (up to an O(|J|) factor), so invoking that moment to prove the ratio is circular.

There is no theorem in this note that such frustrated configurations remain common after the full Gibbs average; nor one that they are rare enough. A pointwise conditional counterexample is not a counterexample to unconditional thin-support control.

## 5. Correct implication / outstanding target

For interior plaquettes in the genuine 2+1-dimensional Penrose theory, proving

sup_{X subset P (thin), 0<=t<=theta} \sum_{p\in X}\langle d_p\rangle_{beta-t\mathbf1_X} <= C |X|(1+log lambda)/lambda

would require a new scale-local Gibbs estimate, likely a gauge-compatible small/large-field background comparison. No noncircular proof of this arbitrary-interior-support statement has been established here. The preceding peelable-face result does not imply a continuum-stable polymer expansion, uniform R3 spectral gap, or continuum R2 mass gap.

## 6. Source context (not used as proof)

Balaban, "Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories," Commun. Math. Phys. 102 (1985), 255-275; https://doi.org/10.1007/BF01229380 . This concerns ultraviolet stability on his lattice setting and cannot simply be transferred to nonperiodic Penrose spacetime lattices.
