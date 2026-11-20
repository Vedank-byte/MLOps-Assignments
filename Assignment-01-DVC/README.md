# Assignment 1 — DVC Dataset Versioning

Practical: dataset version control with Git and DVC. The original command history and project files are not present as standalone source files in the accessible report, so this is a reference workflow rather than an exact transcript.

```powershell
git init
python -m pip install dvc
dvc init
# After placing your actual dataset at data/dataset.csv:
dvc add data/dataset.csv
git add .dvc .gitignore data/dataset.csv.dvc
git commit -m "Track dataset with DVC"
# After editing the dataset:
dvc add data/dataset.csv
git add data/dataset.csv.dvc
git commit -m "Update dataset version"
```

DVC tracks dataset metadata in Git; actual dataset content remains in DVC cache or a configured remote. Replace this reference with the original project commands and dataset metadata before claiming exact reproducibility.
