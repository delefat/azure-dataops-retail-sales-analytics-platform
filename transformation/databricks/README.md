# Databricks Transformation Layer

This folder contains Databricks source notebooks for the Online Retail II Azure DataOps project.

## Notebooks

| Notebook | Purpose |
|---|---|
| `01_bronze_online_retail_ingestion.py` | Loads raw CSV from ADLS Gen2 into Bronze Delta |
| `02_silver_online_retail_transform.py` | Cleans, standardises and validates transaction data |
| `03_gold_sales_analytics.py` | Creates business-ready Gold aggregates |

## Medallion Architecture

- **Bronze**: Raw ingested transaction data with metadata
- **Silver**: Cleaned and standardised transaction-level data
- **Gold**: Aggregated business-ready datasets for reporting

## Gold Outputs

- Sales by Country
- Sales by Product
- Monthly Sales
- Top Customers