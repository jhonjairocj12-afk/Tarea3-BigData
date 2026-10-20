from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, max, desc

# 1. Creamos la sesión de Spark para Batch
spark = SparkSession.builder \
    .appName("AnalisisTransporteMasivoBatch") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("--- 1. CARGA DEL CONJUNTO DE DATOS ---")
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("transporte.csv")

df.printSchema()
print(f"Total de registros cargados: {df.count()}")


print("\n--- 2. LIMPIEZA Y TRANSFORMACIÓN DE DATOS ---")
# Filtramos filas nulas en columnas clave usando los nombres reales del CSV
df_clean = df.dropna(subset=["ciudad", "sistema", "pasajeros_dia"])

print(f"Registros limpios procesados: {df_clean.count()}")


print("\n--- 3. ANÁLISIS EXPLORATORIO (EDA) Y AGREGACIONES ---")
# Agrupamos por ciudad y sistema para calcular métricas
analisis_sistema = df_clean.groupBy("ciudad", "sistema") \
    .agg(
        sum("pasajeros_dia").alias("total_pasajeros"),
        avg("pasajeros_dia").alias("promedio_pasajeros"),
        max("pasajeros_dia").alias("max_pasajeros")
    ) \
    .orderBy(desc("total_pasajeros"))


print("\n--- 4. VISUALIZACIÓN DE RESULTADOS ---")
print("Demanda acumulada de pasajeros por Ciudad y Sistema:")
analisis_sistema.show(15, truncate=False)

spark.stop()
