# R3: Conditional multi-core suppression and the unresolved bad-staple sector
26 October 2026. Scope: finite 2+1 dimensional SU(2) Wilson complex, including Penrose-prism spacetime complexes of bounded incidence. This note proves a joint good-staple contour estimate but NOT an unconditional Peierls estimate, post-integration polymer bound, or mass gap.

## Definitions
For each oriented link e let U_e ∈ SU(2) with normalized Haar measure. Each plaquette p has normalized trace p(W_p)=Tr(W_p)/2 and defect d_p=1-p(W_p) ∈ [0,2]. Couplings β_p ∈ [c_- λ,c_+ λ] with λ=(g_3²h)^(-1), and every edge appears in at most D plaquettes (spatial or temporal). The finite Gibbs law is μ(dU)=Z^(-1) exp(-Σ_p β_p d_p(U))∏_e dU_e. No plaquette independence is presumed.

For a single selected link e, after conditioning all other edges, the incident plaquette terms have quaternion form β_p u_e·q_{p,e}, for q_{p,e} ∈ S³ depending only on other edges. Thus ν_e(du|ext)=z(κ_e)^(-1)e^{k_e·u}du, k_e=Σ_{p∋e}β_pq_{p,e}, κ_e=|k_e|, z(κ)=2I₁(κ)/κ. This includes temporal plaquettes exactly.

For target plaquette p assigned to e, set r_δ=arccos(1-δ), and define the exterior-measurable good event G_{p,e}(δ): κ_e≥c λ and angle(k_e/κ_e,q_{p,e})≤r_δ/2. Assume λ≥1, δ=λ^(-1/2)≤1.

## Theorem 1: sparse core-link selection
Let X be any set of plaquettes, not necessarily connected. Assign one boundary link e(p) to each p∈X. Make a graph on X joining p and p' if e(p)=e(p') or any plaquette (whether in X or not) contains both selected links. Given at most D incident plaquettes per edge and 4 edges per plaquette, each p has at most 4D²-1 neighbors (conservative bound): each plaquette incident on e(p) contains at most 4 candidate links, and each such candidate link may be assigned to at most D target plaquettes. An independent set X0 exists with |X0|≥|X|/(4D²+1). No plaquette contains more than one selected link e(p), p∈X0.

## Theorem 2: exact factorization and conditional good-sector exponential bound
Fix all links not in E0={e(p):p∈X0}. Since no Wilson plaquette contains two selected edges, conditional Gibbs measure factorizes exactly as ∏_{p∈X0} ν_{e(p)}(du_{e(p)}|ext). The target's q_{p,e}, field k_e, and good event G_{p,e} are measurable w.r.t. the exterior.

On G_{p,e}, spherical geometry and the Bessel partition-function lower bound yield ν_e(d_p>δ|ext)≤C(1+κ_e)^(3/2) exp(-κ_e δ/4). Since c λ ≤κ_e≤D c_+ λ, obtain q_λ=C(1+D c_+λ)^(3/2) exp(-c√λ/4). In particular for sufficiently large λ (depending only on c,c_+,D), q_λ≤exp(-c'√λ) for some c'>0.

Let L_X(δ)={d_p>δ for all p∈X}. As L_X⊆L_X0, conditional factorization implies

 μ(L_X(δ) ∩ ∩_{p∈X0} G_{p,e(p)}(δ)) ≤ q_λ^{|X0|} ≤ exp[-c'√λ |X|/(4D²+1)].

This theorem is volume uniform, includes all temporal plaquettes, holds for any X and all Penrose patches of uniformly bounded incidence. It does not require a graph-averaged defect bound.

## Exact decomposition and its limitation
Write G_X=∩_{p∈X0}G_{p,e(p)}. Then
 μ(L_X) ≤ q_λ^{|X0|} + μ(L_X ∩ G_X^c).
The second term is not controlled by the theorem. Union bounding it gives Σ_i μ(G_i^c), which is not exponentially small in |X| and is generally useless for large contours.

A single shared exterior frustrated holonomy can correlate multiple bad-staple events. Hence one cannot assert μ(∩ G_i)≈∏ μ(G_i), nor use the conditional product of core-link laws to estimate probabilities of G_X^c. Even if μ(G_i^c) is small, that alone does not yield an exponential contour bound. A robust full-measure theorem needs a multiscale control of correlated bad-staple clusters, or a different gauge-invariant event decomposition.

## Local structural fact: under good alignment the bad target event is small, not vice versa
The exact one-link law is a probability measure on SU(2) with a von Mises–Fisher density. If a conflicting staple field dominates, k_e can point away from the target q_{p,e} even though every β_p>0. Explicitly k_e=β_0q_0+β_1(-q_0)=(β_0-β_1)q_0. If β_1>β_0 and λ grows, the conditional link concentrates near -q_0 and the target defect tends to 2. Thus a uniform bound over arbitrary conditioned exteriors is false for the general weighted Wilson family.

## Relation to residual polymer activities
A joint event bound on good exteriors does not itself estimate the connected post-integration activities Ψ_{k,Γ}. Their norms include covariance of internal fluctuations, Jacobians, fluctuations of good/bad-sector indicators, background-action extraction, and gauge boundary maps. Even a hypothetical unconditional μ(L_X)≤e^{-a|X|} must be converted into actual activity bounds through a polymer-factorization argument. No such bound is claimed here.

## Proof obligations
1. Find a gauge-covariant multiscale condition that controls bad-staple correlations, not only single-site marginal probabilities.
2. Establish localized cluster or partition-function comparisons that retain temporal interactions and give a regionwise |X| cost for arbitrary connected thin sets.
3. Show the background-subtracted effective potentials have rooted norm small uniformly in h, block level and volume.
4. Independently reconstruct the Hamiltonian and low-energy Wilson frame; no R3/R2 mass gap is obtained here.
