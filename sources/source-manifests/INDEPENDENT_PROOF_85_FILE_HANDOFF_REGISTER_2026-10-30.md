# Independent Proof Reconstruction — original-byte handoff register (2026-10-30)

**Status: 85 local bytes streams HASH VERIFIED; original Git LFS uploads NOT VERIFIED.** This is a counterpart to the existing 20-item archival intake register. It does **not** mark previously missing source families as present.

## Exact mounted inventory

| Evidence category | Files | Original bytes | Intended preservation |
| --- | ---: | ---: | --- |
| Historical dissertation TAR and Stage26 ZIP/NPZ archives | 18 | 65,480,248 | LFS, exact original bytes |
| Historical assistant-generated proof/reproducibility ZIP bundles | 34 | 204,419 | Immutable ZIP containers via LFS (and exact extracted scripts/text via source review) |
| Exact mounted Markdown/README/report streams | 31 | 247,781 | Git original text, deduplicate by byte SHA; do not overwrite versions |
| Rendered assistant conversation fragment | 1 | 6,253 | Git original text; **not a complete transcript** |
| Derived dissertation page PNG | 1 | 204,058 | LFS or separately tracked derived image, **not original source PDF** |
| **TOTAL** | **85** | **66,142,759** | Full machine-readable handoff |

### Local checksum-verified transfer packages

- `LFS_ORIGINAL_BYTES_2026-10-30.zip`: 53 byte-for-byte original/derived binary files, size **65,897,763 bytes**, SHA-256 **ef53216dedf0df81954cdd8635036858620593e8299f729a1ba92905e9948a78**. This includes the 18 historical uploaded scientific archives and all 34 October 28 proof packages, plus a derived image. Individual source ZIPs are preserved as ZIP bytes, not substituted with extracted member trees.
- `GIT_TEXT_EXACT_BYTES_2026-10-30.zip`: 32 exact text files, size **123,991 bytes**, SHA-256 **04d2073e6625f603be877ed020632a41c2aa599dfdb40b31d4940644ca5e35e3**.
- Companion uncompressed CSV `MOUNTED_FILES_SHA256.csv`: all **85** original relative paths, filenames, sizes, SHA-256, origin category, Git/LFS intended destination and explicit `NOT_VERIFIED` remote status.
- Companion `ARCHIVE_MEMBER_SHA256.csv`: **1,163** entries for original TAR/ZIP/NPZ member bytes, including extracted dissertation PDF, saved outer NPZ members, and October 28 proof-certificate/report/script members.
- `VERIFY_ORIGINAL_BYTES.py`: independently checks each extracted handoff byte stream against the 85-item CSV.
- Both transfer archives were reopened, and **each of their 85 original-member streams passed readback SHA-256 and length comparison**. The binary archives were not decompressed/repacked as replacements; the outer handoff stores original containers unchanged.

### Existing register reconciliation

All **19** entries currently mountable from the pre-existing `ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv` match the prior repository's original-byte size and SHA-256. The remaining registered `completed_cage_cut_comparison_2026-10-30.md` (3,217 bytes, SHA-256 `4ea1f8b18c5dbf53e09d7917b25afd0a74c0a6fe74e34bedd8a2b42918250f4c`) is **not mounted** in the current session. Its archive-entry hash is a **previous repository report**, not a new local byte check.

The exact `Branch · Read Conversation Content.txt` original (6,253 bytes, SHA-256 `982ee1b4667e4b1099852408d00211881cc03c9ddc06618efc260485f220b601`) **has now been committed to Git as text and re-read byte-equivalent** at `sources/originals/session-2026-10-30/Branch · Read Conversation Content.txt`. It is a signed-current assistant result, not a transcript. Nothing in this note asserts a remote LFS byte transfer for the other 53 binary items.

The 18 historical binary originals are: `Sharpe_dissertation_v10.7.tar.gz`; `{penrose,square}_seed{101,211,307,419}_stage26.zip` (eight); `penrose_seed101_stage26_full.zip`; and `{penrose,square}_seed{101,211,307,419}_sweep10000_multihit.npz` (eight). The prior register contains their exact per-file byte hashes.

### Source-type qualifications

The 34 research ZIPs are original **assistant-produced deliverables**, not independently verified experimental results. Their names describe research topics, not proof status. The 31 local Markdown/README reports are auxiliary originals, many byte-duplicated inside the assistant ZIPs; they are never treated as native message exports. The original dissertation TAR contains the dissertation PDF, five constituent paper PDFs, and two experiment PDFs; these members are itemized in the hash CSV. **The 52.9 MB Penrose full-chain package** is source data, not proof of accepted scalar spectroscopy or continuum transfer.

### Import and preservation procedure

1. Download both local handoff ZIPs and the companion manifest package; extract without changing relative paths.
2. Run `python VERIFY_ORIGINAL_BYTES.py <extracted-root>`; check every source hash.
3. Compare source SHA-256 against the existing 20-item register and any already committed Git blob; never overwrite a different original.
4. In a local repository clone run `git lfs install`, track relevant ZIP/NPZ/TAR/PNG paths via `.gitattributes`, place only verified missing originals at their manifest destinations, and commit normally. For assistant research packages consider `sources/originals/conversation-independent-proof-2026-10-28/binary/`; for historical Stage26 use the pre-existing `data/raw/session-2026-10-30/` paths.
5. Push **without force** and validate the remote LFS object bytes using `git lfs pull` in a clean second clone and SHA-256 comparison. Git LFS pointers, filenames, a locally constructed handoff and manifest entries are not proof of remote archive success.

### Remaining original-source gaps

No `NOTES.zip` original, 602-entry prepared source tree, all 42 Stage19–35 verification ZIPs, October29–30 theorem deliverables, exact native conversation export/IDs, or the historical twelve-prism oriented original was recoverable from the **currently mounted** byte streams. Those remain distinct high-priority archival gaps. See `docs/evidence/SOURCE_RECONCILIATION_GAPS_2026-10-30.csv`.

**Mathematical state unchanged:** finite-volume and conditional SU2 results exist, but the physical completed-cage uniform current, interacting covariance/gap, R2 continuum reconstruction and four-dimensional Yang–Mills mass gap are OPEN.
