import pandas as pd
import os

folder = "Data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(folder, file))

        duplicates = df.duplicated().sum()

        print(f"{file} -> Duplicates: {duplicates}")