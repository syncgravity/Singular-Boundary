# Exact insertion-free-energy concentration for nonlinear SU(2) Wilson guard backgrounds

Date: 2026-10-26

## Scope
Finite oriented plaquette complex with normalized product SU(2) Haar measure and Wilson action S(U)=sum_p beta_p d(W_p), beta_p >= 0, d(W)=1-(1/2)Tr(W) >=0. No independence assumption on retained guard links and no Gaussian linearization.

## Exact cavity disintegration
Let I denote m internal links, v all remaining links, and P(I) all plaquettes incident on I. Write S=S_out(v)+S_I(u;v), where S_I=sum_{p in P(I)}beta_p d_p. Define Z_I(v)=int exp[-S_I(u;v)]du, E_I(v)=min_u S_I(u;v). Deleting P(I) gives Z_cav=int exp[-S_out(v)]dv, normalized rho(dv)=Z_cav^{-1} exp[-S_out(v)]dv; Z_full=Z_cav a, a=E_rho Z_I. Actual exterior marginal eta=(Z_I/a)rho. Insertion free energy F=-log a=log Z_cav/Z_full >=0.

## Theorem 1 (self-normalized concentration)
For any s>=0, eta(E_I >= F+s) <= exp(-s). For any t in [0,1], E_eta exp[t(E_I-F)] <= 1. Proof: Z_I(v)<=exp[-E_I(v)], hence eta(E>=F+s) <= exp[-F-s]/a=exp(-s). Also Z_I exp(tE) <= Z_I^(1-t), and Jensen concavity E_rho Z_I^(1-t) <= (E_rho Z_I)^(1-t)=a^(1-t); divide by a and multiply by exp(-t F)=a^t. No local spectral/mixing assumptions enter. In particular E_eta E_I <= F (by differentiation at t=0, or Jensen), and eta(E_I >=t) <= exp(F-t). This theorem locates, but does not bound, the insertion free energy F.

## Theorem 2 (averaged nonlinear large-field event)
Assume beta_p >= c_- lambda and bounded incidence, lambda>=1. Let X subset P(I), A_X={d_p>delta for every p in X}. The conditional event numerator N_X(v)=int_{A_X} exp[-S_I]du <= exp[-c_-lambda delta |X|] as Haar mass <=1. Then full Wilson probability P_mu(A_X)=(1/a) E_rho N_X <= exp[-c_-lambda delta |X|+F]. This sharper bound requires neither flat extension nor the small-ball denominator estimate, and has no (3m/2)log lambda term. Equivalently P_mu(A_X) <= exp[-c_-lambda delta |X|] Z_cav/Z_full. For individual X this is exactly a deletion partition-function comparison, not an independent upper bound on F.

More generally for A measurable in interior and exterior such that inf_{u in A(v)} S_I(u;v) >= L(v), P_mu(A) <= a^{-1} E_rho exp[-L(v)]. No independence of exteriors.

## Corollary (conditional criterion that would close contour bound)
If an independent noncircular proof yields F_I <= C_F m (1+log lambda) uniformly for chosen I, and m<=K|X|, then at delta=lambda^-1/2,
P_mu(A_X) <= exp[-c_-sqrt(lambda)|X| + C_F K (1+log lambda)|X|] <= exp[-c sqrt(lambda)|X|] for sufficiently large lambda. This is conditional on the nontrivial insertion free-energy bound.

## What remains open
For a thin interior selection I, F_I=log(Z_cav/Z_full) is the partition-function deletion cost of incident spatial-temporal plaquettes. This is closely related to, and generally at least as difficult as, a dilution free-energy estimate. Thus Theorem 1 is a genuine unconditional concentration around F_I but does not prove F_I=O(m log lambda). Attempting to claim the conditional contour bound unconditionally would be circular. Nor does the theorem imply spatial decay of guard correlations, RG contraction, R3 or R2 mass gap.
