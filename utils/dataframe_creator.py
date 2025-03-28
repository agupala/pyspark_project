from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
import random
from datetime import datetime, timedelta
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class DataFrameCreator:
    spark: SparkSession

    def _generate_sample_data(self, num_records: int = 100) -> List[Tuple[int, int, int, str, float, int, str]]:
        categories = ["Electrónica", "Ropa", "Hogar", "Deportes", "Libros"]
        data = [
            (
                i,
                random.randint(1000, 2000),
                random.randint(500, 700),
                random.choice(categories),
                round(random.uniform(50, 500), 2),
                random.randint(1, 5),
                (datetime(2024, 1, 1) + timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
            )
            for i in range(1, num_records + 1)
        ]
        return data

    def create_sample_dataframe(self, num_records: int = 100) -> DataFrame:
        schema = StructType([
            StructField("order_id", IntegerType(), False),
            StructField("customer_id", IntegerType(), False),
            StructField("product_id", IntegerType(), False),
            StructField("category", StringType(), False),
            StructField("amount", FloatType(), False),
            StructField("quantity", IntegerType(), False),
            StructField("purchase_date", StringType(), False),
        ])

        data = self._generate_sample_data(num_records)
        return self.spark.createDataFrame(data, schema)
