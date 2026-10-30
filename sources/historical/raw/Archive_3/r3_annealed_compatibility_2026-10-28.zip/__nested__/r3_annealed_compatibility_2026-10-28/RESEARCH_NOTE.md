# R3 local compatibility and curvature-frustration audit
Date: 2026-10-28. Status: exact counterexample to necessity of the previously proposed compatible-maximizer probability criterion; exact annealed small-ball result in a two-face SU(2) control complex. **Not an R3 Penrose closure.**

## 1. Archived evidence and target limitation
Audited `r3_compatibility_theorem_2026-10-28/RESEARCH_NOTE.md`, `r3_stepwise_2026-10-28/R3_stepwise_research_note.md`, `penrose_complete_catalogue.npz`, and the supplied dissertation/archive manifests. The catalogue keys (`idx`, `sign`, `length`, `roots`, `distance`, `target`, `faces`, `cidx`, `csign`, `clength`, `ckind`) do not specify the oriented three-step 12-prism spacetime 2-cell attaching words, the cavity/insertion partition Q, or the boundary convention. Therefore the actual Penrose cavity's compatible-minimizer mass cannot be calculated or established from the given data. No theorem below assumes these missing facts.

## 2. A structural problem with exact compatible maximizers
Let U,K independently range over SU(2) with normalized Haar reference measure. Define c(V)=Tr(V)/2 and w_lambda(V)=exp[-lambda(1-c(V))]. The **cavity** has two Wilson faces with holonomies U and UK, respectively, so D_C=lambda[(1-c(U))+(1-c(UK))]. The **inserted** face has holonomy U. K is an exterior block variable with its correlated Gibbs marginal after U is integrated.

For fixed K, an insertion-compatible cavity minimizer must have U=I (since the inserted holonomy is U). For U=I to minimize D_C, it must be stationary. The derivative of c(U) vanishes at I; the derivative of c(UK) at U=I vanishes in all Lie directions precisely when K belongs to the center {I,-I}. Hence for every K not in the center, **no compatible cavity minimizer exists**. The marginal law of K is absolutely continuous with positive density relative to Haar, so the good-event probability mu_C(G) is **exactly zero for all lambda>0**. This is an abstract admissible Wilson-word example, not a verified Penrose prism subcomplex.

Nevertheless, integrating K first gives int w_lambda(UK) dK = a(lambda), independent of U, where a(lambda)=exp(-lambda)2 I_1(lambda)/lambda. Therefore Z_C=a(lambda)^2 and Z_inserted=a(2lambda)a(lambda); consequently

R(lambda) = Z_inserted/Z_C = a(2lambda)/a(lambda) --> 2^(-3/2) as lambda grows.

So the desired logarithmic comparison holds **despite** mu_C(G)=0. In fact insertion cost remains bounded as lambda increases. Thus a polynomial probability of **exactly** compatible global cavity minimizers is not a necessary criterion and can be an unproductive R3 proof obligation.

## 3. Direct Gibbs near-flat event succeeds
After integrating K, the cavity marginal of U has density w_lambda(U)/a(lambda) relative to Haar. Define A_lambda={1-c(U)<=1/(2lambda)}. Using geodesic angle theta in [0,pi], c(U)=cos(theta), and Haar angular density (2/pi)sin^2(theta):

P_C(A_lambda) = [ (2/pi) int_0^{arccos(1-1/(2lambda))} sin^2(theta) exp(-lambda(1-cos theta)) dtheta ] / a(lambda).

For lambda>=1, the event contains the ball theta<=lambda^(-1/2). On that ball w_lambda(U)>=e^(-1/2). Haar(B_r)>=8 r^3/(3 pi^3), for r<=1. On [0,pi], 1-cos(theta)>=2 theta^2/pi^2 and sin^2(theta)<=theta^2, so

a(lambda) <= pi^(5/2)/(2^(5/2) lambda^(3/2)).

Therefore a fully explicit lower bound is

P_C(A_lambda) >= p0 := exp(-1/2) * 2^(11/2)/(3 pi^(11/2)) > 0, independent of lambda.

Restricting the insertion integral to A_lambda also gives R(lambda)>=e^(-1/2)p0. Numerical quadrature finds the actual near-flat probability tends to about 0.1987, and R tends to 2^(-3/2).

This is a genuine Gibbs-averaged small-ball result in the two-face example, unlike a conditional Haar average with independent boundary fields.

## 4. What is established and what is not
**Established:** (i) exact-minimizer-compatible exterior sets can have Gibbs probability zero in a valid SU(2) Wilson-word model; (ii) the same model can have an exact bounded insertion cost and uniform Gibbs near-flat mass; (iii) the relaxed small-ball criterion is strictly more useful than exact compatibility for this purpose.

**Not established:** a uniform bound P_C(D_Q<=C |Q|/lambda)>=exp(-c|Q|)(1+lambda)^(-b|Q|) for the actual Penrose prism, the requisite oriented Penrose incidence, a uniform curvature-redistribution collar, a transfer spectral gap, or a continuum mass gap.

## 5. Corrected R3 proof obligation and a falsifiable audit
Primary target: exhibit measurable A_Q in the actual correlated cavity Gibbs ensemble such that (a) D_Q<=k |Q|/lambda on A_Q, (b) mu_C(A_Q)>=exp(-a|Q|)(1+lambda)^(-b|Q|), with a,b,k independent of ambient volume and support placement. Then R_Q>=exp[-(a+k)|Q|](1+lambda)^(-b|Q|).

To test this, supply or reconstruct: (1) oriented edge list and face-boundary words for each temporal prism and spatial face, (2) the exact removed/insertion face sets, (3) the integrated/fixed and gauge-fixed links, (4) face couplings and temporal boundary identifications, (5) a bounded-degree uniformity statement for admissible Penrose patches. Run the incidence/cycle consistency audit, optimize the cavity energy with Q near-flat to estimate the frustration gap over exterior holonomies, and only then attempt a block transport/relative partition-function inequality. A zero or small classical frustration gap is suggestive but not, by itself, a uniform Gibbs probability theorem.

## 6. Source and reproducibility
Script `verify.py` computes exact Bessel ratios and independent angular quadrature. `certificate.json` records numerical checks and the explicit non-Penrose scope. Earlier compatible-minimizer theorem remains a valid sufficient conditional theorem, but its G-probability route should not be mistaken for a necessary one.
