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
