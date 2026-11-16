# Star-only nonuniform transport: Hall obstruction at six ports (2026-11-16)

## Question

The uniform star-only transport failed at n=6. Could source-dependent weights repair it? For each left source x=(M,tau), let C_star(x) be its distinct star-only candidate trees. We ask whether there are nonnegative weights

\[
\pi(x,T)\geq0,\qquad
\sum_{T\in C_\star(x)}\pi(x,T)=1,\qquad
\sum_x\pi(x,T)\leq1.
\]

All candidates preserve the source cut-load exactly, so this restricted problem splits into exact-profile classes.

## Exact finite result

The verifier `research/verification/verify_pf_i16_star_only_nonuniform_transport.py` exhaustively enumerates the sources and candidate relation at n=4 and n=6. It uses Hopcroft--Karp in each profile class. This is an exact feasibility test: the associated source-to-target flow network has integral capacities, so a fractional unit transport exists if and only if a matching saturates every source.

| ports | profile | sources | distinct star-only targets | maximum matching | result |
|---:|---|---:|---:|---:|---|
| 4 | (1,2,1) | 2 | 2 | 2 | feasible |
| 6 | (1,2,1,2,1) | 4 | 4 | 4 | feasible |
| 6 | (1,2,3,2,1) | 18 | 17 | 17 | impossible |

For the n=6 profile (1,2,3,2,1), the alternating-reachability Hall witness is the entire class: 18 sources have only 17 distinct star-only candidate trees. The deficiency is exactly one. Thus **no nonuniform choice of weights on the star-only relation can repair the obstruction**.

The six matching configurations in this profile are the six perfect matchings whose three intervals pairwise overlap. Each overlap graph is K3, contributing three spanning trees, hence 18 left objects.

## Important correction: exact-profile Hall is too strong

For h=(1,2,3,2,1), the number of right trees with cut-load *exactly* h is 17, while the left multiplicity is 18. Therefore the pointwise claim L(h)<=Q_exact(h) is false already at n=6 and must not be used as the target theorem.

The actual Hall neighborhood for a source of load h consists of all right trees with c(T)<=h coordinatewise, not only trees with c(T)=h. For this same h there are 59 complete-graph port trees with cut-load coordinatewise at most h. The full down-set supply is therefore much larger than the 17 exact-profile star-only candidates. The appropriate exact finite bookkeeping uses least primitive-Dyck majorants / ceiling classes, or the full down-set Hall inequalities; it does not require equality of cut-load profiles.

## Consequence

The failure is only for the restricted candidate relation. In particular, the increasing-path local replacement can lower cut-load and is not captured by the star-only relation. The viable local-switch target must retain profile-lowering moves (at least the increasing path) or enlarge the relation in another way.

The three-move relation (two middle-centred stars plus the increasing path) already repairs this n=6 obstruction: a direct profile-class matching test gives 9 candidate targets for 4 sources at profile (1,2,1,2,1), and 40 candidate targets for 18 sources at profile (1,2,3,2,1), with maximum matchings saturating all sources in both classes. Its uniform transport also has the prior successful finite test through n=8 (maximum column load approximately 0.976423 there). Thus the increasing-path move is not merely an optional enlargement; it removes the first exact Hall obstruction. The star-only restriction is now ruled out even with arbitrary fractional weights. The next meaningful target is an all-orders column-capacity bound for the three-move relation, or a more structured nonuniform transport using its lower-load outputs. Neither is established here.

The weighted one-link inequality and Yang--Mills mass gap remain open.
