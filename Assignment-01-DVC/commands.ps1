# Reference workflow reconstructed from assignment topic, NOT exact original command history.
git init
python -m pip install dvc
dvc init
# Place actual dataset at data/dataset.csv before running the following:
dvc add data/dataset.csv
git add .dvc .gitignore data/dataset.csv.dvc
git commit -m "Track dataset with DVC"
