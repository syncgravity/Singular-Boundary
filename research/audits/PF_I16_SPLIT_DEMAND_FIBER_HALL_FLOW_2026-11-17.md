# PF-I16 Exact Split-Demand Fiber Hall Flow (2026-11-17)

## Status

**Positive exact finite-order result at 6, 8, and 10 ports.** The corrected parent-canonical multivalued-\u03c0 relation admits an exact split-demand quotient Hall flow at each tested order. This is a finite computation; it is not an all-orders proof.

- Branch: `research/pf-i16-admissible-exchange-2026-11-16`
- Verifier: `research/verification/verify_pf_i16_split_demand_fiber_hall_flow.py`
- Workflow: `.github/workflows/pf-i16-split-demand-fiber-hall-flow.yml`
- Workflow run: [44177680653](https://github.com/syncgravity/Singular-Boundary/actions/runs/44177680653)
- Checked-out commit: `2773ccc51d286eb2c8e0675584530a4bf875730d`
- Result: completed / success; exact max-flow deficit zero at every tested order.

## Quotient and demand

For a child source \(x=(M,\tau)\), let \(d(x)=|L_0(\tau)|\) be its number of non-root leaf intervals. For every such leaf \(J\), deleting \(J\) and its endpoints gives a parent source \(p\); write the corresponding fiber as \(F=(p,J)\). Define

\[
\delta(F)=\sum_{x\in F}\frac{1}{d(x)}.
\]

Each child source distributes total demand one equally over its \(d(x)\) non-root leaf fibers. All sources in a fixed fiber have the same retained child-target row \(N(F)\).

The required quotient Hall condition is

\[
\left|\bigcup_{F\in S}N(F)\right|\;\geq\;
\sum_{F\in S}\delta(F)
\qquad\text{for every fiber family }S.
\tag{QH}
\]

For a source family \(A\), let \(S(A)\) be the fibers touched by at least one source in \(A\). Every \(x\in A\) contributes its full split demand \(\sum_{J\in L_0(x)}1/d(x)=1\) among fibers in \(S(A)\). Hence
\[
|A|\leq\sum_{F\in S(A)}\delta(F).
\]
Since \(N(A)=\bigcup_{F\in S(A)}N(F)\), (QH) implies the source-level Hall inequality for the multivalued-\(\pi\) relation.

## Parent-canonical restriction

The verifier does not use the unrestricted forced-leaf-last output row as the final neighborhood. For each fiber \(F=(p,J)\), it:

1. generates the raw forced-last leaf outputs;
2. checks that every child source in the fiber has the same raw row;
3. computes the canonical leaf-last neighborhood \(C_p\) of the parent source (with the one-interval base case handled explicitly);
4. reverses the final guarded switch at \(J\), compresses the resulting tree to the parent ports, and retains a child target only when its projected parent target belongs to \(C_p\);
5. constructs the quotient flow using these retained, parent-canonical rows.

Thus the successful result below applies to the intended parent-canonical multivalued-\(\pi\) relation, not merely to the larger unfiltered leaf-last relation.

## Exact max-flow construction

Let
\[
L=\operatorname{lcm}(1,2,\ldots,s-1),\qquad n=2s.
\]
The verifier clears all rational demands by using integer capacities:

- source-to-fiber capacity \(L\delta(F)\);
- fiber-to-target capacity sufficient to represent adjacency (the row is the retained set \(N(F)\));
- target-to-sink capacity \(L\).

The total required flow is \(L\sum_F\delta(F)=L|X|\), where \(X\) is the complete child-source set. A max flow equal to this total is an exact rational fractional Hall certificate by integral max-flow integrality. No floating-point arithmetic is used for the demand or flow decision.

## Exact output

| Ports \(n\) | Sources | Fibers | Targets | Raw leaf-last incidences | Retained parent-canonical incidences | Scale \(L\) | Exact demand | Scaled demand | Max flow | Deficit |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 22 | 18 | 43 | 159 | 159 | 2 | 22 | 44 | 44 | 0 |
| 8 | 608 | 440 | 1,493 | 23,114 | 19,154 | 6 | 608 | 3,648 | 3,648 | 0 |
| 10 | 31,744 | 21,280 | 95,864 | 9,438,630 | 6,598,466 | 12 | 31,744 | 380,928 | 380,928 | 0 |

The workflow emitted `RESULT: exact split-demand quotient Hall flow exists.` at each of the three orders. At 8 ports, parent-canonical filtering removes 3,960 incidences; at 10 ports it removes 2,840,164 incidences. At 6 ports the raw and retained incidence counts coincide.

## What this proves, and what it does not

For each of \(n=6,8,10\), the computed max flow establishes (QH) for every subfamily of the enumerated finite fiber set. Consequently the source-level Hall condition holds for the finite parent-canonical multivalued-\(\pi\) relation at those orders.

This is stronger than finding a matching for one selected source family: the flow certifies the full fractional quotient demand, and max-flow/min-cut duality certifies all fiber subfamilies at the tested order.

It does **not** prove (QH) for arbitrary \(n\), provide a uniform structural bound, or establish the all-orders Hall theorem. The weighted one-link inequality and the Yang--Mills mass-gap proof therefore remain open.

## Next verification/research tasks

1. Export the successful integral flows (and preferably min-cut/replay data) as standalone certificates for each order, with a small independent verifier that checks capacities, conservation, adjacency, and total demand without rerunning the graph construction.
2. Identify a structural mechanism controlling the quotient neighborhood union as \(n\) grows. In particular, seek a decomposition or expansion inequality that explains why parent-canonical fiber rows jointly carry the split demand.
3. Keep all-orders claims separate from finite-order evidence. Do not promote the observed zero deficits to a theorem for arbitrary \(n\).
