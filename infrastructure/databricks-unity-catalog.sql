CREATE CATALOG IF NOT EXISTS retail_dataops;

CREATE SCHEMA IF NOT EXISTS retail_dataops.raw;
CREATE SCHEMA IF NOT EXISTS retail_dataops.bronze;
CREATE SCHEMA IF NOT EXISTS retail_dataops.silver;
CREATE SCHEMA IF NOT EXISTS retail_dataops.gold;

CREATE STORAGE CREDENTIAL retail_dataops_credential
WITH (
  AZURE_MANAGED_IDENTITY (
    ACCESS_CONNECTOR_ID = '/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-retail-dataops-dev/providers/Microsoft.Databricks/accessConnectors/ac-databricks-storage-dev-abc123',
    MANAGED_IDENTITY_ID = '/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-retail-dataops-dev/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id-databricks-storage-dev-abc123'
  )
);

CREATE EXTERNAL LOCATION retail_raw_location
URL 'abfss://raw@retaildataopsdevabc123.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL retail_dataops_credential);

GRANT READ FILES, WRITE FILES
ON EXTERNAL LOCATION retail_raw_location
TO `delefatob@yahoo.co.uk`;

CREATE EXTERNAL VOLUME retail_dataops.raw.online_retail_volume
LOCATION 'abfss://raw@retaildataopsdevabc123.dfs.core.windows.net/online-retail/';