# Historical sources awaiting archival reconciliation

This is an **open intake backlog**, not evidence that original bytes were uploaded. See [the 20-item exact intake register](ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv) for per-file size and SHA-256. Never mark COMPLETE based on a filename, hash manifest or reconstructed narrative.

| Family | Known scope | Intended preservation | Outstanding verification |
| --- | --- | --- | --- |
| Session originals | 20 named items: 17 binary ZIP/NPZ/TAR and 3 text/Markdown | Binary files via Git LFS; verbatim text in regular Git | Original-byte remote pull and hashes, 1 text source locally unavailable at prior audit |
| Prepared historical tree | 602 tracked text/code paths in independent local import | Merge original files as ordinary Git text, retain origin hashes | Locate exact tree and 582 historic source hashes; preserve remote ancestry |
| NOTES.zip | 188 original Markdown members, 156 byte-distinct from an earlier import | Immutable original ZIP via LFS plus indexed exact text in Git | Match member SHA-256 and retain container ZIP |
| Stage 19–35 historical archive chain | 42 verification ZIP archives identified by historic audits | LFS originals and hash inventory | Recover exact archive names, hashes and byte content; avoid guessing |
| Additional original Stage 7–26 assets | Earlier ZIPs, original snapshots, checkpoints, and scripts | LFS for binary, Git for source | Reconcile against historical reports and asset index |
| Incidence data | 352 MB incidence JSON referenced by existing data policy | LFS / dedicated checksummed immutable storage | Recover original bytes, hash, and verified retrieval |
| Oct 29–30 theorem packages | Signed current, nonlinear flux, local IR, Gaussian/magnetic, Wilson/Agmon, localization, conditional Haar and related patches | Preserve **all** original bundles via LFS, then original member scripts/logs/theorems in Git | Itemize exact filenames+SHA only after reading originals; verify claim mappings |
| CI-1/CI-2 | Original scripts and CSV certificates | Git source, LFS if oversized binary | Recover tests and certificates, clean-checkout execution |
| October 11 SU(2) Phase I artifacts | Original four-vertex code, output; no-measurements audit; continuum fitter | Git exact text and test outputs | Verify exact original sources and claims |
| Conversation histories | Sequential verbatim message exports, source-linked attachments | Git text where appropriate, LFS for compressed exports | Full coverage by conversation ID, attachments, hashes and claim mappings |
| R3-PRISM | Original twelve-prism support/conditioning specification | Git exact original source | Locate and independently certify source |

**Counting caution:** categories overlap. This is a prioritized recovery inventory, not a deduplicated count of distinct objects. Never invent hashes for unavailable originals.

## Completion protocol

1. Record original filename, source identifier, byte size, SHA-256, contents/attachment index, and target repository path.
2. If binary/large, use Git LFS or a content-addressed immutable object store; put original text and executable code in ordinary Git.
3. Upload; retrieve from a *fresh clone* with `git lfs pull`, compare original size/hash and package CRCs; only then change `remote_bytes_verified` to YES and `clean_checkout_verified` to PASS.
4. Link each scientific claim and version to verbatim source, theorem/experiment, code, data, environment, execution log and counterexample/correction; update the claim ledger without deleting historical claims.
5. Preserve all previous commits and frozen snapshots. Complete does not mean proved.

The unresolved proof obligations are governed by `docs/current/CANONICAL_RESEARCH_STATE_2026-10-30.md` and `docs/evidence/SOURCE_RECONCILIATION_GAPS_2026-10-30.csv`.
