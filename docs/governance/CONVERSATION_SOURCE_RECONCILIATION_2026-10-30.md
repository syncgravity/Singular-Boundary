# Conversation-accessible source inventory — 2026-10-30

**Scope:** only file bytes actually mounted in the current conversation and two readable Library handoff documents. This is an accounting record, **not** a completed import or proof certification.

## Mounted original source evidence

- Dissertation archive: `Sharpe_dissertation_v10.7.tar.gz` (7,004,477 bytes; SHA-256 `c405acd6daa5a0a923429ab659b122b22231787d7a30e97db7f2974f278354d1`).
- Eight Stage26 compressed chain summaries: `penrose_seed{101,211,307,419}_stage26.zip` and `square_seed{101,211,307,419}_stage26.zip`.
- Eight Stage26 multihit outputs: `penrose_seed{101,211,307,419}_sweep10000_multihit.npz` and `square_seed{101,211,307,419}_sweep10000_multihit.npz`.
- Full Penrose chain archive: `penrose_seed101_stage26_full.zip` (52,884,778 bytes; SHA-256 `6cfa12935428533cfeaff40a467705d632b19ede07b7f30e0bb9fb7a0cc68657`).
- Conversation excerpt: `Branch · Read Conversation Content.txt` (6,253 bytes; SHA-256 `982ee1b4667e4b1099852408d00211881cc03c9ddc06618efc260485f220b601`).
- Local mathematical note: `completed_cage_cut_comparison_2026-10-30.md` (3,217 bytes; SHA-256 `4ea1f8b18c5dbf53e09d7917b25afd0a74c0a6fe74e34bedd8a2b42918250f4c`). The repository theorem file is separately authored; it is not byte-identical.

**Byte-level original data status:** mounted here, **not verified as committed as exact bytes**. Do not assume historical numerical inputs are in Git or Git LFS on this basis. The earlier project conversation holds a separate 20-file SHA-256 manifest.

## Library source summaries read

- `THEOREM.md`, 2026-10-30: CI-1/CI-2 proofs, examples, named tests. Its theorem has been transcribed to `research/theorems/CONDITIONAL_HAAR_INCOMPLETE_CAGE_CI1_CI2_2026-10-30.md`. The named tests and CSV certificates still require byte import and reproduction.
- `PROJECT_HANDOFF.md`, 2026-10-30: current completed-cage open gate and prior-branch provenance, explicitly not the complete transcript. Findings are indexed in `docs/current/CANONICAL_RESEARCH_STATE_2026-10-30.md`.

## Reconciliation requirements

1. Compare each mounted source with `sources/source-manifests/` original SHA-256 manifests and `data/` or Git LFS material.
2. Obtain every relevant October 29–30 Library ZIP as actual bytes; compare members, source theorem text and script output, not just titles.
3. Preserve absent historical material as `NOT_IMPORTED`. Never invent a repository path for an unavailable file.
4. Project-wide chat completeness **cannot be certified** without full chat exports or a complete external Project source index. Only known/mounted files are accounted for here.
