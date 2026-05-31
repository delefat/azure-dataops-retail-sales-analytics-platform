# Dataset Information

## Overview

This project uses the Online Retail II dataset, a real-world transactional retail dataset containing online sales records from a UK-based online retailer.

The dataset is used to demonstrate an end-to-end Azure DataOps implementation including:

* Azure Data Factory ingestion
* Azure Data Lake Storage Gen2
* Azure Databricks transformations
* Delta Lake architecture
* Azure Synapse Analytics
* Power BI reporting
* CI/CD automation
* Data quality validation
* Monitoring and governance

## Dataset Source

Kaggle:

https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

Original UCI Repository:

https://archive.ics.uci.edu/dataset/352/online+retail

## Dataset Description

The dataset contains transactional sales information including:

* Invoice information
* Product information
* Customer information
* Transaction dates
* Quantity sold
* Unit prices
* Country information

1. Invoice information
2. Product information
3. Customer information
4. Transaction dates
5. Quantity sold
6. Unit prices
7. Country information

## Repository Policy

The original dataset is not stored in this GitHub repository.

To reproduce this project:

1) Download the dataset from Kaggle.

2) Save the file locally as:

   data/sample/online_retail_II.xlsx

3) Upload the file to Azure Data Lake Storage Gen2.

4) Execute the ingestion pipeline.


## Data Flow

Raw Dataset
→ Azure Data Lake (Raw Zone)
→ Bronze Layer
→ Silver Layer
→ Gold Layer
→ Synapse Analytics
→ Power BI Dashboard
