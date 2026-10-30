# Coupled-pivot SU(2) holonomy transport: triangular Haar coordinates and bounded-defect comparison
27 October 2026. Finite-volume theorem, restricted support class. No arbitrary thin-support theorem claimed.

## Setup
Let G=SU(2), normalized product Haar on a finite set of gauge links. S(U)=sum_{p in P0} beta_p d(W_p(U)), d(W)=1-Re tr W/2. For J links, P=P(J), r_p=number of incidences of J with p, and F_e=min_{u_e} sum_{p incident to e} beta_p d(W_p) (all other links fixed). Then pointwise sum_{e in J} F_e <= sum_{p in P} r_p beta_p d(W_p).

Select pivot links A={a_1,...,a_m} outside J and exactly m distinct faces P={p_1,...,p_m}. Condition on all nonpivot links v. Hypothesis T: the coordinate map a -> (W_{p_1}(a,v),...,W_{p_m}(a,v)) is a bijection of G^m preserving normalized Haar for each v. An independently verifiable sufficient geometric condition: after reordering, W_{p_i}(a,v)=L_i(a_1,...,a_{i-1},v) a_i^{epsilon_i} R_i(a_1,...,a_{i-1},v), with epsilon_i in {+1,-1}; every pivot occurs once in its own face and no later pivot occurs in an earlier face. The pivot can appear in *later* faces. The map is triangular, Haar preserving by repeated conditional left/right invariance and inversion. This weakens the individual private-pivot condition (which disallows any pivot in a second face).

Assume all retained Wilson terms not in P depend only on v, with no occurrence of pivots. Then the exact conditional joint measure of W_P given v is product of independent pi_beta(dW)=exp(-beta d(W))dW/q(beta). Hence for t r_*<1,
E_mu exp(t sum_J F_e) <= product_{p in P} q((1-t r_p) beta_p)/q(beta_p) <= C_{t,r_*}^{m}.
As m=|P(J)|<=Delta |J| for bounded link incidence, absolute exp tail P(sum F_e>=A_t |J|+s)<= exp(-t s).

## Bounded-defect extension
Let the remaining pivot-dependent Wilson action be R(a,v)>=0, and after the Haar-coordinate map write R~(W,v). Let omega(v)=sup_W R~(W,v)-inf_W R~(W,v). Conditional to v, the tilted independent product law has RN derivative proportional to e^{-R~}, and for any nonnegative f(W),
 E[f(W)|v] <= exp(omega(v)) E_product f(W).
If sup_v omega(v)<=K m with K independent of coupling/cutoff, then
 E_mu exp(t sum_J F_e) <= exp(Km) product_p q((1-t r_p)beta_p)/q(beta_p) <= (e^K C_{t,r_*})^m.
This condition is sufficient but **not generally valid** for bulk Wilson side faces with beta~lambda: an extra pivot-dependent plaquette can have oscillation 2 beta=O(lambda). Therefore bounded-defect does not prove arbitrary-support R3.

## Example with genuinely coupled pivots
Take fixed exterior holonomies v_i and three pivot variables a,b,c with face words W_1=a v_1, W_2=a b v_2, W_3=b c v_3 (or words with inverses/orientations). In order p1,p2,p3, holonomy map is triangular. Neither a nor b is private to a single selected face, yet the conditional Haar law of W_1,W_2,W_3 is product Haar and the Wilson law factorizes if no further pivot-dependent plaquettes remain. This is an abstract coupled lattice subcomplex example; it is not asserted to occur for arbitrary Penrose interior stars.

## Beyond exact triangular blocks: relative partition comparison
Without bounded oscillation, define the conditional comparison ratio
R_t(v)=Z_{P,R}(v;{(1-t r_p)beta_p})/Z_{P,R}(v;{beta_p}).
Here both integrals use the same pivot-dependent remainder R, and R_t(v) equals exactly the conditional MGF for sum_p t r_p beta_p d(W_p). A uniform bound log R_t(v)<=C|P| is *equivalent to* the sought coupled-pivot conditional comparison and cannot be postulated as a proof. A particular transport a=Psi_v(W) with pushforward density product Wilson whose expected R action is O(|P|) relative to original provides a possible independent route; no such estimate is established generically.

## Caveats
Acyclic triangular incidence and absence/bounded oscillation of remaining pivot interactions are concrete, checkable but strong assumptions. Actual Penrose bulk cell complexes have cycles and extensive O(lambda) incident interactions, so these results do not establish arbitrary thin-support moments, compatible energy tails, R3/R2, or a Yang-Mills mass gap.
