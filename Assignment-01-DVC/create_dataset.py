"""Reference sample dataset for reproducing DVC workflow; not the original dataset."""
from pathlib import Path
import pandas as pd
Path("data").mkdir(exist_ok=True)
pd.DataFrame({"id":[1,2,3,4],"feature":[2.4,3.1,4.5,5.0],"label":[0,0,1,1]}).to_csv("data/dataset.csv",index=False)
print("Created sample data/dataset.csv")
