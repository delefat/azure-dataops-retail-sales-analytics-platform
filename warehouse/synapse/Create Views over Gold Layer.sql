CREATE VIEW vw_sales_by_country
AS
SELECT *
FROM
OPENROWSET(
    BULK 'gold/sales_by_country/',
    DATA_SOURCE = 'RetailDataLake',
    FORMAT = 'DELTA'
) AS rows;