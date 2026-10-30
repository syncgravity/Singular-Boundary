# R3: a Gibbs-controlled exterior-surgery criterion and the still-open Penrose step

**Date:** 27 October 2026. **Status:** rigorous sufficient criterion, explicit exact local Gibbs resampling, and obstruction analysis. **Not** a proof of the absolute exterior-minimum bound for arbitrary Penrose cavities.

## Definitions

Let `R` be retained four-link plaquettes in a finite SU(2) Wilson complex, each link incident on at most `nu` retained faces, with normalized Haar reference `m` and `d(g)=1-ReTr(g)/2`.

`mu_lambda(dx)=Z^{-1}e^{-lambda S_R(x)}m(dx)`, `S_R=sum_{p in R} d(W_p)`.
For a local link block `H`, `A(H)` is the set of retained faces incident on its links, `S_H(u;b)` their nonnegative action at frozen exterior `b`, and `s_H(b)=min_u S_H(u;b)`. Let `h=|H|`.

## Theorem 1: an actual Gibbs surgery implies an absolute exterior-minimum tail

Fix `alpha in (0,1]`, constants `C_0 >= 0`, `a>=0`, independent of ambient volume, and `q=|Q|`. Suppose for each `t>=0` the measurable bad set `E_t={x:lambda s_H(x_{H^c})>=t}` is partitioned into at most `M_q<=exp(C_0 q)` measurable pieces. On each piece there exists a one-to-one differentiable surgery `T_j` (on the ambient configuration variables, with all unchanged links retained exactly), changing at most `a q` links and satisfying:

1. `lambda[S_R(x)-S_R(T_j x)] >= alpha t - C_0 q(1+log(1+lambda))` for all `x` in that piece;
2. its Haar volume Jacobian `J_j(x)` satisfies `J_j(x)>=exp[-C_0 q(1+log(1+lambda))]`;
3. the images have total multiplicity at most `M_q` (injective on each piece suffices with at most `M_q` pieces).

Then exactly by Haar change of variables,

`mu_lambda(E_t) <= min(1, exp[-alpha t + 3 C_0 q(1+log(1+lambda))])`.

Consequently `lambda E_mu s_H <= (3C_0/alpha)q(1+log(1+lambda)) + 1/alpha` (replace the first term by zero if q=0). This criterion explicitly lists the three estimates a candidate Penrose surgery must prove; bounded number of changed links **alone** does not imply any of them.

**Proof:** On each piece, `e^{-lambda S(x)}<= e^{-alpha t + C_0 q(1+log(1+lambda))}e^{-lambda S(T_jx)}` and `dm(x)=J_j(x)^{-1}dm(T_jx)`. Summing integrals over at most `M_q` images and dividing by `Z` gives the bound. Integrate its clipped exponential tail to obtain the expectation bound. No Gibbs mixing, Gaussian expansion or approximated Haar Jacobian is used.

## Theorem 2: unconditional exact resampling only controls thermal excess

For every frozen exterior `b`, define the conditional block measure `nu_b(du)=Z_H(b)^{-1}e^{-lambda S_H(u;b)}du`. A compact-Haar small ball about any minimizer `u*(b)` gives for lambda>=1

`Z_H(b) >= exp[-lambda s_H(b)] [c_H e^{-2nu}lambda^{-3/2}]^h`, `c_H=8/(3pi^3)`.

Thus for `X=lambda[S_H(u;b)-s_H(b)]`,

`P_mu(X>=3h log(lambda)+2h(2nu-log c_H)+2z | b) <= e^{-z}`,

and `lambda E_mu[S_H-s_H|b] <= h[(3/2)log(lambda)+2nu-log(c_H)]`.

This holds for the **actual interacting retained Gibbs measure** and all exterior fields, including the nonflat ones. It is a legitimate Gibbs resampling action/entropy comparison, with no ambient-volume cost. It does **not** change `s_H(b)` because `b` is frozen.

## Single-link countercheck against a pointwise surgery

For one link U with two fixed opposite staples `A=I` and `B=-I`, the incident action is

`d(U)+d(-U)=2` for every U. Therefore `s_{\{e\}}(b)=F_e=2`, while any Haar-preserving adjustment of just U has action decrement exactly zero. The boundary data are a valid group assignment, though their unconditional occurrence under the 3D retained Gibbs measure must be investigated separately. This explicitly falsifies a *pointwise* locally improving surgery that freezes the exterior.

## Connection to the earlier nested Penrose certificates

The previous audited three-step direct-Z5 Penrose rhombus-prism supports have a stable 14-face inserted set. Its local 14-face Bianchi decomposition yields `sum_Q d(W_q)<=44 sum_{A} d(W_p)` for 54 retained faces. The 101-link block containing those face boundaries and its 232-link first collar were checked across four ambient radii in the preceding conversation. Those are incidence and nonabelian factor-count certificates, not a map `T_j` meeting Theorem 1. The earlier 1/10/41-link collar tests also found 2/8/24 exterior linear compatibility directions, respectively. These facts do **not** certify an ambient-uniform exterior surgery or an absolute distribution of `s_H`.

## Conditional local-energy and insertion consequences

If Theorem 1's hypotheses are proved with constants independent of volume for an `H` of `h<=Aq`, then from the conditional-Haar energy bound:

`lambda E_mu S_H <= h[(3/2)log(lambda)+2nu-log c_H] +(3C_0/alpha)q[1+log(1+lambda)]+1/alpha`.

For every target retained face set `A_0 subset A(H)`, `lambda sum_{p in A_0} E_mu d(W_p) <= lambda E_mu S_H` because plaquette deficits are nonnegative. If the inserted faces obey an independently verified nonabelian filling estimate `sum_Q d(W_q)<=K sum_{p in A_0}d(W_p)`, then Jensen yields the R3 insertion inequality `-log(Z_{R\cup Q}/Z_R)<= K lambda sum_{p in A_0} E_mu d(W_p)=O(q[1+log(lambda)])` when `K` is uniform. For supports with newly independent curvature modes, a separate compact-Haar comparison is still required.

## Precise open requirement

**Unproved:** for all target Penrose supports and their interacting retained measures, produce an exterior-dependent, essentially injective repair `T_j` that moves at most `O(q)` links, decreases the full retained Wilson action by `alpha s_H` in an appropriate event, and preserves Haar volume up to a factor `exp[-O(q log lambda)]`, with `exp[O(q)]` multiplicity. In particular, this cannot be inferred from `rank(d2)` or from the existence of independent inserted-holonomy Haar coordinates. No unconditional 3D exterior minimum tail, general R3 insertion theorem, or continuum mass-gap proof follows yet.
