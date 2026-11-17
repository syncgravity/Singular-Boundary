# PF-I16: structural charging program and exact finite certificates

Date: 2026-11-17

## 1. Charging formulation

Let X_k be the sources whose first overcrowded odd cut is k. A source x belongs to one fixed parent/deleted-interval fiber F=(p,J) for each non-root leaf J of its overlap tree. Write d(x)=|L_0(x)| and assign the split demand

\[
\delta(F)=\sum_{x\in F}\frac1{d(x)}.
\]

Then every source contributes exactly one unit over its leaf fibers. For any source family A, if S(A) is the set of fibers touched by A,

\[
|A|\le\sum_{F\in S(A)}\delta(F).
\]

Consequently the weighted quotient Hall inequality

\[
\left|\bigcup_{F\in S}(N(F)\cap Y_k)\right|
\ge \sum_{F\in S}\delta(F) \tag{CH}
\]

for every fiber subfamily S is sufficient for source-level Hall in the same-cut relation.

The exact flow network has source-to-fiber capacity delta(F), fiber-to-each-neighbor-target capacity delta(F), and target-to-sink capacity one. A saturating flow is a structural charge assignment: it routes every source's unit demand, split over its leaf representations, to target trees without overloading any target.

## 2. Exact finite charging theorem at 8 and 10 ports

For n=8 and n=10, d(x) divides 12. Thus multiply every demand and target capacity by 12 and obtain an integer network. The verifier is:

`research/verification/verify_pf_i16_overcrowded_cut_split_maxflow.py`

The corrected workflow run

https://github.com/syncgravity/Singular-Boundary/actions/runs/44078442710

completed successfully with:

| Ports | Complement sources | Fixed fibers | Distinct same-cut targets | Scaled demand | Flow |
|---:|---:|---:|---:|---:|---:|
| 8 | 600 | 424 | 1,458 | 7,200 | 7,200 |
| 10 | 31,728 | 21,240 | 95,125 | 380,736 | 380,736 |

Thus (CH) holds for every fiber subfamily at n=8 and n=10. This is stronger than checking individual fibers or a uniform row-spreading allocation: it proves existence of a nonuniform, capacity-respecting charge for every fiber subfamily at those two orders.

The demand totals are 600 and 31,728 respectively, exactly the numbers of complementary sources. The target capacities are 12 per target. The flow is integral, so after dividing by 12 it gives an explicit rational charging.

## 3. What the computation does and does not establish

The successful flows establish the finite weighted quotient Hall theorem at n=8 and n=10. Together with the all-orders terminal-class Hall theorem and the first-overcrowded-cut decomposition, this establishes Hall for the tested multivalued-pi relation at those finite orders.

It does not establish (CH) for arbitrary s. In particular, the fact that all d(x) divide 12 is special to these tested orders; for general s, the natural equal-leaf split has denominators among 1,...,s-1. More importantly, max-flow existence at two orders does not identify a formula for the charge or prove a uniform expansion estimate.

## 4. Structural theorem still required

The all-orders target is a recursively defined charge, not a fresh max-flow solution at each order. A viable form would be a family of nonnegative coefficients

\[
\lambda_s(F,T)\ge0
\]

such that:

1. lambda_s(F,T)=0 unless T is an admissible same-cut target for F;
2. sum_T lambda_s(F,T)=delta(F) for every fiber F;
3. sum_F lambda_s(F,T)<=1 for every target T;
4. the coefficients are defined from the parent charge at order 2s-2 and the final guarded switch, with no dependence on a global maximum-flow computation.

The natural recursive attempt is: choose a non-root leaf J with probability 1/d(x), charge the parent source to a parent target, and distribute that parent-target charge among its guarded final-switch lifts. The unresolved point is the target-side congestion estimate when distinct deleted intervals J and distinct parent sources lift to the same child target. The local theorem gives at least 2^{s-2} same-cut lifts per fiber, but it does not bound this cross-fiber congestion.

A proof of item 3 from the recursive rule would be the desired structural charging theorem and would imply (CH) for all s. No such congestion lemma is claimed here.

## 5. Correct logical boundary

- Uniform spreading over each fiber's neighborhood can fail even when (CH) holds.
- A failed equal-leaf split would only obstruct that split, not necessarily original source-level Hall.
- A successful split-demand flow proves the finite-order quotient Hall condition.
- Local fiber Hall alone is not enough for (CH).
- The weighted one-link inequality and Yang--Mills mass gap are not claimed.