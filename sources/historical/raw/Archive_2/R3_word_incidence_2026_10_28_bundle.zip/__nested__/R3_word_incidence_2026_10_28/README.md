# Word-level Penrose incidence exporter

**Read `FORMAL_NOTE.md` first.** The supplied example has 14 temporal faces but is **NOT** the unavailable historical Q14 insertion; it has 35 support links and 53 affected retained faces, not 36 and 62.

Run `python certificate.py && python verify_words.py`, or supply the historical 14 canonical Z^5 face labels with `python certificate.py --canonical-Q historical_Q_labels.json`. Then rerun verification.

Dependencies: numpy, scipy; no external services.
