import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database/bluestock_mf.db")

processed = Path("data/processed")

files = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum_by_fund_house": "03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance": "07_scheme_performance.csv",
    "investor_transactions": "08_investor_transactions.csv",
    "portfolio_holdings": "09_portfolio_holdings.csv",
    "benchmark_indices": "10_benchmark_indices.csv"
}

for table, file in files.items():

    df = pd.read_csv(processed / file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table} : {len(df)} rows loaded")