# Buffered cyclic defects under nonlinear SU(2) Wilson Gibbs measures
27 October 2026. Exact conditional theorem and explicit cyclic example. Arbitrary-support Penrose conclusion open.

## Definitions
Consider an arbitrary finite (possibly nonperiodic) SU(2) Wilson cell complex, with normalized product Haar link measure, nonnegative Wilson action S(U)=sum_p beta_p d(W_p), d(g)=1-(1/2)Tr(g), couplings beta_p <= c_+ lambda, lambda>=2, uniformly bounded face lengths and link incidence. Pick two disjoint sets A and B of links, n=|A|+|B|, and let w be all other links. Define S_L(a,b;w) to be the sum of **all** plaquette terms touching A union B; the residual exterior action S_out(w) contains no dependence on a or b. Let S_A(a;b,w) be the sum of plaquette terms touching A (all of which are in S_L), and E_A(b,w)=min_a S_A(a;b,w). Then S_L>=S_A>=E_A>=0 pointwise (because S_L includes S_A plus other nonnegative Wilson terms). Let M_L(w)=min_{a,b}S_L(a,b;w). Let Z_L(w)=int e^{-S_L(a,b;w)} da db.

## Theorem: buffered defect conditional tail
For all w and all s>=0,
  mu(E_A(b,w)>=s | w) <= min{1, exp(M_L(w)+C n+(3/2)n log lambda -s)}.
Equivalently, mu(E_A>=M_L(w)+C n+(3/2)n log lambda+t |w)<=e^{-t}.
Proof: Numerator is at most e^{-s} since S_L>=E_A and integration of remaining factors against normalized Haar <=1. At a global minimizer (a*,b*) of S_L, stationary points and bounded local Wilson Hessian give S_L <= M_L+C n on product SU(2) balls of radius c/sqrt(lambda). Their Haar volume >=(c0 lambda^(-3/2))^n; hence Z_L>=exp(-M_L-Cn)(c0 lambda^(-3/2))^n. Divide. The bound is fully nonlinear, uses no independence of pivot fields, and includes cycles and all spatial-temporal plaquettes touching A union B.

## Corollaries
(A) If each frozen exterior w has a jointly flat extension for the complete buffered action S_L, i.e. M_L(w)=0, then unconditional mu(E_A>=C n+(3/2)n log lambda+t)<=e^{-t}. If n<=C_0|A| or n<=C_0|Q|, this is a support-local cutoff-uniform absolute tail.
(B) If a deterministic bound M_L(w)<=L_n holds, then the corresponding threshold shifts by L_n. If there is only an exterior-marginal tail bound mu(M_L>=L_n+s)<=Bexp(-ct), use union bound; it is not an independent solution.
(C) The same tail holds for relative minimum gaps E_A-E_{A,t} if the diluted action is nonnegative, since 0<=E_A-E_{A,t}<=E_A.
(D) This is a **sufficient geometric condition** not established for arbitrary Penrose cavity supports. An arbitrary exterior can impose nontrivial holonomy around cycles on the boundary of L, forcing M_L(w)~lambda. Adding finitely many buffer links does not automatically remove such incompatibility.

## Explicit closed three-face cyclic model
Let a,b,h in SU(2), each Haar a priori, with S=lambda[d(a)+d(b)+d((ab)^(-1)h)]. Treat A={a,b}, B={h}, and no frozen w. Then the full joint configuration a=b=h=I is flat so M_L=0 and the buffered theorem gives P(E_A(h)>= (9/2)log lambda+C+s)<=e^{-s}. Even more explicitly, the exact joint partition function is q(lambda)^3, where q(lambda)=int_SU2 exp[-lambda d(g)] dg=e^{-lambda}2I_1(lambda)/lambda ~ sqrt(2/pi)lambda^(-3/2). Proof: integrate over h in the third face first, giving q; integrate a and b independently to obtain q^3. The marginal h density is Z_A(h)/q^3, where Z_A(h)=int exp(-S_A(a,b;h)) da db and E_A(h)=min S_A. Since Z_A(h)<=e^{-E_A(h)}, P(E_A>=s)<=q(lambda)^(-3)e^{-s} <= C lambda^(9/2)e^{-s}. This independently confirms cutoff-uniform absolute cycle-defect suppression in the true interacting joint Gibbs measure (not for frozen h).

## Geometry of the obstruction
For frozen h, E_A(h)>=2lambda theta(h)^2/(3pi^2), as in prior cyclic note. However the **unfrozen** h is not Haar under the interacting joint Gibbs measure: its marginal is Z_A(h)/q^3 and penalizes frustrated holonomy. The distinction between fixed and jointly integrated boundary is essential. For generic Penrose supports, w can retain nontrivial fixed outer loop holonomies and the buffer minimum M_L(w) can be order lambda. No general bounded buffer size or support-local tail for M_L is proved. The theorem does not imply arbitrary-support insertion free energy or the R3/R2 mass gap.
