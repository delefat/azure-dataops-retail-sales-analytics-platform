\# Alert Rules



\## ADF Pipeline Failure



Condition:



\- Pipeline run status = Failed



Action:



\- Email notification

\- Teams notification

\- Incident log entry



\## Databricks Job Failure



Condition:



\- Job run failed



Action:



\- Review notebook logs

\- Validate source data availability

\- Re-run pipeline after remediation



\## Data Quality Failure



Condition:



\- Unit/data quality test failure



Action:



\- Stop downstream processing

\- Investigate invalid records

\- Reprocess Silver/Gold layer

