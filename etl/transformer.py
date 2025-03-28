from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def transform_data(df: DataFrame) -> DataFrame:
    """
    Aplica transformaciones al DataFrame de entrada.
    
    :param df: DataFrame original.
    :return: DataFrame transformado.
    """
    return df.withColumn("amount_with_tax", col("amount") * 1.21)
