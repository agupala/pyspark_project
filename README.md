# Estructura del Proyecto ETL con PySpark

Este proyecto implementa un proceso ETL simple utilizando PySpark y programación orientada a objetos (POO).

## 📁 Estructura de Carpetas

```
etl_project/
│── .data/                # Carpeta con datos de entrada
│── output/              # Carpeta con datos procesados
│── etl/                 # Módulo con clases ETL
│   │── extractor.py     # Clase para extracción de datos
│   │── transformer.py   # Clase para transformación
│   │── loader.py        # Clase para carga de datos
│   │── etl_job.py       # Script principal que orquesta el ETL
│── main.py              # Punto de entrada del script
│── requirements.txt     # Dependencias necesarias
│── Pipfile              # Archivo de configuración de Pipenv
│── README.md            # Explicación del proyecto
```

---

## 🛠️ Instalación y Uso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/etl_pyspark.git
cd etl_pyspark
```

## 2️⃣ Crear un entorno virtual

### 📌 Opción 1: Usando `venv`

```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
pip install -r requirements.txt
```

### 📌 Opción 2: Usando `Pipenv`

```bash
pip install pipenv
pipenv install
pipenv shell
```

## 3️⃣ Ejecutar el script ETL

```bash
python main.py
```

---

## 📦 Dependencias (`requirements.txt`)

El archivo `requirements.txt` incluye las librerías necesarias para ejecutar el proyecto:
```plaintext
pyspark
pandas
```
Si necesitas instalar las dependencias manualmente, puedes hacerlo con:
```bash
pip install pyspark pandas
```

---

## 📌 Código Principal

### **`main.py`**

```python
from pyspark.sql import SparkSession
from etl.etl_job import ETLJob

def main():
    spark = SparkSession.builder \
        .appName("ETL Example") \
        .getOrCreate()

    etl = ETLJob(spark)
    etl.run()

    spark.stop()

if __name__ == "__main__":
    main()
```

---

## 🔄 Módulos ETL

### **`etl/extractor.py`**

```python
from pyspark.sql import SparkSession, DataFrame

class Extractor:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def extract(self, file_path: str) -> DataFrame:
        return self.spark.read.csv(file_path, header=True, inferSchema=True)
```

### **`etl/transformer.py`**

```python
from pyspark.sql import DataFrame

class Transformer:
    def transform(self, df: DataFrame) -> DataFrame:
        return df.withColumnRenamed("amount", "total_amount")
```

### **`etl/loader.py`**

```python
from pyspark.sql import DataFrame

class Loader:
    def load(self, df: DataFrame, output_path: str):
        df.write.mode("overwrite").parquet(output_path)
```

### **`etl/etl_job.py`**

```python
from etl.extractor import Extractor
from etl.transformer import Transformer
from etl.loader import Loader

class ETLJob:
    def __init__(self, spark):
        self.spark = spark
        self.extractor = Extractor(spark)
        self.transformer = Transformer()
        self.loader = Loader()

    def run(self):
        df = self.extractor.extract(".data/sales.csv")
        df_transformed = self.transformer.transform(df)
        self.loader.load(df_transformed, "output/sales_processed.parquet")
```

---

## 📊 Dataset de Ejemplo (`.data/sales.csv`)

```csv
order_id,customer_id,amount,date
1,101,250.75,2024-03-01
2,102,100.50,2024-03-02
3,103,320.00,2024-03-03
```

Para generar datos aleatorios:
```python
import pandas as pd
import random
from datetime import datetime, timedelta

data = {
    "order_id": list(range(1, 101)),
    "customer_id": [random.randint(100, 200) for _ in range(100)],
    "amount": [round(random.uniform(50, 500), 2) for _ in range(100)],
    "date": [(datetime(2024, 3, 1) + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(100)]
}

df = pd.DataFrame(data)
df.to_csv(".data/sales.csv", index=False)
print("Archivo sales.csv generado correctamente.")
```

---

## 🚀 Subir el Proyecto a GitHub

```bash
cd etl_project
git init
git add .
git commit -m "Primer commit - ETL con PySpark"
git remote add origin https://github.com/TU-USUARIO/etl_pyspark.git
git branch -M main
git push -u origin main
```

Ahora podés compartir tu código en GitHub y demostrar tu conocimiento en PySpark y ETL. 🚀