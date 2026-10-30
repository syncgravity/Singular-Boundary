# Gauge-compatible local partition comparison: an exact frustration-sensitive formula

Date: 2026-10-26. Status: exact finite-volume identity and explicit obstruction; no continuum-uniform Gibbs contour theorem.

## Setup
Let G be any finite SU(2) space-time plaquette complex with Wilson action S(U)=sum_p beta_p (1-p(W_p)), beta_p>0, p(W)=Tr W/2. Take a set J of links with no plaquette containing two J-links. Condition on all other link values V. For each e in J, write the incident action S_e(u;V)=B_e-u\cdot k_e(V), where B_e=sum_{p\ni e}beta_p and k_e=sum_{p\ni e}beta_p q_{ep}(V), with |q_{ep}|=1 in the unit-quaternion representation. Set kappa_e=|k_e|, F_e=B_e-kappa_e>=0. Haar-normalized z(kappa)=2I_1(kappa)/kappa. The exterior action S_out(V) contains exactly the plaquettes not incident on J.

## Theorem 1: exact gauge-compatible cavity comparison
The full partition function is
Z(beta)=int dV exp[-S_out(V)] prod_{e in J} exp[-B_e] z(kappa_e(V)).
For any modified couplings beta'_p on plaquettes incident on J, leaving S_out unchanged, write B'_e, kappa'_e and F'_e. Then
Z(beta')/Z(beta) = E_{eta_beta}[prod_{e in J} R_e(V)],
R_e(V)=exp(B_e-B'_e) z(kappa'_e)/z(kappa_e).
Here eta_beta is the **actual exterior marginal** of the original full Wilson Gibbs measure. The formula is gauge invariant: under an exterior gauge transformation, all staple quaternions for a given link rotate by a common SO(4) isometry, so their vector lengths and hence R_e are invariant.

Define ell(x)=log z(x)-x. Then the exact logarithmic cavity correction is
log R_e = F_e-F'_e + ell(kappa'_e)-ell(kappa_e).
For x>=0 there are universal c,C>0 such that c(1+x)^(-3/2) <= exp(ell(x)) <= C(1+x)^(-3/2). Consequently, if beta,beta' <= c_+ lambda, incidence <=D, and lambda>=1,
log R_e <= (F_e-F'_e) + C_0 + (3/2)log(1+Dc_+lambda).
Hence
log[Z(beta')/Z(beta)] <= C_0|J|(1+log lambda) + log E_{eta_beta} exp(sum_{e in J}(F_e-F'_e)).
This is an **exact boundary-compatible reduction** with no explicit O(lambda |Y|) penalty. It has replaced the crude boundary penalty by a correlated frustration exponential moment, which is not yet bounded.

## Theorem 2: conditional Gibbs-energy identity
Given V, the cavity density is proportional to exp(u\cdot k_e). Its expected incident action is
E[S_e(U_e;V)|V] = F_e + kappa_e[1-m(kappa_e)], m(x)=d/dx log z(x)=I_2(x)/I_1(x).
The excess term is universally bounded by a finite constant C_SU2, since it is continuous on [0,infinity), vanishes at zero, and tends to 3/2 at infinity. Thus E[S_e|V] -F_e lies in [0,C_SU2] uniformly in beta, volume, geometry. For J independent, sum over e. This separates intrinsic *exterior frustration* from thermal fluctuations at each selected link, without using an independent-staples comparison.

## An exact obstruction to a pointwise repair estimate
Consider one shared link in two positive-coupling plaquettes with beta_0=beta_1=lambda and exterior staples q_1=-q_0. The incident action is S_e(u)=2lambda for every u, giving kappa=0 and F_e=2lambda. If the target plaquette is repaired from p_0=-1 (u=-q_0) to p_0=+1 (u=q_0), the other plaquette changes from p_1=+1 to p_1=-1. Its action increases by 2lambda. Thus no deterministic link repair simultaneously (i) fixes the target defect, (ii) fixes all exterior links, and (iii) costs only O(log lambda) in the neighboring Wilson action. This is a *conditional counterexample*, not an unconditional typical-event no-go. It shows why a gauge-equivariant local repair requires a jointly adjusted exterior background or an averaged entropy/energy argument.

## What would close the probability step
To infer a small joint bad-staple probability, it would suffice to prove a **uniform frustration moment estimate** under the genuine exterior measure, for example
log E_{eta_beta} exp(sum_{e in J}(F_e-F'_e)) <= C |J|(1+log lambda)
for the prescribed diluted couplings, or a more suitable tilted-event variant that avoids exponential moments dominated by rare frustration sectors. The exact identity above does *not* establish this estimate. In the full Wilson measure such a bound is a new constructive gauge-theory task: it must cope with nonlocal compatibility and all spacetime plaquettes. Without it, the formerly proposed e^{-c sqrt(lambda)|J|} contour and residual polymer norms are unproved.

## Audit
Proved: exact cavity integration; exact frustration-sensitive comparison; uniform conditional thermal excess; deterministic pointwise-repair obstruction. Not proved: O(|J|log lambda) Gibbs partition correction; joint bad-staple rarity; continuum-stable connected polymers; uniform R3/R2 gap.
