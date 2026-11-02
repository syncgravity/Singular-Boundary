# Branch reconciliation record — 2026-11-01

## Scope

This is an **administrative integration** of research navigation, not a mathematical proof certification. No experimental data, theorem coefficients, original attachments, or historical claim ledger rows are deleted or replaced.

## Verified baseline and actions

- Baseline canonical `main` README was dated 2026-10-30 and pointed to the older snapshot.
- `docs/research-navigation-provenance-2026-11-01`: one commit ahead, zero behind original main, eight additive documentation files; merged via PR #3 at merge commit `872bf0195e8eb145bd560fad39207b9b44450afa`.
- README rewritten as canonical navigation entry, with P0–P5 gates and evidence standards at commit `13ae05631f93efec0f9f70bef0ba9fa32cecd5c6`.
- `fix/reproducible-research-handoff-2026-10-30`: 2 ahead/193 behind original main, adds `research/REPRODUCIBILITY_WORKFLOW.md` and `research/scripts/verify_research_handoff.py`; PR #2 remains draft. PR documents missing ZIP/path test coverage, bundle-specific manifests and unexecuted CI. Do not merge until independently tested and updated against current main.
- `audit/2026-10-28-independent-reconstruction`: 506 ahead/552 behind original main, touches README, claim ledger, handoff notes, and extensive research records. **Do not merge wholesale:** audit for duplicates, orientation supersessions, and ledger conflicts; selective provenance-preserving cherry-picks or new reviewed PRs are required.

## Outstanding integration work

1. Compare the audit branch claim ledger with canonical claim ledger by immutable claim ID; preserve original order and report conflicting revisions explicitly.
2. Inventory branch-only theorem reports, executable scripts and research data; identify what exists independently on main and what is missing.
3. Validate the reproducibility verifier against malformed archives, traversal paths, duplicate members, wrong SHA and missing-file cases; execute CI and rebase or port deliberately.
4. Recover historical original data via verified SHA-256 readback and Git LFS where appropriate; never assert Library-only material is in Git.
5. Cross-check navigation index entries against theorem bodies, status and correction chains. Filename-derived categorization remains provisional.
6. Independently audit P1 corrected operator signs and all dependencies before treating an inherited mathematical statement as publication-certified.

## Scientific continuity

P2 nonlinear connected-radius majorant, P3 Wilson completed-cage current (or independent alternative), P4 physical spectral controls, P5 continuum reconstruction remain open. P0 provenance and cross-model identity and P1 complete orientation certification have unresolved verification scopes. Preserve this distinction in the claim ledger and future communications.
