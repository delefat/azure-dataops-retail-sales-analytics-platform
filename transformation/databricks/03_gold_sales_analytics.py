# Databricks notebook source
# ============================================================
# Notebook: 03_gold_sales_analytics
# Purpose: Create Gold business aggregates for reporting
# Author: Dele Fatoba
# ============================================================

from pyspark.sql.functions import (
    col,
    sum as spark_sum,
    countDistinct,
    count,
    year,
    month,
    round as spark_round
)

storage_account = "retaildataopsdevv4ptce

silver_path = (
    f"abfss://silver@{storage_account}.dfs.core.windows.net/"
    "online-retail/transactions"
)

gold_base_path = (
    f"abfss://gold@{storage_account}.dfs.core.windows.net/"
    "online-retail"
)


sales_df = spark.read.format("delta").load(silver_path)

display(sales_df.limit(20))



sales_only_df = sales_df.filter(col("transaction_type") == "SALE")



sales_by_country = (
    sales_only_df
    .groupBy("country")
    .agg(
        spark_round(spark_sum("sales_amount"), 2).alias("total_sales"),
        countDistinct("invoice_no").alias("transaction_count"),
        countDistinct("customer_id").alias("unique_customers")
    )
    .orderBy(col("total_sales").desc())
)



sales_by_product = (
    sales_only_df
    .groupBy("stock_code", "product_description")
    .agg(
        spark_round(spark_sum("sales_amount"), 2).alias("total_sales"),
        spark_sum("quantity").alias("total_quantity_sold"),
        countDistinct("invoice_no").alias("transaction_count")
    )
    .orderBy(col("total_sales").desc())
)



monthly_sales = (
    sales_only_df
    .withColumn("sales_year", year(col("invoice_date")))
    .withColumn("sales_month", month(col("invoice_date")))
    .groupBy("sales_year", "sales_month")
    .agg(
        spark_round(spark_sum("sales_amount"), 2).alias("monthly_sales"),
        countDistinct("invoice_no").alias("monthly_transactions"),
        countDistinct("customer_id").alias("unique_customers")
    )
    .orderBy("sales_year", "sales_month")
)



top_customers = (
    sales_only_df
    .filter(col("customer_id").isNotNull())
    .groupBy("customer_id", "country")
    .agg(
        spark_round(spark_sum("sales_amount"), 2).alias("customer_total_sales"),
        countDistinct("invoice_no").alias("order_count")
    )
    .orderBy(col("customer_total_sales").desc())
)


sales_by_country.write.format("delta").mode("overwrite").save(f"{gold_base_path}/sales_by_country")
sales_by_product.write.format("delta").mode("overwrite").save(f"{gold_base_path}/sales_by_product")
monthly_sales.write.format("delta").mode("overwrite").save(f"{gold_base_path}/monthly_sales")
top_customers.write.format("delta").mode("overwrite").save(f"{gold_base_path}/top_customers")

print("Gold Delta tables created successfully.")