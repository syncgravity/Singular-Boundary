# PF-I16 — Bounded temporal-port budget for recursive multi-row link elimination

**Date:** 2026-11-14  
**Status:** Combinatorial port-budget lemma ESTABLISHED for the elementary four-dimensional plaquette incidence system. The multi-cut analytic contraction estimate remains OPEN.  
**Scope:** finite collections of elementary plaquettes in the 4D hypercubic lattice; recursive conditional-cumulant partitions of original row labels. No P0–P5 gate is promoted.

## 1. Incidence data

Let rows be elementary plaquettes. Each row has four boundary links, so
\[
|X_i|=4.
\tag{1.1}
\]
Each unoriented link belongs to six elementary plaquettes in four dimensions: for each of the three transverse coordinate directions, there are two plaquettes containing the link. Hence
\[
|I_e|:=|\{i:e\in X_i\}|\le6
\tag{1.2}
\]
for any selected finite row family (with equality in the full local lattice family away from finite-volume degeneracies).

For a current super-row represented by a nonempty block B of original row labels, define its e-port set
\[
P_e(B)=B\cap I_e.
\tag{1.3}
\]
The port labels are the original row-time labels, not merely the number of current super-rows incident to e.

## 2. Port conservation under the exact conditional-cumulant partition identity

At a selected link e, the law-of-total-cumulance identity partitions its current incident row labels into blocks. In original labels this is a partition
\[
\pi\in\Pi(I_e).
\]
For each block B, the conditional cumulant H_B removes the e-coordinate and creates one super-row whose remaining e'-ports are exactly the union of the original ports carried by B:
\[
P_{e'}(B)=B\cap I_{e'}.
\tag{2.1}
\]

Because the blocks of \pi are disjoint and cover I_e, and because every original row label belongs to exactly one current super-row along any fixed recursion branch, no original (e', row-time) port is duplicated or lost when super-rows are merged. In particular, for every other link e',
\[
\sum_{B\in\pi}|P_{e'}(B)|
=|I_e\cap I_{e'}|
\le |I_{e'}|\le6.
\tag{2.2}
\]
More generally, at every stage of a recursion branch, the total number of e'-ports across all current super-rows is at most six.

Thus a super-row may be a genuinely multi-time path-functional on e', but it never carries more than six original time ports on that link.

## 3. Global linear port budget

Let E_* be the set of links appearing in at least one original row. Since each row has four boundary links,
\[
|E_*|\le\sum_i|X_i|=4r.
\tag{3.1}
\]
The total number of original row-link ports is exactly
\[
\sum_{e\in E_*}|I_e|
=\sum_{i=1}^r|X_i|
=4r.
\tag{3.2}
\]
At any stage and along any fixed branch, recursive block merging preserves this total port count: it only regroups original labels. A link is eliminated at most once on that branch, because after conditioning on e, every H_B is a function only of the other link paths.

Consequently, if a valid multi-cut estimate incurs at most C^k loss for k temporal ports/cuts, its accumulated port-count loss along one branch is at most
\[
C^{4r}.
\tag{3.3}
\]
Likewise, the local conditional-cumulant partition count at each eliminated link is at most
\[
\mathrm{Bell}(6)=203,
\]
and the total number of partition branches is bounded by
\[
\prod_{e\in E_*}\mathrm{Bell}(|I_e|)
\le203^{4r}.
\tag{3.4}
\]
This is exponential in r, not superexponential.

## 4. What this does and does not solve

The result removes one combinatorial concern: the sixfold link incidence does not cause an unbounded number of time ports to accumulate on a super-row. The full recursion has only O(r) original row-link ports, and each individual link sees at most six of them.

It does **not** prove that the analytic multi-cut contraction can be bounded by C^k. In particular, (3.3) is useful only after proving a path-functional cumulant inequality whose loss is exponential in its port count and whose temporal bonds can be assigned to original row pairs sharing the link.

The exact two-state interlaced-time counterexample remains in force: a coefficient-one bound based only on the minimum cross-set time gap is false. The required analytic lemma must retain the full ordered cut profile.

## 5. Disposition

- Four ports per plaquette row: **ESTABLISHED**.
- At most six original row-time ports per lattice link: **ESTABLISHED**.
- Conservation of original ports under block-partition super-row merging: **ESTABLISHED**.
- Total recursion port budget at most 4r: **ESTABLISHED**.
- Bell(6) local partition overhead is exponential in total row order: **ESTABLISHED**.
- Exponential-in-port-count multi-cut covariance/cumulant estimate: **OPEN**.
- Support-restricted temporal tree after multi-cut regrouping: **OPEN**.
- Marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
