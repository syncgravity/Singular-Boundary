# Star-only nonuniform transport: Hall obstruction at six ports (2026-11-16)

## Question

The uniform star-only transport failed at n=6. Could source-dependent weights repair it? For each left source x=(M,tau), let C_star(x) be its distinct star-only candidate trees. We ask whether there are nonnegative weights

\[
\pi(x,T)\geq0,\qquad
\sum_{T\in C_\star(x)}\pi(x,T)=1,\qquad
\sum_x\pi(x,T)\leq1.
\]

All candidates preserve the source cut-load exactly, so the problem splits into exact-profile classes.

## Exact finite result

The verifier `research/verification/verify_pf_i16_star_only_nonuniform_transport.py` exhaustively enumerates the sources and candidate relation at n=4 and n=6. It uses Hopcroft--Karp in each profile class. This is an exact feasibility test: the associated source-to-target flow network has integral capacities, so a fractional unit transport exists if and only if a matching saturates every source.

| ports | profile | sources | distinct star-only targets | maximum matching | result |
|---:|---|---:|---:|---:|---|
| 4 | (1,2,1) | 2 | 2 | 2 | feasible |
| 6 | (1,2,1,2,1) | 4 | 4 | 4 | feasible |
| 6 | (1,2,3,2,1) | 18 | 17 | 17 | impossible |

For the n=6 profile (1,2,3,2,1), the alternating-reachability Hall witness is the entire class: 18 sources have only 17 distinct star-only candidate trees. The deficiency is exactly one. Thus **no nonuniform choice of weights on the star-only relation can repair the obstruction**.

The six matching configurations in this profile are the six perfect matchings whose three intervals pairwise overlap. Each overlap graph is K3, contributing three spanning trees, hence 18 left objects.

## Important boundary: this is not a counterexample to the target inequality

The failure is only for the restricted candidate relation. For this same profile, there are 59 complete-graph port trees with cut-load coordinatewise at most (1,2,3,2,1), so the full down-set neighborhood is much larger than the 17 exact-profile star-only candidates. In particular, the increasing-path local replacement can lower cut-load and is not captured by the star-only relation.

Therefore the viable local-switch target must retain profile-lowering moves (at least the increasing path) or enlarge the relation in another way. The earlier three-move transport (two middle-centred stars plus the increasing path) has a successful uniform finite test through n=8; the star-only restriction is now ruled out even with arbitrary fractional weights.

## Consequence

Do not pursue an all-orders theorem for star-only fractional transport. The next meaningful target is an all-orders column-capacity bound for the three-move relation, or a more structured nonuniform transport using its lower-load outputs. Neither is established here. The weighted one-link inequality and Yang--Mills mass gap remain open.
