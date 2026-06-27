import pandas as pd

df = pd.read_csv("Data/raw/01_fund_master.csv")

print(df["fund_house"].unique())
print(df["category"].unique())
print(df["sub_category"].unique())
print(df["risk_category"].unique())