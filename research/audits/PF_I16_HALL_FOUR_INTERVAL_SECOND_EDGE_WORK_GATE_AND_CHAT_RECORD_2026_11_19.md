# PF-I16 second-edge replacement work gate and conversation record

Date: 2026-11-19 (UTC workflow records)
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`
Pull request: #119 (open, draft; not merged)
Purpose: preserve the decision trail and establish a reproducible CI gate for the first-edge-anchored second-edge replacement search. This record includes the immediately preceding ChatGPT work-gate exchange so the research sequence and limitations are durable in the repository.

## 1. User-directed work order

The governing order is:

1. Prove PF-specific all-orders accepted-face support-diagram confluence.
2. Authenticate one physical regulator on a single source geometry.
3. Derive and verify the finite physical SU(2) Hamiltonian on that regulator.
4. Prove a uniform all-functions interacting-vacuum Poincare inequality (SI).
5. Address continuum/OS reconstruction only after the preceding gates.

The four-interval search is a diagnostic within gate 1. It is not permission to skip accepted-face confluence and proceed directly to the physical regulator. No PR merge is authorized by this work record.

## 2. Existing all-orders result and boundary

The repository record `PF_I16_ALL_ORDERS_CANONICAL_SIBLING_PORT_TREE_DIAMOND_2026_11_19.md` proves an all-finite-order diamond for canonical sibling source reductions at the labelled port-tree / guarded-reversal level. For sibling sources (p,q) over (r), with canonical deleted leaves (K=\ell(p)), (J=\ell(q)), and a common target in the two canonical fiber neighborhoods, the two guarded inverse orders agree and the common target belongs to the full parent neighborhood (C(r)).

This result does **not** prove canonical membership (C_{can}(r)), accepted-face support-diagram isomorphism, L6c naturality of support diagrams, L7b oriented boundary-word compatibility, or restriction coherence under further deletions. The canonical-parent strengthening is known to fail in finite census examples. Accordingly, the accepted-face all-orders confluence theorem remains open.

The general terminating-rewrite/Newman transfer theorem is conditional: source termination and local source diamonds are not enough. Every source critical-pair diamond must lift to a support-diagram isomorphism preserving all intersections (including empty higher intersections), relative-collapse certificates, oriented boundary cycles and ordered footprint words; those local isomorphisms must commute with every further restriction. Those PF-specific hypotheses remain to be established.

## 3. Prior bounded search and why it was not the next gate

The existing two-edge-anchored search kept the first two matched edges fixed and varied the third. It reported 8,007 eligible inventory edges, 62 third-edge choices passing its triangle support tests, and no common fourth edge for the graph-5 / graph-12 parent patterns. Its scope is restricted to that fixed first-two-edge family.

The prior response correctly identified the next diagnostic as varying the second matched edge while keeping the first anchored. It also identified a reproducibility issue: the small two-edge search artifact did not contain the complete `edge_support_options` table required by the replacement verifier. This was resolved by retrieving the full support-inventory artifact from workflow run `44576452636`.

## 4. Authenticated full support inventory

Downloaded artifact:
- Workflow run: `44576452636`
- Job: `135745124704`
- Artifact name: `pf-i16-four-interval-support-inventory`
- Artifact ID: `14555459234`
- Artifact SHA-256 (GitHub artifact ZIP): `3c89758d9473bdd09da50e2359f509b50255cfa74e71fae9cd18e2a091f3eb27`
- Unpacked file: `pf_i16_four_interval_support_inventory.json`
- Unpacked file size: 16,031,515 bytes
- Unpacked JSON SHA-256: `5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f`

Parsed inventory fields and frozen target:
- Schema: as recorded in the artifact.
- Target: 4,294 vertices, 8,382 edges, 4,089 accepted faces.
- Target face-key SHA-256: `f0f63287b3194a8625e4dd5c0a7369b04da315406fdc64a0d828627814ada7eb`.
- `edge_support_options`: 8,007 eligible matched edges.
- Total support options: 214,108.
- Eligible edges vertex-disjoint from the frozen triple: 8,004.
- Frozen first edge: `[-7,-4,5,7,0] -> [-6,-4,5,7,0]`.
- Frozen second edge in the original motif: `[-7,-3,5,7,-1] -> [-7,-3,6,7,-1]`.
- Frozen third edge in the original motif: `[-6,-3,5,6,-1] -> [-6,-3,5,6,0]`.

The full JSON was inspected after unpacking; it contains the support-option table missing from the smaller summary artifact. The file hash above is the hash of the unpacked JSON bytes, not the ZIP.

## 5. Replacement search verifier and exact scope

The branch contains:
- `research/scripts/verify_pf_i16_hall_four_interval_second_edge_frontier.py`
- `research/scripts/verify_pf_i16_hall_four_interval_second_edge_replacement_search.py`
- `research/scripts/verify_pf_i16_hall_four_interval_parent_compatibility.py`
- `research/scripts/export_pf_i16_hall_source_records.py`

The frontier stage enumerates every second matched edge in the frozen Ngrid=12 inventory that is vertex-disjoint from the first edge and has at least one support pair satisfying:
1. each support collapses to its own distinguished matched edge;
2. the pair intersection is nonempty and collapses to a vertex; and
3. the two footprints satisfy the two-sided open-complementary-arc test.

The replacement stage checks the frontier edge-set digest and independently recomputes every support-pair witness count. For every frontier second edge, it then ranges over compatible third edges and all eligible first-three support assignments satisfying:
1. individual matched-edge collapse;
2. nonempty pair intersections with vertex collapse;
3. two-sided open-arc footprints;
4. contractible first-three union; and
5. the two non-root relative deletion collapses for the star parent.

For each fixed second/third pair, graph-5 and graph-12 fourth-edge candidate sets are aggregated over all qualifying first-three support assignments. The fourth support is intentionally relaxed: the candidate needs the required exact incidence mask and two-sided footprints, but is not required to collapse to its matched edge or pass the full four-support L6c/L7b diagram. Thus an empty common candidate set is a necessary-condition obstruction only within the frozen target and support inventory; a surviving edge is only a candidate.

No Hall demands, loads, deficiencies, matching outcomes, or flows enter these target/support searches.

## 6. CI gate established by this record

The workflow already runs the frontier and replacement scripts in the PR-triggered `index-check` job and uploads their artifacts. The previous successful run `44576452636` predates the second-edge replacement stages and therefore is **not** evidence that these new stages passed.

This record is paired with a workflow-trigger update so that pushes to this research branch which change either second-edge verifier also trigger the full `index-check` job. The commit changing this workflow is intended to trigger a fresh run. The fresh runs, not the earlier run, are the pass/fail gate for the replacement search. As of the latest inspection, the push and PR runs are both in progress at the parent-compatibility stage; no second-edge outcome is yet available.

Expected artifacts from the fresh run:
- `pf-i16-four-interval-second-edge-frontier`
- `pf-i16-four-interval-second-edge-replacement-search`

The output must be archived with its workflow run ID, job ID, artifact IDs, artifact SHA-256 values, unpacked JSON hashes, target face-key hash, and headline counts. Do not transcribe a result until the run completes and the output is inspected.

## 7. Decision rules after the run

- **If no common fourth edge survives for any anchored second/third pair:** record a bounded necessary-condition obstruction for the frozen first edge, Ngrid=12 target, and supports of at most three rhombi. Do not call it a global no-go theorem.
- **If one or more common fourth edges survive:** preserve every witness and promote only those witnesses to full support-diagram verification. For each candidate, record all nonempty and empty pair/triple/four-way intersections, cell/collapse type, union, both relative deletion orders, every oriented boundary cycle, anchored edge, ordered footprint word, and an explicit diagram isomorphism between both reduction paths. Then test restriction coherence under further deletions.
- In either case, continue the all-orders proof independently of this finite diagnostic. A finite obstruction does not close L8; a finite survivor does not prove L8.

## 8. Conversation record: 2026-11-19 work-gate continuation

The user directed: “Please proceed to the work gate, ensuring that all records are established, including this chat, and well-curated as required to build the final proof.”

Immediately preceding assistant response (research conclusion):
- Restated the work order: accepted-face confluence first, then one authenticated physical regulator, then finite SU(2) Hamiltonian, then uniform all-functions SI.
- Confirmed PR #119 was open/draft and the existing two-edge-anchored search was bounded, not a global no-go.
- Identified the next step as varying the second matched edge while keeping the first fixed.
- Reported that the small search artifact lacked the complete support-option table and that the replacement search had not yet been run.

This continuation:
- Retrieved the complete support inventory artifact from run `44576452636` and verified its unpacked JSON structure, dimensions, target hash, support-option count, file size and SHA-256 (Section 4).
- Inspected the frontier and replacement verifier source. The replacement verifier rechecks the frontier's candidate edge digest and every first-two support-pair count before enumerating third-edge support assignments.
- Established the CI trigger path so the next branch push runs the second-edge replacement gate.
- No merge was performed. Fresh workflow runs are active: push run `44644620629` and pull-request run `44644613219`, both on head commit `e374ff4299f175bb5d946709a578b7fd9649c922`. In both runs, the full inventory enumeration has passed. The parent-compatibility verifier is still running; the second-edge frontier and replacement stages have not yet started. The final result remains pending until one run completes and its output artifacts are inspected.

## 9. Status ledger

| Obligation | Status |
|---|---|
| Source port-tree sibling diamond | Proved for canonical sibling fibers |
| Canonical parent membership at common parent | Open; finite counterexamples to general strengthening |
| PF accepted-face all-orders support confluence | Open |
| Full first-edge-anchored second-edge replacement search | CI gate established; fresh run pending |
| Full four-support L6c/L7b witness certificate | Not yet established |
| Single authenticated physical regulator | Open; do not advance ahead of gate 1 |
| Physical finite SU(2) Hamiltonian on that regulator | Open |
| Uniform all-functions interacting-vacuum SI | Open |
| Continuum/OS reconstruction and mass gap | Open |

## 10. Research-integrity constraints

Keep the target window and face inventory fixed for this search. A changed window or acceptance domain is a new candidate geometry and requires a new inventory hash. Preserve the complete raw artifacts and verifier outputs. Distinguish theorem, conditional theorem, finite census, bounded exhaustive search, and heuristic. Never promote a finite search result to an all-orders theorem. Do not merge PR #119 or any related PR without explicit user authorization.
