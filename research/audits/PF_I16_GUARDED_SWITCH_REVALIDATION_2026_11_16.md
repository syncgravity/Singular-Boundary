# Guarded local-switch inverse and finite revalidation (2026-11-16)

## 1. Guarded transition

Let T be a tree on the current port set V, let e={u,w} be a current
edge, and let J={a,b} be a new matching interval overlapping e. Write
the four distinct endpoints in increasing order as x1<x2<x3<x4. The
guarded forward move chooses one of the three local trees

- S0 = {x1x2, x2x3, x2x4},
- S1 = {x1x2, x2x3, x3x4},
- S2 = {x1x3, x2x3, x3x4},

and forms U=(T-e) union S_j, subject to e notin S_j.

Because e and J overlap, their endpoints alternate. Thus e is either
{x1,x3} or {x2,x4}. If e={x1,x3}, S2 is forbidden and S0,S1 are
valid. If e={x2,x4}, S0 is forbidden and S1,S2 are valid. Exactly
two of the three local patterns survive for every chosen overlapping
edge.

The no-reinsertion guard is part of the transition relation. Without it,
the move may put the old edge straight back; such a move is excluded even
though the resulting graph can still be a tree. The guard is important
below because it makes every edge of the inserted local tree incident to
at least one new endpoint.

## 2. Exact inverse

For a tree U on V union {a,b}, define
delta_U(J)={f in E(U): f meets J}. Given the chosen e and S_j, the inverse
edge set is

    E(T) = (E(U) minus delta_U(J)) union {e}.

The guarded inverse checks are:

1. e is not in S_j (the defining forward guard);
2. S_j is a subset of E(U);
3. delta_U(J)=delta_{S_j}(J);
4. e is not in E(U) (a redundant consistency check: it follows from
   U being a tree, S_j subset U, and e notin S_j).

The complete local tree condition matters: checking only the edges incident
to a,b would fail to verify the full prescribed local configuration.
The incidence equality says there are no extra edges at either new endpoint.
Under these conditions, deleting a,b and restoring e recovers the exact
predecessor. In the guarded cases S_j minus J consists of the two old
endpoints with no edge between them. Since a,b have no external incident
edges, deleting them from U leaves exactly two components; e reconnects
those components.

For a genuine forward history, these checks hold when moves are reversed
in reverse chronological order. The endpoints a,b are new at their
insertion; all later insertions have first been undone; and the replaced
edge was not reinserted by the guard.

## 3. At least two distinct outputs per source

Root the overlap spanning tree tau at the matching interval containing
port 1 and fix any parent-before-child order of its s-1 non-root
intervals.

When inserting child interval J, the maintained tree path joining the
endpoints of its parent interval contains an edge overlapping J. Indeed,
if the parent and child interleave as p<a<q<b, the p-to-q path crosses
the cut at a; if a<p<b<q, it crosses the cut at b. The crossing edge
overlaps J. For that edge, exactly two local patterns pass the guard.
Therefore every current state has at least two valid next transitions.

For this fixed insertion order, different histories have different final
labeled trees. To reverse the last step, its child J is known. Since the
guard excludes the old-old edge, all three edges of S_j meet J, so
delta_U(J)=S_j. Its support outside J identifies the two old endpoints,
hence identifies e. Thus the last predecessor is unique. Repeating this
argument backward along the fixed order recovers the entire history.
Consequently the at-least-two branching at each of s-1 steps yields at
least 2^(s-1) distinct final trees for every source (M,tau).

This proves a sourcewise distinct-output floor of 2^(s-1). It replaces
the former 3^(s-1) floor, which is invalid after the no-reinsertion guard.

## 4. Corrected exact finite enumeration

The forward enumerator was rerun independently with exact rational
column accumulation and the no-reinsertion guard. Every transition state
was checked to have at least twice as many successor states as current
states; every output was checked to be a tree and to satisfy c(T)<=m(M);
and every source was checked against the 2^(s-1) distinct-output floor.

| Ports n | Sources (M,tau) | Distinct target trees | Source degree range | Degree floor | Maximum weighted column |
|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 3 | 2–3 | 2 | 5/6 = 0.8333333333 |
| 6 | 22 | 43 | 4–24 | 4 | 19033/13464 = 1.4136215092 |
| 8 | 608 | 1493 | 8–297 | 8 | 882579599341774396916901475041277863425921 / 354366397581230860789644812360005986409200 = 2.4905849013 |

Worst target trees and exact source-degree profiles:

- n=4: two tied worst targets, T={(1,2),(2,3),(2,4)} and
  T={(1,2),(2,3),(3,4)}; each has profile {(2,1),(3,1)}.
- n=6: T={(1,2),(2,3),(3,4),(4,5),(4,6)}; profile
  {(4,1),(6,3),(9,2),(10,1),(11,1),(12,1),(15,1),(17,1),(24,1)}.
- n=8: T={(1,2),(2,3),(3,4),(3,8),(4,5),(5,6),(5,7)}; profile
  {(8,1),(12,3),(18,2),(20,4),(24,5),(28,1),(29,1),(30,5),
  (31,1),(33,1),(34,2),(35,1),(36,7),(37,1),(38,1),(39,1),
  (41,2),(44,1),(47,1),(48,2),(49,2),(51,2),(52,3),(53,1),
  (55,1),(57,2),(60,2),(61,3),(63,2),(66,1),(67,2),(68,1),
  (69,2),(71,2),(72,2),(73,1),(75,1),(76,1),(77,1),(80,1),
  (81,1),(86,1),(87,1),(88,1),(89,3),(90,1),(92,1),(93,1),
  (95,1),(99,1),(101,1),(102,1),(103,1),(104,1),(106,1),
  (113,2),(118,2),(121,1),(124,1),(132,1),(135,1),(142,1),
  (159,1),(187,1)}.

Each profile is a histogram (degree, number of incident sources), and
its exact sum of count/degree reconstructs the corresponding maximum
column. The maximum source-incidence counts at the worst targets are
2, 12, and 104 for n=4,6,8 respectively.

## 5. Consequence and proof boundary

The corrected degree floor is valid, but the uniform source-to-distinct-
outputs transport is not a fractional Hall certificate: its weighted
column already exceeds one at n=6, and is larger at n=8. The exact
overloads above are counterexamples to this particular transport
construction, not counterexamples to the full down-set Hall inequality.
The inverse lemma and branching estimate are now established for the
guarded relation. A different sourcewise weighting or a different
coupling is needed to prove the weighted one-link inequality.

No all-orders weighted-column bound or Yang--Mills mass-gap proof is
claimed.


## 6. Reverse-replay checks

The inverse checker was independently replayed on every generated forward
history for n=4 and n=6. It verified the exact incidence set, the
no-reinsertion guard, absence of the replaced edge at the inverse stage,
the restored edge count, acyclicity, connectivity, and final recovery of
the root interval.

| Ports | Sources | Total forward histories replayed backward | Maximum histories for one source-target pair |
|---:|---:|---:|---:|
| 4 | 2 | 5 | 1 |
| 6 | 22 | 278 | 2 |

This validates the inverse implementation at these finite orders. The
n=8 forward distinct-output and weighted-column enumeration was run, but
the ancestry-history replay was not run at n=8.
