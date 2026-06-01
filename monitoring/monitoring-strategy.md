\# Monitoring and Observability Strategy



\## Monitoring Scope



This project monitors:



\- Azure Data Factory pipeline runs

\- Databricks notebook/job execution

\- ADLS Gen2 storage usage

\- Synapse Serverless SQL query activity

\- Data quality test results

\- Cost and resource health



\## Key Metrics



| Component | Metric |

|---|---|

| Azure Data Factory | Pipeline success/failure |

| Databricks | Job duration and failure count |

| ADLS Gen2 | Storage capacity and transactions |

| Synapse | Query failures and data scanned |

| Power BI | Dataset refresh status |



\## Alerting



Recommended alerts:



\- ADF pipeline failure

\- Databricks job failure

\- Synapse query failure

\- Storage access failure

\- Unexpected cost increase



\## Log Analytics



Azure Log Analytics is used as the central workspace for operational monitoring.

