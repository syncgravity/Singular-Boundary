# Intake reconciliation — 2026-11-11

## Verified binary custody

The authoritative LFS inventory is `LFS_INTAKE_LOCAL_2026-11-11.csv`: 19 objects (18 previously registered binary originals plus the identified Stage 26 incidence export). All 19 were fetched in a fresh clone from intake commit `826470c384aa0aa0147cb5ba17c474cea15059db`; byte sizes and SHA-256 values matched the manifest. The two older 2026-10-30 registers have been updated for their 18 binary rows. The Stage 26 export is also appended to the session-originals register.

The export is not a certified R3 partition. Its metadata says `partition_certified=true` while `inserted_faces` and `fixed_edges` are empty. The README and runbook preserve this warning.

## Recovered but not yet repository-imported transcripts

Two local PF-I16 source transcripts have been byte-hash verified. Their metadata is in `PF_I16_CONTINUATION_SOURCE_REGISTER_2026-11-11.csv`. Their full source bytes are not yet in Git; the theorem record identifies them as transcript-reported rather than independently audited. Do not treat this metadata register or a summary as a substitute for the original transcript bytes.

## Still unresolved

- `global_whitney_11face.npz`: expected hash and provenance caveats remain in `data/RESEARCH_ASSET_REGISTRY.csv`; original bytes are not committed.
- `ASSET_INDEX.csv` and `ORIGIN.csv`: unavailable; not reconstructed.
- Separate archival cage-cut source conversation: unavailable; the theorem record remains in the repository.
- PF-I16 transcript original-byte import: pending.

No theorem claim was promoted by this intake reconciliation. In particular, the independent-subsystem fourth-order algebra does not imply spatial connected-support/tree decay, all-orders convergence, continuum existence, or a physical mass gap.
