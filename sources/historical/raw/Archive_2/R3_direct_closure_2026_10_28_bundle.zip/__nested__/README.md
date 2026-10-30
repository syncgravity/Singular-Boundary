# Direct R3 closure attempt

Read `FORMAL_NOTE.md` for the theorem and its exact scope. Run `python -m unittest -v test_peeling` for the five verification tests. Run `python peeling_certificate.py incidence.json` to check a concrete full retained-face incidence, with the 54 fill face labels in `fill`. A successful certificate proves a volume-uniform `λ E S_fill <= 81` for 54 faces. This certificate is sufficient, not necessary; the project-specific incidence file was not present in the inspected artifacts.
