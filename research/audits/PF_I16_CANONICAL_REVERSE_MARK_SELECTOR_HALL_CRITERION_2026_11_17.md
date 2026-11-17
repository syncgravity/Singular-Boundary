# PF-I16: exact Hall criterion for a canonical reverse-mark selector

Date: 2026-11-17

## 1. Selector problem, stated without fractional ambiguity

Fix a parent-source matching Q, so distinct parent sources p have distinct
representatives Q(p) in their canonical parent target neighborhoods.

A row is r=(p,J), where J is a non-root leaf interval occurring in at least
one child source in the (p,J)-fiber. Let E_r be the set of distinct child
port trees obtained by taking Q(p) as parent target and inserting J last
through a guarded local switch. Let delta_r be the split demand
[
  delta_r = \sum_{x\in X(p,J)} 1/d(x).
]

A target T in E_r has reverse mark J and inverse parent target Q(p).
For a fixed T and fixed J, the inverse parent target is unique. Hence, if
T is assigned to two rows r=(p,J), r'=(p',J), then Q(p)=Q(p') and
injectivity of Q forces p=p'. Thus same-mark collisions are already
separated by Q. The only remaining conflict is assigning one T to two
different marks.

A canonical-mark selector is a function m(T) choosing one valid reverse
mark of each target T. For every row r=(p,J), we require at least delta_r
units of target capacity among targets with m(T)=J and T in E_r. Since
each selected target has capacity one and cannot be assigned to another
row, this means at least
[
  q_r=\lceil delta_r\rceil
]
distinct targets from E_r must be assigned to row r.

## 2. Exact selector-existence theorem

Form the bipartite graph with left vertices the rows r and right vertices
the child targets T. Join r to T exactly when T is in E_r. Give row r the
integer quota q_r=ceil(delta_r).

**Theorem.** A selector assignment exists that assigns each target to at
most one row, assigns every row at least q_r distinct targets, and labels
each assigned target by that row's mark J, if and only if
[
  |N(R)| \ge \sum_{r\in R}q_r
  \qquad\text{for every set R of rows.}                 (S)
]

**Proof.** Replace each row r by q_r identical left clones, each adjacent
to precisely E_r. A matching saturating all clones is exactly an assignment
of q_r distinct targets to every row, with no target assigned twice.
Hall's marriage theorem says that such a matching exists exactly when
every clone subset has at least as many neighbors as clones. For any
clone subset, let R be the set of rows represented. Its neighborhood is
N(R), and the number of clones in the subset is at most
sum_{r in R} q_r. Thus (S) implies Hall for every clone subset. Conversely,
taking all q_r clones of every row in R gives Hall's inequality (S).
After matching, label each matched target by the J of its matched row.
Because a target has only one matched row, this defines the required
selector on assigned targets. On unassigned targets choose any valid
reverse mark; the target-side classification guarantees at least one for
targets under consideration. Q-injectivity and uniqueness of P_J(T)
ensure that the assignment cannot give the same target to two rows with
the same J but different p. This proves the theorem. □

## 3. Why the previous fractional argument did not prove a selector

A fractional flow with row demand delta_r and target capacity one proves
only
[
  |N(R)|\ge\sum_{r\in R}delta_r.
]
It may split the capacity of one target between rows with different marks.
Such a split is a transport kernel, not a function m(T). It therefore does
not produce a canonical-mark selector. The integer clone construction
shows the exact additional rounding cost: each row consumes ceil(delta_r)
distinct targets.

In particular, the earlier proposed implication from a fractional
submeasure nu_r to a selector was invalid unless the supports of the
nu_r are pairwise disjoint across rows. That disjointness is precisely
what the selector assignment must establish.

## 4. The fiber demand must not be silently assumed at most one

For a fixed parent tree tau with s-1 vertices, let L be its number of
non-root leaves. If a child is formed by attaching the new leaf J to a
parent vertex I, then the child has d(x)=L when I is a non-root leaf of
tau, and d(x)=L+1 otherwise. Consequently, for a fixed (p,J)-fiber,
[
 delta(p,J)=a/L+b/(L+1),
]
where a is the number of child sources in that fiber attached at non-root
leaves of tau and b is the number attached elsewhere. The general bound
|X(p,J)|<=s-1 does not by itself imply delta(p,J)<=1. The value must be
computed from the actual allowed attachment vertices. The selector quota
is ceil(delta), not delta.

## 5. What remains to prove

The selector problem is now exactly reduced to the integer Hall expansion
(S) for the fixed-representative row graph. This is a clean sufficient
route to the mixed lift kernel, but it is not established by the known
split-demand max-flow results: those verify the weaker fractional demand
inequality using all canonical parent targets, not one fixed representative
Q(p) per parent source, and not the rounded quotas ceil(delta).

The local two-lift bound for a fixed inserted leaf and a fixed parent
target does not alone imply (S), because a row can have quota greater than
two and different rows can compete for the same child targets through
different reverse marks.

No all-orders proof of (S), and hence no all-orders canonical-mark selector,
is claimed in this audit. The next proof obligation is the mixed integer
Hall inequality (S), with the actual row quotas and the fixed parent
representatives made explicit.
