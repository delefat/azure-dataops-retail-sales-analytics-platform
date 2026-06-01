# Databricks notebook source
# ============================================================
# Notebook: 01_bronze_online_retail_ingestion
# Purpose: Load Online Retail II CSV into Bronze Delta layer
# Author: Dele Fatoba
# ============================================================

from pyspark.sql.functions import current_timestamp, input_file_name


storage_account = "retaildataopsdevv4ptce"


storage_key = dbutils.secrets.get(
scope="dataopsecretscope",
key="storage-account-key"
)

# Configure Spark to access ADLS Gen2

spark.conf.set(
f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
storage_key
)

# Test connectivity to ADLS

display(
dbutils.fs.ls(
f"abfss://raw@{storage_account}.dfs.core.windows.net/"
)
)

#Source CSV File

raw_file_path = (
    f"abfss://raw@{storage_account}.dfs.core.windows.net/"
    "online-retail/online_retail_II.csv"
)


# Bronze Output Path

bronze_output_path = (
    f"abfss://bronze@{storage_account}.dfs.core.windows.net/"
    "online-retail/transactions"
)


# Read CSV

bronze_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .option("multiLine", "true")
    .option("escape", "\"")
    .csv(raw_file_path)
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("source_file", input_file_name())
)



display(bronze_df.limit(20))
bronze_df.printSchema()
print(f"Bronze record count: {bronze_df.count()}")



(
    bronze_df.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .save(bronze_output_path)
)

print(f"Bronze Delta created at: {bronze_output_path}")

Verify Bronze Output

display(
spark.read
.format("delta")
.load(bronze_output_path)
.limit(20)
)