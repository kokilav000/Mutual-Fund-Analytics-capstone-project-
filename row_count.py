import pandas as pd
from sqlalchemy import create_engine, text

# Create SQLite connection
engine = create_engine("sqlite:///database/bluestock_mf.db")

tables = [
    "fund_master",
    "nav_history",
    "aum_by_fund_house",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_count",
    "scheme_performance",
    "investor_transactions",
    "portfolio_holdings",
    "benchmark_indices"
]

with engine.connect() as conn:
    print("=" * 50)
    print("Row Count Verification")
    print("=" * 50)

    for table in tables:
        result = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        )
        count = result.scalar()
        print(f"{table:<30} {count}")

print("=" * 50)
print("Verification Completed")