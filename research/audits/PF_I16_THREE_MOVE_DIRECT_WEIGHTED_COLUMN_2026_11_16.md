# Direct weighted-column decomposition for the three-move relation (2026-11-16)

## Exact targetwise identity

For a target tree T, let
\[
I_d(T)=\#\{x:T\in C(x),\ |C(x)|=d\}.
\]
Then the transport column is exactly
\[
W(T)=\sum_d\frac{I_d(T)}d.
\]
Writing \(I(T)=\sum_d I_d(T)\), and defining the harmonic mean of the degrees of incident sources by
\[
H(T)=\frac{I(T)}{W(T)},
\]
gives the equivalent targetwise criterion
\[
\boxed{W(T)\le1\quad\Longleftrightarrow\quad H(T)\ge I(T).}
\]
This is the direct incidence/degree balance; unlike the failed global estimate, it retains the full degree distribution among sources incident to each target.

## Exact finite test

Re-ran the three-move enumeration for n=4,6,8 and accumulated the exact degree histogram \(I_d(T)\) for every target. The worst-column target and its incident-source degree data are:

| n | worst target T (edge notation) | I(T) | exact W(T) | H(T)=I/W |
|---:|---|---:|---:|---:|
| 4 | {13,23,34} | 2 | 2/3 | 3 |
| 6 | {12,23,34,45,46} | 12 | 4/5 | 15 |
| 8 | {15,24,34,45,56,57,58} | 252 | 10304714186475339488603141793890797933127858844353922727 / 10553535319085571286580606709514309996986442323121646400 | 258.084877686377... |

The n=8 exact column slack is
\[
1-W(T)=
\frac{248821132610231797977464915623512063858583478767723673}
{10553535319085571286580606709514309996986442323121646400}
\approx0.023577040782.
\]
Thus the hardest tested target has only about 2.36% column slack.

For the n=8 worst target, grouping incident sources by candidate-set size gives:

| Candidate-set size d | Incident sources | Contribution to W(T) |
|---:|---:|---:|
| 99–127 | 12 | 0.104654605 |
| 128–191 | 40 | 0.236362338 |
| 192–255 | 56 | 0.245776221 |
| 256–383 | 78 | 0.238608369 |
| 384–552 | 66 | 0.151021427 |
| **Total** | **252** | **0.976422959** |

Each bin contribution is accumulated exactly as a rational number in the verifier; the displayed decimals are rounded. The source-degree histogram itself has 49 distinct degree values, ranging from 99 to 552.

The experiment confirms the mechanism behind the failed crude bound: 252 sources reach the worst target, but most of those sources have candidate sets much larger than the global minimum 27. Replacing every denominator by 27 destroys the compensation.

## Verifier update

The verifier at research/verification/verify_pf_i16_local_switch_fractional_transport.py now:
- retains the exact \(I_d(T)\) histogram for every target;
- reconstructs each worst-column mass from its degree strata and asserts equality with the original column accumulator;
- reports the harmonic mean \(H(T)\);
- reports degree-bin source counts and exact bin masses; and
- reports the largest individual degree-stratum contribution.

This is instrumentation for reproducible direct-column analysis. The earlier exact finite checks remain unchanged: 2, 22, and 608 left sources at n=4,6,8; 3, 45, and 1,688 distinct target trees; maximum columns 2/3, 4/5, and the exact n=8 rational above.

## Analytic target and proof boundary

The all-orders statement still needed is
\[
\boxed{\sum_d I_d(T)/d\le1\quad\text{for every labeled port tree }T.}
\]
The equivalent harmonic-mean form suggests a reverse-switch counting problem with degree-sensitive weights: a proof must show that the many sources reaching a complicated target have sufficiently large candidate families. A bound on \(I(T)\) alone cannot work, as the previous test showed.

No analytic estimate for \(I_d(T)\), no all-orders weighted-column bound, no n=10 three-move enumeration, and no weighted one-link or Yang--Mills mass-gap proof is established here. The finite computation identifies the precise weighted distribution that a proof must control; it does not prove the inequality beyond the tested orders.
