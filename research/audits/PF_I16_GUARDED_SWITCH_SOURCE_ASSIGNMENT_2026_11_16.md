# PF-I16 guarded-switch source assignment audit — 2026-11-16

## Question

The uniform source weighting
\[
  \alpha_x(T)=\frac{1}{|C(x)|}\mathbf 1_{T\in C(x)}
\]
overloads some target columns at six and eight ports. This does **not** imply a Hall obstruction: it only says that the uniform distribution on each source's neighborhood is a poor choice.

We therefore test a stronger, exact finite certificate. Let the left vertices be all source objects
\[
  x=(M,\tau),\qquad \tau\in\mathcal T(H_M),
\]
and let the right vertices be port trees obtainable from x by the guarded local-switch procedure. An injective map \(\Phi\) from left vertices to right vertices is a unit-capacity transport:
\[
  \pi(x,T)=\mathbf 1_{T=\Phi(x)}.
\]
It saturates every source and puts at most one unit on each target.

## Exact finite result

The verifier enumerates the complete guarded neighborhood \(C(x)\) for every source, then runs Hopcroft–Karp on the resulting bipartite graph. It checks source saturation, not just a numerical LP objective.

| Ports n | Sources | Union of guarded output trees | Maximum matching | Result |
|---:|---:|---:|---:|---|
| 4 | 2 | 3 | 2 | saturated |
| 6 | 22 | 43 | 22 | saturated |
| 8 | 608 | 1493 | 608 | saturated |

The exact CI log reports all three source-saturating matchings. The run completed successfully:
- Workflow run: https://github.com/syncgravity/Singular-Boundary/actions/runs/43970642059
- Commit: `df34b03957405edc5a55367debdeb86a1773f38f`
- Job: `guarded-switch`
- Both the guarded-neighborhood enumeration and injective-assignment test passed.

## Consequence at the tested orders

Every edge in a guarded local replacement preserves or lowers each port-cut load, so every output satisfies
\[
  c_k(\Phi(M,\tau))\le m_k(M)\quad(1\le k<n).
\]
For \(0\le x_k\le1\), this implies
\[
  \prod_k x_k^{m_k(M)}
  \le
  \prod_k x_k^{c_k(\Phi(M,\tau))}.
\]
Injectivity means no target tree is used twice. Thus the guarded relation gives a termwise injection proof of the weighted inequality at n=4,6,8 (with the exact finite source families enumerated by the verifier).

## What this does not establish

1. It is not an all-orders injection theorem. The maximum matching is computed separately at each tested n; no canonical formula or inductive extension has yet been proved.
2. It is not a matching in the full coordinatewise relation unless one uses the inclusion of guarded outputs in that relation. It does, however, provide a valid matching in that larger relation at the tested orders.
3. It does not prove the all-orders weighted one-link inequality or the Yang–Mills mass gap.

## Reproduction

Run:

```bash
python research/verification/verify_pf_i16_guarded_switch_injective_assignment.py
```

The script imports the guarded transition enumerator in
`verify_pf_i16_local_switch_fractional_transport.py`, enumerates every source neighborhood, computes a maximum bipartite matching, and raises a failing exit status if any tested source is unmatched. If saturation fails, it prints an alternating-reachability Hall-deficit witness.

The previous uniform-column overloads remain valid and are not contradicted: a nonuniform, source-to-target assignment can succeed even when uniform neighborhood weights overload columns.
