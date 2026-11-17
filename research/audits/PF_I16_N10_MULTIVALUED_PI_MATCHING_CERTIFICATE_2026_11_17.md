# PF-I16: independently verified n=10 multivalued-pi Hall matching certificate

Date: 2026-11-17

Branch: `research/pf-i16-admissible-exchange-2026-11-16`

Workflow: [44031284003](https://github.com/syncgravity/Singular-Boundary/actions/runs/44031284003)

Artifact: [pf-i16-n10-multivalued-pi-matching-certificate](https://github.com/syncgravity/Singular-Boundary/actions/runs/44031284003/artifacts/14309344057)

## Result

The multivalued-pi child relation at ten ports has a left-saturating matching, and the selected matching has an independently replayed certificate.

- Child sources: 31,744
- Distinct child target trees in the relation: 95,864
- Matched child sources: 31,744 / 31,744
- Deficiency: 0
- Distinct parent sources represented: 608
- Parent-source fiber sizes among matched children: 12–98
- Distinct assigned (parent source, projected parent target) pairs: 10,179
- Multiplicity of an assigned parent-source/parent-target pair: 1–43
- Selected leaf-index histogram: {1: 7,765; 2: 8,458; 3: 7,630; 4: 7,891}

The certificate checker reports:

`PASS: explicit n=10 multivalued-pi matching certificate`

The certificate contains one row per child source, recording the child matching target, a selected non-root leaf interval, the parent matching source, and the projected parent target. The checker independently verifies source enumeration, selected leaf validity, parent deletion/compression, final-switch inversion, canonical parent-neighborhood membership, and global uniqueness of the child targets.

## A useful quotient interpretation

The certificate induces a *nonuniform integral allocation* of child-source demand to parent-leaf fibers.

For each child source (x), the matching chooses exactly one admissible non-root leaf (ell(x)), hence one fiber
[
f(x)=(\pi_{\ell(x)}(x),\ell(x)).
]
The assigned target (T_x) belongs to that fiber's restricted neighborhood, and the (T_x) are globally distinct. Thus the selected fiber demand
[
d_f=|\{x:f(x)=f\}|
]
is routed injectively into the fiber neighborhood, with no target capacity exceeded.

In this certificate:
- 16,176 distinct parent-leaf fibers receive positive selected demand;
- each selected fiber receives demand 1–4;
- the demand histogram is 1: 6,353; 2: 5,400; 3: 3,101; 4: 1,322.

This is a genuine nonuniform alternative to the failed uniform split-demand transport. It is not a proof of a general allocation theorem: the selected leaf and target are obtained jointly by a finite maximum-matching computation. In particular, it does not establish that a canonical or local deterministic rule can make these choices for arbitrary even (n).

## What this establishes, and what it does not

It establishes a finite, independently checkable Hall-saturating matching for the multivalued-pi restricted relation at (n=10). The relation retains 15,834,241 unique child-source/target incidences in the generating run, about 76.891940% of the all-orders incidence set, while still matching every child source.

It does not prove Hall for arbitrary (n), nor the weighted one-link inequality. The uniform split-demand column bound remains false at (n=6,8); that failure is avoided here by choosing one leaf per source as part of a global matching, not by proving a universal closed-form fractional transport.

## Next proof obligation

A viable all-orders route must replace the finite matching computation with a structural theorem that, for every even (n), jointly chooses for each child source:
1. one admissible non-root leaf;
2. one parent-neighborhood target after inverse final-switch projection;
3. a child lift such that all chosen child targets are distinct.

Equivalently, prove Hall directly for the multivalued-pi relation, or prove a recursive augmenting/exchange theorem whose invariants imply Hall. Parent-target reuse is permitted and substantial (10,179 distinct parent-source/target pairs for 31,744 children), so a proof must control global child-target collisions rather than demand injectivity after parent projection.

The implication from an all-orders load-dominating matching to the weighted inequality is recorded in `PF_I16_MULTIVALUED_PI_ALL_ORDERS_PROOF_PROGRAM_2026_11_16.md`.
