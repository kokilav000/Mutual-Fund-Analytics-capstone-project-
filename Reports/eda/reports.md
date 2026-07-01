# Mutual Fund Analytics Capstone Project

## Exploratory Data Analysis (EDA) Report

### Project Objective

The objective of this Exploratory Data Analysis (EDA) is to examine the mutual fund industry dataset from 2022–2025 and identify key trends related to Net Asset Value (NAV), Assets Under Management (AUM), SIP inflows, investor demographics, geographic distribution, folio growth, fund performance, and portfolio allocation. The analysis provides insights that support investment decision-making and serves as the foundation for dashboard development.

---

# Dataset Overview

The project uses the following datasets:

| Dataset                      | Description                              |
| ---------------------------- | ---------------------------------------- |
| 01_fund_master.csv           | Mutual fund scheme master information    |
| 02_nav_history.csv           | Historical daily NAV data                |
| 03_aum_by_fund_house.csv     | AUM by fund house                        |
| 04_monthly_sip_inflows.csv   | Monthly SIP inflows                      |
| 05_category_inflows.csv      | Net inflows by mutual fund category      |
| 06_industry_folio_count.csv  | Industry folio statistics                |
| 07_scheme_performance.csv    | Scheme return performance                |
| 08_investor_transactions.csv | Investor transaction details             |
| 09_portfolio_holdings.csv    | Portfolio holdings and sector allocation |

---

# Data Cleaning

The following preprocessing steps were completed before analysis:

* Converted all date columns to datetime format.
* Removed duplicate records.
* Validated missing values.
* Standardized categorical values.
* Verified numerical fields such as NAV, AUM, SIP inflows, and transaction amounts.
* Checked consistency of transaction types and KYC status.

---

# Exploratory Data Analysis

The following visualizations were created:

1. Daily NAV Trend (2022–2026)
2. AUM Growth by Fund House
3. Monthly SIP Inflow Trend
4. Category-wise Net Inflow Heatmap
5. Investor Age Group Distribution
6. SIP Amount Box Plot by Age Group
7. Gender Distribution
8. State-wise Investment Distribution
9. T30 vs B30 Investor Distribution
10. Folio Count Growth
11. NAV Return Correlation Heatmap
12. Sector Allocation Donut Chart
13. Top 10 Fund Houses by AUM
14. Transaction Type Distribution
15. Payment Mode Distribution
16. Annual Income Distribution
17. Average Investment Amount by Age Group

---

# Key Findings

### 1. NAV Growth

Daily NAV values showed a steady long-term upward trend, indicating sustained growth across most mutual fund schemes despite periodic market fluctuations.

### 2. AUM Expansion

Assets Under Management increased consistently across major fund houses, with SBI Mutual Fund maintaining the highest AUM throughout the analysis period.

### 3. SIP Growth

Monthly SIP inflows demonstrated continuous growth and reached their highest level in December 2025, reflecting increasing retail investor participation.

### 4. Category Preferences

Large Cap, Mid Cap, and Flexi Cap funds consistently attracted higher net inflows compared to other categories.

### 5. Investor Demographics

Most investors belong to young and middle-aged groups, highlighting strong participation from working professionals.

### 6. Gender Participation

Male investors represented a larger share of total investors in the available dataset.

### 7. Geographic Trends

Investments were concentrated in major states and T30 cities, indicating higher participation from metropolitan regions.

### 8. Industry Growth

Industry folio counts increased significantly during the study period, demonstrating continuous expansion of the mutual fund investor base.

### 9. Portfolio Allocation

Financial Services, Information Technology, and Healthcare formed the largest sector allocations across equity mutual fund portfolios.

### 10. Fund Correlation

Most selected mutual fund schemes exhibited positive return correlations, reflecting similar market movement patterns among diversified equity funds.

---

# Conclusion

The exploratory data analysis reveals strong growth in India's mutual fund industry between 2022 and 2025. NAV values, AUM, SIP inflows, and folio counts indicate increasing investor confidence and expanding market participation. Demographic and geographic analyses provide insights into investor behavior, while portfolio allocation and correlation analysis improve understanding of fund composition and diversification.

The insights generated through this analysis provide a solid foundation for developing interactive dashboards and conducting advanced predictive analytics in subsequent phases of the project.

---

# Deliverables

* EDA_Analysis.ipynb containing all analysis
* 15+ visualization charts
* Exported PNG chart files
* EDA_Report.md
* Cleaned datasets used for analysis
