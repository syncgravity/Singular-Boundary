# Switch ancestry and sourcewise history quotient (2026-11-16)

## Why history counting needs a quotient

For a source x=(M,tau), let H_x(T) be the number of legal parent-before-child insertion histories that end at T. This is not the transport multiplicity. The transport relation is set-valued:
`C(x) = {T : H_x(T) > 0}`, and `d(x) = |C(x)|`.

The exact column is
`W(T) = sum_x 1_{H_x(T)>0} / d(x)`.
Replacing the indicator by H_x(T), or weighting histories uniformly, overcounts whenever two histories from the same source coalesce at the same labeled tree.

## An ancestry-resolved representation

A legal history is recorded as a sequence of steps
`sigma = ((J_1,e_1,epsilon_1), ..., (J_{s-1},e_{s-1},epsilon_{s-1}))`,
where:
- J_i is the next matching interval in a parent-before-child order of tau rooted at the interval containing port 1;
- e_i is the current port-tree edge selected for replacement, and it overlaps J_i;
- epsilon_i is one of the two middle-centered stars or the increasing path on the four ordered endpoints of e_i and J_i.

The verifier file `verify_pf_i16_switch_ancestry_quotient.py` retains the full history in each forward state. At the end it groups histories by their final labeled tree T and records:
1. H_x(T), the raw number of histories;
2. one lexicographically canonical history for the pair (x,T);
3. d(x), the number of distinct final trees.

It then accumulates the transport using 1/d(x) once per distinct target, and separately reports raw history counts. This safeguards against confusing history multiplicity with source-target incidence.

## What this refinement does and does not give

For fixed T, define A(T) = {(x,sigma): sigma is a legal history from x ending at T}. There is a projection p:(x,sigma) -> (x,T). The desired column is not the size of A(T); it is the weighted size of its image:
`W(T) = sum_{(x,T) in p(A(T))} 1/d(x)`.

Thus a reverse-count proof must bound the image after collapsing all histories with the same source and target. A bound on raw histories is useful only if accompanied by a bound on coalescence H_x(T), or a direct way to count canonical representatives.

The verifier is configured for exact ancestry-resolved enumeration at n=4 and n=6. It has not yet been executed in this work session. It is intentionally separate from the n=8 fractional-column verifier because retaining all histories can grow much faster than retaining only distinct output trees. No n=8 ancestry run or all-orders estimate is claimed.

## Mathematical proof boundary

This is a sharper combinatorial model, not a proof of W(T)<=1. It identifies the exact quotient that a reverse-switch argument must control and supplies a finite verifier to measure history coalescence without corrupting the transport weights.
