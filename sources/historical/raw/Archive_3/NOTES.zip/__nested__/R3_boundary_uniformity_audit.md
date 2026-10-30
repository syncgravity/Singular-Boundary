# R3 closure: boundary-uniformity audit and a corrected proof target
**Date:** 2026-10-28  
**Status:** New independent mathematical stress test; NOT a proof or disproof of the original unrestricted R3 statement, because the exact admissible boundary class and insertion conventions have not yet been recovered.

## 1. Source and provenance
The available branch note (`Branch · Branch · Compare Continuum Mass Gaps.txt`) records the target

\[
Z_{\mathrm{inserted}}/Z_{\mathrm{cavity}}\ge e^{-C|Q|(1+\log\lambda)}.
\]

It separately records a finite 15-state SU(2) mixed-sector positivity test and a global 37-link Haar estimate with \(111\log(\lambda)/2\) coefficient. Those are distinct from this new boundary-condition stress test.

## 2. Precise model for the test
Take one SU(2) link \(U\), normalized Haar measure \(dU\), and \(c(U)=\frac12\mathrm{Tr}\,U\in[-1,1]\). Let \(\lambda>0\). Define

\[
Z_0(\lambda)=\int_{SU(2)}e^{\lambda c(U)}dU,
\qquad
Z_1(\lambda)=\int_{SU(2)}e^{\lambda c(U)}e^{-\lambda c(U)}dU=1.
\]

The second factor can be written \(e^{\lambda c((-I)U)}\), since \(-I\) is central in SU(2). This represents two locally incompatible Wilson preferences for the same link with a fixed surrounding holonomy of \(-I\). Whether this local configuration is admissible as a *gauge-consistent embedded Penrose cavity* is a separate geometry/topology question; the counterexample is to a boundary-uniform claim over any local Wilson products allowing this configuration, NOT automatically to the exact R3 theorem.

## 3. Exact evaluation and obstruction
SU(2) Weyl integration for a class function yields

\[
\int_{SU(2)}f(c(U))\,dU=\frac2\pi\int_0^\pi f(\cos\theta)\sin^2\theta\,d\theta.
\]

Using the modified Bessel function \(I_1\),

\[
Z_0(\lambda)=\frac{2 I_1(\lambda)}{\lambda},\qquad
R(\lambda)=\frac{Z_1}{Z_0}=\frac{\lambda}{2I_1(\lambda)}.
\]

As \(\lambda\to\infty\),

\[
R(\lambda)\sim\sqrt{\frac\pi2}\lambda^{3/2}e^{-\lambda};\qquad
-\log R(\lambda)=\lambda-\tfrac32\log\lambda-\tfrac12\log(\pi/2)+o(1).
\]

Therefore for **any constant** \(C\) independent of \(\lambda\), the bound
\(R(\lambda)\ge e^{-C(1+\log\lambda)}\) fails for sufficiently large \(\lambda\).

This does not establish failure of an *averaged* insertion comparison, nor of a comparison allowing nearby link relaxation, nor of a comparison under compatibility assumptions. It warns that unrestricted fixed-boundary pointwise comparison can encounter an order-\(\lambda\) frustration cost.

## 4. Correctly partition the R3 task
**Task A, boundary admissibility:** Establish exactly which gauge-invariant boundary classes arise for the R3 Penrose cavities and whether the antialigned example can be embedded. If the example is excluded, prove the geometric compatibility property that excludes it.

**Task B, compare the right ensembles:** Distinguish (i) pointwise ratios conditional on all exterior links, (ii) annealed ratios integrated against the cavity Gibbs boundary measure, and (iii) modified ratios with a relaxed collar. The stress test only rules out the universal form of (i) for models admitting the configuration above.

**Task C, prove local probability bounds:** Given a movable collar \(N(Q)\) of size at most \(b|Q|\), define an event \(A_Q\) of compatible near-flat configurations and prove, *from independently verified local estimates*,
\[
\mathbb P_{\rm cavity}(A_Q)\ge c^{|Q|}(1+\lambda)^{-p|Q|}
\]
with \(c,p,b\) independent of ambient volume and \(Q\). If the insertion weight \(W_Q\ge d^{|Q|}\) on \(A_Q\), then
\[
\mathbb E_{\rm cavity} W_Q\ge (cd)^{|Q|}(1+\lambda)^{-p|Q|}.
\]
This implication is elementary. **The substantive unsolved work is proving the event probability bound without assuming the desired conclusion in disguise.** Additional normalization factors from the chosen Wilson-action convention must be tracked.

**Task D, uniform transfer consequence:** Only after establishing Task C should we derive the three-slab overlap/transfer estimate with explicit constants. Nothing here implies a continuum mass gap by itself.

## 5. Why the ordinary Haar-ball estimate is inadequate
A global event restricting every one of \(E\) independent links to a near-identity ball of radius \(\lambda^{-1/2}\) has Haar volume of order \(\lambda^{-3E/2}\) and hence a free-energy cost of \(3E\log\lambda/2\). If \(E\) scales with the entire complex rather than \(|Q|\), this is not the R3 requirement. Localizing the event requires control of the conditional distribution induced by *outside* plaquettes, which is exactly where the boundary frustration above enters.

## 6. A proposed *conditional* R3 lemma for proof development
Let \(G\) be an admissible finite bounded-incidence SU(2) cell complex; \(Q\) a finite plaquette insertion set; \(N(Q)\) a collar containing at most \(b|Q|\) gauge-fixed edges; and \(\mu_{G,Q,\lambda}\) the reference cavity measure. Assume a separately verified **collar-repair lemma** constructs a gauge-covariant measurable transformation on the collar such that:

1. the transformed fields satisfy each inserted plaquette within \(O(\lambda^{-1/2})\) of the identity;
2. the loss of existing Wilson action under repair is at most \(A|Q|(1+\log\lambda)\) in the *integrated* comparison (not merely a pointwise energy bound);
3. the transformation's multiplicity/Jacobian or measure-preimage cost is at most \(B|Q|(1+\log\lambda)\);
4. all constants are uniform in ambient size, inserted supports, and gauge-invariant exterior conditions **within an explicitly stated admissibility class**.

Under these nontrivial assumptions, a support-local insertion bound follows by the change-of-variables method. **The lemma above is an agenda, not a proved existence statement.** The formulation must be refined to avoid overlapping images and to pin down precise Wilson-action normalizations.

## 7. Decision rule for the next proof
First establish (A) whether the conflicting Wilson preferences are physically/admissibly realizable in the original Penrose prism setting; and (B) whether the intended ratio is pointwise conditional, averaged, or collar-relaxed. If (A) yes and (B) pointwise, the proposed logarithmic bound cannot hold as stated. If the boundary is integrated/relaxed, develop the collar-repair map and compare all preimage weights. Do not spend further effort extrapolating the 15-state sign pattern until these hypotheses are settled.
