# Localized mesoscopic Wilson Gibbs comparison: exact finite-collar theorem and entropy obstruction

Date: 2026-10-26. Context: SU(2) Wilson action on finite 2+1D bounded-incidence Penrose/square spacetime complexes. No continuum mass gap is presumed.

## Theorem 1. Conditional compatible-minimum comparison

Let Q be m internal links of a finite spacetime collar, v all exterior links, P(Q) the plaquettes meeting Q. Fix couplings beta_p in [0,c_+ lambda], lambda>=1, with at most D plaquettes incident to any link. Write

S_beta(u;v)=sum_{p in P(Q)} beta_p (1-Tr W_p(u,v)/2),
E_beta(v)=min_{u in SU(2)^Q} S_beta(u;v),
Z_beta(v)=int exp[-S_beta(u;v)] prod_{e in Q}du_e.

There are c,C>0 depending only on c_+,D (and Haar normalization) such that

exp[-E_beta(v)] [c lambda^{-3/2}]^m exp[-Cm] <= Z_beta(v) <= exp[-E_beta(v)]. (1)

The bound holds for every exterior gauge field v, on every finite bounded-incidence graph, independently of total volume. The minimizing set is gauge equivariant; no gauge-fixed representative is required for the inequality.

Proof: A minimizer u* exists. Parametrize u_e=exp(X_e)u_e* with |X_e|<=rho/sqrt(lambda), rho small fixed. Gradient of S vanishes at u* in all internal directions, and bounded incidence gives |D^2 S(u)[X,X]|<= C lambda sum_e |X_e|² on all SU(2)^m. Thus S(u)<=E_beta(v)+Cm on the product ball. Normalized Haar volume of each SU(2) ball is >=c lambda^{-3/2}. Integrate for lower bound; upper follows from S>=E. The argument includes all temporal plaquettes meeting Q.

## Corollary 2. Conditional coupling dilution, without fictitious staple alignment

If beta'_p<=beta_p with both families bounded by c_+lambda, then

0<=log[Z_beta'(v)/Z_beta(v)] <= [E_beta(v)-E_beta'(v)]+(3m/2)log(lambda)+C'm. (2)

The same holds for the full partition function after integrating v, with right-hand minimum shift placed inside a log exponential moment against the original exterior marginal eta_beta:

log[Z_full(beta')/Z_full(beta)] <= (3m/2)log(lambda)+C'm+log E_{eta_beta} exp[E_beta(v)-E_beta'(v)]. (3)

The independent constant in (2) may depend on the chosen fixed lower radius and Haar convention; all constants uniform in lambda,m and volume.

## Corollary 3. Fully localized Gibbs event estimate for ANY event A on Q

Let E_beta,A(v)=inf_{u in A(v)} S_beta(u;v), with inf empty = +infinity. Then

P_beta(A|v) <= [c^{-1}lambda^{3/2}]^m exp[C m - (E_beta,A(v)-E_beta(v))]. (4)

This is a genuine conditional Gibbs probability estimate. The factor exp[O(m log lambda)] is the entropy cost, while E_beta,A-E_beta is the *compatible* excess energy in the actual exterior temporal field. It can be integrated over v, but a useful bound requires control of that excess uniformly or probabilistically.

## Surface-repair scaling and why the naive mesoscopic strategy is not closed

On a free planar disk with N faces and prescribed boundary holonomy angle theta, compatible configurations exist with action <= beta_max theta²/(2N). At the former threshold theta²~lambda^{-1/2}, beta~lambda, the energy is O(sqrt(lambda)/N). But the general compatible-minimum estimate (1) has entropy cost O(m log lambda), and for regular mesoscopic disks m=Theta(N). Thus the crude combined bound has cost

O(sqrt(lambda)/N + N log lambda). (5)

Optimizing (5) yields N~lambda^{1/4}/sqrt(log lambda) and cost O(lambda^{1/4}sqrt(log lambda)), rather than O(log lambda). In particular choosing N~sqrt(lambda)/log lambda to lower the minimum repair energy to O(log lambda) incurs entropy O(sqrt(lambda)). This is an obstruction to the **current proof method**, not a theorem that true partition-function ratios grow that rapidly: most of the entropy may cancel between numerator and denominator, but proving cancellation needs scale-local fluctuation determinant/covariance estimates.

In the full spacetime theory the free-disk background need not be compatible with fixed transverse temporal plaquettes, so E_beta,A and E_beta must be computed in the FULL collar action. No claim that (5) supplies an actual Wilson probability bound is made absent a compatible repair with controlled excess energy.

## Necessary next independent theorem

One needs a gauge-covariant local repair map/coupling interpolation plus a *relative* fluctuation determinant comparison canceling the O(m log lambda) factors, and a Gibbs-averaged bound on compatible E_beta-E_beta'. Equations (1)-(4) alone do not imply |J|log lambda thin-support free energy, all-contour suppression, or continuum-stable background-subtracted connected polymers. R3 and R2 mass gap remain open.
