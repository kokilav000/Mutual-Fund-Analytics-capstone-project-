import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv(
    "Data/raw/HDFC_Top100_NAV.csv",
    index=False
)

print("Downloaded Successfully")
print(df.head())