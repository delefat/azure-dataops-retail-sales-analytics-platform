# Databricks notebook source
# ============================================================
# Notebook: 02_silver_online_retail_transform
# Purpose: Clean and standardise Bronze transactions into Silver
# Author: Dele Fatoba
# ============================================================

from pyspark.sql.functions import (
    col,
    trim,
    upper,
    to_timestamp,
    regexp_replace,
    current_timestamp,
    when
)

# COMMAND ----------

bronze_table_name = "retail_dataops.bronze.online_retail_transactions"
silver_table_name = "retail_dataops.silver.online_retail_transactions"

# COMMAND ----------

bronze_df = spark.table(bronze_table_name)

display(bronze_df.limit(20))
bronze_df.printSchema()

# COMMAND ----------

silver_df = (
    bronze_df
    .withColumnRenamed("Invoice", "invoice_no")
    .withColumnRenamed("StockCode", "stock_code")
    .withColumnRenamed("Description", "product_description")
    .withColumnRenamed("Quantity", "quantity")
    .withColumnRenamed("InvoiceDate", "invoice_date")
    .withColumnRenamed("Price", "unit_price")
    .withColumnRenamed("Customer ID", "customer_id")
    .withColumnRenamed("Country", "country")
)

# COMMAND ----------

silver_df = (
    silver_df
    .withColumn("invoice_no", trim(col("invoice_no").cast("string")))
    .withColumn("stock_code", trim(col("stock_code").cast("string")))
    .withColumn("product_description", trim(col("product_description")))
    .withColumn("quantity", col("quantity").cast("int"))
    .withColumn("invoice_date", to_timestamp(col("invoice_date")))
    .withColumn("unit_price", col("unit_price").cast("double"))
    .withColumn("customer_id", regexp_replace(col("customer_id").cast("string"), "\\.0$", ""))
    .withColumn("country", upper(trim(col("country"))))
    .withColumn(
        "transaction_type",
        when(col("quantity") < 0, "RETURN").otherwise("SALE")
    )
    .withColumn("sales_amount", col("quantity") * col("unit_price"))
    .withColumn("silver_processed_timestamp", current_timestamp())
)

# COMMAND ----------

silver_df = (
    silver_df
    .filter(col("invoice_no").isNotNull())
    .filter(col("stock_code").isNotNull())
    .filter(col("invoice_date").isNotNull())
    .filter(col("unit_price") > 0)
    .dropDuplicates(["invoice_no", "stock_code", "invoice_date", "customer_id"])
)

# COMMAND ----------

display(silver_df.limit(20))
silver_df.printSchema()

print(f"Silver record count: {silver_df.count():,}")

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS retail_dataops.silver")

(
    silver_df.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(silver_table_name)
)

print(f"Silver Delta table created: {silver_table_name}")

# COMMAND ----------

display(
    spark.table(silver_table_name)
    .limit(20)
)