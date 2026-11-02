# The Singular Boundary

**Canonical research repository and evidence-preserving proof program.**

The Singular Boundary investigates quasicrystalline and Penrose geometry, finite-volume SU(2) lattice gauge systems, Wilson Hamiltonians, connected score expansions, and possible mathematical routes toward a nontrivial interacting continuum Yang–Mills theory with a positive mass gap.

> **Scientific status — 2026-11-01:** This is an active research program, **not a completed proof of the four-dimensional Yang–Mills existence and mass-gap problem**. Finite-volume identities, exact low-order calculations, conditional inequalities, and intrinsic Peter–Weyl estimates are recorded with their limitations. No λ=1 all-order interacting convergence theorem, regulator-uniform Penrose deleted-face current theorem, full physical temporal spectral theorem, or continuum Osterwalder–Schrader reconstruction and positive mass gap has been established.

## Read this before beginning or resuming research

| Question | Starting point |
| --- | --- |
| What is the latest defensible mathematical checkpoint? | [Current checkpoint](docs/research/CURRENT_CHECKPOINT.md) |
| What must actually be proved, without circular dependencies? | [P0–P5 proof dependencies](docs/research/PROOF_DEPENDENCIES.md) |
| Has a theorem already been calculated, corrected, or superseded? | [Theorem navigator](docs/research/THEOREM_INDEX.md) and [correction history](docs/research/DISCOVERY_TIMELINE.md) |
| How should an AI or researcher resume without duplicating work? | [Mandatory research handoff](docs/research/AI_RESEARCH_HANDOFF.md) |
| How strong is the evidence for a result? | [Evidence protocol](docs/research/EVIDENCE_PROTOCOL.md) |
| Where are primary sources, scripts, and missing originals? | [Source and code map](docs/research/SOURCE_AND_CODE_MAP.md) |
| Which claims are proved, conditional, numerical, or open? | [Append-only claim ledger](research/claims/CLAIM_LEDGER.csv) |
| What is missing from durable original-byte storage? | [Archival intake register](sources/source-manifests/ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv) and [backlog](sources/source-manifests/HISTORICAL_ARCHIVE_BACKLOG_2026-10-30.md) |

## The actual proof frontier

**P0 — Model identity and provenance.** Verify geometric incidence, original-link operator, Gauss sector, boundary conditions, physical temporal construction, regulator conventions, source bytes, and production data. The M55 spatial reconstruction is not interchangeable with the temporal Q14, twelve-prism, or continuum records.

**P1 — Operator algebra.** Respect the full November 1 shared-link sign/orientation correction sequence. The operator may appear as `D^-=R_A-L_B` or `D^+=R_A+L_B` under different orientations; never import a carré-du-champ sign without a coordinate and original-link convention check.

**P2 — Connected analytic convergence.** Exact two-, three-, and four-face polynomial calculations, all-length free-electric Peter–Weyl inverse bounds, and an intrinsic analytic bilinear estimate provide the latest recorded foundation. The **nonlinear connected recurrence still needs a noncircular all-order analytic-radius and interval-growth majorant**. Formal Gevrey growth, even improved estimates, is not ordinary convergence at physical coupling.

**P3 — Penrose interacting vacuum.** The deleted-face signed-current condition `sup_f T_(f,h) = o(h^(-1/4))` is a **sufficient condition within one proposed route**, not a theorem already established for the physical Wilson vacuum and not a necessary premise of every mass-gap proof. The essential issue is a regulator-uniform Wilson-specific current/anti-depletion or alternative completed-cage estimate.

**P4 — Physical spectrum.** Establish the required Gauss-invariant, source-visible, interacting temporal/infrared spectral estimates. Finite reference-operator gaps and gauge-charged response coercivity do not certify a continuum physical mass gap.

**P5 — Continuum theory.** Specify and prove the correct dimension, normalization, limit order, nontriviality, reflection positivity/OS reconstruction, and positive mass gap without circular assumptions.

The program should not be declared closer to completion solely because a new identity, countermodel, numerical checker, or conditional sufficient criterion was added.

## Operating rules for researchers and AI systems

1. Read the latest checkpoint, P0–P5 map, and correction/supersession chain before beginning mathematics.
2. Specify model, spatial/temporal dimension, topology, boundary conditions, gauge sector, link orientations, differential-generator normalization, and whether `S=log Ω` or `S=log Ω²`.
3. Distinguish **source located**, **source retrieved**, **statement inspected**, **derivation independently checked**, **code reproduced**, and **publication-ready**. A verification log alone is not independent mathematical certification.
4. Record every claim's exact assumptions, scope, source commit, proof, dependence chain, counterexamples, limitations, verifier, inputs, output hashes, and status.
5. Never overwrite immutable original evidence, silently fix old transcripts, substitute reconstructed files for original bytes, or upgrade a numerical/candidate result to a proof.
6. Keep separate research tracks separate until a genuine mathematical implication joins them. Explicitly mark any additional hypothesis that has not been proved.
7. For new work, prefer a theorem that closes a mapped dependency over another equivalent rewriting of an open condition.
8. Preserve original binaries in Git LFS or a verified archive, with original SHA-256 and fresh-clone readback. A Library reference is not evidence of Git byte preservation.
9. Use reviewed branches and pull requests; never force-push canonical history or blindly merge divergent experimental research.
10. Reconcile the ledger and checkpoint whenever the mathematical frontier changes.

## Research areas and original records

- [R3-PRISM](research/problems/R3-PRISM.md): original twelve-prism geometry and Wilson insertion.
- [R3-IR](research/problems/R3-IR.md): gauge-neutral Hamiltonian, completed-cage magnetic deletion, conditional vacuum current, infrared covariance.
- [R2](research/problems/R2.md): time normalization, continuum reconstruction, mass-gap obligations.
- [D1](research/problems/D1.md): source/production-action certification, Stage 7–26 experimental provenance.
- [Repository research navigator](docs/research/README.md): theorem index, chronology, evidence, handoff and dependency map.

## Archival integrity

The repository contains curated mathematical records, original-source references, numerical audit reports and historical correction chains. It is **not** a verified complete copy of every historical conversation or binary archive. Consult the [Git LFS intake runbook](docs/governance/LOCAL_GIT_LFS_INTAKE_RUNBOOK.md), [reconciliation tracker](docs/evidence/SOURCE_RECONCILIATION_GAPS_2026-10-30.csv), and [repository standard](docs/governance/REPOSITORY_OPERATING_STANDARD.md) before describing source preservation as complete.

The independent prepared 602-file tree, the original historical data families, and proof bundles require item-by-item reconciliation and verified upload/readback. Git ancestry and failed experiments must be preserved. Historical notes are evidence, not automatic mathematical endorsement.

## Research continuity

A new collaborator or AI should first state the **highest defensible checkpoint and exact remaining obligation**. It should cite immutable commits and original files, detect prior corrections, and avoid restarting superseded calculations. The goal is a coherent, reproducible, independently reviewable proof program, not an unbroken stream of claimed theorems.

