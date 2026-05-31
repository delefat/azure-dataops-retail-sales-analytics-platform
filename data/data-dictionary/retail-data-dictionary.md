# Retail Sales Data Dictionary

## Dataset

Online Retail II

## Business Purpose

The dataset represents online retail transactions and is used to analyze:

* Revenue trends
* Product performance
* Customer purchasing behavior
* Geographic sales distribution
* Customer lifetime value
* Inventory demand patterns

---

## Source Columns

| Column Name | Data Type | Description                                   |
| ----------- | --------- | --------------------------------------------- |
| Invoice     | String    | Unique invoice number for a sales transaction |
| StockCode   | String    | Unique product identifier                     |
| Description | String    | Product description                           |
| Quantity    | Integer   | Quantity purchased                            |
| InvoiceDate | DateTime  | Date and time of transaction                  |
| Price       | Decimal   | Unit selling price                            |
| Customer ID | String    | Unique customer identifier                    |
| Country     | String    | Customer country                              |

---

## Data Quality Rules

### Invoice

* Cannot be null
* Must be unique within transaction scope

### StockCode

* Cannot be null
* Must exist in Product dimension

### Quantity

* Must be greater than zero
* Negative values indicate returns

### Price

* Must be greater than zero

### Customer ID

* Nullable in source
* Records without Customer ID are excluded from customer analytics

### InvoiceDate

* Cannot be null

---

## Bronze Layer

Purpose:

Store source data with minimal transformation.

Additional Metadata Columns:

| Column              | Description               |
| ------------------- | ------------------------- |
| ingestion_timestamp | Timestamp data was loaded |
| source_file         | Source file name          |

---

## Silver Layer

Purpose:

Apply cleansing and standardization.

Transformations:

* Remove duplicate records
* Standardize country values
* Convert dates to standard format
* Validate numeric fields
* Remove invalid records

---

## Gold Layer

Purpose:

Provide business-ready analytical datasets.

### Gold Tables

#### GoldSalesByCountry

| Column           | Description            |
| ---------------- | ---------------------- |
| Country          | Customer country       |
| TotalSales       | Total sales revenue    |
| TransactionCount | Number of transactions |

#### GoldSalesByProduct

| Column       | Description         |
| ------------ | ------------------- |
| Product      | Product description |
| TotalSales   | Revenue generated   |
| QuantitySold | Units sold          |

#### GoldMonthlySales

| Column       | Description           |
| ------------ | --------------------- |
| SalesYear    | Year                  |
| SalesMonth   | Month                 |
| MonthlySales | Total monthly revenue |

---

## Star Schema Design

### FactSales

Measures:

* Sales Amount
* Quantity Sold

Foreign Keys:

* Customer Key
* Product Key
* Date Key

### DimCustomer

Customer attributes.

### DimProduct

Product attributes.

### DimDate

Calendar attributes.

### DimCountry

Geographic attributes.
