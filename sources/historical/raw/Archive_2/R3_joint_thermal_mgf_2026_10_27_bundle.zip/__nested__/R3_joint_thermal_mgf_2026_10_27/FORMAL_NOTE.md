# Original Q14: uniform joint thermal exponential moment and remaining frustration obstruction

Scope: fully interacting compact SU(2) Wilson Gibbs measure on any finite retained 3-periodic-time Penrose prism containing the original Q14 neighborhood. Underlying geometry: original `cavity_audit.py`, original `verify_bianchi.py`, exact optimal 54-face fractional cover in `R3_Q14_full_cover_2026_10_27_bundle.zip`. The exact weight sum is 22, supported on 40 links. The cover has 54 fill faces, 10 outside A(H), 103 retained faces in selected link stars (49 outside fill), and 225 pair-staple loops of freely reduced length 6. These counts are imported from the independently certified prior bundle; the scripts included here reproduce its cover and words.

## Theorem 1: joint thermal fluctuations, no independence assumption

Let `S_e(U_e;omega)=n_e-U_e dot M_e`, `R_e=|M_e|`, and `m_e=n_e-R_e`. Define `X_e=lambda(S_e-m_e)`. For ANY finite retained Wilson Gibbs law, ANY fixed link e, ANY lambda>=0 and any s in [0,1),

`E[exp(s X_e) | U_(not e)] <= (1-s)^(-3/2)`.

Proof. If t=lambda R_e=0 then X_e=0 identically. Otherwise gauge-rotate so M_e points along the identity quaternion and put `y=1-u_0`. The conditional SU(2) Haar law of y on [0,2] has density proportional to `y^(1/2)(2-y)^(1/2) exp(-t y)`. Consequently the density of `X=t y` is proportional to `x^(1/2) exp(-x) h_t(x)` with `h_t(x)=sqrt(2-x/t) 1_(0<=x<=2t)`, a decreasing function. Hence X is dominated in first-order stochastic order by a Gamma(shape=3/2,rate=1) variable (monotone likelihood ratio relative to the gamma density). Its nonnegative exponential moment is bounded by `(1-s)^(-3/2)`. The conclusion survives averaging the exterior environment.

Let `w_e>=0`, `W=sum_e w_e>0`, and `T=sum_e w_e X_e`. Weighted Holder, with exponents `W/w_e`, gives, without independence,

`E exp(s T/W) <= product_e (E exp(s X_e))^(w_e/W) <= (1-s)^(-3/2)`.

For the original fractional cover W=22, so the bound is `E exp((s/22)T)<=(1-s)^(-3/2)`. In particular `E T<=33`. Chernoff implies for z>3/2:

`P(T>=22 z) <= (z/(3/2))^(3/2) exp(-z+3/2)`.

With `M=sum_e w_e m_e`, the full 54-face fill energy satisfies pointwise `lambda S_F <= lambda M + T` and, for all s in [0,1),

`E exp((s/22)(lambda S_F-lambda M)) <= (1-s)^(-3/2)`.

The bounded difference is not a bound on `lambda S_F` itself, because M is a strongly correlated random function of the retained exterior fields.

## Theorem 2: exact finite 225-loop expression and nontrivial conditional obstruction

At each selected link with n_e retained incident plaquettes, let `a_(e,i)` be the SU(2) staple and `L_(e,ij)=a_(e,i) a_(e,j)^(-1)`. Then

`m_e = [2 sum_{i<j} d(L_(e,ij))] / [n_e+|sum_i a_(e,i)|]`.

This equality is pointwise and independent of U_e. Consequently

`0<=m_e<= (2/n_e) sum_{i<j}d(L_(e,ij))`.

For t>0 and general fixed exterior link values, the pair loops L are U_e-independent, so conditioning only at link e cannot suppress their energy: take an environment whose two staples are I and -I; then d(L)=2 deterministically, regardless of lambda. This is an obstruction to a *uniform-in-exterior conditional* bound, not to a Gibbs-averaged bound under the actual full measure.

The upper curvature comparison plus the optimal cover yields

`lambda E S_F <= 33 + lambda sum_{e in C} [2 w_e/n_e] sum_{i<j} E d(L_(e,ij))`.

To infer `lambda E S_F=O(log(1+lambda))` it is sufficient, but NOT established, to bound the weighted 225-loop Gibbs expectation by `O(log(1+lambda)/lambda)` ambient-uniformly. One cannot replace this by a bound on the single-link thermal X_e.

## Critical logical boundary

This work proves a genuinely *joint*, nonstationary, fully interacting Gibbs exponential-moment estimate for **thermal excess**. It does not prove a joint exponential-moment estimate for **pair-staple disagreements**. A direct attempt to derive the latter from the former is circular: the disagreements are functions of the frozen environments whose conditional minima are not diminished by updating the selected link. Controlling them requires further resampling involving additional links, or another Gibbs comparison principle with a noncircular exterior-energy estimate. The 49 additional retained star faces remain part of that problem.

## Reproduction

`solve_cover.py`, `pair_bounds.py`, `verify_pair_words.py` regenerate the original incidence and exact word inventory. `verify_mgf.py` performs independent numerical checks of the single-link mgf and the analytic gamma bound; numerical checks supplement, not replace, the proof. The crucial new proof does not depend on sampling or numerics.
