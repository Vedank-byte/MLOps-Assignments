"""Reference version-change demonstration, not a copy of the original run."""
from pathlib import Path
import pandas as pd
path=Path("data/dataset.csv")
df=pd.read_csv(path)
df.loc[len(df)]={"id":5,"feature":5.5,"label":1}
df.to_csv(path,index=False)
print("Updated",path,"rows:",len(df))
