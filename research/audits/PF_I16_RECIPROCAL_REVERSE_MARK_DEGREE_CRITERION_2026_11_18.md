# PF-I16: reciprocal reverse-mark degree criterion for mixed Hall

Date: 2026-11-18

## Status

This records a new sufficient condition for the direct mixed-fiber Hall inequality. It is an exact implication, not yet an established bound. No finite computation is claimed here.

The retained-grandparent shortcut remains disproved. The all-orders blockwise Hall inequality remains open.

## Definitions

Fix an odd first-overcrowded cut block (k). Let (mathcal F_k) be its ((p,J))-fibers, with demand
[
delta(F)=sum_{xin F}rac1{d(x)}
=rac{a(p,J)}{d(p)}+rac{b(p,J)}{d(p)+1}.
]
For each target (Tin Y_k), define its complete eligible reverse-mark fiber set
[
mathcal R_k(T)={Finmathcal F_k:Tin N_k(F)},
qquad
r_k(T)=|mathcal R_k(T)|.
]
Set (1/r_k(T)=0) when (r_k(T)=0).

## Reciprocal-degree lemma

If every fiber satisfies
[
oxed{quad
delta(F)le
sum_{Tin N_k(F)}rac1{r_k(T)},
quad}
	ag{RD}
]
then the blockwise mixed Hall inequality holds:
[
left|igcup_{Fin S}N_k(F)ight|
gesum_{Fin S}delta(F)
qquad(Ssubseteqmathcal F_k).
]

### Proof

For arbitrary nonnegative fiber weights (z_F), every target satisfies
[
max_{Finmathcal R_k(T)}z_F
ge rac1{r_k(T)}
sum_{Finmathcal R_k(T)}z_F,
]
with both sides zero if (mathcal R_k(T)) is empty. Summing over targets and reversing the finite sums gives
[
egin{aligned}
sum_{Tin Y_k}max_{Finmathcal R_k(T)}z_F
&ge
sum_F z_Fsum_{Tin N_k(F)}rac1{r_k(T)}\
&ge sum_Fdelta(F)z_F.
end{aligned}
]
This is exactly the weighted dual (MR). Equivalently, for a fiber family (S), summing the reciprocal-degree shares over its incident targets gives
[
sum_{Tincup_{Fin S}N_k(F)}
rac{|mathcal R_k(T)cap S|}{r_k(T)}
ge sum_{Fin S}delta(F).
]
Each summand on the left is at most one, proving the union inequality.

The allocation interpretation is particularly direct: give each target (T) one unit of capacity, split equally among *all* its eligible fibers. Fiber (F) receives
[
q(F)=sum_{Tin N_k(F)}1/r_k(T).
]
If (q(F)gedelta(F)), trim its received shares to total exactly (delta(F)). Trimming preserves every target capacity constraint.

## Why this is distinct from the failed uniform row transport

The previously rejected transport assigned a constant (delta(F)/|N_k(F)|) along every edge of a fiber row. Its target load was overloaded at ten ports.

(RD) instead assigns a target-dependent share (1/r_k(T)). It prices a target according to its actual reverse-mark competition, so high-collision targets contribute less to every incident fiber and low-collision targets contribute more. It preserves capacity one identically before any trimming. It also treats crossing and noncrossing fibers together, provided (mathcal R_k(T)) includes every eligible fiber in the block.

## Exact finite test and proof obligation

The next finite diagnostic should compute, with exact rational arithmetic,
[
q(F)-delta(F)
=
sum_{Tin N_k(F)}rac1{r_k(T)}-delta(F)
]
for every fiber in each cut block, using the *complete* target-side eligible-fiber incidence relation. The test must include all competing crossing and noncrossing fibers in (r_k(T)); computing reciprocal degrees within a restricted subfamily would overstate the available capacity.

A single negative value refutes (RD) as a sufficient route at that order, but does not refute mixed Hall. Nonnegative values for all fibers at finite orders certify only those orders. An all-orders proof would still need a structural lower bound on the reciprocal-degree sum, likely by grouping target reverse marks according to the deleted interval's two possible boundary starts and the parent overlap-tree attachment type.

The exact local demand identity supplies the right comparison: each parent overlap-neighbor (I) contributes (1/d(p)) when it is a non-root leaf and (1/(d(p)+1)) when it is root/internal. The unresolved step is to show that the target-side reciprocal competition leaves at least this much capacity for each fiber.

## Proof boundary

**Proved here:** (RD) implies the full weighted mixed-Hall dual and hence blockwise Hall.

**Not proved:** (RD) itself at any new order, or for all orders. No new workflow or finite result is claimed.

**Still open:** the all-orders multivalued-(pi) Hall theorem, and therefore the unconditional weighted one-link inequality.
