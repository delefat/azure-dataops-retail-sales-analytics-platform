def test_bronze_silver_gold_tables_exist(spark):
    tables = [
        "retail_dataops.bronze.online_retail_transactions",
        "retail_dataops.silver.online_retail_transactions",
        "retail_dataops.gold.sales_by_country",
        "retail_dataops.gold.sales_by_product",
        "retail_dataops.gold.monthly_sales",
        "retail_dataops.gold.top_customers"
    ]

    for table_name in tables:
        df = spark.table(table_name)
        assert df.count() > 0