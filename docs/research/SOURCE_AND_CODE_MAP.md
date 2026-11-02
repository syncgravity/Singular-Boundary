# Source, code and numerical provenance map

At baseline commit, the repository tree contains **1923 tracked blobs**, of which **335** are theorem Markdown records. These counts are repository-tree metadata, not proof validation.

| Evidence class | Location | Required next link |
|---|---|---|
| Canonical claims | [append-only ledger](../../research/claims/CLAIM_LEDGER.csv) and [append-only entries](../../research/claims/append_only/) | claim ID, exact theorem, qualification, correction |
| Original theorem prose | [theorem index](THEOREM_INDEX.md) | stable file path and commit SHA |
| Independent audit and discrepancies | [research audits](../../research/audits/) | tested assertions, impacted theorem IDs |
| Executable checkers | [scripts directory](../../scripts/) | command, environment, expected output and verified checksum |
| Historical source archives | [historical sources](../../sources/historical/) | raw origin, size, SHA256, chain of custody |
| Source manifests and missing assets | [source manifests](../../sources/source-manifests/) | exact preservation state; missing ≠ negative result |
| Original simulation data | [data policy](../../data/README.md), [intake runbook](../../docs/governance/LOCAL_GIT_LFS_INTAKE_RUNBOOK.md) | fresh-clone LFS readback and hash |
| Verbatim conversations | [conversation directory](../../sources/conversations/) | original file + attachment mapping + quoted line spans |

## Artifact accessibility

Many theorem files point to companion **Library Proof Audits ZIP files**. A filename or claimed SHA is not evidence that its bytes exist in GitHub. Record an independently verified URI/checksum for every bundle and maintain an exact mapping to the theorem, verifier, data and output. Until this exists, state **external artifact referenced; repository byte coverage not audited**.

## Reproducibility record template

For each theorem and numerical result record: `claim_id`; `source_path@commit`; `artifact_sha256`; `script_path@commit`; `python/interpreter + dependencies`; `command`; `inputs_sha256`; `outputs_sha256`; `machine-independent assertions`; `last_replay_date`; `reviewer`; `status`. Preserve negative outcomes and unexpected changes. No regeneration can replace original random streams or archived Monte Carlo without a new run ID.

## Current local materials

The user has supplied Stage26 seed archives and Penrose/square sweep files alongside a dissertation archive and proof-review transcript in this conversation. They have **not** been automatically uploaded to GitHub by this navigation work. Their preservation remains subject to the source intake and fresh readback protocol.
