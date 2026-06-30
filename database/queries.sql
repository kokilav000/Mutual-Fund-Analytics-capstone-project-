--1 Top 5 Funds by AUM

SELECT fund_house,
SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-------------------------------------------------

--2 Average NAV per Month

SELECT
strftime('%Y-%m',date) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month;

-------------------------------------------------

--3 SIP YoY Growth

SELECT
month,
yoy_growth_pct
FROM monthly_sip_inflows;

-------------------------------------------------

--4 Transactions by State

SELECT
state,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-------------------------------------------------

--5 Funds with Expense Ratio <1%

SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct<1;

-------------------------------------------------

--6 Top Performing Funds (5-Year Return)

SELECT
scheme_name,
return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-------------------------------------------------

--7 Average Expense Ratio

SELECT
AVG(expense_ratio_pct)
FROM scheme_performance;

-------------------------------------------------

--8 Category-wise Net Inflow

SELECT
category,
SUM(net_inflow_crore)
FROM category_inflows
GROUP BY category;

-------------------------------------------------

--9 Portfolio Sector Allocation

SELECT
sector,
SUM(weight_pct)
FROM portfolio_holdings
GROUP BY sector
ORDER BY SUM(weight_pct) DESC;

-------------------------------------------------

--10 Benchmark Closing Price

SELECT
index_name,
AVG(close_value)
FROM benchmark_indices
GROUP BY index_name;