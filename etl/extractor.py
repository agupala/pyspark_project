from pyspark.sql import SparkSession, DataFrame

def extract_data(spark: SparkSession, file_path: str) -> DataFrame:
    """
    Extrae datos desde un archivo CSV y lo convierte en un DataFrame de PySpark.
    
    :param spark: Sesión de Spark.
    :param file_path: Ruta del archivo CSV.
    :return: DataFrame con los datos extraídos.
    """
    return spark.read.csv(file_path, header=True, inferSchema=True)
