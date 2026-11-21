# PF-I16 — Increasing-parent-map shortcut obstruction for the weighted interval one-link bound

**Date:** 2026-11-16  
**Status:** exact obstruction to a tempting reduction; no closure of the weighted one-link inequality is claimed.

## Target

For a perfect matching $M$ of the ordered ports $[2s]$, let $H_M$ be its interval-overlap graph and let
$$
m_k(M)=\#\{[a,b]\in M:a\le k<b\}.
$$
The left multiplicity at a load $h$ is
$$
L(h)=\sum_{M:H_M\text{ connected},\ m(M)=h}\tau(H_M).
$$
The weighted one-link target is a cut-load-dominated assignment of these $\tau(H_M)$ copies to distinct labeled port trees, or equivalently the associated capacitated Hall inequalities.

## Why the temporal increasing-parent construction does not transfer verbatim

For an interval graph whose vertices are ordered by increasing right endpoint, later neighbors of each vertex form a clique. If $d_j$ is the number of later neighbors of vertex $j$, then choosing one later neighbor for every nonlast vertex gives
$$
\prod_{j=1}^{s-1}d_j
$$
increasing rooted parent maps. Every such map is an increasing rooted spanning tree.

This is not the number $\tau(H_M)$ of all spanning trees. In particular, for the complete graph $K_3$, the increasing-parent count is $2\cdot1=2$, whereas $\tau(K_3)=3$. Thus the exact increasing-parent representation used for the temporal Ursell coefficient cannot simply be substituted for the matching-side spanning-tree multiplicity.

## An all-orders family showing the size of the missing factor

For every $s\ge2$, take
$$
M_s=\{[i,s+i+1]:1\le i\le s\}
$$
on ports $[2s]$. These are disjoint-endpoint nested-shift intervals, and every pair has overlapping interiors. Hence $H_{M_s}=K_s$.

In increasing-right-endpoint order, $d_j=s-j$, so the number of increasing parent maps is
$$
\prod_{j=1}^{s-1}(s-j)=(s-1)!.
$$
But Cayley's formula gives
$$
\tau(H_{M_s})=\tau(K_s)=s^{s-2}.
$$
The ratio is therefore exactly
$$
\frac{\tau(H_{M_s})}{\#\{\text{increasing parent maps}\}}
=\frac{s^{s-2}}{(s-1)!}
\sim\frac{e^s}{\sqrt{2\pi}\,s^{3/2}}.
$$

So any proof that first replaces all spanning trees of $H_M$ by increasing parent maps must separately recover an exponential-in-$s$ multiplicity factor; it cannot claim a one-to-one representation. This does not obstruct a bound with a sufficiently large exponential constant, but it does invalidate a constant-one transfer.

## Consequence for the next construction

The matching-side source must retain arbitrary spanning-tree structure, or use a controlled many-to-one encoding of it. The all-orders local-switch witness remains valid for every $(M,\tau)$, but its unresolved issue is precisely the aggregate fiber/column-mass bound. The next useful target is therefore a decorated encoding or fractional transport that handles all $\tau(H_M)$ copies, not merely the increasing-parent subset.

No all-orders Hall inequality, weighted one-link inequality, or Yang–Mills mass-gap proof is claimed here.
