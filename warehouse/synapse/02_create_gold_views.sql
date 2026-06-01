USE RetailDataOps;
GO

CREATE OR ALTER VIEW gold.vw_sales_by_country AS
SELECT *
FROM OPENROWSET(
    BULK 'https://retaildataopsdevv4ptce.dfs.core.windows.net/gold/online-retail/sales_by_country/',
    FORMAT = 'DELTA'
) AS rows;
GO

CREATE OR ALTER VIEW gold.vw_sales_by_product AS
SELECT *
FROM OPENROWSET(
    BULK 'https://retaildataopsdevv4ptce.dfs.core.windows.net/gold/online-retail/sales_by_product/',
    FORMAT = 'DELTA'
) AS rows;
GO

CREATE OR ALTER VIEW gold.vw_monthly_sales AS
SELECT *
FROM OPENROWSET(
    BULK 'https://retaildataopsdevv4ptce.dfs.core.windows.net/gold/online-retail/monthly_sales/',
    FORMAT = 'DELTA'
) AS rows;
GO

CREATE OR ALTER VIEW gold.vw_top_customers AS
SELECT *
FROM OPENROWSET(
    BULK 'https://retaildataopsdevv4ptce.dfs.core.windows.net/gold/online-retail/top_customers/',
    FORMAT = 'DELTA'
) AS rows;
GO