# CEP reproducibility package

The current records are publicly available in [release v1.1.0](https://github.com/13573681375/CEP-reproducibility-package/releases/tag/v1.1.0).

Download `CEP13_current_records.zip`, `publication_manifest.json`, and `install_release.py`. The installer obtains the unchanged v1.0.0 base archives if needed and checks their SHA256. Run:

```text
python install_release.py --output NEW_EMPTY_ARTIFACT_DIRECTORY
cd NEW_EMPTY_ARTIFACT_DIRECTORY
python -m pip install -r reproducibility/requirements.txt
python reproducibility/reproduce.py verify
python reproducibility/run_minimal_review.py --output NEW_EMPTY_RERUN_DIRECTORY
```

The release includes raw records, fixed configurations, model/terminal arrays, source, failure records, and instructions for restoring large derived exports. Actual C1, C2, and corrected finite-age reruns and an unauthenticated public-download hash check are recorded in [the publication receipt](https://github.com/13573681375/CEP-reproducibility-package/blob/cep13-publication/results/publication/receipt.json).

See `CEP13_comparison_audit.json` in the release: the historical Ge adaptation does not enforce the present M=2 per-sample cap. Its performance data are retained and are not an equal-capacity or equal-tracking ranking. NR-V2X traces are simulator outputs; hardware radio measurement is not claimed. No data DOI has been assigned.
