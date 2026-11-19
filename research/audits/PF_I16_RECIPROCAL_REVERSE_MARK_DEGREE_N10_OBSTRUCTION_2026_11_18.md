# PF-I16: reciprocal reverse-mark degree diagnostic — exact ten-port obstruction

Date: 2026-11-18

## Result

The continued exact reciprocal reverse-mark degree diagnostic completed successfully at both n=8 and n=10. At n=10, the sufficient condition (RD) fails in every first-overcrowded-cut block. This rejects equal reciprocal splitting as a fiberwise allocation beyond the eight-port counterexample. It does **not** refute blockwise mixed Hall, split-demand Hall, or the all-orders multivalued-π Hall theorem.

Workflow:
- [44392154434](https://github.com/syncgravity/Singular-Boundary/actions/runs/44392154434), successful.
- Diagnostic: `research/verification/verify_pf_i16_reciprocal_reverse_mark_degree.py`.
- Artifact: [pf-i16-reciprocal-reverse-mark-degree](https://github.com/syncgravity/Singular-Boundary/actions/runs/44392154434/artifacts/14468993881).

The run checked out commit `1f1da7d7d2e660573e3d794a4537544d17344dbc` on `research/pf-i16-direct-mixed-hall-2026-11-18`. The job log and uploaded artifact agree. All reported demand and reciprocal-degree calculations use exact rational arithmetic.

## Exact n=10 census

The computation enumerated all 31,744 sources:
- (X_3): 30,528 sources;
- (X_5): 1,128 sources;
- (X_7): 72 sources;
- terminal class: 16 sources.

For each block, the target reverse degree counts every eligible fiber in that same block, including crossing and noncrossing deleted intervals. The census is:

| Cut | Fibers | Targets | Fiber-target incidences | Negative RD fibers |
|---:|---:|---:|---:|---:|
| 3 | 19,792 | 90,751 | 6,243,410 | 4,896 |
| 5 | 1,328 | 4,068 | 181,674 | 228 |
| 7 | 120 | 306 | 8,343 | 15 |
| **Total** | **21,240** | **95,125** | **6,433,427** | **5,139** |

The exact minimum slacks are:
[
min_{F\in X_3}(q(F)-\delta(F))
=-\frac{2228458211181273977}{911269137711009000},
]
[
min_{F\in X_5}(q(F)-\delta(F))
=-\frac{771499531}{412650360},
\qquad
min_{F\in X_7}(q(F)-\delta(F))
=-\frac{604}{495}.
]

The first negative (X_3) fiber has:
[
J=(2,10),\qquad |F|=4,qquad |N_3(F)|=16,
]
[
\delta(F)=\frac52,qquad
q(F)=\frac{49714633096248523}{911269137711009000},
]
and hence
[
q(F)-\delta(F)
=-\frac{2228458211181273977}{911269137711009000}.
]
Its target reverse degrees range from 176 to 500. Its parent source is
[
p=\left(
((1,4),(2,8),(3,6),(5,7)),
((0,2),(1,3),(2,3))
\right).
]

The aggregate reciprocal-capacity surpluses remain positive:
[
\sum_{F\in X_3}(q(F)-\delta(F))=60223,
\]
[
\sum_{F\in X_5}(q(F)-\delta(F))=2940,
\qquad
\sum_{F\in X_7}(q(F)-\delta(F))=234.
]
These equal target count minus total split demand in each block:
(90751-30528=60223),
(4068-1128=2940), and
(306-72=234).

Thus the defect is not aggregate capacity shortage. Equal splitting of each target among all eligible reverse-mark fibers leaves thousands of individual fibers below demand, despite large total slack.

## n=8 control, retained

The same completed run reproduced the exact n=8 census:
- 424 fibers, 1,458 targets, 18,147 incidences;
- 98 negative fibers (90 in cut 3 and 8 in cut 5);
- minimum slacks (-169259/95760) and (-451/420);
- aggregate surpluses 792 and 66.

The previously recorded exact n=8 witness and interpretation remain unchanged; see `PF_I16_RECIPROCAL_REVERSE_MARK_DEGREE_N8_OBSTRUCTION_2026_11_18.md`.

## Interpretation and proof boundary

The reciprocal-degree lemma remains a correct sufficient implication:
if every fiber satisfies
[
\delta(F)\le\sum_{T\in N_k(F)}\frac1{r_k(T)},
]
then the weighted mixed-Hall dual follows by averaging the incident fiber weights at each target. What fails is the premise, at n=8 and n=10.

The negative fibers do **not** furnish a Hall-deficient family. In particular, they do not show
[
\left|\bigcup_{F\in S}N_k(F)\right|
<\sum_{F\in S}\delta(F)
]
for any (S). They do not invalidate the exact split-demand max-flow certificates at n=6,8,10, and do not refute nonuniform capacity allocations.

The next mathematical route must abandon equal reciprocal splitting and address the full weighted dual
[
\sum_F\delta(F)z_F
\le
\sum_T\max_{F:T\in N_k(F)}z_F
\qquad(z_F\ge0),
]
or construct a nonuniform feasible target-to-fiber allocation with target capacity one. A useful structural approach must explain how to direct capacity toward high-demand/low-reciprocal-share fibers while controlling collisions among crossing and noncrossing fibers. No such all-orders allocation or dual bound is established here.

**Proved:** the reciprocal-degree condition implies mixed Hall.

**Disproved:** that condition at n=8 and n=10.

**Still open:** arbitrary-family blockwise mixed Hall, all-orders multivalued-π Hall, and the unconditional weighted one-link inequality. No Yang–Mills mass-gap conclusion follows.
