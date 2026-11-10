# CEP13 versioned evidence package

This extension preserves the frozen controller and historical outcomes. It includes current raw CSV/JSON logs, full correction vectors, caches, model and terminal arrays, failed and rejected cases, and source code. The base v1.0.0 archives remain unchanged. Download the two base archives, CEP13_current_records.zip, publication_manifest.json, and install_release.py into one directory, then run:

```
python install_release.py --output NEW_EMPTY_ARTIFACT_DIRECTORY
cd NEW_EMPTY_ARTIFACT_DIRECTORY
python -m pip install -r reproducibility/requirements.txt
python reproducibility/reproduce.py verify
python reproducibility/run_minimal_review.py --output NEW_EMPTY_RERUN_DIRECTORY
```

The installer downloads missing base archives only from their public v1.0.0 URLs and verifies their SHA256. It extracts the base and original audit companion, then overlays current records. The minimal command runs one original C1 case, one original added C2 state and one corrected finite-age design, without changing an archived input. Current checks/design/run-finite/check-histories commands remain available in reproducibility/reproduce.py. Verification checks file identity; it is not mathematical certification.

Large full_constraint_rows.npz and complete_decision_records.npz files contain derived row exports. Their primitive raw records and exact model arrays are included; 90 cases and 108 dense files were reconstructed and checked against originals, including bitwise array and byte-identical NPZ-container checks in the recorded environment. To restore them:

```
python reproducibility/restore_derived_exports.py --output NEW_EMPTY_DENSE_EXPORT_DIRECTORY
```

This reconstructs rows without running a solver or integrating a vehicle. Cross-platform BLAS/zlib differences can change binary hashes: a mismatch must be investigated, never hidden by rounding or relaxing acceptance. Original full files are preserved in the local author project. No precision reduction, altered physical tolerance, new feedback gain or replacement of unfavorable data is used.

C2_causal_and_fallback contains the causal-reference equivalence audit, 284 current command-increment exclusion witnesses, and six actual horizon1/2/10 runs with fixed in-domain optimizer faults. The initial analysis-index error and its correction are retained. The comparison C is mathematically equivalent to the proposed current-graph QP; it is not an external recent baseline. The finite grid is not a full-dimensional volume.

network_validation contains exact public-source NR-V2X builds, raw SQLite and packet-event logs for seeds/runs1/2/3 and both reservation modes, a one-way causal controller replay, and every stop/error record. These are network-simulator outputs, not radio hardware measurements. All six radio traces exceed at least one original Bf1/D1 service requirement. Four replays stop on the existing current-radius check; two complete physical integration and have metrics reconstructed from their180 saved steps after a summary-only unknown-outcome metadata error. No out-of-contract full-task guarantee is claimed. The new48-byte measured application layout differs from the earlier unexecuted design sketch and is explicitly documented.

The newest Faliero author code is retained with its BSD license and exact-source provenance. Original-scene reproduction and equal-tracking external ranking are not claimed without a complete validated run. Ge's lower tracking error and faster computation remain in the historical records. No independent follower identification, RF hardware, HIL or full emergency-stop validation is asserted.

Research-tool assistance and author review are disclosed in the manuscript. This data release does not approve the manuscript, complete the Elsevier Declarations tool, create a DOI or submit to a journal. The author-approved grant names/numbers are unchanged; recipients still need factual confirmation for the official form.

An unintended constant-leader optimizer-fault attempt is preserved under unintended_constant_leader_attempt with its configuration mismatch disclosed. The final six varying-leader fault runs explicitly execute the prespecified sin-cubed profile. All36 forced decisions use verified tails; the first attempts are not relabelled as those runs.

The separate CEP13_comparison_audit.json is part of this release. It checks actual Ge data attempts:3 per sample on178 of180 samples, compared with the present configured M2 cap. The historical equal-available-capacity description is withdrawn; all measured performance numbers remain intact. Do not use these points as a strict shared-M2 or equal-tracking comparison.