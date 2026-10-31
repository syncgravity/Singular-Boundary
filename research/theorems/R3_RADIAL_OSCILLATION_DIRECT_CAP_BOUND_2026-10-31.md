# R3-IR-594 — Direct one-sided radial oscillation cap bound

Let μ be the *normalized* SU2 Haar class measure on the radial half-sphere [0,π/2], with density proportional to sin²u du. Assume ψ:[0,π/2]→(0,∞) is measurable and define O = sup_{0≤v≤u≤π/2}[log ψ(u)−log ψ(v)]_+ <∞. (Here radial u=0 is the center, u increasing goes toward the equator.) For any center interval I=[0,δ], 0<δ<π/2, write m=μ(I) and the reweighted probability ν(I)=∫_I ψ² dμ / ∫ ψ² dμ. For any u∈I, v∉I, we have log ψ(v)−log ψ(u)≤O and thus ψ(v)²≤e^{2O}ψ(u)². Integrate this pointwise inequality with u and v independent under μ to obtain

 (∫_{I^c}ψ²dμ) (∫_I 1dμ) ≤ e^{2O} (∫_I ψ²dμ) (∫_{I^c}1dμ).

Therefore ν(I) ≥ m/[m+e^{2O}(1−m)] ≥ e^{−2O}m. Both inequalities are exact; no derivative equation or current estimate is needed. For a center-symmetric SU2 marginal on [0,π], the same formula applies to the union of the two endpoint caps, after folding to [0,π/2].

Under the previous branch's reported Ward identity, O is the supremum of positive NET increments of the signed score: O=sup_{v≤u}[−(4/A)∫_v^u C(cos t)/sin t dt]_+. Thus the minimum sufficient analytic object for this cap comparison is interval control of the signed current, not an L1 positive-part current budget T. The exact countermodel in R3-IR-593 shows O can vanish while T diverges.

**Limitations:** This lemma is an abstract measure inequality, not a proof that the actual nonlinear SU2 deleted vacuum meets any uniform O_{f,h} estimate. The prior branch's proposed condition sup O_{f,h}=o(h^{−1/4}) would imply the same cap-comparison consequence as its stronger T condition **provided** all other assumptions in its magnetic-deletion and bulk estimates hold. Those dependencies and the physical continuum Yang-Mills mass gap remain open.
