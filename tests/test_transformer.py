import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from etl.transformer import transform_data
from utils.dataframe_creator import DataFrameCreator

@pytest.fixture
def spark():
    return SparkSession.builder.master("local").appName("test").getOrCreate()

def test_transform_data(spark):
    df = DataFrameCreator(spark).create_sample_dataframe(num_records=50)
    transformed_df = transform_data(df)

    # Verificar que la nueva columna "amount_with_tax" existe
    assert "amount_with_tax" in transformed_df.columns

    # Verificar que el cálculo es correcto
    row = transformed_df.select("amount", "amount_with_tax").first()
    assert row["amount_with_tax"] == row["amount"] * 1.21
