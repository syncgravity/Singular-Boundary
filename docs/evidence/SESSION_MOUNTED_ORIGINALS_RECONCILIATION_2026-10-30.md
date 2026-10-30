# Mounted original-source reconciliation — 2026-10-30

## Scope and evidence boundary

This document records a **partial archival intake**, not a claim of complete conversation or original-source coverage. A current-session byte inspection independently hashed 19 mounted original artifacts. The existing [20-item archival intake register](../../sources/source-manifests/ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv) already lists each with exact destination, size and SHA-256; **no duplicate ledger entries were added**.

The one remaining unmounted entry in that register is `completed_cage_cut_comparison_2026-10-30.md`. Its registered size/hash are prior repository assertions, **not independently rechecked in this intake**. The `Branch · Read Conversation Content.txt` file was inspected; it is a 6,253-byte **rendered assistant result** headed “The Singular Boundary — Signed Radial-Current Theorem”, not a full verbatim ChatGPT conversation transcript. Do not mark any chat fully exported based on this file.

## Original byte verification

All 19 original file sizes and SHA-256 digests match the named rows in `ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv`:

* Dissertation source: `Sharpe_dissertation_v10.7.tar.gz` (7,004,477 bytes).
* Stage 26 original archives: `penrose_seed{101,211,307,419}_stage26.zip` and `square_seed{101,211,307,419}_stage26.zip` (eight originals).
* Additional `penrose_seed101_stage26_full.zip` (52,884,778 bytes).
* Sweep datasets: `{penrose,square}_seed{101,211,307,419}_sweep10000_multihit.npz` (eight originals).
* Single text source: `Branch · Read Conversation Content.txt` (6,253 bytes).

The exact originals were packaged without changing their internal bytes in `singular_boundary_2026-10-30_verified_originals_handoff.zip`, a local handoff of 65,495,275 bytes. The handoff SHA-256 is `cf8a63ac4573d441b93ed8a6dab50427d3813aa98df47ac62d87466b726e5cc4`. It contains `MANIFEST.csv`, `README.md`, `verify_originals.py`, and all 19 originals under `originals/`. The ZIP central-directory/CRC test returned no error.

**Remote Git LFS status: NOT VERIFIED** for the 18 binary originals. A local handoff ZIP, a SHA-256 manifest, or a Git pointer is not proof of remote bytes. The handoff is not itself committed to GitHub. After user-side LFS push, check original byte size and SHA-256 from a clean clone with `git lfs pull` before editing the existing intake register's verification flags. Preserve existing branch history.

## Mathematical and chronology reconciliation

The source excerpt states a signed radial-score Ward identity for the actual deleted interacting SU(2) vacuum and a conditional bulk criterion involving `sup_f T_{f,h}=o(h^{-1/4})`. It also presents an oscillatory, positive SU(2) rotor **countermodel to the necessity of an older sufficient effective-potential budget**, not a counterexample to the Wilson interacting vacuum. The reported deterministic table is **source-asserted and not newly independently executed in this intake**. See the existing R3-IR claim family and canonical research state before allocating any new claim ID. No new theorem, proof, or continuum result is certified here.

The excerpt mentions the previous audit branch, a prior ledger commit prefix `35e4b46`, and a signed-current ZIP with an asserted SHA-256; that ZIP was **not mounted here**. Those are references in the text, not original byte verification of that older deliverable.

The following research gates remain open: nonlinear **completed-cage** uniform current/cap control in the true Wilson vacuum; full physical connected low-energy source/covariance bounds; the independent R3-PRISM source-word specification and its comparison; R2 spatial/temporal continuum control, positivity and spectral reconstruction; and D1 production-action/source certification. The finite-volume exact Haar **incomplete**-cage theorem and nonuniform completed-cage cap positivity may not be substituted for these gates.

## Unavailable original historical material

No complete verbatim predecessor conversation exports, ChatGPT source IDs, full branch structure, or message-level UTC times were recoverable from the 19 mounted bytes. This intake does not certify the prepared 602-file tree, 188 `NOTES.zip` members, 42 historical verification archives, October 29–30 theorem ZIPs, CI-1/CI-2 original scripts/certificates, or original 352-MB incidence data. The canonical backlog and gap tracker remain OPEN. Retrospective chronologies and previous assistant statements must not be misrepresented as original messages.

## Verification / downstream operations

1. Read `MANIFEST.csv` within the local handoff; execute `python3 verify_originals.py` beside the extracted `originals/` directory.
2. Place each original at its manifest's destination (18 binary objects under `data/raw/session-2026-10-30/`, one text object under `sources/originals/session-2026-10-30/`).
3. Use Git LFS for ZIP, NPZ and TAR.GZ; preserve byte-identical original objects and existing Git history.
4. Push normally, fresh-clone the repository, pull LFS objects, verify size/hash and ZIP CRC, *then* change remote status fields.
5. Recover and index other conversations as verbatim exports with real identifiers; link claims only after matched source review.

This audit does **not** claim a four-dimensional interacting continuum Yang–Mills mass-gap proof.
