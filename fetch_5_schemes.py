import requests
import pandas as pd

schemes = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"Data/raw/{name}.csv",
        index=False
    )
    print(name, "saved")