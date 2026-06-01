def test_silver_required_columns_exist(spark):
    df = spark.table("retail_dataops.silver.online_retail_transactions")

    required_columns = {
        "invoice_no",
        "stock_code",
        "product_description",
        "quantity",
        "invoice_date",
        "unit_price",
        "customer_id",
        "country",
        "sales_amount",
        "transaction_type"
    }

    assert required_columns.issubset(set(df.columns))


def test_silver_invoice_no_not_null(spark):
    df = spark.table("retail_dataops.silver.online_retail_transactions")
    assert df.filter("invoice_no IS NULL").count() == 0


def test_gold_sales_by_country_populated(spark):
    df = spark.table("retail_dataops.gold.sales_by_country")
    assert df.count() > 0