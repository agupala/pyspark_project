from pyspark.sql import DataFrame

def load_data(df: DataFrame, output_path: str) -> None:
    """
    Guarda el DataFrame transformado en un archivo CSV.
    
    :param df: DataFrame a guardar.
    :param output_path: Ruta de destino del archivo CSV.
    """
    df.write.mode("overwrite").csv(output_path, header=True)
