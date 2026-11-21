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

This record is paired with a workflow-trigger update so that pushes to this research branch which change either second-edge verifier also trigger the full `index-check` job. The commit changing this workflow is intended to trigger a fresh run. The fresh runs, not the earlier run, are the pass/fail gate for the replacement search. The push and PR-triggered runs completed successfully; their artifacts and exact outputs are recorded in Section 11. The two runs used different workflow head SHAs, so their unpacked replacement JSON was compared byte-for-byte before treating the result as reproducible.

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
| Full first-edge-anchored second-edge replacement search | Completed bounded search; 17 second-edge survivors and 52 second/third pairs; full four-support certification remains open |
| Full four-support L6c/L7b witness certificate | Not yet established |
| Single authenticated physical regulator | Open; do not advance ahead of gate 1 |
| Physical finite SU(2) Hamiltonian on that regulator | Open |
| Uniform all-functions interacting-vacuum SI | Open |
| Continuum/OS reconstruction and mass gap | Open |

## 10. Research-integrity constraints

Keep the target window and face inventory fixed for this search. A changed window or acceptance domain is a new candidate geometry and requires a new inventory hash. Preserve the complete raw artifacts and verifier outputs. Distinguish theorem, conditional theorem, finite census, bounded exhaustive search, and heuristic. Never promote a finite search result to an all-orders theorem. Do not merge PR #119 or any related PR without explicit user authorization.


## 11. Completed second-edge gate: artifact audit and result (2026-11-20 UTC)

### 11.1 Workflow identity and completion

Both GitHub Actions runs completed with conclusion `success`, and every step in the `index-check` job completed successfully, including the frontier, replacement search, theorem source inventory/hash checks, theorem catalog/navigation checks, the existing cumulant/temporal verifier suite, and Proof Atlas checks.

| Trigger | Run | Job | Workflow head SHA | Result |
|---|---:|---:|---|---|
| Push | [44644620629](https://github.com/syncgravity/Singular-Boundary/actions/runs/44644620629) | 135983929256 | `e374ff4299f175bb5d946709a578b7fd9649c922` | success |
| pull_request | [44644613219](https://github.com/syncgravity/Singular-Boundary/actions/runs/44644613219) | 135983905125 | `95d16de130e4ab5d9fe7ec224ead56d9f45cd3d8` | success |

The PR itself remains #119, open, draft, and unmerged. At the time of this audit, its branch head was `e8a8150ffe0dbbce40823e8296f4e5339b834d34`. The run head SHAs differ; therefore success is reported per run, not represented as though both jobs tested the identical commit.

### 11.2 Reproducibility comparison

The replacement artifacts from the two runs were downloaded and unpacked. Their JSON payloads are byte-identical:

- Push artifact ID `14590713975`; GitHub artifact digest `sha256:011047f8d37dde7d993140d866c724a3ab4a8f761a1cc4d92be0dbcdd17bb145`.
- PR artifact ID `14589689235`; GitHub artifact digest `sha256:7bd86af520c6002b25207a1985533bc76e5d6300006b0142084f68ebe21de6bf`.
- Both unpack to `pf_i16_four_interval_second_edge_replacement_search.json`, 6,413,571 bytes, SHA-256 `e4974b8ee430c7fe7e853153cae1b9d98337f1164000d073c31babbcf5425b2f`.
- The canonicalized common-witness list hash is `7c8473adcf810b8a44dfe9bef470bbad790357e95572431551fe61f422c0cca8`.

The different ZIP digests are expected to include archive-level metadata; the extracted JSON byte hashes and witness-list hash agree exactly.

Other push-run artifacts inspected:

| Artifact | ID | ZIP SHA-256 | Unpacked JSON SHA-256 |
|---|---:|---|---|
| second-edge frontier | 14588740367 | `35a913b9748a757faf006c0601fbf8b9d7a1bab4dc0d1ac6e187cecb99b3b003` | `ce5261042b7e7ee53869e5b8d736d12d4eb410c1711d008972653f4f4b8eea07` |
| parent compatibility | 14588635136 | `b829a41ce34f742ff390727ec18d070b51cd34fb71e143cf63812c17fbcc655c` | `092ee60c55066cc2b3c0cbb106c5085ef45242bced72a0c5c4503cf76d67449b` |
| prior two-edge-anchored search | 14587913902 | `4053000be4c6ac7097221e70ea9f481f7dc6b65362c684a7d558b89543860e50` | `8bafac58b7ea6a5d7b5b0b3a288fd312b72aaf264cfafb924af27fc3e69a9cd5` |

Frontier artifact facts:
- Fixed first matched edge: `[-7,-4,5,7,0] -> [-6,-4,5,7,0]`.
- Eligible second edges vertex-disjoint from it: 8,006.
- First-edge support options: 28; all 28 collapse to the distinguished matched edge.
- Second-edge frontier: 172 edges with at least one parent-compatible support pair.
- Total support-pair witnesses: 10,733.
- Frontier edge-set SHA-256: `aaf59b5226ec47883ed6a3cd0121f862ecead160c1e6c2aba86a8c50919b7bb2`.

### 11.3 Replacement-search result

The replacement verifier independently consumed the frontier digest and enumerated:
- 172 frontier second edges;
- 10,733 first-two support-pair witnesses;
- 446,394 qualifying first-three support assignments;
- 52 second/third matched-edge pairs with at least one common fourth-edge candidate;
- 17 distinct second matched edges with at least one such common fourth-edge candidate.

**Conclusion:** the earlier zero-common-fourth-edge result for the one fixed first-two-edge family does not extend to the complete first-edge-anchored second-edge frontier. The new search has genuine survivors. It is incorrect to state a no-go obstruction for all second-edge replacements with the first edge fixed.

The surviving candidates are not yet four-interval lifts. The verifier's explicit filter list says the fourth supports are relaxed supersets: it imposes neither fourth-edge collapse to the distinguished edge nor the complete four-support L6c/L7b test. Its nonclaims explicitly exclude all-first-edge choices, supports beyond the Ngrid=12 one-to-three-rhombus inventory, complete four-support certification, geometric L8, and the all-orders Hall inequality.

The parent-compatibility artifact independently reports:
- 13 four-interval overlap graphs;
- 8,004 candidate edges vertex-disjoint from the frozen triple;
- 249 locally relevant fourth edges after the support-incidence prefilter;
- no common fourth edge for all 13 graphs;
- graph-5 / graph-12 candidate-set intersection count zero for the *fixed frozen triple*.
This fixed-triple result is compatible with the replacement-search survivors because the latter vary the second and third matched edges; they do not contradict the narrower fixed-triple obstruction.

### 11.4 Representative exact surviving witness

One explicit survivor is:

- First edge (fixed): `[-7,-4,5,7,0] -> [-6,-4,5,7,0]`.
- Second edge: `[-8,-4,5,8,0] -> [-8,-4,5,9,0]`.
- Third edge: `[-8,-3,6,8,-1] -> [-8,-3,6,8,0]`.
- Common fourth-edge candidates:
  1. `[-8,-5,5,9,1] -> [-8,-5,6,9,1]`;
  2. `[-8,-5,5,9,1] -> [-7,-5,5,9,1]`;
  3. `[-7,-5,5,9,1] -> [-7,-4,5,9,1]`.

These are common candidates after aggregation over the qualifying first-three support assignments for that fixed second/third pair. They are not asserted to have any single compatible fourth support that passes the full four-support diagram checks.

### 11.5 Required next proof operation

The next gate is no longer another broad second-edge search. It is a **witness-lifting gate**:

1. Preserve all 52 surviving second/third pairs and all common fourth-edge candidates; do not select only the representative above.
2. Recover the actual qualifying first-three support assignments and support witnesses behind each aggregated candidate.
3. For each surviving quadruple, enumerate every support choice for the fourth matched edge that collapses to that edge and satisfies the same boundary/open-arc requirements.
4. Compute the complete four-support intersection diagram: all six pairwise intersections, all four triple intersections, the four-way intersection, including empty cases; record dimensions/collapse types and the union.
5. Check every deletion restriction and both relative-collapse orders, with the distinguished matched edges retained.
6. Compare the two parent/deletion paths as labelled incidence diagrams, including oriented boundary cycles, anchored edges, ordered footprint words, and explicit diagram isomorphisms.
7. Check restriction coherence under all further source deletions relevant to the critical-pair diamond.

A surviving common edge only opens this gate; it does not discharge it. If all survivors fail a necessary full L6c/L7b condition, record the precise obstruction and test whether it is invariant across all 52 pairs before considering any broader conclusion.

### 11.6 Status correction and research integrity

- The second-edge frontier and replacement workflow gates are **complete and successful**.
- The bounded search result is **positive**: 17 second-edge survivors / 52 second-third pairs.
- Full four-support L6c/L7b certification is **not yet established**.
- PF-specific accepted-face all-orders confluence / geometric L8 remains **open**.
- The single authenticated physical regulator, finite physical SU(2) Hamiltonian on it, uniform all-functions SI, and continuum/OS reconstruction remain **open and downstream**.
- No PR was merged. No Hall demands, flow outcomes, or Hall deficiencies were used in the target/support search.


## 12. Completed same-assignment witness-lifting gate and corrected interpretation (2026-11-20 UTC)

### 12.1 Workflow identity and reproducibility

The witness-lifting verifier and the complete existing theorem-index job both completed successfully in two duplicate workflow runs on the **same** branch head:

| Trigger | Run | Job | Head SHA | Result |
|---|---:|---:|---|---|
| Push | [44653134866](https://github.com/syncgravity/Singular-Boundary/actions/runs/44653134866) | 136012713719 | `f93b16e6254e6ebdb0a395e6c36602026af4697c` | success |
| pull_request | [44653144296](https://github.com/syncgravity/Singular-Boundary/actions/runs/44653144296) | 136012744880 | `f93b16e6254e6ebdb0a395e6c36602026af4697c` | success |

The witness-lifting step and artifact upload both passed in each job. The full job also completed the inventory, parent-compatibility, fixed-two-edge search, second-edge frontier, second-edge replacement, theorem-source/hash, theorem-catalog, cumulant/temporal verifier, and Proof Atlas checks.

Witness-lifting artifacts:

- Push artifact ID: `14595027397`; GitHub ZIP digest `sha256:eff10dcb53187e4d834787b6ab90088b6bed4681a019b8d8c676d1a97ca20211`.
- PR artifact ID: `14594331899`; GitHub ZIP digest `sha256:0b007665063ddaedddd74fb4d51de441eecbb430fd72abbba3ff6088e9a74297`.
- Both contain `pf_i16_four_interval_witness_lifting.json`, 38,922 bytes, byte-identical SHA-256 `061e5c09aade70b001a6164e50a03c8ff440eab21fbeadba635d99fc5d232c73`.
- The artifact records the replacement-search JSON input hash as `e4974b8ee430c7fe7e853153cae1b9d98337f1164000d073c31babbcf5425b2f`, matching the previously audited second-edge replacement payload.

### 12.2 Exact result

The verifier reopened all 52 second/third pairs that had survived the aggregated replacement search. It independently recomputed 7,396 qualifying first-three support assignments in total across those per-pair searches. For every pair, it then required one *identical exact first-three face-support assignment* to admit fourth supports for both the graph-5 and graph-12 attachment patterns. The fourth support on each side could differ, but each had to collapse to its own distinguished matched edge and satisfy the required pairwise intersection/nonintersection, point-collapse, and two-sided open-arc tests.

The output is:

- Aggregated surviving second/third pairs reopened: 52.
- Per-pair qualifying first-three support assignments recomputed (sum): 7,396.
- Pairs with a same-first-three-assignment survivor: **0**.
- Same-triple common-fourth-edge witness count: **0**.
- Full pairwise support-witness tuple count: **0**.

Every one of the 52 pairs had at least one aggregated common fourth-edge candidate before this stricter lifting test. The failure is therefore not a failure to reproduce the previous 52-pair frontier; it is the failure to find a common fourth-edge support on both graph patterns for one identical first-three support assignment.

### 12.3 Critical mathematical qualification: this is not an L6c no-go result

The zero result must be interpreted more narrowly than a failure of the adopted L6c condition.

The verifier imposes identity of the first-three *face-index support assignment* across the graph-5 and graph-12 source families. That is a stronger requirement than the adopted L6c equivalence. The finite alternative-triple L6c/L7b audit explicitly states that L6c forgets shared-cell identity and dimension while retaining the labelled incidence diagram; it records 32 vertex-to-edge footprint dimension changes that pass L6c and L7b. Thus literal equality of support face indices is not an invariant required by the established L6c convention.

Consequently, the new result proves only this bounded negative statement:

> For the fixed first matched edge, the frozen Ngrid=12 PF-I11 target inventory, supports of one to three rhombi, and the 52 aggregated second/third pairs, there is no common fourth-edge realization using the *same exact first-three face-support assignment* on both graph-5 and graph-12 attachment patterns, under the verifier's fourth-support collapse and pairwise-footprint filters.

It does **not** prove that no L6c-compatible four-interval support-diagram isomorphism exists. Different first-three support realizations on the two source families may still be equivalent after forgetting cell identity/dimension, and the verifier does not test that possibility. Nor does it rule out other first-edge choices, larger support families, or a different geometric realization.

### 12.4 What the artifact did not establish

Because no same-assignment witness survived, the code never entered the branch that exports a four-support family diagram. Accordingly, this artifact contains **no computed four-support intersection diagrams** and no four-support deletion-collapse certificates. It does not establish:

- the six pairwise, four triple, and one four-way intersection data for any accepted four-support witness;
- an explicit labelled incidence-diagram isomorphism between the two parent/deletion paths;
- the complete ordered multi-footprint L7b boundary-word comparison;
- restriction coherence under further source deletions; or
- PF-specific geometric L8.

The CI success means the verifier ran to completion and its assertions passed. It does not mean the mathematical witness-existence condition passed.

### 12.5 Corrected next proof operation

Do **not** respond to this zero result by weakening L6c, and do not report it as a four-interval L6c obstruction. Replace the literal same-face-index test with a diagram-level lifting test that respects the adopted equivalence:

1. For each of the 52 (second, third) pairs and each common fourth matched edge, enumerate graph-5 and graph-12 four-support realizations independently. The first-three supports may differ between the two families.
2. Require every individual support to collapse to its distinguished matched edge; impose the exact pairwise overlap graph, point-collapse, and anchored open-arc conditions.
3. Compute all 15 labelled intersections (six pairs, four triples, four-way, with empty cases retained), the union, and the relevant relative-collapse data for each family.
4. Compare the resulting labelled incidence diagrams under the precise L6c equivalence: preserve interval labels, intersection incidence and collapse structure, but do not require shared-cell identity or dimension where the adopted definition forgets them.
5. Compare the complete oriented boundary cycles and ordered multi-footprint words under L7b, anchored at each directed matched edge. This must preserve cyclic order and incidence among multiple footprints, not merely individual open-arc booleans.
6. Only after a diagram-level pair survives should its two deletion paths be checked against the actual source-parent records and tested for restriction coherence under further deletions.

This is the next finite diagnostic toward the local support-diamond hypothesis of the conditional all-orders confluence theorem. A positive finite result would still not prove all-orders naturality; a bounded zero result would still need a proof that the tested family exhausts the relevant local critical-pair class.

### 12.6 Status ledger update

- Same-assignment witness-lifting verifier: **completed reproducibly; zero survivors**.
- Same-face-index four-support ansatz for the fixed first-edge frontier: **bounded obstruction**.
- L6c-compatible four-support diagram-level lifting: **open; not tested by this verifier**.
- Full four-support L6c/L7b certification: **open**.
- Restriction coherence and PF-specific all-orders accepted-face confluence / geometric L8: **open**.
- Authenticated physical regulator, physical SU(2) Hamiltonian on it, uniform all-functions SI, continuum/OS reconstruction: **open and downstream**.
- PR #119 remains open, draft, and unmerged; PR #118 remains open and unmerged. No merge was performed.


## 13. Completed independent four-support diagram-lifting CI gate (2026-11-20 UTC)

### 13.1 Workflow completion and reproducibility

The independent four-support lifting verifier was run in the full theorem-index workflow on the same branch head in both trigger modes:

| Trigger | Run | Job | Head SHA | Result |
|---|---:|---:|---|---|
| Push | [44665402346](https://github.com/syncgravity/Singular-Boundary/actions/runs/44665402346) | 136053330304 | `210da5db8e7697e81678d3d852ecdea89fb2b2d7` | success |
| pull_request | [44665410702](https://github.com/syncgravity/Singular-Boundary/actions/runs/44665410702) | 136053356824 | `210da5db8e7697e81678d3d852ecdea89fb2b2d7` | success |

All 46 substantive steps completed successfully, including support inventory, parent-compatibility, two-edge-anchored search, second-edge frontier, replacement search, same-assignment witness lifting, independent diagram lifting, theorem source/hash inventory, theorem catalog/navigation, the cumulant/temporal verifier suite, and Proof Atlas checks.

Independent diagram-lifting artifacts:

- Push artifact ID `14600441119`; artifact ZIP SHA-256 `1cfe2efe01003fa331d3e5303e96e92e8bf7a230ea3c8ddd63fdcb6887a0d94e`.
- PR artifact ID `14600691430`; artifact ZIP SHA-256 `df1d7d917ad8513a8273ba80f56737acb0713ab8f15af27e12f750df2afbde60`.
- Both contain `pf_i16_four_interval_independent_diagram_lifting.json`, 15,489,814 bytes, byte-identical SHA-256 `cd51d14450ac4c80e78bc7112b7bb2a3168a43b3d7c753eed725dcdc08fa54c0`.
- Both consume the same replacement-search JSON hash `e4974b8ee430c7fe7e853153cae1b9d98337f1164000d073c31babbcf5425b2f`.
- The inventory target in the output is 4,294 vertices, 8,382 edges, and 4,089 faces, with face-key SHA-256 `f0f63287b3194a8625e4dd5c0a7369b04da315406fdc64a0d828627814ada7eb`.

The replacement-search artifacts from both runs also unpack to the same 6,413,571-byte JSON payload, SHA-256 `e4974b8ee430c7fe7e853153cae1b9d98337f1164000d073c31babbcf5425b2f`. Thus the duplicate workflow executions agree on both the upstream candidate set and the independent-lift output.

### 13.2 Exact independent-lift output

The verifier reopened all 52 aggregated second/third matched-edge pairs and recomputed 7,396 qualifying first-three support assignments (summed across the per-pair searches). It allowed graph-5 and graph-12 to use independent first-three face-support assignments, unlike the same-assignment verifier in Section 12.

The artifact reports:

- Aggregated second/third pairs reopened: 52.
- Qualifying first-three assignments recomputed: 7,396.
- Actual four-support realizations satisfying individual edge-collapse and required pairwise footprint conditions: graph-5 514; graph-12 810.
- Realizations retained after requiring all nonempty intersections to be point-contractible, the four-support union to be point-contractible, and deletion of interval 4 to collapse onto the retained triple: graph-5 514; graph-12 482.
- Second/third pairs with at least one common fourth matched edge admitting such independent realizations on both patterns: **50 of 52**.
- Total common pair/fourth-edge cases: **64**.

The 15 labelled intersection entries are emitted for every retained realization (four single supports, six pairs, four triples, and the four-way intersection), including empty cases, with face/edge/vertex counts, point-contractibility flags for nonempty intersections, and a cell digest. The artifact also emits union cell counts and contractibility, all four single-deletion relative-collapse booleans, and anchored boundary-footprint words with ordered footprint positions and footprint-meeting relations.

### 13.3 Important qualification: this is a candidate-lifting result, not a full L6c/L7b certificate

The artifact's own nonclaims are binding:

- Its parent restriction signature is a coarse finite L6c signature and has not been compared with every actual source-parent record.
- It does not establish an explicit source-prescribed diagram isomorphism.
- Its boundary words and footprint-meeting relations are exported, but are not yet certified against the source-prescribed multi-footprint words for all relevant order-eight sources.
- It does not establish restriction coherence under all further deletions, PF-specific all-orders accepted-face confluence, geometric L8, or the all-orders Hall theorem.

There is an additional deletion-collapse distinction that must be preserved. The verifier records all four single-deletion collapse results, but its candidate-retention predicate requires only the interval-4 deletion collapse, together with all nonempty intersections and the union being point-contractible. Among the retained candidates:

- Every graph-5 candidate has relative-deletion vector (drop supports 0,1,2,3): `(false,true,true,true)`.
- Every retained graph-12 candidate has vector `(true,true,true,true)`.

Therefore the graph-5 candidates do **not** pass all four possible single-deletion relative-collapse tests. Whether the failed drop-0 collapse is fatal depends on which deletion restriction(s) the actual source-parent diamond requires. This cannot be settled from the coarse artifact signature; it must be checked against the actual source records and their marked-parent maps. Do not describe all 514 graph-5 candidates as passing every deletion restriction.

The retained diagrams also have different nonempty-intersection counts: graph-5 has 9 of 15 entries nonempty, graph-12 has 11 of 15. Their boundary-footprint count patterns are respectively (3,2,2,1) and (2,3,3,2). These are not to be declared equivalent or inequivalent in isolation: the two attachment patterns must first be matched to their actual source-parent combinatorics and the adopted labelled L6c comparison. The common coarse retained-parent signature is not a substitute for that comparison.

### 13.4 Correct next operation

The next operation is now **source-record matching and restriction adjudication**, not a broader candidate search:

1. Export the actual order-eight source records and marked parent maps for every one of the 52 second/third pairs and the 64 common pair/fourth-edge cases.
2. Identify exactly which support deletions correspond to each source parent on graph-5 and graph-12. In particular, determine whether graph-5's failed drop-0 relative collapse is required by the critical-pair diamond or is an irrelevant deletion for that source family.
3. Compare each exported 15-entry labelled intersection diagram with its own source-prescribed overlap graph, retaining empty intersections and interval labels.
4. Compare the two retained-parent diagrams under the precise L6c convention; do not require literal cell identity/dimension, but do require the full labelled incidence/collapse structure prescribed by the source maps.
5. Compare the complete oriented boundary cycles and ordered multi-footprint words against the source-prescribed L7b data, including the meeting relations among footprints.
6. Test restriction coherence for the actual further-deletion maps in the source critical-pair family.

Only candidates passing the actual parent restrictions and source-prescribed L6c/L7b comparisons should be promoted. If the graph-5 drop-0 collapse is required, the present 514/482 retained counts are not a valid four-parent lift and the search must be refined with that requirement; if it is not required for this source diamond, document the exact parent map that explains why.

### 13.5 Updated status

- Independent four-support diagram-lifting verifier: **completed reproducibly in two full CI runs**.
- Same-assignment ansatz: **bounded zero result**, not an L6c no-go (Section 12).
- Independent graph-5 / graph-12 candidate lifts: **positive bounded result, 50/52 pairs and 64 common pair/edge cases**, subject to source-parent adjudication.
- Full all-deletion L6c parent naturality: **not established**; graph-5 drop-0 relative collapse fails for every retained candidate under the current indexing.
- Source-prescribed L6c diagram isomorphisms and L7b ordered multi-footprint matches: **open**.
- Restriction coherence and PF-specific geometric L8: **open**.
- Physical regulator, finite physical SU(2) Hamiltonian on it, uniform all-functions SI, and continuum/OS reconstruction: **open and downstream**.
- PR #119 remains open, draft, and unmerged; PR #118 remains open, draft, and unmerged. No merge was performed.


## 14. Source-parent mark audit correction (2026-11-20 UTC)

The first CI execution of `verify_pf_i16_four_interval_source_parent_mark_audit.py` failed at an assertion that incorrectly required every parent tree after deleting interval 3 to be the star `((0,1),(0,2))`. The failure was in the audit's expected-value assertion, not in source enumeration or the geometric verifier. Re-enumerating the canonical order-eight source records shows that the retained three-interval overlap graph is a triangle, and its spanning tree depends on the source record.

Correct parent-tree histograms after deleting interval 3:

| Source overlap family | Sources with mark 3 | Parent tree `((0,1),(0,2))` | Parent tree `((0,1),(1,2))` | Parent tree `((0,2),(1,2))` |
|---|---:|---:|---:|---:|
| Graph 5 | 12 | 4 | 4 | 4 |
| Graph 12 | 36 | 12 | 12 | 12 |

The other mark census remains:
- Graph 5: 12 sources; root index 0 in all; mark 3 eligible in all 12; among those, other eligible marks are (1,2) in 4, (1,) in 4, and (2,) in 4.
- Graph 12: 48 sources; root index 0 in all; mark 3 eligible in 36; among those, other eligible marks are empty in 12, (1,) in 12, and (2,) in 12.

Thus the following statements remain supported: interval 0 is always the root and never an eligible reverse mark; every actual co-deletion with interval 3 is interval 1 or 2; and deletion of interval 0 is not a source-parent operation. However, the stronger claim that deleting interval 3 always leaves the same *tree* is false. It leaves the same labelled three-vertex overlap graph, but one of three spanning trees occurs. The source parent tree must therefore be carried per source record, not collapsed to a single star signature.

The verifier was corrected in commit `7ff717093c9d4a49d25a87675c03b7c7a8d7f5a3` to assert the three exact histograms and to expose whether the parent tree is unique. The corrected verifier passed in the complete theorem-index workflow run [44707308083](https://github.com/syncgravity/Singular-Boundary/actions/runs/44707308083), job `136189996539`, on branch head `61443f3a7d962fea32c7478353db33134954ae75`. The earlier failures in runs [44675033035](https://github.com/syncgravity/Singular-Boundary/actions/runs/44675033035) and [44675038856](https://github.com/syncgravity/Singular-Boundary/actions/runs/44675038856) are now classified as an incorrect expected parent-tree histogram in the audit script. No geometric L6c/L7b conclusion follows from those failures.

This correction strengthens the next source-labelled comparison: enumerate source records with their exact marked parent trees, and compare each geometric parent diagram against the corresponding source-record restriction. Do not assume a common star parent tree across graph-5 or graph-12 families.


## 15. Source-labelled four-support restriction audit completed (2026-11-20 UTC)

The source-record matching and restriction adjudication requested in Sections 13.4 and 14 has now been carried out at the exact finite combinatorial scope supported by the source exporter and geometric artifact.

### 15.1 Reproducible execution

- Full workflow: [44707308083](https://github.com/syncgravity/Singular-Boundary/actions/runs/44707308083), job `136189996539`, conclusion **success**.
- Tested head: `61443f3a7d962fea32c7478353db33134954ae75`.
- New verifier: `research/scripts/verify_pf_i16_source_labelled_four_support_restriction_audit.py`.
- Durable audit: `research/audits/PF_I16_SOURCE_LABELLED_FOUR_SUPPORT_RESTRICTION_AUDIT_2026_11_20.md`.
- Source-labelled audit artifact ID `14621730510`; decompressed JSON SHA-256 `bb0ca92bbd5cef3cd6c2e26585e02c8f07acadc0c4836fe5937643a07a915958`.
- Input independent-diagram artifact ID `14620896650`; JSON SHA-256 `cd51d14450ac4c80e78bc7112b7bb2a3168a43b3d7c753eed725dcdc08fa54c0`.
- Source-parent artifact ID `14621091054`; JSON SHA-256 `3a2086899b7967c3239e36babb8209adb8a51c7cb0a2409f4980d5c6ecdccc2f`.

### 15.2 What is now positively established

The audit enumerates both root-preserving graph isomorphisms, `(0,1,2,3)` and `(0,2,1,3)`, for all 996 retained geometric witnesses and every relevant order-eight source record with mark 3. This produces 47,040 explicit witness/source/isomorphism rows.

| Family | Sources | Sources with mark 3 | Retained witnesses | Compatibility rows |
|---|---:|---:|---:|---:|
| Graph 5 | 12 | 12 | 514 | 12,336 |
| Graph 12 | 48 | 36 | 482 | 34,704 |
| **Total** | **60** | **48** | **996** | **47,040** |

For each row the verifier carries exact source intervals, source tree, eligible marks, parent tree after each legal deletion, mapped geometric supports, and all source critical deletion pairs. It checks all 15 labelled intersection entries per geometric witness, every source-legal relative deletion, every parent-tree edge against its mapped pair intersection, and the ordered reciprocal footprint data.

The source critical-pair census is 20 graph-5 diamonds and 24 graph-12 diamonds, total 44. For all 44:
- both source deletion orders leave the same reindexed parent tree;
- both corresponding relative-collapse checks pass;
- the remaining pair intersection is nonempty and point-contractible; and
- the 15-entry incidence table restricts to the same remaining pair in either order.

**The graph-5 drop-0 issue is resolved at source-mark level:** support 0 corresponds to the root under both root-preserving graph isomorphisms, and interval 0 is never an eligible reverse mark. The failed drop-0 collapse in the 514 graph-5 witnesses is therefore not a required source-parent deletion. All source-eligible deletions 1, 2, and 3 pass. Graph 12 passes all four geometric single-deletion tests.

The three distinct source parent trees after deleting interval 3 are all carried per source record. Every edge in each such parent tree maps to a nonempty, point-contractible pair intersection with reciprocal footprint entries of matching cell type and vertices.

### 15.3 What this does not establish

The 47,040 rows are exhaustive combinatorial compatibility checks under the two root-preserving graph maps. They are **not** an authenticated source-record-to-target-edge embedding: the source exporter still does not prescribe which geometric matched-edge vector realizes each source interval or reverse mark.

Likewise:
- source records do not prescribe the oriented boundary cycle or ordered multi-footprint word required for a full source-to-target L7b comparison;
- the target words are internally checked for order, reciprocal pair footprints, and meet relations, but are not compared with a source-prescribed word;
- relative-collapse booleans are not elementary collapse sequences or maps, so the audit does not prove collapse-map commutation around the diamonds;
- higher triple and four-way intersections have no source-side prescribed comparison object; and
- the finite result does not establish geometric L8, all-orders Hall, or the physical/regulator theorem.

Accordingly, Sections 13.3–13.4 should be read with this update: the actual source mark sets, source parent trees, eligible deletion checks, and abstract source-tree/table diamonds have now been audited. The remaining operation is to derive the authenticated source-to-target incidence embedding from the PF-I16 Z^5 geometry, then export complete oriented boundary cycles and elementary collapse certificates and rerun the diamonds with explicit comparison maps.

### 15.4 Current gate status

- Independent four-support diagrams: **passed**.
- Actual order-eight source mark and parent-tree census: **passed**.
- Source-labelled compatibility over both graph automorphisms: **passed, finite scope**.
- All source-eligible relative deletions: **passed**.
- All 44 abstract source parent-tree diamonds and remaining-pair table restrictions: **passed**.
- Source-to-geometric matched-edge embedding: **open**.
- Source-prescribed oriented L7b comparison: **open**.
- Elementary collapse-map commutation / full geometric restriction coherence: **open**.
- Geometric L8: **open**.
- All-orders Hall: **separate and open**.
- PR #119: remains draft, open, and unmerged; no merge was performed.


## 16. Complete source-labelled restriction and collapse-certificate addendum · 20 November 2026

The source-parent mark correction is now confirmed by successful workflow 44707308083. The actual delete-interval-3 parent-tree histogram is three spanning trees, not one star; the corrected source audit retains each source-specific tree.

The order-eight graph-5/graph-12 candidate lane has been extended beyond the original graph-isomorphism check:

- **58,608** explicit port-to-\(\mathbb Z^5\) embeddings across 996 retained witnesses, 60 relevant source records, and both root-preserving graph maps. L1 injectivity, L2 positive unit-edge realization, L3 accepted support endpoints, and exact L4–L5 overlap-graph preservation pass in local replay.
- **98,192** exact parent port-map restriction/compression checks pass. The child port map restricted to retained ports equals the reconstructed parent port map.
- Complete oriented boundary cycles and anchored open complementary arcs are now exported and checked together with ordered multi-footprint words.
- Parent-origin coherence: 514/514 graph-5 witnesses and 240/482 graph-12 witnesses pass the coarse labelled pair/triple incidence and ordered footprint-neighbor/meet-word comparison. This leaves 50/64 common pair/fourth-edge cases with a coherent witness in both families.
- Deterministic elementary relative-collapse certificates now export the actual free face-edge and edge-vertex pairs. All 3,984 single-deletion certificates match the prior booleans. All 5,012 two-path critical-pair collapse tests succeed to the same grandparent union.
- In 3,224 two-path tests the paths use the same free-pair set and differ only by swaps of disjoint elementary pairs. In 1,788 tests they use different free-pair sets; both paths still succeed, so these cases remain unresolved rather than no-go results.
- Intersecting parent-diagram coherence and strict same-pair-set collapse coherence leaves **18/64** common cases. All 18 use the same fourth edge
  \[
  (-7,-2,6,6,-2)\to(-7,-2,6,6,-1),
  \]
  across 18 distinct second/third-edge pairs. The second/third edges come from a nine-edge local set.

These counts were initially local replays. The corrected comprehensive CI replay subsequently passed in workflow 44833369833, and the collapse artifact was downloaded and inspected; see section 17 for artifact provenance and the exact finite disposition.

### Exact limits

- The 60 source records are only the graph-5 and graph-12 families among the 608 order-eight records; the other overlap-graph families are not covered.
- The two root-preserving graph maps both pass. The source overlap graph does not choose a unique map.
- The 18-case fourth-edge pattern is a finite candidate anchor, not a source-independent rule or theorem.
- The same-assignment first-three-support witness-lifting search still has zero survivors; graph-5 and graph-12 support realizations are independent even when they share the matched-edge quadruple.
- The 1,788 different-pair-set collapse tests have not been shown impossible to reconcile by alternate certificates.
- The parent boundary comparison is a coarse labelled ordered-word alignment with cycle hashes, not yet a vertex-level cycle isomorphism or a commuting family of elementary collapse maps.
- Arbitrary connected-support L7b, geometric L8, and the all-orders Hall inequality remain open.

PR #119 remains a draft research lane. No PR has been merged and no L8 or physical proof gate is promoted by this addendum.


## 17. Full CI completion and artifact reconciliation (2026-11-21 UTC)

The corrected comprehensive workflow completed successfully on PR #119 head `1b66ca65ca15ad9622b610f622e3559997188ce8`:

- [Workflow 44833369833](https://github.com/syncgravity/Singular-Boundary/actions/runs/44833369833), job `index-check` (`136623622049`): **success**.
- PR #119 remains draft, open, and unmerged.
- The preceding run's only failure was a witness-counter accounting defect: the collapse verifier counted the same witness once per root-preserving graph isomorphism. The corrected code verifies both maps give the same verdict, then counts the witness once. The elementary collapse computations themselves were not changed.

The collapse artifact (`14680929981`, ZIP SHA-256 `a717a6ef2e1006225f31ef64b5a22033e2305b8bfe8fec53e3e3c2a885f6adbf`) was downloaded and inspected. Its embedded input payload hashes match the independent diagram artifact (`14681735833`, JSON SHA-256 `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba`) and parent-coherence artifact (`14682100468`, JSON SHA-256 `a1b4817a329a55a848e490f34c492176586069110382920bbe26a7495bccd27b`).

CI-verified collapse results:

- 3,984/3,984 single-deletion certificates agree with the independent-diagram booleans.
- 5,012 two-path critical-pair tests succeed; both orders reach the same grandparent support union.
- 3,224 tests have identical elementary free-pair sets and differ only by swaps of disjoint pairs.
- 1,788 tests use different deterministic free-pair sets. Both paths succeed to the same target, but equivalence of the collapse maps is not established.
- Witness-level all-critical-pair same-pair-set counts: graph 5 = 312; graph 12 = 102.
- Strict collapse-pair-set coherence in both families: 28/64 common cases.
- Parent-diagram coherence in both families: 50/64 common cases.
- Joint survivors: 18/64, across 18 distinct second/third matched-edge pairs, all sharing the fourth edge `(-7,-2,6,6,-2) -> (-7,-2,6,6,-1)`.

The source-labelled restriction artifact reports 58,608 finite embeddings and 98,192 commuting parent port-map restrictions. The parent-coherence artifact confirms graph 5 = 514/514, graph 12 = 240/482, and 50/64 common cases with at least one coherent witness in each family.

This is a finite Ngrid=12, graph-5/graph-12 order-eight result. It is not an all-source or all-orders theorem. The artifact explicitly leaves geometric L8 open. Vertex/cell-level orientation-preserving boundary-cycle comparison maps, natural equivalence for the 1,788 different-pair-set cases, arbitrary connected-support L7b, geometric L8, and the all-orders Hall inequality remain open.
