# Local Git LFS intake and clean-clone verification

**Operate from a fresh clone of the existing `main` branch. Do not push a separately initialized historical Git root onto `main` and never force-push.**

Prerequisites: Git, Git LFS, access to the private repository, and a secure local directory containing the unchanged original files.

```bash
git clone git@github.com:syncgravity/singular-boundary.git
cd singular-boundary
git lfs install
git lfs env
git pull --ff-only origin main
git check-attr filter -- data/raw/session-2026-10-30/Sharpe_dissertation_v10.7.tar.gz
```

Expected `filter: lfs`. If not, STOP and fix `.gitattributes` before staging. Keep original source archives unchanged. Use `sources/source-manifests/ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv` to find exact SHA-256, size and target path for each of 20 known session originals. Do not place text-only sources under LFS merely because they accompany the dataset.

For each original binary:

```bash
mkdir -p data/raw/session-2026-10-30
cp -p "/absolute/path/to/original/archive.zip" "data/raw/session-2026-10-30/archive.zip"
shasum -a 256 "data/raw/session-2026-10-30/archive.zip"
git add .gitattributes "data/raw/session-2026-10-30/archive.zip"
git lfs ls-files
git diff --cached --stat
git commit -m "Preserve original archive.zip immutable research source"
git push origin main
```

Use the actual file name and verify it against the manifest; do not literally upload `archive.zip`. For the 18 identified binary session originals, repeat or batch after matching each local source to the manifest. For text records, place exact bytes in the registered `sources/originals/` path and use normal Git (unless deliberately changed with an explicit reason). For privacy, inspect verbatim conversations before committing.

**Verify the remote object, not just the pointer:**

```bash
cd ..
git clone git@github.com:syncgravity/singular-boundary.git singular-boundary-retrieval-test
cd singular-boundary-retrieval-test
git lfs pull
git lfs fsck
python3 scripts/historical/verify_local_originals.py data/raw/session-2026-10-30
```

The included verifier expects **all 20** manifest items in one directory; when testing binaries alone, use per-file SHA-256 against the intake CSV and separately verify text originals. Do not mark full-manifest PASS until all 20 originals are present and verified. Check files are actual content rather than LFS pointer stubs. Never mark a missing source as received.

After verified retrieval, update the per-item register and commit verification evidence: date, original SHA-256, fresh-clone commit SHA, test command, result, and (for LFS objects) OID and pointer path. Record any partial failures without deleting history.

For the separately prepared 602-file text tree, import its *content* through a branch rooted in this repository and check origin SHA-256; do not splice its independent Git history by force. Follow the conversation provenance protocol for each recovered chat.

This procedure requires authenticated Git LFS access and appropriate storage quotas; current ChatGPT execution cannot perform the networked LFS transfer.
