from pyspark.sql import SparkSession
from utils.dataframe_creator import DataFrameCreator
from etl.etl_job import run_etl

def main() -> None:
    spark = SparkSession.builder.appName("ETLExample").getOrCreate()

    # Generar datos
    df_creator = DataFrameCreator(spark)
    df = df_creator.create_sample_dataframe(num_records=200)
    df.write.mode("overwrite").csv("data/input_data.csv", header=True)

    # Ejecutar ETL
    run_etl("data/input_data.csv", "output/transformed_data.csv")

    spark.stop()

if __name__ == "__main__":
    main()
