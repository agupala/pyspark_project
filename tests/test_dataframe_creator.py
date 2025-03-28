import pytest
from pyspark.sql import SparkSession
from utils.dataframe_creator import DataFrameCreator

@pytest.fixture
def spark():
    return SparkSession.builder.master("local").appName("test").getOrCreate()

def test_create_dataframe(spark):
    df = DataFrameCreator(spark).create_sample_dataframe(num_records=50)

    # Verificar que el DataFrame no está vacío
    assert df.count() > 0

    # Verificar las columnas esperadas
    expected_columns = {"order_id", "customer_id", "product_id", "category", "amount", "quantity", "purchase_date"}
    assert set(df.columns) == expected_columns
