# Binary asset policy

No original large binary data have been committed to ordinary Git. `ASSET_INDEX.csv` exists in the prepared local archival import, but is **not yet available in this remote branch**.

The raw Stage 7 ZIP, Stage 19 source bundles, Stage 26 checkpoints, NPZ archives, dissertation tarball and 352 MB incidence JSON should remain immutable. Git LFS is not yet installed or verified in the working container, and the large objects have **not** been uploaded.

When a network-enabled Git environment with Git LFS is available:

1. Clone this existing remote without overwriting its history.
2. Import the prepared textual source tree and verify each original byte hash against `sources/source-manifests/ORIGIN.csv`.
3. Confirm Git LFS installation and authorization before placing immutable binary originals under `data/raw/`; inspect attributes using `git check-attr filter -- data/raw/<filename>`.
4. Verify file hashes and remote LFS pointer/object retrieval from a fresh checkout.
5. If storage quotas make LFS unsuitable, keep binaries in immutable content-addressed external storage, and commit the checksums plus access policy.

Do not claim that a GitHub commit containing a manifest has uploaded the scientific data itself.
