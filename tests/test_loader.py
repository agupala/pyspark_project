import pytest
import os
from pyspark.sql import SparkSession
from etl.loader import load_data
from utils.dataframe_creator import DataFrameCreator

@pytest.fixture
def spark():
    return SparkSession.builder.master("local").appName("test").getOrCreate()

def test_load_data(spark, tmp_path):
    df = DataFrameCreator(spark).create_sample_dataframe(num_records=50)
    output_path = str(tmp_path / "output")

    # Guardar los datos
    load_data(df, output_path)

    # Verificar que la carpeta de salida no está vacía
    assert os.listdir(output_path), "La carpeta de salida está vacía."
