import pandas as pd
import os

folder = "Data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):

        print("\n" + "="*60)
        print("FILE:", file)

        df = pd.read_csv(os.path.join(folder, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())
      