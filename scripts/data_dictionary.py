import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
OUTPUT = Path("reports/data_dictionary.md")

files = sorted(RAW.glob("*.csv"))

with open(OUTPUT, "w", encoding="utf-8") as f:

    f.write("# Mutual Fund Analytics - Data Dictionary\n\n")

    for file in files:

        df = pd.read_csv(file)

        f.write(f"## {file.name}\n\n")
        f.write("| Column | Data Type |\n")
        f.write("|--------|-----------|\n")

        for col, dtype in zip(df.columns, df.dtypes):
            f.write(f"| {col} | {dtype} |\n")

        f.write("\n")
        