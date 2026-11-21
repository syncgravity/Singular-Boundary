# Reverse counting: cut-load eligibility bound and its limitation (2026-11-16)

## Fixed-target necessary condition

Fix a labeled port tree T on n=2s ports. If a source x=(M,tau) reaches T under the three-move local-switch relation, then its matching load dominates the target load:
[
m(M)ge c(T)
]
coordinatewise. Write
[
mathcal M(T)={M: M	ext{ is a perfect matching and }m(M)ge c(T)}.
]
The number of source objects over a fixed matching M is exactly tau(H_M). Every source has at least 3^{s-1} distinct candidate trees. Therefore
[
W(T)=sum_{x:Tin C(x)}rac1{|C(x)|}
le rac1{3^{s-1}}sum_{Minmathcal M(T)}	au(H_M).
	ag{R1}
]
This is a valid reverse-counting relaxation: it counts every source whose cut-load could permit T, whether or not the local-switch relation actually connects that source to T.

## Exact eight-port test of the relaxation

For the previously identified worst target
[
T_*={15,24,34,45,56,57,58},
]
the target cut profile is
[
c(T_*)=(1,2,3,2,3,2,1).
]
Exhaustive enumeration of the 105 perfect matchings on eight ports gives:
- 42 matchings M with m(M) >= c(T_*);
- the corresponding overlap-tree counts tau(H_M) are 8 for 18 matchings and 16 for 24 matchings;
- hence sum_{M in M(T_*)} tau(H_M) = 18*8+24*16 = 528.

Since s=4, (R1) gives
[
W(T_*)le 528/27=176/9approx19.5556.
]
The exact weighted column from the three-move relation is approximately 0.976422959218. Thus the cut-load relaxation loses almost all of the useful information. It is not a proof of the desired column bound.

## What the reverse count must retain

The missing restriction is not another coordinatewise load condition. It is the *switch ancestry*: for a source (M,tau), T must be obtainable by a parent-before-child insertion history in which each inserted matching interval overlaps the edge being replaced, and the three replacement edges are one of the permitted local trees. Merely satisfying m(M)>=c(T) does not encode that ancestry.

A sharper reverse enumeration should therefore count compatible triples (M,tau,history) over T, then quotient histories that lead to the same source and use the source's distinct-output degree |C(M,tau)| as the denominator. Counting histories without this quotient is unsafe: different histories can coalesce to the same candidate tree, and the source weight is uniform over distinct outputs, not over histories.

## Proof boundary

(R1) is a correct but weak upper bound. The 8-port calculation is exact and reproducible by enumerating perfect matchings and spanning trees of their interval-overlap graphs. It does not establish W(T)<=1, nor does it supply an all-orders reverse-switch count. The required next ingredient is a degree-sensitive count of *switch-compatible* sources, rather than all cut-load-eligible sources.
