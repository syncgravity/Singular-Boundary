# PF-I16: exact n=10 nonuniform split-demand flow certificate and support audit

Date: 2026-11-18 (workflow completed 2026-11-19 UTC)

## Result

**The corrected n=10 split-demand flow certificate was exported and successfully replayed.** This closes the instrumentation task, not the all-orders Hall theorem.

Workflow: [44432123349](https://github.com/syncgravity/Singular-Boundary/actions/runs/44432123349)
- Checked-out commit: `75141c303dfad6191c5a797c262b704a6049fe5a`.
- Job `certificate`: success.
- Flow construction, independent replay, and artifact upload all completed.
- Artifact: [pf-i16-n10-split-demand-flow-certificate](https://github.com/syncgravity/Singular-Boundary/actions/runs/44432123349/artifacts/14490510306)
- Artifact SHA-256: `d23af0dcf97433db01d209f220c0cafd6baef08109dea9f11ae78757e577d096`.

The first run [44426921009](https://github.com/syncgravity/Singular-Boundary/actions/runs/44426921009) remains a harness failure after flow construction due to the missing `Counter` import. The correction was made in `75141c3`; the successful rerun is the authoritative result.

## 1. Exact flow and replay

The builder reports:

| Quantity | n=10 result |
|---|---:|
| Sources | 31,744 |
| Fibers | 21,280 |
| Full eligible target universe | 95,864 |
| Exact total fiber demand | 31,744 |
| Scale | 12 |
| Scaled demand / max flow | 380,928 |
| Positive fiber-target arcs | 49,584 |
| Targets receiving positive flow | 32,414 |
| Maximum target load | 12 / 12 |

Important schema distinction: the certificate interns only targets receiving positive flow. Its `target_count=32,414` is therefore the used-target count, not the full 95,864-target universe.

The replay checker completed with:
```text
PASS: independent n=10 split-demand flow certificate replay
sources=31744 fibers=21280 targets=32414
positive_flow_arcs=49584
used_targets=32414
max_target_load=12 / capacity=12
total_scaled_flow=380928
```

The checker does not rerun max-flow. It reconstructs all sources and fibers, verifies every fiber exactly once, recomputes its exact rational demand and retained row, checks every positive assignment is eligible, checks fiber conservation, and checks target capacity and total flow.

**Independence boundary:** the checker is independent of the max-flow algorithm and serialized flow construction, but shares the repository's canonical source enumeration, candidate-output, inverse-switch, and compression primitives. It is not a second implementation of the mathematical relation.

## 2. What the allocation actually looks like

The exported Dinic allocation has the following support:

| Positive targets per fiber | Fibers |
|---:|---:|
| 1 | 3,296 |
| 2 | 9,649 |
| 3 | 6,477 |
| 4 | 1,737 |
| 5 | 115 |
| 6 | 6 |

Thus the 21,280 fibers use 49,584 positive arcs. Every one of the 32,414 interned targets receives positive flow. Of these, 31,040 are saturated at 12 units; 1,374 are partially loaded. Target ownership counts are: 17,432 with one fiber owner, 12,973 with two, 1,836 with three, 167 with four, and 6 with five. No target in this exported allocation is shared by more than five fibers.

There are 608 distinct eight-port parent sources, and the certificate has exactly 35 deleted-interval fibers for each parent source in this finite n=10 census. This is a useful regularity of the finite fiber index set, not yet an all-orders theorem about the relation.

Classifying each fiber by the first crowded odd cut of its child matching and whether its deleted interval crosses that cut gives:

| Source block | Noncrossing fibers | Crossing fibers | Total fibers | Positive arcs |
|---:|---:|---:|---:|---:|
| (X_3) | 11,280 | 8,512 | 19,792 | 47,178 |
| (X_5) | 888 | 440 | 1,328 | 2,194 |
| (X_7) | 72 | 48 | 120 | 170 |
| Terminal | 40 | 0 | 40 | 42 |
| **Total** | **12,280** | **9,000** | **21,280** | **49,584** |

This confirms that the successful global flow simultaneously handles crossing and noncrossing fibers; it does not isolate them as independent allocations.

## 3. Mathematical interpretation

The certificate is a concrete primal witness for the finite split-demand quotient Hall instance at n=10. Together with the already recorded n=6 and n=8 exact flows, it confirms finite split-demand Hall at those orders.

It does **not** reveal a canonical allocation rule by itself. The flow is one Dinic output, dependent on network vertex/edge ordering; support counts and saturation patterns are diagnostics, not invariants. In particular:
- the allocation is nonuniform;
- targets can be shared by multiple fibers;
- a fixed one-target-per-fiber selector is not what the certificate provides;
- the positive support is only a subset of the eligible target universe;
- no extrapolation from the n=10 support histogram is an all-orders proof.

The terminal-target-access diagnostic printed by the builder still fails at n=6, 8, and 10 (many complement sources have no retained (Q)-target). That is a separate proposed strengthening and has no bearing on the successful full split-demand flow.

## 4. Consequence for the all-orders proof program

The proof target remains the blockwise weighted dual
[
sum_{Finmathcal F_k}delta(F)z_F
le
sum_{Tin Y_k}max_{F:Tin N_k(F)}z_F
qquad(z_Fge0).
]

The exact demand identity remains the useful local input:
[
delta(p,J)=rac{a(p,J)}{d(p)}+rac{b(p,J)}{d(p)+1},
]
where (a) counts overlapping parent non-root leaves and (b) counts overlapping parent root/internal vertices. The noncrossing cut recursion and crossing-leaf localization remain valid. The failed reciprocal-degree condition and retained-grandparent rerouting shortcut remain rejected.

**Next proof obligation:** find a structural, order-uniform capacity allocation or weighted-dual argument that explains how capacity is exchanged among all eligible reverse-mark fibers, including crossing/noncrossing collisions. The finite Dinic allocation can guide discovery but cannot be copied as a proof. A promising direction is to study the reverse-mark exchange graph together with the parent canonical suffix data, rather than choose one fixed mark or merge sibling fibers through a grandparent.

## 5. Final status

- **Proved:** exact finite split-demand Hall at n=6, 8, and 10; n=10 exported allocation and replay; all-orders local cut recursion, target cut preservation, and crossing-leaf localization; exact source-side demand formula.
- **Disproved:** equal reciprocal reverse-degree splitting at n=8 and n=10; the proposed retained-grandparent sibling rerouting at the four-interval parent.
- **Open:** arbitrary-family blockwise mixed Hall; all-orders multivalued-(pi) Hall; unconditional weighted one-link inequality.
- **Not claimed:** an all-orders Hall proof or a Yang--Mills mass-gap result.
