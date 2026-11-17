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

Let \(M'=M\setminus\{J\}\) be the remaining matching intervals, and let \(I_q=\{j:q(j)=q\}\) be the (possibly multi-cut) fiber of a parent cut q. A remaining interval I crosses parent cut q exactly when it crosses every child cut in I_q. Consequently

\[
m_q(M')=\#\{I\in M': I\text{ crosses every }j\in I_q\}.
\tag{2}
\]

This is the correct cut-level relation. It is an intersection count across the child-cut window, not generally the load at one selected child cut.

## What follows safely

1. A left non-crossing leaf deletion sends the distinguished child cut k to parent cut k-2.
2. A right non-crossing leaf deletion sends it to parent cut k.
3. A crossing deletion sends it to parent cut k-1, which is even when k is odd.
4. No conclusion about the parent's *first* overcrowded odd cut follows from these facts alone.

For crossing leaves, the separate localization result remains valid: for k>=5, a is k-1 or k; for k=3, a is 1,2,or 3. This localization was proved by comparing a preceding odd child cut with the internal parent cut after deletion. It is not affected by the correction here.

## Finite mixed-family evidence remains valid

The exact all-fiber multivalued-pi max-flow certificate is independent of the withdrawn parent-block claim. It includes all non-root leaf fibers and enforces both the parent-canonical target condition and the same-first-overcrowded-target-cut restriction:

| Ports | Fibers | Scaled demand | Max flow | Deficit |
|---:|---:|---:|---:|---:|
| 6 | 18 | 44 | 44 | 0 |
| 8 | 440 | 3,648 | 3,648 | 0 |
| 10 | 21,280 | 380,928 | 380,928 | 0 |

Workflow run 44177680653. These finite certificates remain valid.

## Revised next target

Use (1)–(2) to stratify non-crossing fibers by the *cut window* I_q, not by an assumed parent first-crowded-cut label. The next useful exact diagnostic is to record, for each parent fiber (p,J), the window I_q around the distinguished cut and the parent matching load at nearby odd q. This will determine whether any stronger parent-block statement is true under the additional leaf/overlap-tree constraints. Until that census or a proof is supplied, no recursive source-block classification for non-crossing fibers is claimed.
