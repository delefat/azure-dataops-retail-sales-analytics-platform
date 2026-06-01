# Databricks notebook source
# ============================================================
# Notebook: 01_bronze_online_retail_ingestion
# Purpose: Load Online Retail II CSV from Unity Catalog Volume
#          into Bronze Delta table
# Author: Dele Fatoba
# ============================================================

from pyspark.sql.functions import current_timestamp, input_file_name

# COMMAND ----------

# Source file in Unity Catalog Volume
# This volume points to ADLS Gen2 through:
# Storage Credential -> External Location -> External Volume

source_file_path = (
    "/Volumes/retail_dataops/raw/online_retail_volume/"
    "online_retail_II.csv"
)

# Bronze managed Delta table in Unity Catalog

bronze_table_name = "retail_dataops.bronze.online_retail_transactions"

# COMMAND ----------

# Validate source file path

display(
    dbutils.fs.ls(
        "/Volumes/retail_dataops/raw/online_retail_volume/"
    )
)

# COMMAND ----------

# Read CSV from Unity Catalog Volume

bronze_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .option("multiLine", "true")
    .option("escape", "\"")
    .csv(source_file_path)
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("source_file", input_file_name())
)

# COMMAND ----------

display(bronze_df.limit(20))

bronze_df.printSchema()

print(f"Bronze record count: {bronze_df.count():,}")

# COMMAND ----------

# Create Bronze schema if it does not exist

spark.sql("CREATE CATALOG IF NOT EXISTS retail_dataops")
spark.sql("CREATE SCHEMA IF NOT EXISTS retail_dataops.bronze")

# COMMAND ----------

# Write Bronze Delta table as a Unity Catalog managed table

(
    bronze_df.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(bronze_table_name)
)

print(f"Bronze Delta table created: {bronze_table_name}")

# COMMAND ----------

# Verify Bronze table

display(
    spark.table(bronze_table_name)
    .limit(20)
)