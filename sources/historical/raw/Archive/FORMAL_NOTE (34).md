# R3: Coupled curvature compatibility and cavity-event audit (27 October 2026)

## Setting
Finite oriented 3-dimensional cell complex with SU(2) link matrices; spatial and temporal faces are treated identically as Wilson faces. Couplings satisfy c_- lambda <= beta_p <= c_+ lambda. Let I be m deleted interior links, P(I) incident faces, and rho_I exterior cavity measure with all P(I) couplings removed. E_I(v) = min_{u in SU(2)^I} sum_{p in P(I)} beta_p (1 - Tr W_p(u,v)/2).

## Theorem 1: nonabelian cellular filling constraint (deterministic)
Let f be an oriented plaquette and let Sigma be a shellable disk with boundary loop equal to the boundary loop of f (possibly transported along a fixed basepoint path). The ordered product of transported face holonomies of Sigma equals the boundary holonomy up to conjugation. If Sigma has q faces, then the SU(2) conjugacy geodesic angle theta obeys

 theta(W_f) <= sum_{p in Sigma} theta(W_p).

Using d(W)=1-cos(theta(W)), theta(W)^2 <= (pi^2/2)d(W), and d(W) <= theta(W)^2/2, obtain

 d(W_f) <= (pi^2/4) q sum_{p in Sigma} d(W_p).

This is valid for every single configuration and includes spatial and temporal faces; it requires an actual shellable disk and identical boundary holonomy, not merely an abstract homological filling. The conjugacy angle is invariant under conjugation and obeys the bi-invariant group triangle inequality.

## Theorem 2: staple-pair Bianchi filling and frustration reduction (deterministic; conditional on geometry)
Let J be plaquette-separated selected interior links. For e in J let q_{ep}(v) denote transported exterior staples of incident faces. For each pair (p,p') incident to e, the group element q_{ep} q_{ep'}^{-1} is, up to orientation/conjugation, a holonomy of the loop obtained by cancelling the selected link in the two face boundaries. Suppose this loop admits a shellable filling Sigma_{e;p,p'} consisting exclusively of *undeleted* faces, of at most L faces, and with total filling multiplicity over all e,p,p' at most K |J|. This assumption needs verification for the actual 3D Penrose/prism cell structure and boundary topology; in a cube, the complementary four faces of a 3-cell furnish such a filling for two adjacent faces incident to a shared edge.

The quaternion identity and Bianchi filling bound give

 F_e = [sum_{p<p'} beta_p beta_p' |q_ep-q_ep'|^2] / (B_e+|k_e|)
     <= C c_+ lambda sum_{p<p'} d(q_ep q_ep'^{-1})
     <= C c_+ lambda L sum_{p<p'} sum_{q in Sigma_{e;p,p'}} d_q(v).

Here |q-q'|^2=2 d(qq'^{-1}) and B_e+|k_e| >= B_e >= each beta_p. Hence

 F_J(v) <= C lambda L sum_{e,p<p'} sum_{q in Sigma_{e;p,p'}} d_q(v).

The exterior filling event sum over appearances of d_q <= A |J| log(lambda)/lambda implies F_J<= C A L |J|log(lambda), and for separated selected links E_I=F_J. If the cavity measure gives this exterior filling event probability at least lambda^{-C|J|}, the desired compatibility result follows. Crucially the Bianchi identity *does not prove that Gibbs probability lower bound*. For general interior sets I whose incident plaquettes overlap, E_I is a joint minimum rather than sum_e F_e and the reduction requires a separate compatible simultaneous filling construction.

## Theorem 3: exact cavity-event reformulation
For a_I=E_{rho_I} Z_I and F_I=-log a_I, E_I(v)=min S_I, the conditional partition function satisfies

 c^m lambda^{-3m/2} exp[-E_I(v)-Cm] <= Z_I(v) <= exp[-E_I(v)].

Therefore

 E_rho exp[-E_I] >= a_I >= c^m lambda^{-3m/2} E_rho exp[-E_I].

In particular, an independent upper bound F_I <= C m log(lambda) implies the target event via elementary truncation only for a sufficiently large threshold: set T=F_I + log 2; since Z_I <= exp(-E_I), splitting a_I into E_I <=T and E_I >T gives rho_I(E_I <= T) >= a_I/2 >= exp[-C' m log(lambda)]/2. But this direction uses the very insertion bound in question and is not a noncircular proof. Conversely, a compatible event of probability >= exp[-C m log(lambda)] at E <= C m log(lambda) implies F_I<= C'm log(lambda). Hence the purported event estimate and insertion cost are quantitatively equivalent up to O(m log(lambda)) losses. Reexpressing one as the other is not a solution.

## A separate rigorous noncircular reference class
When P(I) admits private Haar shield edges outside all undeleted faces, the event is provable by SU(2) ball integration, with lower bound (c lambda^-3/2)^r, r<=Dm; this does not encompass arbitrary interior Penrose supports.

## Conclusion
No unconditional polynomial-probability theorem for all thin interior Penrose supports has been proved by the present methods. The Bianchi/holonomy constraints provide deterministic compatibility on suitable fillings but no cavity large-deviation lower bound. The latter is an independent interacting weak-coupling estimate, which cannot be inferred from bounded incidence, pure-gauge Bianchi identities, Gaussian curvature covariance, or global volume-average action control alone. R3/R2 remain open.
