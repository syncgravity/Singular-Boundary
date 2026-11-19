# PF-I16: exporting the nonuniform n=10 split-demand flow

Date: 2026-11-18

## Motivation

The exact split-demand quotient flow already succeeds at n=6,8,10, but the earlier verifier reported only the max-flow value. The successful n=10 flow is a concrete nonuniform target-capacity allocation. Extracting it is the next useful step after the failure of equal reciprocal reverse-degree splitting: it allows the actual capacity routing to be inspected for a structural rule.

## Changes made

On branch `research/pf-i16-direct-mixed-hall-2026-11-18`:

1. `research/verification/verify_pf_i16_split_demand_fiber_hall_flow.py` now records the positive flow on each fiber-to-target arc after a successful n=10 max flow and writes `n10_split_demand_flow_certificate.json`.
2. The certificate interns target trees once and stores, for each fiber, its parent source, deleted interval, a representative child source, exact rational demand, and positive target allocations in scaled integer units.
3. `research/verification/verify_pf_i16_split_demand_flow_certificate.py` is a separate checker. It does not run max flow. It reconstructs all 31,744 sources and 21,280 fibers, recomputes the retained parent-canonical row for each fiber, and checks:
   - every fiber occurs exactly once;
   - every exact rational fiber demand is reconstructed;
   - every positive-flow target belongs to the fiber's retained multivalued-π row;
   - allocated units equal the fiber's scaled demand;
   - no target receives more than the scale-12 capacity;
   - total flow equals total split demand.
4. `.github/workflows/pf-i16-export-split-demand-flow.yml` is a manual-dispatch workflow that runs the flow builder, runs the replay checker, and uploads the JSON certificate for 90 days.

## Important implementation boundary

The first targeted run [44426921009](https://github.com/syncgravity/Singular-Boundary/actions/runs/44426921009) failed after completing the exact n=10 max flow and writing an 8,204,258-byte certificate. The log shows 31,744 sources, 21,280 fibers, 95,864 targets, scaled demand and max flow both 380,928, 49,584 positive fiber-target arcs, 32,414 used targets, and maximum target load 12. The failure was a harness `NameError: Counter is not defined` in the pre-existing terminal-target-access diagnostic, invoked after the flow computations; it was not a max-flow or certificate-export failure. Because the builder exited nonzero, the replay and upload steps were skipped, so the certificate has not yet been independently replayed or preserved as a workflow artifact. The missing `Counter` import was fixed in commit `75141c303dfad6191c5a797c262b704a6049fe5a`. The targeted rerun [44432123349](https://github.com/syncgravity/Singular-Boundary/actions/runs/44432123349) is now in progress. No replay pass is claimed yet. The existing finite split-demand flow results remain the previously verified results from workflow [44177680653](https://github.com/syncgravity/Singular-Boundary/actions/runs/44177680653); this new work only adds export and independent replay instrumentation.

The replay checker independently validates the exported allocation against the reconstructed finite relation, but it shares the repository's canonical source enumeration, switch inversion, compression, and candidate-output primitives. It is independent of the max-flow implementation and serialized flow construction, not an independently implemented mathematical definition of the relation.

## Intended mathematical use

Once the manual workflow passes, inspect:
- the distribution of positive flow arcs per fiber;
- which fibers receive zero, partial, or full target capacity;
- whether target capacities are typically saturated;
- how crossing and noncrossing fibers share targets;
- whether the support can be organized by parent source, deleted interval, cut block, or leaf count.

The objective is to discover a structural nonuniform allocation rule or augmenting/exchange invariant. A single finite flow certificate will not prove an all-orders allocation theorem.

## Proof boundary

This instrumentation does not alter the Hall relation, the split-demand theorem, or the weighted dual. All-orders mixed Hall remains open, as does the unconditional weighted one-link inequality. No Yang--Mills mass-gap conclusion is claimed.
