# R3 Gibbs small-ball audit: unconditional finite-energy bound and the missing logarithmic improvement
Date: 2026-10-28. This is **NOT** a proof of the requested R3 support-uniform logarithmic bound for the actual Penrose cavity.

## Source audit
Inspected the available R3 shared-edge note, previous stepwise audit, and the numerical Penrose catalogue. The latter stores arrays `idx,sign,length,roots,distance,target,faces,cidx,csign,clength,ckind,F,graph_hash,threshold,coverage_version`. It does not label the original 3-step/12-prism spacetime complex, its ordered plaquette boundary words, its inserted plaquette set Q, or its boundary convention. Stage 26 archives contain Monte Carlo data, not a certified R3 spacetime incidence specification. No assertion about the actual Penrose cavity's edge incidence can therefore be verified from these sources.

## Theorem (correlated Gibbs finite-energy near-flat bound)
Let G be a finite oriented lattice 2-complex with compact SU(2) link variables, all edges used by an inserted support Q integrated against normalized Haar measure (no fixed boundary links on those faces). The reference/cavity law has density proportional to ∏_{p∈C} exp[-β_p (1 - 1/2 Tr H_p)] with 0≤β_p≤λ. Assume every plaquette in Q has boundary-word length ≤L counting repeated edges, and each edge occurs in at most d *cavity* face words, with multiplicity counted. For λ≥1 and nonempty Q, set E_Q to be the distinct edges in the words of Q; m=|E_Q|≤L|Q|. Define D_Q=∑_{p∈Q}(1 - 1/2 Tr H_p).

Then
P_C[D_Q ≤ |Q|/(2λ)] ≥ [a_L λ^{-3/2} exp(-2dλ)]^m ≥ [a_L λ^{-3/2} exp(-2dλ)]^{L|Q|},
where a_L=8/(3π³L³) (valid L≥1).
Consequently the insertion ratio R_Q=E_C[exp(-λ D_Q)] satisfies
R_Q ≥ exp(-|Q|/2) [a_L λ^{-3/2} exp(-2dλ)]^{L|Q|}.
Equivalently,
-log R_Q ≤ |Q| [1/2 + L(2dλ + (3/2)log λ + log(1/a_L))].
The constants are independent of the ambient lattice volume whenever L,d are uniform. **The leading cost is O(λ|Q|), not O(|Q| log λ)**. This is not R3 closure.

### Proof
1. Conditional on every other link, the Gibbs density of a selected edge u has weight g(u) consisting only of incident cavity Wilson factors. Since each normalized factor lies in [e^{-2λ},1] and at most d factors occur, e^{-2dλ}≤g(u)≤1. Its normalization is ≤1. Thus the conditional probability of any measurable Haar set B is ≥e^{-2dλ} Haar(B), regardless of correlations or external link values. The same estimate applies sequentially to the m selected edges, even after conditioning previously chosen edges.
2. Identify SU(2) with unit quaternions (cos θ,sin θ n), 0≤θ≤π. Haar probability of the radius-ε geodesic ball about I is (2/π)∫_0^ε sin²θ dθ. Since sin θ≥2θ/π for 0≤θ≤π/2, Haar(B_ε)≥8ε³/(3π³). Set ε=1/(L√λ)≤π/2. The event that **every** edge in E_Q lies in B_ε has probability at least (a_L λ^-3/2 e^-2dλ)^m.
3. On this event, every inserted face holonomy is a product of at most L rotations with bi-invariant geodesic angles at most ε (inverses do not alter distance); the triangle inequality gives angle(H_p)≤Lε=λ^-1/2. Hence 1-(Tr H_p)/2=1-cos angle ≤ angle²/2 ≤1/(2λ), and D_Q≤|Q|/(2λ).
4. Restrict the Gibbs expectation defining R_Q to the event above, obtaining the stated insertion bound. Finally, since the base is ≤1 and m≤L|Q|, substitute the larger exponent.

If some inserted edges are fixed by Dirichlet data, the event that all such links lie near I can have zero probability. No unconditional arbitrary-fixed-boundary statement follows. Likewise, Wilson models with additional interactions need a separately proved bounded conditional-density ratio.

## Critical obstruction to converting this into R3
The O(λ) term comes from replacing the correlated cavity's conditional law by the very crude uniform lower envelope e^-2dλ Haar. To obtain the desired polynomial cost, one must prove that compatible near-flat Q configurations are not exponentially disfavored by existing cavity faces, e.g. via a low-energy collar transport or a direct Gibbs small-ball probability bound. Bounding degrees L,d alone does not provide this; the frustrated one-link example in the previous audit has O(λ) suppression even after Gibbs averaging.

## Target for a Penrose-specific proof
Provide a checked *spacetime* incidence table with each face's ordered edge word and signed orientations, Q, cavity face set C, Wilson coupling convention, independently integrated versus fixed links, and allowed Penrose patch class. Then (a) verify L,d and boundary integrability; (b) enumerate minimal compatible assignments and local action-barrier certificates; (c) attempt to replace e^-2dλ by a polynomial lower conditional probability on a gauge-compatible collar; (d) establish volume-uniform multiplicity/Jacobian controls. Without these inputs or a proved alternative structural theorem, the requested logarithmic lower bound remains unresolved.

## Significance
This is a genuine theorem for arbitrary correlated finite-volume Wilson Gibbs measures under explicit integrated-edge and bounded-incidence hypotheses. It is deliberately weaker than the original R3 target and cannot establish the continuum Yang–Mills mass gap.
