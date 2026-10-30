# Localized cavity curvature bound: boundary-sensitive theorem and thin-support audit

27 October 2026.  Status: rigorous localized theorem; arbitrary thin-support cutoff-sharp conclusion NOT established.

## Definitions
Let G be a finite oriented cell complex whose faces have at most L edges and whose links meet at most D faces. Put gauge group SU(2), normalized Haar product measure, d_p(U)=1-(1/2)Tr W_p(U) in [0,2]. Let P_0 be the undeleted plaquettes in a Wilson cavity, with beta_p in [c_- lambda,c_+ lambda], lambda>=2. Let Q subset P_0 be any set of *distinct* undeleted faces, q=|Q|. Let K=union_{p in Q} boundary edges of p, k=|K|<=Lq. Put Y={p in P_0\Q: boundary p intersects K}, y=|Y|<=Dk. For repetitions a_p<=M let A=sum_{p in Q}a_p, so q<=A and sum a_p d_p<=M sum_Q d_p.

## Theorem (boundary-sensitive localized expectation and joint lower tail)
For the genuine cavity Gibbs measure rho, uniformly in global volume and boundary-link configuration,

 E_rho sum_{p in Q} d_p <= [ (3/2) k log lambda + C k + 2 c_+ lambda y ]/(c_- lambda).

For integer multiplicity a_p<=M,

 E_rho D_Q <= M[(3/2)k log lambda+Ck+2c_+lambda y]/(c_-lambda),

 rho[D_Q <= 2M ((3/2)k log lambda+Ck+2c_+lambda y)/(c_-lambda)] >= 1/2.

All constants depend only on c_+,c_-,L,D and uniform small-ball geometry; no ambient lattice volume appears. Spatial and temporal faces are included.

### Proof
Freeze all links v outside K. The entire action involving K is S_K(u;v)=sum_{p in Q} beta_p d_p(u)+sum_{p in Y} beta_p d_p(u,v). All remaining faces are independent of u and cancel in the conditional Gibbs density. Write Z_K(v)=integral_{SU(2)^K} e^{-S_K(u;v)}du. The identity D(nu_v||Haar_K)=-E_{nu_v} S_K - log Z_K(v)>=0 gives E_{nu_v} S_K <= -log Z_K(v). Since S_K>= sum_{p in Q}beta_p d_p, the left dominates c_- lambda E_{nu_v}sum_Qd_p.

To lower-bound Z_K(v), restrict every K link to a ball around identity of radius eps/sqrt(lambda). Every face p in Q has all its edges in K, hence W_p close to identity; bounded face length implies sum_{p in Q}beta_p d_p <= C q <= C'k (since every face has at least one boundary edge). For Y faces, regardless of v, the defect is <=2, so their total action is <=2c_+lambda y. Haar ball probability >= c lambda^-3/2 per link, giving Z_K(v)>=(c lambda^-3/2)^k exp(-Ck-2 c_+ lambda y). Substitute into entropy inequality, then integrate over the true marginal law of v. The multiplicity bound and Markov give the joint lower-tail result.

## A more informative trial-field refinement
For every measurable center assignment g(v)=(g_e(v))_{e in K} such that Q-face action at g(v) is at most A_Q(v), and Y-face action at g(v) at most A_Y(v), the same argument with lambda^-1 geodesic balls (global Lipschitz control, no stationary assumption) yields

 c_-lambda E_{nu_v} sum_Q d_p <= 3 k log lambda+Ck + A_Q(v)+A_Y(v).

In particular, an independent gauge-compatible repair construction making E_v[A_Q+A_Y] <= C k log lambda would prove the cutoff-sharp thin bound; this is not established by the entropy argument itself. Using balls of radius lambda^-1/2 around a stationary *joint* minimum gives a 3/2 factor but does not ensure the Q faces are flat.

## Obstruction and precise scope
For thin Q, k=O(q), y=O(q), so the theorem only gives E D_Q <= C_M(q log lambda/lambda+y)=O(A), not O(A log lambda/lambda). The boundary term cannot be dropped from this argument: fixing exterior links arbitrarily can force undeleted Y faces into competing staple orientations for Q repairs, with O(lambda) energy cost. A local entropy bound with an O(y) defect error is stronger than the older ambient-volume estimate, but not the arbitrary-thin theorem. For y=0 (a face-isolated union of closed incidence components), it establishes E D_Q <= C A log lambda/lambda and hence joint probability >=1/2. For y<=C A log lambda/lambda, likewise. For general y, a new bound on the relative surface action under the actual cavity marginal, or an alternative direct local Wilson comparison, is necessary. No R3 or continuum R2 claim follows.
