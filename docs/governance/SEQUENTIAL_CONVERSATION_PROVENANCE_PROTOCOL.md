# Sequential conversation provenance protocol

Status: ACTIVE archival protocol; historical completeness NOT YET VERIFIED.

## Two immutable layers

1. `sources/conversations/`: original exports, named by sequence ID, UTC date and source conversation identifier. Preserve complete text, attachments manifest, hashes and original order. Never rewrite original messages; corrections are linked separately.
2. `research/`: canonical claims, definitions, theorems, proof obligations and reproductions. Each claim references source conversation ID, message span, evidence file and Git commit.

## Mandatory conversation register

Create `sources/conversations/INDEX.csv` with fields:
`sequence_id,conversation_title,started_utc,ended_utc,predecessor_id,successor_id,transcript_path,transcript_sha256,attachment_manifest_path,import_status,claim_review_status,notes`.

Statuses: DISCOVERED, EXPORTED, HASH_VERIFIED, CLAIMS_EXTRACTED, RECONCILED, UNAVAILABLE. No guessed dates, missing messages or inferred transcripts.

## Claim reconciliation

For each conversation, record: newly stated definitions and assumptions; claimed theorem and proof location; numerical result with input/code/environment; counterexample; correction/retraction; dependency; open gate; publication eligibility. Mark whether the claim is verbatim source-asserted, mechanically reproduced, independently proved, conditional, numerical or unverified. A later chat does not silently supersede an earlier result; add explicit supersession edges.

## Publication audit gate

Before publication, every cited result must resolve to an exact source or independently reconstructed proof, all numerical figures to exact original data and scripts, and all known counterexamples and caveats must be cross-referenced. Compare sequential chat register to full Project export. Missing chats are blockers for a claim of complete historical provenance, but do not automatically invalidate independently verified theorems.

## Present limitation

GitHub and currently accessible Project files do not supply a complete enumerated list or verbatim exports of every ChatGPT Project conversation. The present conversation cannot certify historical completeness. Request/export missing conversations and import exact bytes before setting any register entry to RECONCILED.

## Retrieval-first policy correction — 2026-10-30

Before requesting exports, search available prior-conversation context and Project/Library files, reconstruct the research sequence and reconcile each recoverable claim with Git. Retrieved summaries are useful evidence of research history but are not verbatim transcripts; record this distinction. Request an export only for a specifically identified source gap that cannot be recovered by existing access. Do not impose bulk manual export on the researcher.
