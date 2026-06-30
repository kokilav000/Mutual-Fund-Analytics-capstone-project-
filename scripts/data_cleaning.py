import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================
# Folder Paths
# ==========================================

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

PROCESSED.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Mutual Fund Analytics - Data Cleaning")
print("=" * 60)


# ==========================================
# Helper Function
# ==========================================

def save_file(df, filename):
    df.to_csv(PROCESSED / filename, index=False)
    print(f"✓ {filename} saved ({len(df)} rows)")


# ==========================================
# 01_fund_master.csv
# ==========================================

print("\nCleaning 01_fund_master.csv...")

fund = pd.read_csv(RAW / "01_fund_master.csv")

print("Original Rows :", len(fund))

fund.columns = fund.columns.str.strip()

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund = fund.drop_duplicates()

fund = fund[
    fund["expense_ratio_pct"] > 0
]

fund = fund[
    fund["exit_load_pct"] >= 0
]

text_columns = [
    "fund_house",
    "scheme_name",
    "category",
    "sub_category",
    "plan",
    "benchmark",
    "fund_manager",
    "risk_category",
    "sebi_category_code"
]

for col in text_columns:
    fund[col] = (
        fund[col]
        .astype(str)
        .str.strip()
    )

save_file(fund, "01_fund_master.csv")


# ==========================================
# 02_nav_history.csv
# ==========================================

print("\nCleaning 02_nav_history.csv...")

nav = pd.read_csv(RAW / "02_nav_history.csv")

print("Original Rows :", len(nav))

nav.columns = nav.columns.str.strip()

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.dropna(subset=["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav.drop_duplicates()

nav = nav[
    nav["nav"] > 0
]

save_file(nav, "02_nav_history.csv")


# ==========================================
# 03_aum_by_fund_house.csv
# ==========================================

print("\nCleaning 03_aum_by_fund_house.csv...")

aum = pd.read_csv(
    RAW / "03_aum_by_fund_house.csv"
)

print("Original Rows :", len(aum))

aum.columns = aum.columns.str.strip()

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum = aum.drop_duplicates()

aum = aum[
    aum["aum_crore"] > 0
]

aum = aum[
    aum["num_schemes"] > 0
]

aum["fund_house"] = (
    aum["fund_house"]
    .astype(str)
    .str.strip()
)

save_file(
    aum,
    "03_aum_by_fund_house.csv"
)

# ==========================================
# 04_monthly_sip_inflows.csv
# ==========================================

print("\nCleaning 04_monthly_sip_inflows.csv...")

sip = pd.read_csv(RAW / "04_monthly_sip_inflows.csv")

print("Original Rows :", len(sip))

sip.columns = sip.columns.str.strip()

# Convert month to datetime
sip["month"] = pd.to_datetime(
    sip["month"],
    format="%Y-%m",
    errors="coerce"
)

# Remove duplicate rows
sip = sip.drop_duplicates()

# Convert numeric columns
numeric_cols = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]

for col in numeric_cols:
    sip[col] = pd.to_numeric(sip[col], errors="coerce")

# Keep missing YoY values (first year has no previous year)
sip["yoy_growth_pct"] = sip["yoy_growth_pct"].fillna(0)

# Remove invalid values
sip = sip[
    (sip["sip_inflow_crore"] > 0) &
    (sip["active_sip_accounts_crore"] > 0) &
    (sip["new_sip_accounts_lakh"] > 0) &
    (sip["sip_aum_lakh_crore"] > 0)
]

save_file(sip, "04_monthly_sip_inflows.csv")


# ==========================================
# 05_category_inflows.csv
# ==========================================

print("\nCleaning 05_category_inflows.csv...")

category = pd.read_csv(
    RAW / "05_category_inflows.csv"
)

print("Original Rows :", len(category))

category.columns = category.columns.str.strip()

category["month"] = pd.to_datetime(
    category["month"],
    format="%Y-%m",
    errors="coerce"
)

category = category.drop_duplicates()

category["net_inflow_crore"] = pd.to_numeric(
    category["net_inflow_crore"],
    errors="coerce"
)

category = category.dropna(subset=["net_inflow_crore"])

category["category"] = (
    category["category"]
    .astype(str)
    .str.strip()
)

save_file(
    category,
    "05_category_inflows.csv"
)


# ==========================================
# 06_industry_folio_count.csv
# ==========================================

print("\nCleaning 06_industry_folio_count.csv...")

folio = pd.read_csv(
    RAW / "06_industry_folio_count.csv"
)

print("Original Rows :", len(folio))

folio.columns = folio.columns.str.strip()

folio["month"] = pd.to_datetime(
    folio["month"],
    format="%Y-%m",
    errors="coerce"
)

folio = folio.drop_duplicates()

folio_columns = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for col in folio_columns:
    folio[col] = pd.to_numeric(
        folio[col],
        errors="coerce"
    )

folio = folio[
    (folio["total_folios_crore"] > 0) &
    (folio["equity_folios_crore"] > 0) &
    (folio["debt_folios_crore"] > 0) &
    (folio["hybrid_folios_crore"] > 0) &
    (folio["others_folios_crore"] > 0)
]

save_file(
    folio,
    "06_industry_folio_count.csv"
)

# ==========================================
# 07_scheme_performance.csv
# ==========================================

print("\nCleaning 07_scheme_performance.csv...")

perf = pd.read_csv(RAW / "07_scheme_performance.csv")

print("Original Rows :", len(perf))

perf.columns = perf.columns.str.strip()

perf = perf.drop_duplicates()

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in return_columns:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

perf["expense_flag"] = np.where(
    perf["expense_ratio_pct"].between(0.1, 2.5),
    "OK",
    "Check"
)

save_file(perf, "07_scheme_performance.csv")


# ==========================================
# 08_investor_transactions.csv
# ==========================================

print("\nCleaning 08_investor_transactions.csv...")

txn = pd.read_csv(RAW / "08_investor_transactions.csv")

print("Original Rows :", len(txn))

txn.columns = txn.columns.str.strip()

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn = txn.drop_duplicates()

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

txn["transaction_type"] = txn["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

txn["amount_inr"] = pd.to_numeric(
    txn["amount_inr"],
    errors="coerce"
)

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

save_file(txn, "08_investor_transactions.csv")


# ==========================================
# 09_portfolio_holdings.csv
# ==========================================

print("\nCleaning 09_portfolio_holdings.csv...")

portfolio = pd.read_csv(
    RAW / "09_portfolio_holdings.csv"
)

print("Original Rows :", len(portfolio))

portfolio.columns = portfolio.columns.str.strip()

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"],
    errors="coerce"
)

portfolio = portfolio.drop_duplicates()

numeric_columns = [
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]

for col in numeric_columns:
    portfolio[col] = pd.to_numeric(
        portfolio[col],
        errors="coerce"
    )

portfolio = portfolio[
    (portfolio["weight_pct"] > 0) &
    (portfolio["market_value_cr"] > 0) &
    (portfolio["current_price_inr"] > 0)
]

save_file(
    portfolio,
    "09_portfolio_holdings.csv"
)


# ==========================================
# 10_benchmark_indices.csv
# ==========================================

print("\nCleaning 10_benchmark_indices.csv...")

benchmark = pd.read_csv(
    RAW / "10_benchmark_indices.csv"
)

print("Original Rows :", len(benchmark))

benchmark.columns = benchmark.columns.str.strip()

benchmark["date"] = pd.to_datetime(
    benchmark["date"],
    errors="coerce"
)

benchmark = benchmark.drop_duplicates()

benchmark = benchmark.sort_values(
    ["index_name", "date"]
)

benchmark["close_value"] = pd.to_numeric(
    benchmark["close_value"],
    errors="coerce"
)

benchmark = benchmark[
    benchmark["close_value"] > 0
]

save_file(
    benchmark,
    "10_benchmark_indices.csv"
)
