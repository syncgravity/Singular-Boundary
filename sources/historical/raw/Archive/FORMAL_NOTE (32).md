# Correlated shield repair: exact finite-block conditional inequality and the unclosed Penrose step

Date: 2026-10-26. Finite SU(2) Wilson spacetime cell complex. This is a rigorous *conditional* correlated-shield theorem; it does not establish arbitrary interior Penrose cavity compatibility or an R3/R2 mass gap.

## Definitions
Fix interior link set I with m links, P(I) all plaquettes incident on I, exterior cavity Gibbs law rho_I(dv) proportional to exp[-S_out(v)]dv, where S_out sums plaquettes outside P(I). Let H be a subset of r exterior links and w the other exterior links. Assume bounded incidence D, face length L, beta_p<=c_+ lambda with lambda>=1, and r<=a m. Write S_out(h,w) for the undeleted action, and S_I(u;h,w) for the deleted action. All Haar products are normalized. For each w set M_out(w)=min_h S_out(h,w) and define Delta(w;h*)=S_out(h*,w)-M_out(w)>=0. Define E_I(h,w)=min_u S_I(u;h,w).

## Lemma: correlated conditional ball inequality
For any measurable target h*(w) in SU(2)^H and any u*(w) in SU(2)^I, and any fixed eps in (0,1), there exist c,C>0 depending only on local degree, face length, c_+, eps and the SU(2) metric, such that for lambda>=1

 rho_I( d_H(h,h*(w))_infty <= eps/lambda | w ) >= (c lambda^{-3})^r exp[-Delta(w;h*)-C r].

Indeed the conditional density is exp[-S_out(h,w)] / Z_out(w), with Z_out(w)<=exp[-M_out(w)] since normalized Haar. The map changing all r shield coordinates within eps/lambda changes each affected undeleted plaquette holonomy by at most L eps/lambda; the SU2 Wilson defect d(W) is globally Lipschitz with constant <=1 relative to the round-angle metric (or an absolute constant), so S_out(h,w)<=S_out(h*,w)+C lambda r*(eps/lambda)=S_out(h*,w)+C r. Haar ball probabilities are >=(c lambda^-3)^r. All exterior variables have their true interacting conditional distribution; no independence is used.

Similarly, on this ball S_I(u*;h,w) <= S_I(u*;h*,w)+C r, because a shield link affects at most D deleted plaquettes. Therefore the gauge-invariant compatible-energy event {E_I(h,w) <= S_I(u*;h*,w)+C r} contains this conditional ball. Formulating only by E_I renders the event gauge invariant; the chosen targets are merely witnesses.

## Corollary: correlated-repair criterion
Suppose on a cavity-exterior event W in the w variables with marginal probability rho_I^w(W)>=exp[-a_0 m(1+log lambda)], one can select targets h*(w),u*(w) satisfying Delta(w;h*) <= a_1 m(1+log lambda) and S_I(u*;h*,w)<=a_2 m(1+log lambda). If r<=a m, the unconditional exterior cavity probability obeys
 rho_I(E_I <= (a_2 + C a) m(1+log lambda)) >= exp[-C'(a,a_0,a_1,a_2,D,L,c_+) m(1+log lambda)].
If Delta and S_I are O(m) and rho_I^w(W)>=e^{-O(m)}, still obtains e^{-O(m log lambda)}. This suffices for the insertion free-energy bound by the previously derived interior-minimizer Haar-ball integral.

## Essential limitation
The assertion that target shields can be selected with Delta=O(m log lambda) **does not follow** from bounded incidence, gauge invariance, or locality. For a single shield variable h, if an undeleted plaquette fixes it near 1 and deleted plaquettes require h near -1, then Delta can be 2 lambda. This is a valid local obstruction to arbitrary-target conditional comparison (though not a counterexample to the unconditional cavity-compatibility statement). Even strong correlation can be managed if a low-cost joint repair exists; existence under the Penrose cavity distribution is not proved. This inequality cannot be used with Delta replaced by zero without independent demonstration. It is not a proof of the user's full requested claim.

## Global gauge and soft-mode qualification
The conditional repair is on actual SU2 link variables, so it is valid without selecting a gauge. Targets u*,h* transform covariantly if one wants an equivariant construction; the enlarged event defined only through E_I is invariant. In the full nonabelian spacetime complex, plaquette Bianchi constraints may prevent simultaneous low-cost corrections of all deleted and undeleted faces, and all exterior temporal plaquettes must be included in Delta.

## A useful exact Hölder diagnostic
For any event A of the shield links (with w fixed), let P_w be conditional cavity law and H_w normalized Haar on H. Then
 P_w(A) >= H_w(A) exp[-sup_{h in A} S_out(h,w)+M_out(w)].
It is precisely the added action relative to the exterior minimizer that must be quantitatively bounded. Suppressing this term is invalid. The lemma above refines this with explicit polynomial Haar volume for a repair ball.
