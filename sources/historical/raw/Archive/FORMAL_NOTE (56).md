# Independent support-local frustration moments on pivoted Wilson stars

27 October 2026. Research note; restricted theorem, not arbitrary-support R3.

## Setting
Finite SU(2) gauge complex, normalized product Haar link measure, Wilson action S=\sum_{p\in P_0}\beta_p[1-\tfrac12\mathrm{tr} W_p], with beta_p>0. For a link e, collect incident retained faces P(e), with m_e=|P(e)|. Conditional on all links except e, S_e(u)=B_e-k_e\cdot u; F_e=B_e-|k_e|=\min_u S_e(u), where u and staples are unit quaternions, B_e=\sum_{p\ni e}\beta_p.

## Private-petal hypothesis
For every p in P(e), choose a distinct pivot link a_p\ne e which occurs in p exactly once and occurs in no other retained plaquette of the *full cavity* (and the choices a_p are distinct). The shared link e and all remaining links may participate in arbitrarily many additional Wilson interactions not involving the a_p; in particular, other nonpivot link variables need not be independent.

After conditioning on all nonpivot variables, the map (U_{a_p})_p -> (W_p)_p is a product of Haar preserving left/right translations and inversion. The joint conditional density is \prod_p e^{-\beta_p d(W_p)}/q(\beta_p) with q(\beta)=\int e^{-\beta d(W)}dW=e^{-\beta}z(\beta), z(\beta)=2I_1(\beta)/\beta. Thus the W_p are independent Wilson variables, even unconditionally and independent of every nonpivot variable. [Strictly: with exterior conditioned the measure of other variables has integrated-out effective density multiplied by \prod q(\beta_p), constant; so correct.]

By minimization over e, F_e \le S_e(U_e)=\sum_{p\ni e}\beta_p d(W_p) for the actually sampled U_e. Therefore for 0<t<1,
 E exp(t F_e) \le \prod_{p\ni e} E_{\pi_{\beta_p}} exp(t\beta_p d(W_p))
 =\prod_{p\ni e} q((1-t)\beta_p)/q(\beta_p)
 =\prod_{p\ni e} e^{t\beta_p} z((1-t)\beta_p)/z(\beta_p)
 \le C_t^{m_e}.
Since e^{-x}z(x) is comparable uniformly to (1+x)^(-3/2), C_t can be chosen finite depending only on t, not beta or the lattice size. Consequences P(F_e\ge s)\le C_t^{m_e}e^{-ts}, E F_e \le (m_e/t)\log C_t.

## Joint version
For a set J of links, suppose every face in P(J)=\cup_{e\in J}P(e) has a distinct private pivot a_p outside J, belonging to no other retained face. Let r_p=#{e\in J:e\in p} and assume r_p\le r_* (bounded face perimeter). Pointwise \sum_{e\in J}F_e\le\sum_{p\in P(J)} r_p\beta_p d(W_p). For 0<t<1/r_*,
 E exp(t\sum_{e\in J}F_e)\le\prod_{p\in P(J)}q((1-tr_p)\beta_p)/q(\beta_p)\le C_{t,r_*}^{|P(J)|}.
Therefore P(\sum_{e\in J}F_e\ge s)\le\exp[-ts+|P(J)|\log C_{t,r_*}], and if bounded incidence |P(J)|\le \Delta |J| the tail is support-local and cutoff uniform.

## Caveats
The private-pivot requirement is substantive and generally fails for bulk Penrose rhombus-prism face supports; arbitrary cavity boundaries do not create such private links automatically. No unconditional support-local E exp(t\sum F_e) for generic interior J follows. The argument is independent of unknown insertion ratios only for the explicitly specified private-pivot class. There is no assertion of R3 or continuum mass gap.
