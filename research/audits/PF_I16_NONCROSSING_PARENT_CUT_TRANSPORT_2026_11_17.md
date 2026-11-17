# PF-I16: correction — cut compression across a deleted interval

Date: 2026-11-17

## Correction notice

The preceding draft of this audit claimed that every non-crossing leaf deletion sends the parent first-overcrowded odd cut to k-2 (for a left leaf) or k (for a right leaf). That claim was not justified: a parent cut can correspond to several child cuts when deleted endpoints lie between consecutive retained ports. In particular, an odd parent cut can straddle an even child cut, whose matching load is not controlled by the first-overcrowded-odd-cut hypothesis. **The claimed parent-block theorem is withdrawn.** Do not use it in any proof.

## Exact cut-compression identity

Let J=[a,b] be the deleted matching interval. For every child cut j between child ports j and j+1, define

\[
q(j)=j-\mathbf 1_{a\le j}-\mathbf 1_{b\le j}.
\tag{1}
\]

This is the parent cut obtained by deleting a,b and compressing labels. The map j↦q(j) is nondecreasing and can be constant across one or two consecutive child cuts. The child cut k maps to:

- q(k)=k when J lies strictly to the right of k (a>k);
- q(k)=k-1 when J crosses k (a<=k<b);
- q(k)=k-2 when J lies at or to the left of k (b<=k).

These identities are exact. They identify the image of the distinguished child cut, but they do **not** determine the first overcrowded odd cut of the parent matching.

## Exact parent-load formula

Let M' = M minus {J} be the remaining matching intervals, and let I_q={j:q(j)=q} be the (possibly multi-cut) fiber of a parent cut q. A remaining interval I crosses parent cut q exactly when it crosses every child cut in I_q. Consequently

\[
m_q(M')=\#\{I\in M': I\text{ crosses every }j\in I_q\}.
\tag{2}
\]

Since I_q is a consecutive window of at most three child cuts, this is equivalently the number of remaining matching intervals spanning the whole window. It is an intersection/bridge count, not generally the load at one selected child cut.

## Exact finite census

Verifier: `research/verification/verify_pf_i16_noncrossing_cut_window_census.py`

Successful workflow: https://github.com/syncgravity/Singular-Boundary/actions/runs/44196672160 (commit `003380b2ad1ce304bb733d7f008fd37ddbb8418b`).

The verifier checks the cut map, all parent-cut load identities, and parent first-overcrowded-cut distributions for every non-root leaf fiber at 6, 8, and 10 ports:

| Ports | Child cut k | Leaf class | Fibers | Parent first-overcrowded odd cut distribution |
|---:|---:|---|---:|---|
| 6 | 3 | crossing | 24 | none: 24 |
| 8 | 3 | crossing | 608 | none: 104; 3: 504 |
| 8 | 3 | right | 360 | 3: 360 |
| 8 | 5 | crossing | 48 | none: 48 |
| 8 | 5 | left | 18 | 3: 18 |
| 10 | 3 | crossing | 29,776 | none: 352; 3: 27,768; 5: 1,656 |
| 10 | 3 | right | 34,020 | 3: 34,020 |
| 10 | 5 | crossing | 1,216 | none: 208; 5: 1,008 |
| 10 | 5 | left | 564 | 3: 564 |
| 10 | 5 | right | 720 | 5: 720 |
| 10 | 7 | crossing | 96 | none: 96 |
| 10 | 7 | left | 72 | 5: 72 |

Here “none” means the parent matching has no odd cut of load at least three. The finite data show a useful pattern for non-crossing fibers in this range: left fibers have parent first crowded cut k-2, while right fibers have parent first crowded cut k. But this is only a finite pattern and does not repair the earlier proof gap; an all-orders argument must still control all parent odd cuts and the multi-cut windows.

Crossing fibers behave differently: their parent may have no crowded odd cut, may retain cut k, or (for child k=3) may have first crowded cut 5. Thus crossing fibers cannot be merged into the non-crossing source-block recursion using only q(k)=k-1.

## What follows safely

1. A left non-crossing leaf deletion sends the distinguished child cut k to parent cut k-2.
2. A right non-crossing leaf deletion sends it to parent cut k.
3. A crossing deletion sends it to parent cut k-1, which is even when k is odd.
4. No general parent-first-cut conclusion follows from these identities alone.
5. The crossing localization theorem remains valid: for k>=5, a is k-1 or k; for k=3, a is 1,2,or 3.

## Finite mixed-family evidence remains valid

The exact all-fiber multivalued-pi max-flow certificate is independent of the withdrawn parent-block claim. It includes all non-root leaf fibers and enforces both the parent-canonical target condition and the same-first-overcrowded-target-cut restriction:

| Ports | Fibers | Scaled demand | Max flow | Deficit |
|---:|---:|---:|---:|---:|
| 6 | 18 | 44 | 44 | 0 |
| 8 | 440 | 3,648 | 3,648 | 0 |
| 10 | 21,280 | 380,928 | 380,928 | 0 |

Workflow run 44177680653. These finite certificates remain valid.

## Revised structural target

The census suggests splitting the quotient analysis into:
- non-crossing fibers, where the finite parent first-cut pattern is k-2/k;
- crossing fibers, whose parent first-cut can vary and must be treated using the window I_{k-1} and its spanning-interval count.

The immediate all-orders target is a weighted expansion estimate for the union of these two families, not separate local Hall statements. Any proof must account for target collisions between fibers with different windows and must not infer parent-block membership from the distinguished-cut image alone.
