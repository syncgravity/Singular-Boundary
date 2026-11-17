# PF-I16: factorized charge over the complete canonical parent neighborhood

Date: 2026-11-17

## Objective

Retain the full multivalued-\(\pi\) relation. For each fixed parent/deleted-interval fiber \(F=(p,J)\), construct a fractional allocation of its split demand
\[
\delta(F)=\sum_{x\in F}\frac1{d(x)},\qquad d(x)=|L_0(\tau_x)|,
\]
over the complete canonical parent neighborhood \(C_p=C_{\rm can}(p)\), without choosing an injective fixed parent representative.

## Exact fiber decomposition

For each \(P\in C_p\), let \(\mathcal L_J(P)\) be the set of distinct child port trees obtained by valid guarded final switches inserting \(J\) last whose inverse parent tree is \(P\).

The fixed-\((p,J)\) fiber theorem supplies:
1. the child row is common to every child source in \(F\);
2. inverse final switching is unique for fixed \((T,J)\);
3. every \(P\in C_p\) has at least two valid final-switch lifts;
4. lift sets for distinct parent targets are disjoint.

Thus
\[
N(F)=\bigsqcup_{P\in C_p}\mathcal L_J(P).
\]

## Proposed factorized charge

Define
\[
\boxed{
\lambda(F,T)=
\frac{\delta(F)}
{|C_p|\,|\mathcal L_J(P_J(T))|}
\quad(T\in N(F)).
}
\tag{FC}
\]

For each fiber,
\[
\sum_{T\in N(F)}\lambda(F,T)
=\sum_{P\in C_p}|\mathcal L_J(P)|
\frac{\delta(F)}{|C_p|\,|\mathcal L_J(P)|}
=\delta(F).
\]
So (FC) is a genuine fractional row allocation over all canonical parent targets. It does not assume parent-source/parent-target injectivity. It is generally nonuniform on the child target row.

For a child target \(T\), the exact load is
\[
L(T)=
\sum_{J\in\mathcal J(T)}
\sum_{p:\,P_J(T)\in C_p}
\frac{\delta(p,J)}
{|C_p|\,|\mathcal L_J(P_J(T))|}.
\tag{1}
\]
A bound \(L(T)\le1\) for every target proves the split-demand quotient Hall inequality.

## Parent-side reduction

Set
\[
A_J(P)=\sum_{p:\,P\in C_p}\frac{\delta(p,J)}{|C_p|}.
\]
Then
\[
L(T)=\sum_{J\in\mathcal J(T)}
\frac{A_J(P_J(T))}
{|\mathcal L_J(P_J(T))|}
\le\frac12\sum_{J\in\mathcal J(T)}A_J(P_J(T)),
\tag{2}
\]
using the all-orders lower bound \(|\mathcal L_J(P)|\ge2\).

Therefore a sufficient target-side theorem is
\[
\boxed{
\sum_{J\in\mathcal J(T)}A_J(P_J(T))\le2
\quad\text{for every target }T.
}
\tag{3}
\]
This is now the focused structural problem: control parent-source incidence mass over the valid reverse marks of a target. The corrected reverse-mark classification (Type I and Type II only; distance-three leaf/leaf candidates are invalid) must be used when analyzing \(\mathcal J(T)\).

## Verification

Verifier: `research/verification/verify_pf_i16_factorized_reverse_switch_charge.py`

Workflow: `.github/workflows/pf-i16-factorized-reverse-switch-charge.yml`

The verifier computes the charge exactly with rational arithmetic at 4, 6, 8, and 10 ports. It:
- constructs every fixed \((p,J)\) fiber for complementary sources;
- checks common child rows;
- enumerates the complete canonical parent neighborhood;
- partitions child outputs by their unique inverse parent target;
- checks every parent target has a lift;
- assigns \(\delta(F)/|C_p|\) to each parent target and divides it uniformly over that parent's complete lift set;
- checks exact conservation of total demand and computes every target column load.

A successful maximum column load at most one is a finite fractional Hall certificate for that order. A load above one rejects only this particular factorized allocation, not multivalued-\(\pi\) Hall.

## Diagnostic correction

An initial implementation compared parent-target keys encoded by a port-count-dependent integer encoder with child-target keys represented as edge tuples. The resulting set mismatch was a verifier key-type bug, not a mathematical counterexample. The verifier now uses canonical edge tuples consistently. No mathematical conclusion should be drawn from the earlier failed runs.

## Status

The factorized allocation is an exact structural construction conditional only on the already established fixed-fiber inverse partition and lift lower bound. The target capacity-one estimate (1), or sufficient estimate (3), remains open until the exact finite run is complete and, more importantly, until an all-orders argument is found.

No all-orders complement Hall theorem, weighted one-link inequality, or Yang–Mills mass gap is claimed.


## Verifier correction (2026-11-17)

The first completed run exposed an implementation error in the target-load accumulator: the loop iterated over each lift as `Tcode` but incremented the stale outer-loop variable `T`. Consequently it accumulated each fiber's total charge on one unrelated final target, producing artificial loads (including values greater than 1) and a severely undercounted target-column set. Those numerical loads and the associated apparent overload are invalid and must not be interpreted mathematically.

The verifier was corrected to increment `loads[Tcode]` in commit `4d1c8a823be07a5b18a1dadf727236579147fd2c`. A fresh workflow run is required before reporting any factorized-charge result. The structural identity and conservation argument above are unaffected; the finite target-column computation is pending re-verification.


## Corrected exact finite result (2026-11-17)

The corrected accumulator was run successfully in GitHub Actions run [44156298056](https://github.com/syncgravity/Singular-Boundary/actions/runs/44156298056), at commit `3900934774f08e6d5ab98deca0bbf8222648dcfe`. Exact rational output:

| Ports | Complement sources | Fibers | Split demand | Child target columns | Maximum load | Overloaded targets |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | 18 | 12 | 18 | 37 | 5/4 | 4 |
| 8 | 600 | 424 | 600 | 1,482 | 247217/75600 | 123 |
| 10 | 31,728 | 21,240 | 31,728 | 95,844 | 2173943720504674434439/221974028224149801600 | 6,641 |

At n=6, the maximally loaded target is the tree with edges `(1,2),(2,3),(3,4),(3,6),(4,5)`, at exact load `5/4`. At n=8 and n=10, the maximum loads are approximately 3.270066137566 and 9.793685044583. Every run verifies exact total column load equals total split demand. Hence this is a failure of the uniform-over-parent-targets / uniform-over-lifts allocation, not a Hall obstruction.

A diagnostic extension now records each worst target's contributing fibers and the corresponding raw parent-incidence upper bound. This will distinguish whether the dominant concentration comes from many parent fibers mapping to the same reverse parent, or from unusually small lift multiplicities.


## Next test: nonuniform split-demand fiber flow

The uniform factorized charge is too concentrated. The next relaxation removes both uniformity requirements while retaining the exact source-to-fiber decomposition. For each source x with d(x) non-root leaves, assign demand 1/d(x) to each leaf fiber F=(p,J). The fiber's complete child-target row N(F) is common to every source in that fiber. The necessary sufficient quotient condition for this split demand is

\[
\left|\bigcup_{F\in S}N(F)\right|\ge \sum_{F\in S}\delta(F),\qquad
\delta(F)=\sum_{x\in F}\frac1{d(x)}.
\]

This is tested by an exact capacitated bipartite max-flow network: source-to-fiber capacity L*delta(F), target-to-sink capacity L, where L=lcm(1,...,s-1), and each fiber is adjacent to every target in N(F). All capacities are integers; max-flow integrality makes a full flow an exact rational fractional Hall certificate, not a numerical LP approximation. A deficient min-cut would reject this fiber quotient only, not the original source Hall statement.

Verifier: `research/verification/verify_pf_i16_split_demand_fiber_hall_flow.py`.
Workflow: `.github/workflows/pf-i16-split-demand-fiber-hall-flow.yml`.
Workflow run is queued as [44159648991](https://github.com/syncgravity/Singular-Boundary/actions/runs/44159648991). It currently tests n=6 and n=8, where the graph is small enough for exact max flow.


## Split-demand flow verifier correction (2026-11-17)

The first queued run [44159648991](https://github.com/syncgravity/Singular-Boundary/actions/runs/44159648991) failed before constructing the network: `sources(n)` is a generator, but the verifier called `len(sources(n))`. This is a Python harness error, not a Hall result. The verifier now materializes the source iterator once as `all_sources=list(sources(n))`, counts that list, and uses it consistently for the fiber construction and accounting (commit `4d5c12357cbd46c2e9ec093131ea62efea272e20`). A fresh push-triggered workflow run is pending. No quotient-Hall conclusion is drawn from the failed run.
