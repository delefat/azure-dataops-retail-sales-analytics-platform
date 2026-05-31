# Azure DataOps Retail Sales Analytics Platform

## Project Overview

This project is an original Azure DataOps portfolio implementation inspired by the modern data warehouse engineering patterns, using Azure Data Factory, Databricks, Azure Data Lake Storage Gen2 (ADLS Gen2), Azure Synapse Analytics, Power BI, CI/CD, testing, monitoring, and data governance.

The solution demonstrates how enterprise organizations can build a scalable, secure, and automated data platform to ingest, transform, store, and analyze retail sales data using Microsoft Azure services and DataOps best practices.

## Business Scenario

A fictional retail organization requires a modern cloud data platform to:

- Ingest sales, customer, product, and store data
- Implement a Medallion Architecture (Bronze, Silver, Gold)
- Support business intelligence and analytics
- Automate deployments through CI/CD
- Enforce data quality and governance
- Monitor platform performance and reliability



## Credits and Inspiration

This project was designed and implemented as an independent portfolio solution.

The architecture and engineering practices were inspired by industry-standard Azure DataOps, Data Lakehouse, and Modern Data Warehouse patterns, including publicly available Microsoft reference architectures and Azure best-practice guidance.

All implementation, documentation, customization, deployment automation, testing strategy, and business use cases in this repository were developed specifically for this portfolio project.


## Infrastructure as Code

This project demonstrates Infrastructure-as-Code (IaC) using both Microsoft-native and cloud-agnostic deployment approaches.

### Deployment Options

* **Bicep** – Microsoft-native Infrastructure-as-Code for Azure resources
* **Terraform** – Industry-standard multi-cloud Infrastructure-as-Code platform

### Azure Resources Deployed

The infrastructure deployment provisions the following Azure services:

* Azure Resource Group
* Azure Data Lake Storage Gen2 (ADLS Gen2)
* Raw, Bronze, Silver and Gold storage containers
* Azure Data Factory
* Azure Databricks Workspace
* Azure Key Vault
* Azure Log Analytics Workspace
* Managed Identity and Role-Based Access Control (RBAC)

### Primary Deployment Method

- **Bicep** is used as the primary deployment method for the Azure implementation.
- **Terraform** is included to demonstrate equivalent cloud infrastructure provisioning capability.

This approach showcases enterprise Infrastructure-as-Code practices and supports repeatable, automated environment provisioning.

