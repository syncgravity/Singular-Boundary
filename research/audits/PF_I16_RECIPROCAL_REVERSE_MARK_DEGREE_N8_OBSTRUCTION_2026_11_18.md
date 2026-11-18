# PF-I16: reciprocal reverse-mark degree diagnostic — exact eight-port obstruction

Date: 2026-11-18

## Result

The reciprocal reverse-mark degree sufficient condition (RD) is **false at eight ports**. This rejects equal reciprocal splitting as a universal fiberwise allocation. It does not refute the mixed Hall inequality or the multivalued-π Hall theorem.

Workflow:
- First attempt (stopped after recording n=8): https://github.com/syncgravity/Singular-Boundary/actions/runs/44392067165
- Continued n=8/n=10 run: https://github.com/syncgravity/Singular-Boundary/actions/runs/44392154434
- Diagnostic: `research/verification/verify_pf_i16_reciprocal_reverse_mark_degree.py`

The first attempt's n=8 calculation completed exactly before the harness stopped on the expected negative result. The harness was then corrected to continue rather than assert that RD must pass. The n=10 continuation is pending at the time of this record.

## Exact n=8 census

The computation enumerated all 608 sources and split the complement into first-overcrowded-cut blocks:
- (X_3): 564 sources;
- (X_5): 36 sources;
- terminal class: 8 sources.

The complete blockwise fiber/target incidence census is:
| Cut | Fibers | Targets | Fiber-target incidences | Negative RD fibers |
|---:|---:|---:|---:|---:|
| 3 | 382 | 1,356 | 17,100 | 90 |
| 5 | 42 | 102 | 1,047 | 8 |
| Total | 424 | 1,458 | 18,147 | 98 |

For every target (T), the reciprocal degree (r_k(T)) counts **all** eligible fibers in its cut block, including both crossing and noncrossing deleted intervals. Each fiber row is restricted to the actual retained relation: same first target cut and canonical parent target after the exact guarded inverse.

All calculations use exact rational arithmetic. The fiber demand is the split source demand
[
delta(F)=sum_{xin F}1/d(x).
]
The diagnostic computes
[
q(F)=sum_{Tin N_k(F)}1/r_k(T).
]

Exact block minima:
[
min_{Fin X_3}(q(F)-delta(F))
=-169259/95760,
]
[
min_{Fin X_5}(q(F)-delta(F))
=-451/420.
]
There are 90 negative fibers in (X_3), 8 in (X_5), 98 total.

The first negative (X_3) fiber is:
[
J=(2,8),quad |F|=3,quad |N_3(F)|=8,
]
[
q(F)=22261/95760,qquad delta(F)=2,
qquad q(F)-delta(F)=-169259/95760.
]
Its parent source is
[
p=left(
((1,3),(2,5),(4,6)),
((0,1),(1,2))
ight).
]
The reverse degrees among its eight targets range from 28 to 48.

The first negative (X_5) fiber has
[
q(F)-delta(F)=-451/420.
]

Interestingly, the *aggregate* reciprocal capacity has large surplus:
[
sum_{Fin X_3}(q(F)-delta(F))=792,
qquad
sum_{Fin X_5}(q(F)-delta(F))=66.
]
This is exactly target count minus total block demand (1,356−564 and 102−36). Thus the obstruction is local concentration: some fibers receive too little under equal splitting even though the block has substantial total slack.

## Interpretation

The equal reciprocal allocation
[
lambda_{F,T}=1/r_k(T)
]
cannot be trimmed to meet every fiber demand, because the displayed fibers have (q(F)<delta(F)).

This is a failure of the proposed sufficient criterion (RD), not a Hall obstruction:
- it does not produce a fiber family (S) with (|cup_{Fin S}N_k(F)|<sum_{Fin S}delta(F));
- it does not refute a nonuniform feasible allocation;
- it does not refute the exact split-demand max-flow certificates already obtained at n=8;
- it does not refute BQH(_k) or all-orders Hall.

The positive aggregate slack suggests that a nonuniform target-to-fiber allocation may still exist. But it must direct more capacity to low-reciprocal-degree fibers while preserving target column capacity one. Equivalently, it must use the full weighted dual, not the uniform average lower bound.

## Next step

The n=10 run should be allowed to finish to determine whether the same local obstruction pattern persists and to collect its exact deficit census. The mathematical route should then move beyond reciprocal equal splitting: use a nonuniform allocation or a direct weighted-dual/maximum-flow structure that exploits the large aggregate slack without violating individual target capacities.

## Proof boundary

**Proved:** the reciprocal-degree condition implies mixed Hall.

**Disproved:** the reciprocal-degree condition itself, already at n=8.

**Finite evidence retained:** split-demand Hall flows at n=6,8,10 remain separate and are not affected by this failure.

**Open:** arbitrary-family BQH(_k), all-orders multivalued-π Hall, and the unconditional weighted one-link inequality.
