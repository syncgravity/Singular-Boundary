# PF-I16: all-orders upper bound on a single fiber's split demand

Date: 2026-11-19

## Lemma

Let (n=2s), and let (F=(p,J)) be a parent-source/deleted-interval fiber with parent source (p=(M',\tau')) on (2s-2) ports. Assume (p) has at least two matching intervals. Let
- (d=d(p)=|L_0(\tau')|) be the number of non-root leaves;
- (a=a(p,J)) count parent non-root leaves whose lifted intervals overlap (J);
- (b=b(p,J)) count parent root/internal vertices whose lifted intervals overlap (J).

The exact demand identity is
[
\delta(F)=\frac{a}{d}+\frac{b}{d+1}.
]

Since (\tau') has (s-1) vertices and at least one non-root leaf,
[
1\le d\le s-2,\qquad 0\le a\le d,qquad 0\le b\le s-1-d.
]
Therefore
[
\boxed{
\delta(F)\le 1+\frac{s-1-d}{d+1}
=\frac{s}{d+1}\le\frac{s}{2}.
}
\tag{FDC}
]
Writing (g=a+b) for the number of parent overlap-neighbors of (J), the same identity also gives
[
\boxed{
\frac{g}{d+1}\le\delta(F)\le\frac{g+1}{d+1}.
}
\tag{FDC-local}
]
For the one-interval parent base case, (\delta(F)=1), which also satisfies (\delta(F)\le s/2) at (s=2).

## Proof

The child sources in (F) are exactly the extensions obtained by adjoining (J) to the matching and one edge (JI) to the parent overlap tree, with (I) an overlap-neighbor of (J). If (I) is a non-root leaf, the child leaf count stays (d), contributing (1/d); there are (a) such neighbors. If (I) is root/internal, the child leaf count is (d+1), contributing (1/(d+1)); there are (b) such neighbors. This is the exact demand formula.

There are (s-1) parent interval vertices. Exactly (d) are non-root leaves, so at most (s-1-d) are root/internal. Thus (a\le d), (b\le s-1-d), and
[
\delta(F)\le\frac{d}{d}+\frac{s-1-d}{d+1}
=\frac{s}{d+1}\le\frac{s}{2}.
]
For the local bound, put (g=a+b). Since (a/d\ge a/(d+1)),
[
\delta(F)\ge\frac{a+b}{d+1}=\frac{g}{d+1}.
]
Also
[
\delta(F)=\frac{g}{d+1}+\frac{a}{d(d+1)}
\le\frac{g+1}{d+1},
]
using (a\le d). QED.

## Why this matters, and what it does not prove

This gives an order-uniform cap on the demand of one fiber and a sharper local comparison with the degree of (J) in the parent overlap graph. For the row-normalized allocation,
[
\lambda_k(F,T)=\frac{\delta(F)}{|N_k(F)|},
]
it yields
[
\lambda_k(F,T)\le\frac{s}{2|N_k(F)|}.
]
The bound may help combine the noncrossing row-expansion estimate with a target-side reverse-incidence estimate. It does not itself bound the sum of competing fibers at a target, and therefore does not establish (RNL_k), (BQH_k), or Hall.

## Status

**Proved:** the single-fiber demand cap (FDC) and local degree comparison (FDC-local), conditional only on the already-proved exact demand identity.

**Open:** target-load control across different fibers, arbitrary-family blockwise mixed Hall, and the all-orders multivalued-(\pi) Hall theorem.
