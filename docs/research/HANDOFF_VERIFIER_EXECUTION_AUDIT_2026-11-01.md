# Handoff verifier executed fixture audit — 2026-11-01

**Target:** `research/scripts/verify_research_handoff.py`, source read from branch `fix/reproducible-research-handoff-2026-10-30`, blob `c6d29c46ef53ea02a23102b9c4f3e2e2c956a5ad`. The script was manually transcribed line-for-line into a temporary isolated local test directory; this is a **source-transcription test**, not cryptographic byte identity to the GitHub file.

## Executed results

- Valid ZIP with exact manifest hash: PASS (accepted).
- Tampered payload with unchanged manifest: PASS (rejected).
- Missing manifest-listed file: PASS (rejected).
- Manifest traversal path `../escape.txt`: PASS (rejected).
- ZIP traversal member `../bad`: PASS (rejected).
- Duplicate ZIP member `data.txt`: PASS (rejected).
- Basic regular-file ZIP: PASS.
- **ZIP Unix symlink metadata** (`ZipInfo.create_system=3`, symlink mode in `external_attr`) with otherwise matching bytes: **ACCEPTED**.
- **Internal directory symlink** pointing to a file within the permitted root, with a matching manifest digest: **ACCEPTED**.

These last two are not demonstrated path escapes, but they violate the stricter goal of refusing symlinks and prove that the script does not enforce a regular-file-only archive policy. An internal symlink cannot necessarily escape the root because `verify_dir` calls `resolve()` and rejects external targets; nevertheless this is an explicit acceptance behavior and must be specified or corrected.

## Required correction prior to merging PR #2

- Reject non-regular ZIP entries using Unix mode metadata when `create_system==3` (or define a carefully justified alternate policy).
- Decide whether to forbid directory symlinks entirely; if so use `lstat` and check every path component rather than only resolved-root containment.
- Validate all ZIP entry names, including directories, and normalize path forms before duplicate-name checks.
- Include fixture tests for symlinks and nested bundle-prefix manipulation.
- Test incomplete/malformed manifest and independent SHA-256 calculation; do not claim this file has been accepted for production until CI and exact-source readback pass.

## Boundary

This suite tests integrity verification behavior, **not** physical Yang–Mills calculations. Original scientific inputs were independently inspected in [the uploaded-input audit](INDEPENDENT_SOURCE_INPUT_AUDIT_2026-11-01.md). Historical claim certification remains blocked.
