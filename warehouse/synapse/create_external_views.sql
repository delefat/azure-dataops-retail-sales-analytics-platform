-- Intended Synapse Serverless SQL views over Gold Delta outputs.
-- Synapse deployment is currently excluded due to subscription regional SQL provisioning restrictions.

CREATE OR ALTER VIEW retail.vw_sales_by_country
AS
SELECT *
FROM OPENROWSET(
    BULK 'online-retail/sales_by_country/',
    DATA_SOURCE = 'RetailGoldDataLake',
    FORMAT = 'DELTA'
) AS rows;
GO

CREATE OR ALTER VIEW retail.vw_sales_by_product
AS
SELECT *
FROM OPENROWSET(
    BULK 'online-retail/sales_by_product/',
    DATA_SOURCE = 'RetailGoldDataLake',
    FORMAT = 'DELTA'
) AS rows;
GO

CREATE OR ALTER VIEW retail.vw_monthly_sales
AS
SELECT *
FROM OPENROWSET(
    BULK 'online-retail/monthly_sales/',
    DATA_SOURCE = 'RetailGoldDataLake',
    FORMAT = 'DELTA'
) AS rows;
GO

CREATE OR ALTER VIEW retail.vw_top_customers
AS
SELECT *
FROM OPENROWSET(
    BULK 'online-retail/top_customers/',
    DATA_SOURCE = 'RetailGoldDataLake',
    FORMAT = 'DELTA'
) AS rows;
GO