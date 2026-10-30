# Historical archive coverage and October 28 onward gap ledger

**Compiled:** 2026-10-30. **Status:** open archival reconciliation, not completeness certification.

## Verified sources presently available in the conversation

- `Archive.zip`: SHA-256 `a5cf86c062a069fde3ae529f26502a17bf84ea7b28a149ad369fbd5b188d4f71` (263 primary files, including 19 nested ZIPs).
- `Archive 2.zip`: SHA-256 `de111958540678aa8b5de95af85921a4e69c9e1ab908cf42107ecfaa3ff4b4ad` (35 primary files, including 10 nested ZIPs).
- Across both archives: **298 primary entries and 351 nested entries** (counts include ZIP archive entries and duplicates of equivalent contents, excluding AppleDouble); full SHA-256 inventory is in the locally generated `OCT26_28_SOURCE_MANIFEST_2026-10-30.json`.
- Source-only text handoff has **579 files**, SHA-256 `eb5e4ab2ff1f2d041e4514a36f4c18265d6688afaab1cd3ed23ccde31f26ab07`; it has **not** been pushed to this repository. Eight separate standalone historical notes and the historical indexing README **have** been checked in under `sources/historical/2026-10-26/`.
- The downloadable `HISTORICAL_COVERAGE_LEDGER_2026-10-30.json` is a conversation artifact, not yet a repository file. It records 362 archive item paths with an explicit October 26–28 date marker, including nested duplicates: 4 marked Oct 26, 328 marked Oct 27, 30 marked Oct 28. **These are filename hints, not unique independently verified documents or creation dates.** Many files such as `FORMAL_NOTE (107).md` have no date in the filename; date-marked counts therefore DO NOT measure true coverage.

## Explicitly unverified

1. Whether all research files **dated October 28 onward** are present: **NO verification possible** from the two recovered archives. The user reports additional records not uploaded.
2. Whether a given file named `FORMAL_NOTE (n).md` is the last version, or a duplicate of a document already in Git: **not verified**.
3. Full cross-inventory of the GitHub repository against the 579 text handoff members: **not completed**; a GitHub file-by-file commit is not equivalent to uploading the handoff ZIP.
4. Original ZIP, binary checkpoint, simulation, and full catalogue payloads: **not bulk-committed** by the archive provenance entries.
5. Oct 29–30 and later non-archived analyses/claims, GitHub branches, private conversation history and attachments: **not exhaustively inventoried**.

## Working policy for completion

- Preserve historic files as byte-identical sources (source path and SHA-256), not replacements for current canonical theorems.
- When recovered files have clashing names, use archive-root namespaces; compare hashes before deciding genuine duplicates.
- Prioritize **a read-only repository tree census** and a deterministic manifest diff against local archive sources and the pre-existing published research corpus.
- Record gaps as `missing`, `not checked`, `duplicate by hash`, `filename conflict`, or `committed verified`; avoid interpreting absence from these archives as proof that a source never existed.
- Future user LFS uploads can supply binaries; future other-Oct28-plus uploads can extend the coverage ledger without rewriting the history.

**Scientific warning:** this is a preservation ledger, not a new completed-cage signed-current bound, verified original production action, or SU(2) continuum mass-gap theorem.
