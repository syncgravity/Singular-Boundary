# PF-I16: target-side reverse-mark structure and congestion reduction

Date: 2026-11-17

## 1. Reverse marks are not uniformly bounded

For a target tree T and a proposed inserted interval J={a,b}, the inverse routine in
`verify_pf_i16_source_dependent_leaf_peeling.py` first forms

```
S_T(a,b) = (N_T(a) union N_T(b)) minus {a,b}.
```

A valid reverse mark requires |S_T(a,b)|=2, say S={u,v}, and the induced
four-vertex tree on {a,b,u,v} to be one of the three allowed local trees.
The inverse parent tree is then uniquely
[
P_J(T)=(T-E(T[{a,b,u,v}]))\cup\{uv\}.
]
This uniqueness is conditional on J being a valid mark. It does not bound
the number of valid J, nor the number of parent sources whose canonical
neighborhood contains P_J(T).

The double-star example gives an unbounded family: if uv is the central edge,
with r leaves at u and q leaves at v, every cross-side leaf pair (a,b) has
S_T(a,b)={u,v} and induces the path a-u-v-b. Thus there are rq candidate
reverse marks.

## 2. Exact tree-theoretic classification of the raw two-neighbor condition

Before imposing port order, interval, canonical-parent, and no-reinsertion
constraints, the condition |S_T(a,b)|=2 together with connectedness of
T[{a,b} union S_T(a,b)] has only three distance types:

1. dist_T(a,b)=1 and deg_T(a)+deg_T(b)=4. The induced four-vertex tree is
   either a 3-star (degree pair 1,3) or a 4-path (degree pair 2,2).
2. dist_T(a,b)=2 and deg_T(a)+deg_T(b)=3. One endpoint is a leaf and the
   other has degree two; the induced four-vertex tree is a 4-path.
3. dist_T(a,b)=3 and both a,b are leaves. Their two neighbors u,v are
   adjacent, and the induced tree is a 4-path.

For dist 1, the external-neighbor sets are disjoint and their total size is
deg(a)+deg(b)-2. For dist 2, they intersect in the middle vertex, so their
union has size deg(a)+deg(b)-1. For dist 3, they are disjoint and have total
size deg(a)+deg(b); connectedness of the induced four-vertex set forces the
two middle neighbors to be adjacent. At distance at least 4, the induced
four-vertex set cannot be connected.

This classification makes the high-multiplicity part visible: type 3 marks
are exactly pairs of leaves on opposite sides of an edge whose two endpoints
are adjacent. Their count can be quadratic in the number of leaves. Any
uniform bound on |J(T)| is therefore impossible.

The actual relation is a subset of these raw candidates, since it also
requires the interval order, the local pattern in sorted port order, the
guard, and membership of P_J(T) in a canonical parent neighborhood.

## 3. Parent-source collision kernel

For a fixed valid mark J and its unique parent target P=P_J(T), define
[
mathcal P(J,P)=\{p: (p,J)\text{ is a nonempty child fiber and }
                         P\in C_{\rm can}(p)\}.
]
The target load for any factorized charge is exactly
[
L(T)=\sum_{J\in\mathcal J(T)}
       \sum_{p\in\mathcal P(J,P_J(T))}
       \alpha(p,J,P_J(T))\,
       \beta(p,J,P_J(T),T).
	ag{1}
]
Thus reverse uniqueness removes history multiplicity but leaves a
well-defined parent-source collision kernel at each mark and a sum over
marks.

A useful way to expose the two separate tasks is to set
[
A(J,P)=\sum_{p\in\mathcal P(J,P)}\alpha(p,J,P).
]
Then a sufficient estimate is
[
\alpha(p,J,P)\ge0,\quad
\sum_{P\in C_{\rm can}(p)}\alpha(p,J,P)=\delta(p,J),
]
and
[
\sum_{J\in\mathcal J(T)}
 A(J,P_J(T))\,
 \sup_{p\in\mathcal P(J,P_J(T))}
       \beta(p,J,P_J(T),T)
\le1.
	ag{2}
]
The supremum is a safe bound; if beta depends strongly on p, retain the
inner sum in (1) instead. Equation (2) is not yet established.

## 4. Parent matching gives only a fixed-mark bound

Suppose the canonical parent graph has a matching saturating its parent
sources, written p -> Q(p), with distinct Q(p). Define the sparse parent
allocation
[
\alpha(p,J,P)=
\begin{cases}
\delta(p,J),&P=Q(p),\\
0,&\text{otherwise}.
\end{cases}
]
For a fixed J and fixed child target T, reverse uniqueness gives one P_J(T).
Since Q is injective, at most one parent source p can satisfy Q(p)=P_J(T).
Consequently the contribution to L(T) from this fixed J is at most
[
\delta(p,J)\,\beta(p,J,P_J(T),T)\le\delta(p,J).
]
This eliminates parent-source collisions for each fixed mark.

It does not prove the desired sum over J: the same T can admit many distinct
valid marks, and the corresponding parent sources need not be the same.
The double-star family shows why summing a constant per mark cannot work.

## 5. The remaining structural inequality

The missing step is now sharply isolated. One needs a parent matching/allocation
Q together with a final-lift kernel beta for which
[
\boxed{
\sum_{J\in\mathcal J(T)}
\mathbf 1\{P_J(T)=Q(p_J)\}\,
\delta(p_J,J)\,
\beta(p_J,J,P_J(T),T)\le1
}
]
for every target T, where p_J is the unique parent source selected by Q when
P_J(T) lies in the image of Q.

A necessary design principle is that beta must exploit the *multiplicity of
lifts* and the geometry of the marked leaf pair. In particular, for a
type-3 mark across a bridge uv, the lift kernel must distribute charge across
the many possible leaf-pair marks in a way that reflects the leaf counts on
the two sides. A bound based only on the number of marks, maximum degree, or
the local two-lift lemma is insufficient.

No all-orders choice of Q and beta satisfying this display is proved here.
The n=8 and n=10 max-flow certificates remain finite results and do not
supply such a formula.
