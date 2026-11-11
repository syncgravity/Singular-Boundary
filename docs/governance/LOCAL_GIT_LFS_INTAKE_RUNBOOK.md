# Local Git LFS intake and clean-clone verification

**Current status (2026-11-11):** the original 18 registered binary assets plus the identified Stage 26 incidence export (19 LFS objects total) are pushed to `main`. A fresh clone fetched all 19 objects and matched each file's byte size and SHA-256 against `sources/source-manifests/LFS_INTAKE_LOCAL_2026-11-11.csv`. The historical 2026-10-30 registers have been reconciled for those 18 binary rows. This is not a claim that every historical text source has been recovered.

## Authoritative records

- Current LFS object inventory and custody: `sources/source-manifests/LFS_INTAKE_LOCAL_2026-11-11.csv`.
- Historical intake context: `sources/source-manifests/ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv`.
- Session-original register, now reconciled for the LFS objects: `sources/source-manifests/SESSION_LOCAL_ORIGINALS_VERIFIED_2026-10-30.csv`.
- Binary policy and outstanding provenance gaps: `data/README.md`.

## Future binary intake

Operate from a fresh clone of the existing `main` branch. Do not push a separately initialized historical Git root and never force-push.

```bash
git clone git@github.com:syncgravity/singular-boundary.git
cd singular-boundary
git lfs install
git lfs env
git pull --ff-only origin main
```

Before staging a new binary, add its exact original filename, byte size, SHA-256, provenance, and destination to the appropriate intake manifest. Copy unchanged source bytes into `data/raw/<dated-session>/`, then verify:

```bash
shasum -a 256 data/raw/<dated-session>/<filename>
git check-attr filter -- data/raw/<dated-session>/<filename>
git lfs ls-files
git diff --cached --stat
```

The attribute check must report `filter: lfs`. If not, stop and correct `.gitattributes` before staging. Commit the object and manifest together, then push normally to `main` (or use an explicitly authorized review branch if repository policy requires it).

## Required remote verification

A Git LFS pointer in Git is not proof that its object is retrievable. After push, use an independent fresh clone:

```bash
git clone git@github.com:syncgravity/singular-boundary.git retrieval-test
cd retrieval-test
git lfs pull
git lfs fsck
shasum -a 256 data/raw/<dated-session>/<filename>
```

Compare both byte size and SHA-256 with the committed manifest. Record the commit SHA used for retrieval, command, date, result, and LFS OID/pointer path. Mark `remote_bytes_verified=YES` and `clean_checkout_verified=YES` only after the actual bytes have been retrieved and matched. Record partial failures explicitly; never infer successful retrieval from a commit or pointer alone.

## Known limits and unresolved sources

- The 19 verified LFS objects comprise 18 registered originals plus `penrose_stage26_full_incidence.json`. The export is an exploratory `stage26-simulation-incidence-v1` inventory, not a certified historical R3 12-prism subcomplex. Its `partition_certified=true` field is defective because `inserted_faces` and `fixed_edges` are empty; do not cite it as an R3 partition or insertion estimate.
- `ASSET_INDEX.csv` and `ORIGIN.csv` remain unavailable; do not fabricate replacements.
- The original `global_whitney_11face.npz` remains uncommitted. Its expected hash is recorded in `data/RESEARCH_ASSET_REGISTRY.csv`; a reconstruction script or candidate NPZ is not byte-identical evidence.
- The two PF-I16 continuation transcripts have verified local source hashes, but their full source bytes still need to be committed.
- The separate archival cage-cut source conversation remains unrecovered even though the theorem record is in the repository.

Never claim the complete historical source set is present until each outstanding source is independently recovered, committed, and verified.
