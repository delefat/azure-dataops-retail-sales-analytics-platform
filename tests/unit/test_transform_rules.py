import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, trim, upper, when


@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder
        .appName("retail-dataops-unit-tests")
        .master("local[*]")
        .getOrCreate()
    )


def test_customer_id_decimal_suffix_removed(spark):
    data = [("13085.0",)]
    df = spark.createDataFrame(data, ["customer_id"])

    result = df.withColumn(
        "customer_id_clean",
        regexp_replace(col("customer_id").cast("string"), "\\.0$", "")
    ).collect()[0]["customer_id_clean"]

    assert result == "13085"


def test_country_standardised_to_uppercase(spark):
    data = [(" United Kingdom ",)]
    df = spark.createDataFrame(data, ["country"])

    result = df.withColumn(
        "country_clean",
        upper(trim(col("country")))
    ).collect()[0]["country_clean"]

    assert result == "UNITED KINGDOM"


def test_negative_quantity_classified_as_return(spark):
    data = [(-2,)]
    df = spark.createDataFrame(data, ["quantity"])

    result = df.withColumn(
        "transaction_type",
        when(col("quantity") < 0, "RETURN").otherwise("SALE")
    ).collect()[0]["transaction_type"]

    assert result == "RETURN"