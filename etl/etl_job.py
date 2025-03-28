from pyspark.sql import SparkSession
from etl.extractor import extract_data
from etl.transformer import transform_data
from etl.loader import load_data

def run_etl(input_path: str, output_path: str) -> None:
    """
    Ejecuta el flujo ETL completo.
    
    :param input_path: Ruta del archivo de entrada.
    :param output_path: Ruta de salida.
    """
    spark = SparkSession.builder.appName("ETLExample").getOrCreate()

    df = extract_data(spark, input_path)
    df_transformed = transform_data(df)
    load_data(df_transformed, output_path)

    spark.stop()
